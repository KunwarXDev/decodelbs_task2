import cv2
import numpy as np


def find_gear(th):
    cnts, _ = cv2.findContours(
        th,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    if not cnts:
        return None

    cnt = max(cnts, key=cv2.contourArea)

    if cv2.contourArea(cnt) < 5000:
        return None

    eps = 0.002 * cv2.arcLength(cnt, True)
    cnt = cv2.approxPolyDP(cnt, eps, True)

    area = cv2.contourArea(cnt)
    peri = cv2.arcLength(cnt, True)

    if peri == 0:
        return None

    circ = 4 * np.pi * area / (peri * peri)

    if circ < 0.45:
        return None

    return cnt


def detect_defect(cnt, min_depth=12, min_def=2):
    if cnt is None:
        return True, 0, []

    hull = cv2.convexHull(cnt, returnPoints=False)

    if hull is None or len(hull) < 4:
        return False, 0, []

    defects = cv2.convexityDefects(cnt, hull)

    if defects is None:
        return False, 0, []

    dcnt = 0
    pts = []

    for i in range(defects.shape[0]):
        s, e, f, d = defects[i, 0]

        dep = d / 256.0

        if dep < min_depth:
            continue

        sp = cnt[s][0]
        ep = cnt[e][0]
        fp = cnt[f][0]

        a = np.linalg.norm(ep - sp)
        b = np.linalg.norm(fp - sp)
        c = np.linalg.norm(ep - fp)

        if b == 0 or c == 0:
            continue

        ang = np.degrees(
            np.arccos(
                np.clip(
                    (b * b + c * c - a * a) / (2 * b * c),
                    -1,
                    1,
                )
            )
        )

        if ang < 55 or ang > 135:
            continue

        dcnt += 1
        pts.append(tuple(fp))

    bad = dcnt >= min_def

    return bad, dcnt, pts


def draw_result(img, cnt, bad, pts):
    out = img.copy()

    if cnt is None:
        cv2.putText(
            out,
            "NO GEAR",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2,
        )
        return out

    x, y, w, h = cv2.boundingRect(cnt)

    if bad:
        cv2.drawContours(out, [cnt], -1, (0, 0, 255), 2)
        cv2.rectangle(out, (x, y), (x + w, y + h), (0, 0, 255), 2)

        for p in pts:
            cv2.circle(out, p, 5, (255, 0, 0), -1)

        cv2.putText(
            out,
            "FAIL",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2,
        )
    else:
        cv2.drawContours(out, [cnt], -1, (0, 255, 0), 2)

        cv2.putText(
            out,
            "PASS",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
        )

    return out
