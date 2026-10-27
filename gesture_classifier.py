"""
gesture_classifier.py - Gesture classification logic
"""

import numpy as np
from hand_detector import HandLandmarkIndices

class GestureClassifier:
    """Classify hand gestures from landmarks"""
    
    def __init__(self):
        self.landmark_indices = HandLandmarkIndices()
        
    def get_finger_states(self, landmarks):
        """
        Determine if each finger is open or closed
        """
        if landmarks is None:
            return None
        
        # Thumb: check horizontal distance from MCP (lebih toleran)
        thumb_tip = landmarks[self.landmark_indices.THUMB_TIP]
        thumb_mcp = landmarks[self.landmark_indices.THUMB_MCP]
        thumb_open = abs(thumb_tip.x - thumb_mcp.x) > 0.06  # Turunkan threshold
        
        # Other fingers: check if tip is above PIP joint
        index_tip = landmarks[self.landmark_indices.INDEX_TIP]
        index_pip = landmarks[self.landmark_indices.INDEX_PIP]
        index_open = index_tip.y < index_pip.y - 0.015  # Turunkan threshold
        
        middle_tip = landmarks[self.landmark_indices.MIDDLE_TIP]
        middle_pip = landmarks[self.landmark_indices.MIDDLE_PIP]
        middle_open = middle_tip.y < middle_pip.y - 0.015
        
        ring_tip = landmarks[self.landmark_indices.RING_TIP]
        ring_pip = landmarks[self.landmark_indices.RING_PIP]
        ring_open = ring_tip.y < ring_pip.y - 0.015
        
        pinky_tip = landmarks[self.landmark_indices.PINKY_TIP]
        pinky_pip = landmarks[self.landmark_indices.PINKY_PIP]
        pinky_open = pinky_tip.y < pinky_pip.y - 0.015
        
        return {
            'thumb': thumb_open,
            'index': index_open,
            'middle': middle_open,
            'ring': ring_open,
            'pinky': pinky_open
        }
    
    def is_pointing(self, finger_states):
        """
        Check if gesture is POINTING (One finger up): ☝🏻
        - Only index finger is open
        - All other fingers (including thumb) are closed
        """
        if finger_states is None:
            return False
        return (finger_states['index'] and 
                not finger_states['thumb'] and 
                not finger_states['middle'] and 
                not finger_states['ring'] and 
                not finger_states['pinky'])
    
    def is_thumbs_up(self, finger_states):
        """
        Check if gesture is THUMBS UP: 👍
        - Thumb is OPEN (pointing up)
        - All other fingers are CLOSED
        - Lebih toleran: thumb hanya perlu terbuka, jari lain tertutup
        """
        if finger_states is None:
            return False
        
        # Thumb harus terbuka
        if not finger_states['thumb']:
            return False
        
        # Jari lain harus tertutup (boleh ada sedikit toleransi)
        # Index, middle, ring, pinky semuanya harus closed
        if finger_states['index']:
            return False
        if finger_states['middle']:
            return False
        if finger_states['ring']:
            return False
        if finger_states['pinky']:
            return False
        
        return True
    
    def is_ok_sign(self, finger_states, landmarks):
        """
        Check if gesture is OK SIGN: 👌
        """
        if finger_states is None or landmarks is None:
            return False
        
        # Other fingers must be open
        if not (finger_states['middle'] and 
                finger_states['ring'] and 
                finger_states['pinky']):
            return False
        
        thumb_tip = landmarks[self.landmark_indices.THUMB_TIP]
        index_tip = landmarks[self.landmark_indices.INDEX_TIP]
        distance = np.sqrt((thumb_tip.x - index_tip.x)**2 + 
                          (thumb_tip.y - index_tip.y)**2)
        
        return distance < 0.10  # Turunkan threshold
    
    def is_fist(self, finger_states):
        """
        Check if gesture is FIST: ✊
        """
        if finger_states is None:
            return False
        
        # Semua jari tertutup (termasuk thumb)
        return (not finger_states['thumb'] and 
                not finger_states['index'] and 
                not finger_states['middle'] and 
                not finger_states['ring'] and 
                not finger_states['pinky'])
    
    def is_open_palm(self, finger_states):
        """
        Check if gesture is OPEN PALM: ✋
        """
        if finger_states is None:
            return False
        
        # Semua jari terbuka
        return (finger_states['thumb'] and 
                finger_states['index'] and 
                finger_states['middle'] and 
                finger_states['ring'] and 
                finger_states['pinky'])
    
    def classify(self, landmarks):
        """
        Classify hand gesture from landmarks
        """
        if landmarks is None:
            return "UNKNOWN"
        
        finger_states = self.get_finger_states(landmarks)
        if finger_states is None:
            return "UNKNOWN"
        
        # Check gestures in priority order
        # 1. FIST (paling spesifik)
        if self.is_fist(finger_states):
            return "FIST"
        
        # 2. OPEN_PALM
        if self.is_open_palm(finger_states):
            return "OPEN_PALM"
        
        # 3. POINTING (One finger up) - untuk SUHO
        if self.is_pointing(finger_states):
            return "POINTING"
        
        # 4. THUMBS_UP - untuk KYUNGSOO
        if self.is_thumbs_up(finger_states):
            return "THUMBS_UP"
        
        # 5. OK_SIGN
        if self.is_ok_sign(finger_states, landmarks):
            return "OK_SIGN"
        
        return "UNKNOWN"