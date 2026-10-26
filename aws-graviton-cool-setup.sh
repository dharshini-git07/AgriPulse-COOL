#!/bin/bash
# ==============================================================================
# AgriPulse COOL - AWS Graviton / ARM64 & Cloud-Optimized OpenCV Setup Script
# Designed for AWS Graviton (Ubuntu 24.04 LTS / AMI with COOL pre-installed)
# ==============================================================================

echo "=== [1/4] Updating System Packages ==="
sudo apt-get update && sudo apt-get upgrade -y

echo "=== [2/4] Verifying AWS Graviton ARM64 Architecture ==="
uname -m

echo "=== [3/4] Activating Cloud-Optimized OpenCV (COOL) Environment ==="
if [ -d "/opt/cool" ]; then
    echo "COOL found at /opt/cool. Configuring environment variables..."
    export LD_LIBRARY_PATH="/opt/cool/cpp_sdk/lib:$LD_LIBRARY_PATH"
    export PYTHONPATH="/opt/cool/python_3.12/site-packages/:$PYTHONPATH"
else
    echo "Warning: /opt/cool not detected. Falling back to standard OpenCV 5 pip install..."
    pip install --upgrade opencv-python
fi

echo "=== [4/4] Verifying OpenCV 5 & COOL Activation ==="
python3 -c "import cv2; print(f'Successfully loaded OpenCV: {cv2.__version__} | Path: {cv2.__file__}')"

echo "=== AgriPulse COOL Environment Ready! ==="