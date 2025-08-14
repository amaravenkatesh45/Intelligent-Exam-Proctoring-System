#!/usr/bin/env python3
"""
Simplified Demo of Online Exam Proctoring System
This demo shows basic webcam functionality without complex dependencies
"""

import cv2
import numpy as np
import sys
import os

def main():
    print("=== Online Exam Proctoring System - Demo ===")
    print("This is a simplified demo showing basic webcam functionality")
    print("Press 'q' to quit")
    print("=" * 50)
    
    # Initialize webcam with multiple fallback options
    video_capture = None
    camera_indices = [0, 1, 2, -1]  # Try different camera indices

    for idx in camera_indices:
        try:
            print(f"Trying camera index {idx}...")
            if idx == -1:
                # Try DirectShow backend on Windows
                video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
            else:
                video_capture = cv2.VideoCapture(idx)

            if video_capture.isOpened():
                # Test if we can actually read a frame
                ret, test_frame = video_capture.read()
                if ret and test_frame is not None:
                    print(f"Successfully connected to camera {idx}")
                    break
                else:
                    video_capture.release()
                    video_capture = None
            else:
                if video_capture:
                    video_capture.release()
                video_capture = None
        except Exception as e:
            print(f"Failed to connect to camera {idx}: {e}")
            if video_capture:
                video_capture.release()
            video_capture = None

    if video_capture is None:
        print("Error: Could not access any webcam")
        print("Troubleshooting tips:")
        print("1. Check if camera is being used by another application")
        print("2. Check camera permissions in Windows Settings")
        print("3. Try running as administrator")
        print("4. Make sure camera drivers are installed")
        return

    # Configure camera settings for better performance
    try:
        video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        video_capture.set(cv2.CAP_PROP_FPS, 30)
        video_capture.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        print("Camera configured: 640x480 @ 30fps")
    except Exception as e:
        print(f"Warning: Could not configure camera settings: {e}")
    
    # Check if required model files exist
    models_dir = "models"
    required_files = [
        "opencv_face_detector_uint8.pb",
        "opencv_face_detector.pbtxt"
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(os.path.join(models_dir, file)):
            missing_files.append(file)
    
    if missing_files:
        print(f"Warning: Missing model files: {missing_files}")
        print("Face detection will be limited")
    
    # Load face detection model if available
    face_detector = None
    try:
        if not missing_files:
            face_detector = cv2.dnn.readNetFromTensorflow(
                os.path.join(models_dir, "opencv_face_detector_uint8.pb"),
                os.path.join(models_dir, "opencv_face_detector.pbtxt")
            )
            print("Face detection model loaded successfully")
    except Exception as e:
        print(f"Could not load face detection model: {e}")
    
    frame_count = 0
    
    while True:
        # Capture frame
        ret, frame = video_capture.read()
        if not ret:
            print("Error: Could not read frame")
            break
        
        frame_count += 1
        
        # Create a copy for processing
        display_frame = frame.copy()
        
        # Basic face detection using OpenCV's built-in cascade (if available)
        try:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # Try to use Haar cascade for basic face detection
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            
            # Draw rectangles around faces
            for (x, y, w, h) in faces:
                cv2.rectangle(display_frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                cv2.putText(display_frame, "Face Detected", (x, y-10), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
            
            # Display basic monitoring info
            cv2.putText(display_frame, f"Faces: {len(faces)}", (10, 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(display_frame, f"Frame: {frame_count}", (10, 60), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            
            # Basic alerts
            if len(faces) == 0:
                cv2.putText(display_frame, "ALERT: No face detected!", (10, 100), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            elif len(faces) > 1:
                cv2.putText(display_frame, "ALERT: Multiple faces detected!", (10, 100), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            else:
                cv2.putText(display_frame, "Status: Normal", (10, 100), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                
        except Exception as e:
            cv2.putText(display_frame, f"Error: {str(e)[:50]}", (10, 130), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        
        # Display the frame
        cv2.imshow('Online Exam Proctoring - Demo', display_frame)
        
        # Check for quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Exiting...")
            break
    
    # Cleanup
    video_capture.release()
    cv2.destroyAllWindows()
    print("Demo completed successfully!")

if __name__ == "__main__":
    main()
