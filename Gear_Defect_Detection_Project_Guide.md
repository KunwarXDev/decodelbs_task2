# Gear Defect Detection using OpenCV

## Project Objective

Build a simple computer vision project that detects whether a gear is normal or has a broken/missing tooth using OpenCV.

The project should use only basic image processing techniques. Avoid deep learning or complex architectures. The code should be clean but simple enough to resemble the work of a second-year engineering student.

---

# Tech Stack

- Python 3.x
- OpenCV
- NumPy
- Matplotlib (optional)

---

# Dataset

Download a gear image dataset from Kaggle.

Suggested dataset:
- Defected Gears Dataset

Create the following folder structure after downloading.

```
Gear-Defect-Detection/
│
├── dataset/
│   ├── normal/
│   │      gear1.jpg
│   │      gear2.jpg
│   │      ...
│   │
│   └── defective/
│          gear1.jpg
│          gear2.jpg
│          ...
│
├── output/
│
├── src/
│   ├── preprocess.py
│   ├── detect.py
│   ├── utils.py
│   └── main.py
│
├── requirements.txt
├── README.md
└── report.pdf
```

---

# Project Flow

```
Image / Webcam
        |
Read Image
        |
Convert to Grayscale
        |
Gaussian Blur
        |
Binary Threshold
        |
Find Contours
        |
Select Largest Contour
        |
Create Convex Hull
        |
Find Convexity Defects
        |
Check Missing Tooth
        |
PASS / FAIL
```

---

# Module Description

## preprocess.py

Responsibilities

- Read image
- Resize image
- Convert to grayscale
- Apply Gaussian Blur
- Apply binary threshold
- Return processed image

Functions

```
load_image(path)
preprocess(image)
```

---

## detect.py

Responsibilities

- Find contours
- Select largest contour
- Generate convex hull
- Compute convexity defects
- Detect broken tooth
- Draw contour
- Draw bounding box
- Display PASS or FAIL

Functions

```
find_gear()
detect_defect()
draw_result()
```

---

## utils.py

Utility functions such as

- image display
- image saving
- contour area calculation

Keep this file small.

---

## main.py

Workflow

1. Read image
2. Preprocess image
3. Detect contour
4. Detect defects
5. Show result
6. Save output image

---

# OpenCV Functions

Use only common OpenCV functions.

- cv2.imread()
- cv2.VideoCapture()
- cv2.cvtColor()
- cv2.GaussianBlur()
- cv2.threshold()
- cv2.findContours()
- cv2.contourArea()
- cv2.convexHull()
- cv2.convexityDefects()
- cv2.boundingRect()
- cv2.rectangle()
- cv2.putText()
- cv2.imshow()

Avoid unnecessary optimization.

---

# Detection Logic

A simple approach is enough.

- Find the largest contour.
- Build its convex hull.
- Calculate convexity defects.
- Ignore very small defects caused by noise.
- If one or more significant defects are present, classify the gear as defective.

Pseudo logic

```
if significant_defects > 0:
    result = "FAIL"
else:
    result = "PASS"
```

---

# Coding Style

The project should feel like a student project.

Recommended practices

- Use descriptive variable names.
- Write short functions.
- Add a few simple comments.
- Do not over-engineer the code.
- Avoid advanced design patterns.
- Avoid excessive documentation.
- Keep files under 150 lines where possible.

---

# requirements.txt

```
opencv-python
numpy
matplotlib
```

---

# README Sections

- Introduction
- Objective
- Dataset
- Folder Structure
- Installation
- How to Run
- Working
- Output
- Future Improvements

---

# Possible Improvements

Mention these in the report instead of implementing them.

- Real-time webcam inspection
- Better lighting compensation
- Automatic gear alignment
- CNN-based defect detection
- GUI using Tkinter

---

# Expected Output

Normal Gear

- Green contour
- PASS displayed

Defective Gear

- Red bounding box
- FAIL displayed

Save processed images inside the output folder.

---

# Notes

The project should prioritize readability over sophistication. The implementation should be modular, functional, and realistic for a second-year B.Tech student who has recently learned OpenCV.
