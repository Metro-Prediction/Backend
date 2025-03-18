import cv2
import os
import matplotlib.pyplot as plt

# Define paths
BASE_DATASET_PATH = "C:/Users/china/metro-ai-engine/data"
IMG_PATH = os.path.join(BASE_DATASET_PATH,"metro_project_v1i_yolov5pytorch","train","images")
LABEL_PATH = os.path.join(BASE_DATASET_PATH,"metro_project_v1i_yolov5pytorch","train","labels")

# Debugging
print("Checking path:", os.path.abspath(IMG_PATH))
print("Exists:", os.path.exists(IMG_PATH))

if not os.path.exists(IMG_PATH):
    raise FileNotFoundError(f"Path does not exist: {IMG_PATH}")


# DATASET_PATH = "data/metro_project_v1i_yolov5pytorch"
# IMG_PATH = "\data\metro_project_v1i_yolov5pytorch\train\images"
# LABEL_PATH = "\data\metro_project_v1i_yolov5pytorch\train\labels"

# Read class names (if available)
class_names = {0: "PEOPLE"}  # Modify if you have more classes

# Function to plot image with bounding boxes
def plot_image(image_file):
    img = cv2.imread(os.path.join(IMG_PATH, image_file))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert to RGB

    # Load corresponding label file
    label_file = image_file.replace(".jpg", ".txt").replace(".png", ".txt")
    label_path = os.path.join(LABEL_PATH, label_file)

    if os.path.exists(label_path):
        with open(label_path, "r") as f:
            for line in f.readlines():
                parts = line.strip().split()
                class_id = int(parts[0])
                x_center, y_center, width, height = map(float, parts[1:])

                # Convert from normalized to pixel coordinates
                img_h, img_w, _ = img.shape
                x_center, y_center = int(x_center * img_w), int(y_center * img_h)
                width, height = int(width * img_w), int(height * img_h)

                # Get top-left corner
                x1, y1 = x_center - width // 2, y_center - height // 2
                x2, y2 = x1 + width, y1 + height

                # Draw bounding box
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
                cv2.putText(img, class_names.get(class_id, str(class_id)), 
                            (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Show image
    plt.imshow(img)
    plt.axis("off")
    plt.show()

# Test with a random image
sample_image = os.listdir(IMG_PATH)[30]
plot_image(sample_image)
