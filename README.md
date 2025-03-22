# Virtual Mouse

## Introduction
The **Virtual Mouse** project leverages **OpenCV**, **Mediapipe**, and **PyAutoGUI** to simulate mouse operations through hand gestures. It uses a webcam to track hand landmarks and translates gestures into actions like cursor movement and clicking.

## Features
- **Cursor Control**: Move the mouse using your index finger.
- **Clicking**: Perform clicks by bringing the thumb and index finger close together.
- **Visual Feedback**: Circles indicate movement and click actions.

## Technologies Used
- **Python**
- **OpenCV** (Computer Vision)
- **Mediapipe** (Hand Tracking)
- **PyAutoGUI** (Mouse Control)

## Installation

### Prerequisites
Ensure you have **Python 3.7 or higher** installed.

### Install Required Libraries
```bash
pip install opencv-python mediapipe pyautogui
```

## How to Run
1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Run the script:
```bash
python virtual_mouse.py
```

## How It Works
- **Hand Tracking**: Mediapipe identifies hand landmarks.
- **Coordinate Mapping**: Screen dimensions are mapped to frame dimensions.
- **Cursor Movement**: The index finger controls the cursor.
- **Clicking Mechanism**: The thumb and index finger proximity trigger a click.


## Future Enhancements
- **Right-Click and Drag**: Additional gesture controls.
- **Scrolling**: Use vertical finger movement for scrolling.
