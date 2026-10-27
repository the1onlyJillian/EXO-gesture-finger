"""
hand_detector.py - Hand detection using MediaPipe Tasks API ONLY
"""

import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

class HandDetector:
    """Hand detection using MediaPipe Tasks API"""
    
    def __init__(self, min_detection_confidence=0.7, min_tracking_confidence=0.5):
        """
        Initialize hand detector with Tasks API
        """
        print("🔧 Initializing hand detector with Tasks API...")
        
        try:
            # Base options with model path
            base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')
            
            # Create options
            options = vision.HandLandmarkerOptions(
                base_options=base_options,
                running_mode=vision.RunningMode.IMAGE,
                min_hand_detection_confidence=min_detection_confidence,
                min_hand_presence_confidence=min_tracking_confidence,
                min_tracking_confidence=min_tracking_confidence,
                num_hands=1
            )
            
            # Create detector
            self.detector = vision.HandLandmarker.create_from_options(options)
            print("✅ Hand detector initialized successfully!")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            raise Exception("Could not initialize MediaPipe Tasks API")
    
    def detect(self, frame):
        """
        Detect hand landmarks in frame
        """
        # Convert BGR to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Create MediaPipe Image
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
        
        # Detect
        detection_result = self.detector.detect(mp_image)
        
        # Draw on frame
        annotated_frame = frame.copy()
        landmarks = None
        
        if detection_result.hand_landmarks:
            h, w = frame.shape[:2]
            landmarks = detection_result.hand_landmarks[0]
            
            # Draw connections
            connections = [
                (0, 1), (1, 2), (2, 3), (3, 4),
                (0, 5), (5, 6), (6, 7), (7, 8),
                (0, 9), (9, 10), (10, 11), (11, 12),
                (0, 13), (13, 14), (14, 15), (15, 16),
                (0, 17), (17, 18), (18, 19), (19, 20),
                (5, 9), (9, 13), (13, 17)
            ]
            
            for connection in connections:
                idx1, idx2 = connection
                if idx1 < len(landmarks) and idx2 < len(landmarks):
                    x1 = int(landmarks[idx1].x * w)
                    y1 = int(landmarks[idx1].y * h)
                    x2 = int(landmarks[idx2].x * w)
                    y2 = int(landmarks[idx2].y * h)
                    cv2.line(annotated_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
            # Draw points
            for landmark in landmarks:
                x = int(landmark.x * w)
                y = int(landmark.y * h)
                cv2.circle(annotated_frame, (x, y), 5, (0, 0, 255), -1)
        
        return landmarks, annotated_frame
    
    def close(self):
        """Close hand detector"""
        if hasattr(self, 'detector'):
            self.detector.close()

class HandLandmarkIndices:
    """Hand landmark indices for MediaPipe"""
    WRIST = 0
    THUMB_CMC = 1
    THUMB_MCP = 2
    THUMB_IP = 3
    THUMB_TIP = 4
    INDEX_MCP = 5
    INDEX_PIP = 6
    INDEX_DIP = 7
    INDEX_TIP = 8
    MIDDLE_MCP = 9
    MIDDLE_PIP = 10
    MIDDLE_DIP = 11
    MIDDLE_TIP = 12
    RING_MCP = 13
    RING_PIP = 14
    RING_DIP = 15
    RING_TIP = 16
    PINKY_MCP = 17
    PINKY_PIP = 18
    PINKY_DIP = 19
    PINKY_TIP = 20