@echo off
echo 🚀 Setting up the Metro AI Engine...

:: Create virtual environment
echo 🔹 Creating virtual environment...
python -m venv venv
call venv\Scripts\activate

:: Install dependencies
echo 🔹 Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt

:: Clone YOLOv5
echo 🔹 Cloning YOLOv5...
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip install -r requirements.txt
cd ..

echo ✅ Setup complete! To activate your virtual environment, run:
echo    venv\Scripts\activate
