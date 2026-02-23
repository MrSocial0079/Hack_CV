import cv2
import mediapipe as mp
from eye_utils import LEFT_EYE, RIGHT_EYE

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    h, w, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:
        for face in results.multi_face_landmarks:
            landmarks = face.landmark

            for i in LEFT_EYE:
                x = int(landmarks[i].x*w)
                y = int(landmarks[i].y*h)
                cv2.circle(frame,(x,y),2,(0,255,0),-1)

            for i in RIGHT_EYE:
                x = int(landmarks[i].x*w)
                y = int(landmarks[i].y*h)
                cv2.circle(frame,(x,y),2,(255,0,0),-1)

    cv2.imshow("Eye Detection Validation", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()