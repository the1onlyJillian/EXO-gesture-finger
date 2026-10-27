"""
display_manager.py - Display management with natural quality
"""

import cv2
import numpy as np
from PIL import Image
import os
from config import COLORS

class DisplayManager:
    """Manage application display with natural quality"""
    
    def __init__(self):
        self.image_cache = {}
        
    def load_image(self, image_path, size=(600, 600)):
        """
        Load image from file with good quality
        """
        if image_path in self.image_cache:
            return self.image_cache[image_path]
        
        try:
            if image_path and os.path.exists(image_path):
                # Load dengan PIL
                img = Image.open(image_path)
                
                # Convert ke RGB jika perlu
                if img.mode == 'RGBA':
                    img = img.convert('RGB')
                
                # Resize dengan LANCZOS (kualitas terbaik)
                img = img.resize(size, Image.Resampling.LANCZOS)
                
                # Convert ke numpy array
                img_array = np.array(img)
                
                # Convert RGB ke BGR untuk OpenCV
                if len(img_array.shape) == 3 and img_array.shape[2] == 3:
                    img_array = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
                
                # Cache image
                self.image_cache[image_path] = img_array
                return img_array
                
        except Exception as e:
            print(f"Error loading image {image_path}: {e}")
        
        # Placeholder
        placeholder = np.zeros((size[1], size[0], 3), dtype=np.uint8)
        cv2.putText(placeholder, "No Image", (size[0]//2-60, size[1]//2), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, COLORS['WHITE'], 2)
        return placeholder
    
    def create_display(self, camera_frame, result_frame, gesture_text, 
                      member_name, status_text, effect_type=None, show_confetti=False, is_exo_all=False):
        """
        Create display with camera as background and result as overlay
        """
        if camera_frame is None:
            return np.zeros((500, 800, 3), dtype=np.uint8)
        
        # Gunakan frame camera sebagai background
        display = camera_frame.copy()
        h, w = display.shape[:2]
        
        # Jika ada result (foto member), tampilkan sebagai overlay
        if result_frame is not None:
            # Ukuran berbeda untuk EXO ALL
            if is_exo_all:
                result_h = int(h * 0.7)
                result_w = int(result_h * 1.2)
                x_pos = (w - result_w) // 2
                y_pos = (h - result_h) // 2
                border_thickness = 3
            else:
                result_h = int(h * 0.5)
                result_w = int(result_h * 1.2)
                x_pos = w - result_w - 20
                y_pos = 20
                border_thickness = 1
            
            # Resize dengan INTER_LINEAR (paling natural untuk tampilan)
            # Jangan pakai sharpening biar ga pecah
            result_resized = cv2.resize(result_frame, (result_w, result_h), 
                                       interpolation=cv2.INTER_LINEAR)
            
            # Border
            cv2.rectangle(result_resized, (0, 0), (result_w-1, result_h-1), 
                         (255, 255, 255), border_thickness)
            
            # Untuk EXO ALL, tambahkan border emas
            if is_exo_all:
                cv2.rectangle(result_resized, (3, 3), (result_w-4, result_h-4), 
                             (0, 215, 255), 2)
            
            # Overlay ke display
            display[y_pos:y_pos+result_h, x_pos:x_pos+result_w] = result_resized
        
        return display