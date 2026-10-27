"""
config.py - Application configuration and constants
"""

import os

# Application settings
APP_NAME = "EXO GESTURE SUMMONER"
APP_TAGLINE = ""

# Camera settings
CAMERA_ID = 0
CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480

# Gesture detection settings
MIN_DETECTION_CONFIDENCE = 0.7
MIN_TRACKING_CONFIDENCE = 0.5
COOLDOWN_DURATION = 1.5  # seconds

# Display settings
IMAGE_SIZE = (500, 500)  # Ukuran sedang, cukup untuk kualitas baik
DISPLAY_HEIGHT = 480
DISPLAY_WIDTH = 640

# Color themes (BGR format)
COLORS = {
    'PURPLE': (128, 0, 128),
    'PINK': (255, 0, 255),
    'BLUE': (255, 0, 0),
    'GOLD': (0, 215, 255),
    'WHITE': (255, 255, 255),
    'BLACK': (0, 0, 0),
    'GREEN': (0, 255, 0),
    'YELLOW': (0, 255, 255),
    'RED': (0, 0, 255),
    'CYAN': (255, 255, 0)
}

# Asset paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

IMAGE_PATHS = {
    "SUHO": os.path.join(ASSETS_DIR, "suho", "suho.jpg"),
    "KYUNGSOO": os.path.join(ASSETS_DIR, "kyungsoo", "kyungsoo.jpg"),
    "SKY_TRIO": os.path.join(ASSETS_DIR, "sky_trio", "sky_trio.jpg"),
    "EXO_ALL": os.path.join(ASSETS_DIR, "exo_all", "exo_all.jpg")
}

# Gesture mapping
GESTURE_MAP = {
    "POINTING": {
        "result_name": "SUHO",
        "display_name": "SUHO",
        "sub_text": "☝🏻 LEADER NO. 1",
        "status_text": "⭐ Leader Detected! ⭐",
        "image_key": "SUHO",
        "effect": None
    },
    "THUMBS_UP": {
        "result_name": "KYUNGSOO",
        "display_name": "KYUNGSOO",
        "sub_text": "D.O.",
        "status_text": "💙 Kyungsoo Detected! 💙",
        "image_key": "KYUNGSOO",
        "effect": None
    },
    "OK_SIGN": {
        "result_name": "SKY_TRIO",
        "display_name": "TRIO S.K.Y.",
        "sub_text": "KAI • SEHUN • CHANYEOL",
        "status_text": "✨ S.K.Y. Detected! ✨",
        "image_key": "SKY_TRIO",
        "effect": None
    },
    "EXO_ALL_MEMBERS": {
        "result_name": "EXO_ALL",
        "display_name": "EXO ALL MEMBERS",
        "sub_text": "WE ARE ONE!",
        "status_text": "🌟 EXO Summoned! 🌟",
        "image_key": "EXO_ALL",
        "effect": None
    }
}

# Gesture labels
GESTURE_LABELS = {
    "POINTING": "☝🏻 POINTING",
    "THUMBS_UP": "👍 THUMBS UP",
    "OK_SIGN": "👌 OK SIGN",
    "FIST": "✊ FIST",
    "OPEN_PALM": "✋ OPEN PALM",
    "FINGER_GUN": "👈 FINGER GUN",
    "SARANGHAE": "🫰 SARANGHAE",
    "UNKNOWN": "WAITING... 🤔",
    "SEQUENCE": "FIST → OPEN PALM ✊→✋"
}