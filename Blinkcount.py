import cv2
import mediapipe as mp
import time
from eye_utils import average_EAR

EAR_THRESHOLD = 0.25
CONSEC_FRAMES = 2

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

cap = cv2.VideoCapture(0)

blink_count = 0
frame_counter = 0
closed = False

while True:
    ret, frame = cap.read()
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
                frame_counter = 0

            cv2.putText(frame, f"EAR: {round(ear,3)}",
                        (30,50), cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
            cv2.putText(frame, f"Blinks: {blink_count}",
                        (30,100), cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2)

    cv2.imshow("Blink Counter", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
print("Total Blinks:", blink_count)