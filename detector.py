from tkinter import *
from PIL import Image, ImageTk
import cv2
import numpy as np
import csv
from datetime import datetime

class FaceDetector:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Face Detection")

        self.canvas = Canvas(self.root, width=800, height=600)
        self.canvas.pack()

        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        self.cap = cv2.VideoCapture(0)

        self.trained_classifier = cv2.face.LBPHFaceRecognizer_create()
        self.trained_classifier.read("classifier.xml")  # Load the trained classifier

        self.recorded_ids = {}  # Dictionary to store recorded IDs for each hour

        self.detect_faces()

    def detect_faces(self):
        current_hour = datetime.now().strftime('%Y-%m-%d_%H')

        ret, frame = self.cap.read()

        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            for (x, y, w, h) in faces:
                face_roi = gray[y:y+h, x:x+w]
                label, confidence = self.trained_classifier.predict(face_roi)

                if confidence < 70:  # Threshold for recognizing face
                    if current_hour not in self.recorded_ids:
                        self.recorded_ids[current_hour] = set()

                    if label not in self.recorded_ids[current_hour]:  # Check if ID not recorded for this hour
                        self.recorded_ids[current_hour].add(label)

                        # Save attendance to CSV
                        filename = f"attendance/{current_hour}.csv"

                        with open(filename, 'a', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerow([label, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Present"])

                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(frame, str(label), (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame_rgb)
            imgtk = ImageTk.PhotoImage(image=img)

            self.canvas.create_image(0, 0, anchor=NW, image=imgtk)
            self.canvas.imgtk = imgtk

        self.root.after(10, self.detect_faces)


if __name__ == "__main__":
    root = Tk()
    obj = FaceDetector(root)
    root.mainloop()
