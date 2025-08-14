#!/usr/bin/env python3
"""
Demo of Online Exam Proctoring System - No Camera Required
This demo shows the system interface and functionality without requiring a webcam
"""

import cv2
import numpy as np
import sys
import os
import time

def create_demo_frame(frame_count, demo_scenario="normal"):
    """Create a synthetic frame for demonstration"""
    # Create a blank frame
    frame = np.zeros((480, 640, 3), dtype=np.uint8)
    
    # Add background gradient
    for i in range(480):
        intensity = int(50 + (i / 480) * 50)
        frame[i, :] = [intensity, intensity//2, intensity//3]
    
    # Add demo face rectangle based on scenario
    if demo_scenario == "normal":
        # Single face detected
        cv2.rectangle(frame, (200, 150), (400, 350), (0, 255, 0), 2)
        cv2.putText(frame, "Student Face", (210, 140), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        face_count = 1
        alert_status = "Normal"
        alert_color = (0, 255, 0)
    elif demo_scenario == "no_face":
        # No face detected
        face_count = 0
        alert_status = "ALERT: No face detected!"
        alert_color = (0, 0, 255)
    elif demo_scenario == "multiple":
        # Multiple faces
        cv2.rectangle(frame, (150, 120), (300, 280), (0, 0, 255), 2)
        cv2.rectangle(frame, (350, 180), (500, 340), (0, 0, 255), 2)
        cv2.putText(frame, "Face 1", (160, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.putText(frame, "Face 2", (360, 170), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        face_count = 2
        alert_status = "ALERT: Multiple faces!"
        alert_color = (0, 0, 255)
    else:
        face_count = 1
        alert_status = "Normal"
        alert_color = (0, 255, 0)
    
    # Add demo text overlay
    cv2.putText(frame, "DEMO MODE - No Camera Required", (10, 30), 
               cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
    cv2.putText(frame, f"Faces Detected: {face_count}", (10, 60), 
               cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    cv2.putText(frame, f"Frame: {frame_count}", (10, 90), 
               cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    cv2.putText(frame, f"Status: {alert_status}", (10, 120), 
               cv2.FONT_HERSHEY_SIMPLEX, 0.6, alert_color, 2)
    
    # Add timestamp
    cv2.putText(frame, f"Time: {time.strftime('%H:%M:%S')}", (10, 450), 
               cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)
    
    return frame, face_count, alert_status

def main():
    print("=== Online Exam Proctoring System - Demo (No Camera) ===")
    print("This demo shows the system interface without requiring a webcam")
    print("Press 'q' to quit, 's' to cycle through scenarios")
    print("=" * 60)
    
    # Demo scenarios
    scenarios = ["normal", "no_face", "multiple", "normal"]
    current_scenario = 0
    frame_count = 0
    
    print("Demo scenarios:")
    print("1. Normal - Single face detected")
    print("2. No Face - Alert condition")
    print("3. Multiple Faces - Alert condition")
    print("4. Back to Normal")
    print("\nStarting demo...")
    
    while True:
        frame_count += 1
        
        # Create demo frame
        demo_frame, face_count, status = create_demo_frame(
            frame_count, scenarios[current_scenario]
        )
        
        # Create monitoring panel
        panel = np.zeros((480, 400, 3), dtype=np.uint8)
        panel[:] = (40, 40, 40)  # Dark gray background
        
        # Add monitoring information
        y_pos = 30
        cv2.putText(panel, "MONITORING PANEL", (10, y_pos), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        y_pos += 40
        cv2.putText(panel, f"Faces Detected: {face_count}", (10, y_pos), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0) if face_count == 1 else (0, 0, 255), 2)
        
        y_pos += 30
        cv2.putText(panel, f"Current Scenario:", (10, y_pos), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        y_pos += 25
        cv2.putText(panel, f"{scenarios[current_scenario].title()}", (10, y_pos), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 1)
        
        y_pos += 40
        cv2.putText(panel, "Proctoring Features:", (10, y_pos), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        
        features = [
            "✓ Face Detection",
            "✓ Multiple Person Alert",
            "✓ Real-time Monitoring",
            "✓ Object Detection",
            "✓ Head Pose Tracking",
            "✓ Eye Movement",
            "✓ Anti-spoofing"
        ]
        
        for i, feature in enumerate(features):
            y_pos += 25
            cv2.putText(panel, feature, (20, y_pos), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)
        
        y_pos += 40
        cv2.putText(panel, "Controls:", (10, y_pos), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        y_pos += 25
        cv2.putText(panel, "Press 's' - Next scenario", (20, y_pos), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 0), 1)
        y_pos += 20
        cv2.putText(panel, "Press 'q' - Quit demo", (20, y_pos), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 0), 1)
        
        # Combine demo frame and panel
        combined_frame = np.hstack((demo_frame, panel))
        
        # Display the frame
        cv2.imshow('Online Exam Proctoring - Demo (No Camera)', combined_frame)
        
        # Handle key presses
        key = cv2.waitKey(100) & 0xFF  # 100ms delay for smooth animation
        
        if key == ord('q'):
            print("Exiting demo...")
            break
        elif key == ord('s'):
            current_scenario = (current_scenario + 1) % len(scenarios)
            print(f"Switched to scenario: {scenarios[current_scenario]}")
            frame_count = 0  # Reset frame count for new scenario
        
        # Auto-cycle scenarios every 5 seconds (50 frames at 100ms each)
        if frame_count >= 50:
            current_scenario = (current_scenario + 1) % len(scenarios)
            frame_count = 0
    
    # Cleanup
    cv2.destroyAllWindows()
    print("Demo completed successfully!")
    print("\nTo run with actual webcam, use: python simple_demo.py")

if __name__ == "__main__":
    main()
