from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from tkinter import messagebox
import datetime
from detector import FaceDetector  # Assuming detector.py contains the FaceDetector class

class AttendancePage:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance System")

        title_lbl = Label(self.root, text="ATTENDANCE SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1300, height=35)

        img_top = Image.open(r"C:\Users\saipr\Desktop\sai\win sem 3\information security\face recognition\college_images\facialrecognition.png")  # Update the image path
        img_top = img_top.resize((1300, 220), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=40, width=1300, height=220)

        b1_1 = Button(self.root, text="Take Attendance", command=self.take_attendance, cursor="hand2",
                      font=("times new roman", 25, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=0, y=250, width=650, height=50)

        b1_2 = Button(self.root, text="Import Attendance File", command=self.import_attendance, cursor="hand2",
                      font=("times new roman", 25, "bold"), bg="darkblue", fg="white")
        b1_2.place(x=650, y=250, width=650, height=50)

        img_bottom = Image.open(r"C:\Users\saipr\Desktop\sai\win sem 3\information security\face recognition\college_images\wp2551980.jpg")  # Update the image path
        img_bottom = img_bottom.resize((1300, 420), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=300, width=1300, height=420)

    def take_attendance(self):
        # Initialize the face detector
        detector_window = Toplevel(self.root)
        face_detector = FaceDetector(detector_window)
        detector_window.protocol("WM_DELETE_WINDOW", lambda: self.on_close(face_detector))

    def import_attendance(self):
        os.startfile("attendance")  # Open the attendance folder in the file explorer

    def on_close(self, face_detector):
        face_detector.root.destroy()


if __name__ == "__main__":
    root = Tk()
    app = AttendancePage(root)
    root.mainloop()
