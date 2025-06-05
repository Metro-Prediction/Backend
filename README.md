# Backend
Analysis, Prediction and API to handle traffic data retrieval

# 🚀 Metro AI Engine - YOLOv5 Setup Guide

This project trains an AI model to detect **people in metro stations** using **YOLOv5**. Follow the steps below to set up, train, and test the model.

## 📌 How to Set Up the Project

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/Metro-Prediction/Backend.git
cd Backend
```

### **2️⃣ Activate the Virtual Environment**
- **Windows:**  
  ```batch
  venv\Scripts\activate
  ```
- **Linux/Mac:**  
  ```bash
  source venv/bin/activate
  ```
### **3️⃣ Install Dependencies**
#### **🔹 Windows Users**
Run:
```batch
setup.bat
```

#### **🔹 Linux/Mac Users**
Run:
```bash
bash setup.sh
```

### **4️⃣ Clone YOLOv5 (If Missing)**
If `yolov5/` is not present, manually install it:
```bash
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip install -r requirements.txt
```

## 🔥 How to Train YOLOv5
Once the setup is complete, train YOLOv5 by running:
```bash
cd yolov5
python train.py --img 640 --batch 8 --epochs 50 --data ../dataset.yaml --weights yolov5s.pt --name metro_people --project ../models/yolo
```

## 🔍 How to Run Inference on Test Images
```bash
python detect.py --weights ../models/yolo/yolov5_metro/weights/best.pt --img 640 --conf 0.5 --source ../data/test/images --project ../results/yolo --name test_run
```

✅ This will save detected images inside `/results/yolo/test_run/`

## 🚀 Run on Google Colab (If Local Training Fails)
1. Open [Google Colab](https://colab.research.google.com/).
2. Run the following:
```python
from google.colab import drive
drive.mount('/content/drive')

!git clone https://github.com/ultralytics/yolov5.git
%cd yolov5
!pip install -r requirements.txt
```
3. Upload your dataset to Google Drive and modify `dataset.yaml` to point to `/content/drive/MyDrive/metro-dataset`.

---

## 📌 Notes
- If **YOLOv5 is missing**, manually install it using the commands above.
- If training **crashes due to low memory**, run it on **Google Colab**.



