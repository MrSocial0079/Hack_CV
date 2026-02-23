import cv2
import mediapipe as mp
import time
import csv
import os
from eye_utils import average_EAR

mp_face_mesh = mp.solutions.face_mesh
mp_hands = mp.solutions.hands

face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)
hands = mp_hands.Hands()

EAR_THRESHOLD = 0.25
CONSEC_FRAMES = 2

blink_count = 0
frame_counter = 0
recording = False
log = []

# --- MAC CAMERA FIX ---
cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

if not cap.isOpened():
    print("ERROR: Camera not accessible")
    exit()

# Warm up camera
time.sleep(2)

def is_open_palm(hand_landmarks):
    tips = [8,12,16,20]
    return all(hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip-2].y for tip in tips)

def is_fist(hand_landmarks):
    tips = [8,12,16,20]
    return all(hand_landmarks.landmark[tip].y > hand_landmarks.landmark[tip-2].y for tip in tips)

print("\nShow OPEN PALM to START recording")
print("Show FIST to STOP recording\n")

while True:
    ret, frame = cap.read()

    # --- Prevent crash ---
    if not ret or frame is None:
        print("Waiting for camera frame...")
        continue

    h, w, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_results = face_mesh.process(rgb)
    hand_results = hands.process(rgb)

    # ---- Gesture Detection ----
    if hand_results.multi_hand_landmarks:
        for handL in hand_results.multi_hand_landmarks:
            if is_open_palm(handL):
                recording = True
                print("Recording Started")

            if is_fist(handL):
                recording = False
                print("Recording Stopped")
                break

    # ---- Blink Detection ----
    if recording and face_results.multi_face_landmarks:
        for face in face_results.multi_face_landmarks:
            landmarks = face.landmark
            ear = average_EAR(landmarks, h, w)

            if ear < EAR_THRESHOLD:
                frame_counter += 1
            else:
                if frame_counter >= CONSEC_FRAMES:
                    blink_count += 1
                    log.append([time.time(), blink_count])
                frame_counter = 0

            cv2.putText(frame, f"EAR: {round(ear,3)}",
                        (30,50), cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

            cv2.putText(frame, f"Blinks: {blink_count}",
                        (30,100), cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2)

            status = "REC" if recording else "IDLE"
            cv2.putText(frame, f"Status: {status}",
                        (30,150), cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2)

    cv2.imshow("Blink Recorder", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

# ---- Save Log ----
task = input("Enter task name (reading / watching): ")

os.makedirs("logs", exist_ok=True)
filename = f"logs/{task}.csv"

with open(filename,'w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Timestamp","BlinkCount"])
    writer.writerows(log)

print("Log saved:", filename)