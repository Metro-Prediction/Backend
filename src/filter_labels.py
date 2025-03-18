#dataset contains labels having 2 classes for each image :
#   1. class 0 (PEOPLE)
#   2. class 1 (Safety line)
#the safety line has been removed and only one class of object is being used for detection
#format of yolov5 labels ==>  <class_id> <x_center> <y_center> <width> <height>

import os

#define paths for labels directory
LABELS_DIRECTORY = [
    "C:/Users/china/metro-ai-engine/data/metro_project_v1i_yolov5pytorch/train/labels",
    "C:/Users/china/metro-ai-engine/data/metro_project_v1i_yolov5pytorch/valid/labels",
    "C:/Users/china/metro-ai-engine/data/metro_project_v1i_yolov5pytorch/test/labels"
]

SAFETY_LINE_CLASS_ID = 1

def clean_labels(label_dir):
    for label_file in os.listdir(label_dir):
        file_path = os.path.join(label_dir, label_file)
        with open(file_path, 'r') as f:
            lines = f.readlines()

        filtered_lines = [line for line in lines if not line.startswith(f"{SAFETY_LINE_CLASS_ID} ")]

        with open(file_path,"w") as f:
            f.writelines(filtered_lines)
        
for label_dir in LABELS_DIRECTORY:
    clean_labels(label_dir)

print("removed safety line annotations")
