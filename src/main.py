# main.py - Main script to run gear defect detection

import os
import sys
import cv2
from preprocess import load_image, resize_image, preprocess
from detect import find_gear, detect_defect, draw_result
from utils import show_image, save_image
from evaluate import compute_metrics, print_metrics, save_metrics


def process_single_image(image_path, output_dir="output"):
    """Process a single gear image and return the result and prediction."""
    print(f"\nProcessing: {image_path}")

    # Step 1: Read image
    image = load_image(image_path)
    if image is None:
        return None, None

    # Step 2: Resize for consistent processing
    image = resize_image(image, width=500)

    # Step 3: Preprocess (grayscale, blur, threshold)
    thresh = preprocess(image)

    # Step 4: Find the gear contour
    contour = find_gear(thresh)

    # Step 5: Detect defects
    is_defective, defect_count, defect_points = detect_defect(contour)

    if is_defective:
        print(f"  Result: FAIL ({defect_count} defects found)")
    else:
        print(f"  Result: PASS (No significant defects)")

    # Step 6: Draw result on image
    result_image = draw_result(image, contour, is_defective, defect_points)

    # Step 7: Save output
    filename = os.path.basename(image_path)
    save_path = os.path.join(output_dir, filename)
    save_image(result_image, save_path)

    return result_image, is_defective


def process_folder(folder_path, output_dir="output"):
    """Process all images in a folder. Returns list of predictions (True/False)."""
    predictions = []

    if not os.path.exists(folder_path):
        print(f"Folder not found: {folder_path}")
        return predictions

    # Get all image files
    extensions = ('.jpg', '.jpeg', '.png', '.bmp')
    images = [f for f in os.listdir(folder_path)
              if f.lower().endswith(extensions)]

    if len(images) == 0:
        print(f"No images found in {folder_path}")
        return predictions

    print(f"Found {len(images)} images in {folder_path}")

    for img_name in images:
        img_path = os.path.join(folder_path, img_name)
        _, is_defective = process_single_image(img_path, output_dir)
        if is_defective is not None:
            predictions.append(is_defective)

    return predictions


def main():
    """Main entry point."""
    # Base directory (one level up from src/)
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dataset_dir = os.path.join(base_dir, "dataset")
    output_dir = os.path.join(base_dir, "output")

    # Check if a specific image path was passed as argument
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
        process_single_image(image_path, output_dir)
    else:
        # Process both normal and defective folders
        normal_dir = os.path.join(dataset_dir, "normal")
        defective_dir = os.path.join(dataset_dir, "defective")

        print("=" * 50)
        print("   Gear Defect Detection System")
        print("=" * 50)

        # Collect results for evaluation
        results = []

        if os.path.exists(normal_dir):
            print("\n--- Processing Normal Gears ---")
            normal_preds = process_folder(normal_dir, os.path.join(output_dir, "normal"))
            # Ground truth for normal folder is "normal"
            for pred in normal_preds:
                predicted = "defective" if pred else "normal"
                results.append(("normal", predicted))

        if os.path.exists(defective_dir):
            print("\n--- Processing Defective Gears ---")
            defective_preds = process_folder(defective_dir, os.path.join(output_dir, "defective"))
            # Ground truth for defective folder is "defective"
            for pred in defective_preds:
                predicted = "defective" if pred else "normal"
                results.append(("defective", predicted))

        print("\n" + "=" * 50)
        print("   Processing Complete!")
        print(f"   Results saved in: {output_dir}")
        print("=" * 50)

        # Compute and display evaluation metrics
        if results:
            metrics = compute_metrics(results)
            print_metrics(metrics)
            metrics_path = os.path.join(output_dir, "evaluation_metrics.txt")
            save_metrics(metrics, metrics_path)


if __name__ == "__main__":
    main()
