import cv2
import mediapipe as mp


mp_face_detec = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

with mp_face_detec.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
 
        
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        
        results = face_detection.process(rgb_frame)

        
        if results.detections:
            for detection in results.detections:
                mp_drawing.draw_detection(frame, detection)

        
        cv2.imshow('Face Detection', frame)

        # Break the loop if 's' is pressed on the keyboard
        if cv2.waitKey(5) & 0xFF == ord('s'):
            break


cap.release()
cv2.destroyAllWindows()
