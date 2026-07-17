# utils.py - Utility functions for display and saving

import cv2
import os


def show_image(title, image):
    """Display an image in a window. Press any key to close."""
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def save_image(image, output_path):
    """Save image to the specified path."""
    # Create output directory if it doesn't exist
    folder = os.path.dirname(output_path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)

    cv2.imwrite(output_path, image)
    print(f"Image saved to {output_path}")


def get_contour_area(contour):
    """Return the area of a contour."""
    if contour is None:
        return 0
    return cv2.contourArea(contour)
