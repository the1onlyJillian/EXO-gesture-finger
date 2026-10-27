"""
main.py - Main application for EXO GESTURE SUMMONER
"""

import cv2
import time
import sys

# Import config
from config import (
    APP_NAME, CAMERA_ID, CAMERA_WIDTH, CAMERA_HEIGHT,
    MIN_DETECTION_CONFIDENCE, MIN_TRACKING_CONFIDENCE,
    COOLDOWN_DURATION, IMAGE_SIZE,
    GESTURE_MAP, GESTURE_LABELS, IMAGE_PATHS
)

# Import components
from hand_detector import HandDetector
from gesture_classifier import GestureClassifier
from display_manager import DisplayManager
from effect_manager import EffectManager

class EXOGestureSummoner:
    """Main application class"""
    
    def __init__(self):
        print("=" * 50)
        print("⭐ EXO GESTURE SUMMONER ⭐")
        print("=" * 50)
        print("\n🎯 Supported Gestures:")
        print("  ☝🏻 POINTING     → SUHO")
        print("  👍 THUMBS UP    → KYUNGSOO")
        print("  👌 OK SIGN      → TRIO S.K.Y.")
        print("  ✊ → ✋ FIST → OPEN PALM → EXO ALL 🎉")
        print("\n⌨️  Press 'q' to quit")
        print("=" * 50)
        
        # Initialize components
        try:
            self.hand_detector = HandDetector(
                min_detection_confidence=MIN_DETECTION_CONFIDENCE,
                min_tracking_confidence=MIN_TRACKING_CONFIDENCE
            )
        except Exception as e:
            print(f"❌ Error: {e}")
            sys.exit(1)
            
        self.gesture_classifier = GestureClassifier()
        self.display_manager = DisplayManager()
        self.effect_manager = EffectManager()
        
        # State variables
        self.cap = None
        self.running = False
        
        # Gesture state
        self.current_gesture = "UNKNOWN"
        self.current_result = None
        self.last_trigger_time = 0
        self.sequence_state = None
        self.active_effect = False
        self.is_exo_all = False  # Track jika sedang menampilkan EXO ALL
        
        # Result data
        self.result_image = None
        self.member_name = None
        self.status_text = None
        self.effect_type = None
        
        # Debug
        self.debug_mode = True
        
        # Load images
        self.images = {}
        self.load_images()
        
    def load_images(self):
        """Load all member images"""
        print("\n📁 Loading member images...")
        for key, path in IMAGE_PATHS.items():
            print(f"  Loading {key}...")
            img = self.display_manager.load_image(path, IMAGE_SIZE)
            self.images[key] = img
        print("✅ All images loaded successfully!")
        
    def initialize_camera(self):
        """Initialize webcam"""
        try:
            self.cap = cv2.VideoCapture(CAMERA_ID)
            if not self.cap.isOpened():
                print("❌ Error: Could not open webcam.")
                return False
            
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_WIDTH)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_HEIGHT)
            print("✅ Webcam initialized successfully!")
            return True
        except Exception as e:
            print(f"❌ Error: {e}")
            return False
    
    def process_frame(self, frame):
        """
        Process a single frame
        """
        # Flip for mirror effect
        frame = cv2.flip(frame, 1)
        
        # Detect hand
        try:
            landmarks, annotated_frame = self.hand_detector.detect(frame)
        except Exception as e:
            return frame, None, None, False
    
        # Default values
        gesture_text = "WAITING... 🤔"
        result_frame = None
        is_exo_all = False
        
        if landmarks is not None:
            try:
                # Classify gesture
                gesture = self.gesture_classifier.classify(landmarks)
                self.current_gesture = gesture
                
                # Debug: tampilkan gesture yang terdeteksi
                if self.debug_mode and gesture != "UNKNOWN":
                    print(f"🔍 Gesture detected: {gesture}")
                
                # Check sequence: FIST -> OPEN PALM (EXO ALL)
                if gesture == "FIST":
                    self.sequence_state = "FIST"
                    if self.debug_mode:
                        print("   → FIST detected, waiting for OPEN PALM")
                elif gesture == "OPEN_PALM" and self.sequence_state == "FIST":
                    self.sequence_state = None
                    self.current_result = "EXO_ALL_MEMBERS"
                    self.last_trigger_time = time.time()
                    self.active_effect = True
                    self.is_exo_all = True
                    print("🎉 EXO ALL SUMMONED!")
                else:
                    if gesture != "OPEN_PALM":
                        self.sequence_state = None
                    
                    # Reset EXO ALL flag jika gesture lain
                    if self.is_exo_all and gesture not in ["OPEN_PALM"]:
                        self.is_exo_all = False
                    
                    if self.current_result != "EXO_ALL_MEMBERS":
                        # POINTING = SUHO
                        if gesture == "POINTING":
                            self.current_result = "POINTING"
                            self.last_trigger_time = time.time()
                            self.active_effect = True
                            self.is_exo_all = False
                            print("   → SUHO detected!")
                        elif gesture == "THUMBS_UP":
                            self.current_result = "THUMBS_UP"
                            self.last_trigger_time = time.time()
                            self.active_effect = True
                            self.is_exo_all = False
                            print("   → KYUNGSOO detected!")
                        elif gesture == "OK_SIGN":
                            self.current_result = "OK_SIGN"
                            self.last_trigger_time = time.time()
                            self.active_effect = True
                            self.is_exo_all = False
                            print("   → SKY TRIO detected!")
            except Exception as e:
                print(f"⚠️ Error: {e}")
        
        # Update result display
        if self.current_result and self.current_result in GESTURE_MAP:
            try:
                info = GESTURE_MAP[self.current_result]
                result_frame = self.images.get(info['image_key'])
                # Cek apakah ini EXO ALL
                if self.current_result == "EXO_ALL_MEMBERS":
                    is_exo_all = True
            except Exception as e:
                print(f"⚠️ Error: {e}")
        
        # Apply cooldown
        if time.time() - self.last_trigger_time > COOLDOWN_DURATION:
            self.active_effect = False
        
        return annotated_frame, result_frame, gesture_text, is_exo_all
    
    def run(self):
        """Main application loop"""
        if not self.initialize_camera():
            return
        
        print("\n🚀 Application is running...")
        print("📸 Lakukan gesture di depan kamera!\n")
        self.running = True
        
        # Set window to full screen
        cv2.namedWindow(APP_NAME, cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty(APP_NAME, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        
        try:
            while self.running:
                ret, frame = self.cap.read()
                if not ret:
                    break
                
                camera_frame, result_frame, _, is_exo_all = self.process_frame(frame)
                
                display = self.display_manager.create_display(
                    camera_frame, result_frame, None, None, None, None, False, is_exo_all
                )
                
                cv2.imshow(APP_NAME, display)
                
                if cv2.waitKey(1) & 0xFF in [ord('q'), ord('Q')]:
                    print("\n👋 Shutting down...")
                    self.running = False
                    break
                    
        except KeyboardInterrupt:
            print("\n👋 Interrupted...")
        except Exception as e:
            print(f"\n❌ Error: {e}")
        finally:
            self.cleanup()
    
    def cleanup(self):
        """Clean up resources"""
        if self.cap:
            self.cap.release()
        try:
            self.hand_detector.close()
        except:
            pass
        cv2.destroyAllWindows()
        print("✅ Closed!")

def main():
    try:
        app = EXOGestureSummoner()
        app.run()
    except Exception as e:
        print(f"\n❌ Fatal error: {e}")

if __name__ == "__main__":
    main()