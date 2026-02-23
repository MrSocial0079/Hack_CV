# Blink Rate Detection Prototype

A computer vision prototype for detecting eye blinks in real-time using webcam feed. This project implements the Eye Aspect Ratio (EAR) algorithm with MediaPipe face landmark detection to count blinks during different activities.

## Features

- Real-time eye landmark detection using MediaPipe FaceMesh
- Blink detection using Eye Aspect Ratio (EAR) with configurable thresholds
- Live overlay showing EAR values, blink count, and eye state
- 60-second experiment mode for comparing blink rates between activities
- CSV logging of experimental results
- Robust detection with debounce logic to avoid false positives

## Installation

Install the required dependencies using pip:

```bash
pip install opencv-python mediapipe numpy
```

## Usage

### 1. Eye Detection Test
Test basic eye landmark detection and face tracking:

```bash
python Eyetest.py
```

**Features:**
- Displays eye landmarks (left eye in green, right eye in blue)
- Shows FPS counter and face detection status
- Prints terminal message when face is first detected
- Press ESC to quit

### 2. Blink Counter
Run real-time blink detection with live statistics:

```bash
python Blinkcount.py
```

**Features:**
- Calculates and displays Eye Aspect Ratio (EAR)
- Counts blinks with debounce logic
- Shows eye state (OPEN/CLOSED) and face detection status
- Prints total blink count on exit
- Press ESC to quit

### 3. Experiment Runner
Run timed experiments to measure blink rates during different activities:

```bash
# Reading mode (60 seconds)
python main_hack.py --mode reading

# Movie mode (60 seconds)
python main_hack.py --mode movie

# Custom duration (30 seconds)
python main_hack.py --mode reading --duration 30

# Different camera index
python main_hack.py --mode movie --camera 1
```

**Features:**
- 3-second countdown before experiment starts
- Live progress bar and statistics
- Saves results to `results.csv`
- Supports early termination with ESC
- Calculates blinks per second and per minute

## Command Line Arguments

### main_hack.py

- `--mode`: Experiment mode (`reading` or `movie`) **[required]**
- `--duration`: Duration in seconds (default: 60)
- `--camera`: Camera index (default: 0)

## Understanding the Algorithm

### Eye Aspect Ratio (EAR)

The Eye Aspect Ratio is calculated using 6 landmarks around each eye:

```
EAR = (|A| + |B|) / (2 * |C|)
```

Where:
- A = distance between vertical eye points (top to bottom)
- B = distance between second pair of vertical eye points  
- C = distance between horizontal eye points (left to right)

**Blink Detection Logic:**
1. EAR drops below threshold (0.25) → eye considered "closed"
2. Must stay below threshold for N consecutive frames (3) to count as blink
3. Blink counted only on transition from closed → open

This debounce logic prevents false positives from rapid EAR fluctuations.

## Troubleshooting

### Camera Issues

**Problem:** "Could not open camera" error
**Solutions:**
- Try different camera indices: `--camera 1`, `--camera 2`, etc.
- Check if camera is being used by another application
- Ensure camera permissions are granted

**Find available cameras:**
```python
import cv2
for i in range(5):
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print(f"Camera {i} is available")
        cap.release()
```

### Face Detection Issues

**Problem:** "No face detected" message
**Solutions:**
- Ensure good lighting (avoid backlighting)
- Position face clearly in front of camera
- Remove glasses if they cause reflection issues
- Try different distances from camera (2-4 feet optimal)

### Blink Detection Issues

**Problem:** Too many/few blinks detected
**Solutions:**
- Adjust `EAR_THRESHOLD` in the code (default: 0.25)
  - Lower value = less sensitive (fewer blinks)
  - Higher value = more sensitive (more blinks)
- Adjust `CONSECUTIVE_FRAMES` (default: 3)
  - Higher value = more debounce (fewer false positives)
  - Lower value = more responsive (may catch false positives)

### Performance Issues

**Problem:** Low FPS or lag
**Solutions:**
- Close other applications using the camera
- Reduce webcam resolution if possible
- Ensure adequate CPU resources available

## File Structure

```
blink-rate-prototype/
├── Eyetest.py          # Basic eye landmark detection test
├── Blinkcount.py       # Real-time blink counter with EAR
├── main_hack.py        # Experiment runner with CSV logging
├── README.md           # This file
└── results.csv         # Generated experiment results
```

## CSV Output Format

The `results.csv` file contains:

| Column | Description |
|--------|-------------|
| timestamp | Date and time of experiment |
| mode | "reading" or "movie" |
| duration_seconds | Actual experiment duration |
| total_blinks | Number of blinks detected |
| blinks_per_sec | Blink rate (blinks/second) |
| blinks_per_min | Blink rate (blinks/minute) |

## Technical Notes

- **MediaPipe FaceMesh**: Uses 468 facial landmarks for precise eye tracking
- **No GPU required**: Runs on CPU with real-time performance
- **Robust lighting**: Works in typical indoor classroom lighting
- **Cross-platform**: Compatible with Windows, macOS, and Linux

## Expected Results

Typical blink rates:
- **Normal conversation**: 15-20 blinks/minute
- **Reading**: 5-10 blinks/minute (reduced during concentration)
- **Screen watching**: 5-15 blinks/minute (varies with content)

Use the experiment runner to compare your personal blink rates between reading and movie watching activities!
