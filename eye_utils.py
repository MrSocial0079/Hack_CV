import numpy as np

LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

def compute_EAR(eye_indices, landmarks, h, w):
    pts = [(int(landmarks[i].x*w), int(landmarks[i].y*h)) for i in eye_indices]

    vertical1 = np.linalg.norm(np.array(pts[1]) - np.array(pts[5]))
    vertical2 = np.linalg.norm(np.array(pts[2]) - np.array(pts[4]))
    horizontal = np.linalg.norm(np.array(pts[0]) - np.array(pts[3]))

    EAR = (vertical1 + vertical2) / (2.0 * horizontal)
    return EAR

def average_EAR(landmarks, h, w):
    left = compute_EAR(LEFT_EYE, landmarks, h, w)
    right = compute_EAR(RIGHT_EYE, landmarks, h, w)
    return (left + right) / 2