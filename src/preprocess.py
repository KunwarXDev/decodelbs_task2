# preprocess.py - Image loading and preprocessing for gear defect detection

import cv2
import numpy as np


def load_image(path):
    """Read an image from the given file path."""
    image = cv2.imread(path)
    if image is None:
        print(f"Error: Could not read image from {path}")
        return None
    return image


def resize_image(image, width=500):
    """Resize image to a fixed width while keeping aspect ratio."""
    height, w = image.shape[:2]
    ratio = width / w
    new_height = int(height * ratio)
    resized = cv2.resize(image, (width, new_height))
    return resized


def preprocess(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (9, 9), 2)

    _, th = cv2.threshold(
        blur,
        0,
        255,
        cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU,
    )

    k = np.ones((3, 3), np.uint8)

    th = cv2.morphologyEx(th, cv2.MORPH_OPEN, k)
    th = cv2.morphologyEx(th, cv2.MORPH_CLOSE, k)

    return th