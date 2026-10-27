# download_model.py
import urllib.request
import os

print("Downloading hand landmarker model...")
url = "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task"

try:
    urllib.request.urlretrieve(url, "hand_landmarker.task")
    print("✅ Model downloaded successfully!")
except Exception as e:
    print(f"❌ Error downloading model: {e}")
    print("   Silakan download manual dari:")
    print("   https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task")