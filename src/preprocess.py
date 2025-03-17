import cv2
import logging
import os

logging.basicConfig(level=logging.INFO)

def preprocess_image(image_path, output_dir, size=(640, 640), to_grayscale=False):
    """
    Preprocess an image by resizing and optionally converting to grayscale.

    Args:
        image_path (str): Path to the input image.
        output_dir (str): Directory to save processed image.
        size (tuple): Target (width, height) for resizing.
        to_grayscale (bool): Whether to convert to grayscale.

    Returns:
        str: Path to the processed image.
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")

    # Load the image
    image = cv2.imread(image_path)

    # Resize the image
    resized_image = cv2.resize(image, size)

    # Convert to grayscale if requested
    if to_grayscale:
        resized_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Save the processed image
    filename = os.path.basename(image_path).replace(".jpg", "_processed.jpg")
    output_path = os.path.join(output_dir, filename)
    cv2.imwrite(output_path, resized_image)

    logging.info(f"Processed image saved to: {output_path}")
    return output_path

if __name__ == "__main__":
    INPUT_IMAGE = "data/dummy_image_20250312_005233.jpg"
    OUTPUT_DIR = "/data/processed/"
    preprocess_image(INPUT_IMAGE, OUTPUT_DIR, to_grayscale=False)
