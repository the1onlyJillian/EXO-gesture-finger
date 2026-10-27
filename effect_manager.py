"""
effect_manager.py - Visual effects management
"""

import cv2
import numpy as np
import random

class EffectManager:
    """Manage visual effects for gestures"""
    
    def __init__(self):
        self.confetti_particles = []
        self.sparkle_particles = []
        self.heart_particles = []
        
    def reset_all(self):
        """Reset all effects"""
        self.confetti_particles = []
        self.sparkle_particles = []
        self.heart_particles = []
    
    def apply_glow(self, frame, color=(128, 0, 128), intensity=0.3):
        """
        Apply glow effect
        
        Args:
            frame: Input frame
            color: Glow color (BGR)
            intensity: Glow intensity
            
        Returns:
            numpy.ndarray: Frame with glow
        """
        if frame is None:
            return frame
            
        # Create blurred overlay
        overlay = frame.copy()
        overlay = cv2.GaussianBlur(overlay, (51, 51), 0)
        
        # Color overlay
        colored = np.zeros_like(overlay)
        colored[:, :, 0] = color[0]
        colored[:, :, 1] = color[1]
        colored[:, :, 2] = color[2]
        
        # Blend
        result = cv2.addWeighted(frame, 0.6, colored, 0.2, 0)
        result = cv2.addWeighted(result, 0.8, overlay, 0.2, 0)
        
        return result
    
    def apply_heart(self, frame, num_hearts=8):
        """
        Apply heart effect
        
        Args:
            frame: Input frame
            num_hearts: Number of hearts
            
        Returns:
            numpy.ndarray: Frame with hearts
        """
        if frame is None:
            return frame
            
        h, w = frame.shape[:2]
        result = frame.copy()
        
        # Initialize hearts
        if len(self.heart_particles) < num_hearts:
            self.heart_particles = []
            for _ in range(num_hearts):
                self.heart_particles.append({
                    'x': random.randint(50, w-50),
                    'y': random.randint(50, h-50),
                    'size': random.randint(20, 40),
                    'color': random.choice([(255, 0, 0), (255, 100, 100), (200, 0, 100)])
                })
        
        # Draw hearts
        for heart in self.heart_particles:
            x = heart['x']
            y = heart['y']
            size = heart['size']
            color = heart['color']
            
            # Draw heart using two circles and a triangle
            cv2.ellipse(result, (x - size//3, y - size//3), 
                       (size//2, size//3), 0, 0, 360, color, -1)
            cv2.ellipse(result, (x + size//3, y - size//3), 
                       (size//2, size//3), 0, 0, 360, color, -1)
            pts = np.array([[x, y + size//3], 
                           [x - size//2, y - size//4], 
                           [x + size//2, y - size//4]], np.int32)
            cv2.fillPoly(result, [pts], color)
            
            # Animate heart
            heart['y'] += 1
            if heart['y'] > h + 50:
                heart['y'] = -50
                heart['x'] = random.randint(50, w-50)
                heart['size'] = random.randint(20, 40)
        
        return result
    
    def apply_sparkle(self, frame, num_sparkles=15):
        """
        Apply sparkle effect
        
        Args:
            frame: Input frame
            num_sparkles: Number of sparkles
            
        Returns:
            numpy.ndarray: Frame with sparkles
        """
        if frame is None:
            return frame
            
        h, w = frame.shape[:2]
        result = frame.copy()
        
        # Initialize sparkles
        if len(self.sparkle_particles) < num_sparkles:
            self.sparkle_particles = []
            for _ in range(num_sparkles):
                self.sparkle_particles.append({
                    'x': random.randint(0, w),
                    'y': random.randint(0, h),
                    'size': random.randint(3, 8),
                    'phase': random.randint(0, 4),
                    'color': random.choice([(255, 215, 0), (255, 255, 255), (255, 200, 0)])
                })
        
        # Draw sparkles
        for sparkle in self.sparkle_particles:
            x = sparkle['x']
            y = sparkle['y']
            size = sparkle['size']
            color = sparkle['color']
            
            # Star shape
            cv2.circle(result, (x, y), size, color, -1)
            cv2.circle(result, (x, y), size//2, (255, 255, 255), -1)
            cv2.line(result, (x - size, y), (x + size, y), color, 1)
            cv2.line(result, (x, y - size), (x, y + size), color, 1)
            
            # Animate
            sparkle['phase'] += 1
            sparkle['x'] += random.randint(-1, 1)
            sparkle['y'] += random.randint(-1, 1)
            
            # Keep in bounds
            sparkle['x'] = max(0, min(w-1, sparkle['x']))
            sparkle['y'] = max(0, min(h-1, sparkle['y']))
        
        return result
    
    def apply_confetti(self, frame, num_confetti=40):
        """
        Apply confetti effect
        
        Args:
            frame: Input frame
            num_confetti: Number of confetti pieces
            
        Returns:
            numpy.ndarray: Frame with confetti
        """
        if frame is None:
            return frame
            
        h, w = frame.shape[:2]
        result = frame.copy()
        
        # Initialize confetti
        if len(self.confetti_particles) < num_confetti:
            self.confetti_particles = []
            colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), 
                     (255, 255, 0), (255, 0, 255), (0, 255, 255)]
            for _ in range(num_confetti):
                self.confetti_particles.append({
                    'x': random.randint(0, w),
                    'y': random.randint(-h, 0),
                    'width': random.randint(5, 12),
                    'height': random.randint(3, 6),
                    'color': random.choice(colors),
                    'speed': random.randint(2, 6),
                    'sway': random.randint(-1, 1)
                })
        
        # Draw confetti
        for confetti in self.confetti_particles:
            x = confetti['x']
            y = confetti['y']
            wd = confetti['width']
            ht = confetti['height']
            color = confetti['color']
            
            # Draw rectangle as confetti
            cv2.rectangle(result, (x, y), (x + wd, y + ht), color, -1)
            
            # Animate (falling down)
            confetti['y'] += confetti['speed']
            confetti['x'] += confetti['sway'] + random.randint(-1, 1)
            
            # Reset if off screen
            if confetti['y'] > h:
                confetti['x'] = random.randint(0, w)
                confetti['y'] = -confetti['height']
                confetti['speed'] = random.randint(2, 6)
        
        return result