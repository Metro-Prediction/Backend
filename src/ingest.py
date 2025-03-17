import cv2
import numpy as np
import os
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(level=logging.INFO)

# Ensure output directory exists
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "../data")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_dummy_image(text="Metro Station", size=(640, 640)):
    """
    Generate a synthetic image with text overlay for testing.

    Args:
        text (str): Text to display on the image.
        size (tuple): Image dimensions (width, height).

    Returns:
        str: Path to the saved dummy image.
    """
    img = np.zeros((size[1], size[0], 3), dtype=np.uint8)  # Black image
    cv2.putText(img, text, (50, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Save image with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    image_path = os.path.join(OUTPUT_DIR, f"dummy_image_{timestamp}.jpg")
    cv2.imwrite(image_path, img)
    logging.info(f"Generated image: {image_path}")

    return image_path

if __name__ == "__main__":
    generate_dummy_image()
