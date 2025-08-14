# Setup Guide for Intelligent Online Exam Proctoring System

## Quick Start

### 1. Prerequisites
- Python 3.7 or higher
- Webcam (for testing)
- Git (for version control)

### 2. Basic Setup (Simplified Demo)

```bash
# Clone the repository (after pushing to GitHub)
git clone <your-github-repo-url>
cd Intelligent-Online-Exam-Proctoring-System

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install basic dependencies
pip install opencv-python numpy matplotlib

# Run the simplified demo
cd Code
python simple_demo.py
```

### 3. Full Setup (Advanced)

For the complete functionality, you'll need additional dependencies:

```bash
# Install CMake (required for dlib)
pip install cmake

# Install face recognition libraries (requires Visual C++ Build Tools on Windows)
pip install dlib face-recognition

# Install machine learning libraries
pip install tensorflow keras scikit-learn

# Install all requirements
pip install -r requirements.txt
```

### 4. Download Model Files

Some model files are too large for Git and need to be downloaded separately:

1. **YOLOv3 Weights**: Download from the Google Drive link in `Code/models/link.txt`
   - Save as `Code/models/yolov3.weights`

2. **Additional Models**: Check the `models/` directory for any missing `.hdf5` or `.pkl` files

### 5. Running the System

#### Simple Demo (Basic webcam functionality)
```bash
cd Code
python simple_demo.py
```

#### Full System (All features)
```bash
cd Code
python online_proctoring_system.py
```

## Troubleshooting

### Common Issues

1. **"No module named 'dlib'"**
   - Install Visual C++ Build Tools from Microsoft
   - Or use pre-compiled wheels: `pip install dlib-binary`

2. **"CMake is not installed"**
   - Install CMake from cmake.org
   - Add to PATH during installation

3. **Webcam not working**
   - Check camera permissions
   - Try different camera index in code (0, 1, 2, etc.)

4. **Missing model files**
   - Download from the provided Google Drive links
   - Place in the correct `models/` directory

### System Requirements

- **Minimum**: Python 3.7, 4GB RAM, Basic webcam
- **Recommended**: Python 3.8+, 8GB RAM, HD webcam, GPU support

## Features

- **Face Detection**: Detects faces in real-time
- **Face Recognition**: Identifies registered students
- **Object Detection**: Detects prohibited items
- **Head Pose Estimation**: Monitors head movement
- **Eye Tracking**: Basic gaze detection
- **Mouth Movement**: Detects speaking
- **Face Spoofing Detection**: Anti-spoofing measures

## Project Structure

```
├── Code/
│   ├── models/              # AI models and weights
│   ├── student_db/          # Student face database
│   ├── online_proctoring_system.py  # Main application
│   ├── simple_demo.py       # Simplified demo
│   ├── requirements.txt     # Python dependencies
│   └── *.py                 # Supporting modules
├── Documentation/           # Project documentation
├── New_Functionalities/     # Additional features
└── README.md               # Project overview
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is for educational purposes. Please check the original repository for license information.
