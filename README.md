# Gear Defect Detection using OpenCV

## Introduction

This project uses basic image processing with OpenCV to detect whether a gear is normal or has a broken/missing tooth. It uses contour detection and convexity defect analysis to classify gears as PASS or FAIL.

## Objective

Build a simple computer vision system that can inspect gear images and identify defective gears (broken or missing teeth) using only classical image processing techniques.

## Dataset

The project uses a gear image dataset containing:
- **Normal gears** — Gears with no visible damage
- **Defective gears** — Gears with broken, missing teeth, or rust damage

## Folder Structure

```
Gear-Defect-Detection/
│
├── dataset/
│   ├── normal/
│   └── defective/
│
├── output/
│   ├── normal/
│   └── defective/
│
├── src/
│   ├── preprocess.py
│   ├── detect.py
│   ├── utils.py
│   └── main.py
│
├── requirements.txt
└── README.md
```

## Installation

1. Make sure Python 3.x is installed.

2. Install required packages:
   ```
   pip install -r requirements.txt
   ```

## How to Run

### Process entire dataset
```
python src/main.py
```

### Process a single image
```
python src/main.py path/to/gear_image.jpg
```

## Working

The detection pipeline follows these steps:

1. **Read Image** — Load the gear image from disk
2. **Preprocess** — Convert to grayscale, apply Gaussian blur, and binary threshold
3. **Find Contours** — Detect contours in the thresholded image
4. **Select Largest Contour** — Pick the biggest contour (assumed to be the gear)
5. **Convex Hull** — Build a convex hull around the gear contour
6. **Convexity Defects** — Calculate defects between the contour and its convex hull
7. **Classification** — If significant defects are found, classify as FAIL; otherwise PASS

## Output

- **Normal Gear**: Green contour drawn around the gear with "PASS" label
- **Defective Gear**: Red contour and bounding box with "FAIL" label, defect points marked in blue

Processed images are saved in the `output/` folder.

## Future Improvements

- Real-time webcam inspection
- Better lighting compensation
- Automatic gear alignment
- CNN-based defect detection for higher accuracy
- GUI using Tkinter for user-friendly interface
