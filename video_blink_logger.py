import cv2
import mediapipe as mp
import csv
import os
from eye_utils import average_EAR

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

EAR_THRESHOLD = 0.25
CONSEC_FRAMES = 2

def process_video(video_path, output_name):

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"ERROR: Cannot open {video_path}")
        return

    blink_count = 0
    frame_counter = 0
    log = []
    frame_number = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_number += 1
        h, w, _ = frame.shape

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb)

        if results.multi_face_landmarks:
            for face in results.multi_face_landmarks:
                landmarks = face.landmark
                ear = average_EAR(landmarks, h, w)

                if ear < EAR_THRESHOLD:
                    frame_counter += 1
                else:
                    if frame_counter >= CONSEC_FRAMES:
                        blink_count += 1
                        log.append([frame_number, blink_count])
                    frame_counter = 0

    cap.release()

    os.makedirs("logs", exist_ok=True)
    filename = f"logs/{output_name}.csv"

    with open(filename,'w',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Frame","BlinkCount"])
        writer.writerows(log)

    print(f"Processed: {video_path}")
    print(f"Saved: {filename}")
    print(f"Total Blinks: {blink_count}\n")

# ---- Run Both Videos ----
process_video("videos/reading.MOV", "reading")
process_video("videos/movie.MOV", "movie")