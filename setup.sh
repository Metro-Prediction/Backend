#!/bin/bash

echo "🚀 Setting up the Metro AI Engine..."

# Create a virtual environment
echo "🔹 Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install project dependencies
echo "🔹 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Clone YOLOv5
echo "🔹 Cloning YOLOv5..."
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip install -r requirements.txt
cd ..

echo "✅ Setup complete! To activate your virtual environment, run:"
echo "   source venv/bin/activate"

