from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import os
import cv2
from student import Student
from train import Train
from detector import FaceDetector
from attendance import AttendancePage  
from tkinter import Toplevel

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")

        self.root.title("face Recogntion system")
        self.root.protocol("WM_DELETE_WINDOW", self.on_close) 
        self.face_detector = None 
        
        #1st image
        img=Image.open(r"C:\Users\saipr\Desktop\sai\win sem 3\information security\face recognition\college_images\BestFacialRecognition.jpg")
        img = img.resize((400, 130), Image.LANCZOS)  

        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=400,height=130)
        
        #2nd image
        img1=Image.open(r"C:\Users\saipr\Desktop\sai\win sem 3\information security\face recognition\college_images\facialrecognition.png")
        img1 = img1.resize((500, 130), Image.LANCZOS)  

        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=400,y=0,width=400,height=130)
        
        #3rd image
        img2=Image.open(r"C:\Users\saipr\Desktop\sai\win sem 3\information security\face recognition\college_images\images.jpg")
        img2 = img2.resize((400, 130), Image.LANCZOS)  

        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=800,y=0,width=400,height=130)
        
        #bg image
        img3=Image.open(r"C:\Users\saipr\Desktop\sai\win sem 3\information security\face recognition\college_images\wp2551980.jpg")
        img3 = img3.resize((1450, 600), Image.LANCZOS)  

        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1450,height=600)
        
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1300,height=35)
        
        #student button
        img4=Image.open(r"C:\Users\saipr\Desktop\sai\win sem 3\information security\face recognition\college_images\student.jpeg")
        img4 = img4.resize((200, 200), Image.LANCZOS)  
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=120,y=80,width=200,height=200)
        
        
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=120,y=250,width=200,height=30)
        
         #detect face button
        img5=Image.open(r"C:\Users\saipr\Desktop\sai\win sem 3\information security\face recognition\college_images\face_detector1.jpg")
        img5 = img5.resize((200, 200), Image.LANCZOS)  
        self.photoimg5=ImageTk.PhotoImage(img5)
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.detect_faces)
        b1.place(x=420,y=80,width=200,height=200)
    
        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.detect_faces,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=420,y=250,width=200,height=30)
        
        
         #attendanceface button
    
        ######
        img6=Image.open(r"C:\Users\saipr\Desktop\sai\win sem 3\information security\face recognition\college_images\Attendance.png")
        img6 = img6.resize((200, 200), Image.LANCZOS)  
        self.photoimg6=ImageTk.PhotoImage(img6)
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.open_attendance_page)
        b1.place(x=720,y=80,width=200,height=200)
        
        
        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.open_attendance_page,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=720,y=250,width=200,height=30)
        
         #help desk button
       
        ######
        img7=Image.open(r"C:\Users\saipr\Desktop\sai\win sem 3\information security\face recognition\college_images\Help.png")
        img7= img7.resize((200, 200), Image.LANCZOS)  
        self.photoimg7=ImageTk.PhotoImage(img7)
        b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=1020,y=80,width=200,height=200)
        
        
        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1020,y=250,width=200,height=30)
        
        
        
        ##############################################################################
            #train button
        img8=Image.open(r"C:\Users\saipr\Desktop\sai\win sem 3\information security\face recognition\college_images\Train.jpg")
        img8 = img8.resize((200, 200), Image.LANCZOS)  
        self.photoimg8=ImageTk.PhotoImage(img8)
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data,)
        b1.place(x=120,y=300,width=200,height=200)
        
        
        b1_1=Button(bg_img,text="Train data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=120,y=500,width=200,height=30)
        
         #Photos button
        img9=Image.open(r"C:\Users\saipr\Desktop\sai\win sem 3\information security\face recognition\college_images\Stragged.jpeg")
        img9 = img9.resize((200, 200), Image.LANCZOS)  
        self.photoimg9=ImageTk.PhotoImage(img9)
        b1=Button(bg_img,image=self.photoimg4,cursor="hand2",command=self.open_image)
        b1.place(x=420,y=300,width=200,height=200)
        
        
        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_image,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=420,y=500,width=200,height=30)
         
         
         #Devloper button
        img10=Image.open(r"C:\Users\saipr\Desktop\sai\win sem 3\information security\face recognition\college_images\developer.jpg")
        img10 = img10.resize((200, 200), Image.LANCZOS)  
        self.photoimg10=ImageTk.PhotoImage(img10)
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=720,y=300,width=200,height=200)
    
        b1_1=Button(bg_img,text="Devlopers",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=720,y=500,width=200,height=30)
        
        
         #Exitbutton
        img11=Image.open(r"C:\Users\saipr\Desktop\sai\win sem 3\information security\face recognition\college_images\exit.jpg")
        img11 = img11.resize((200, 200), Image.LANCZOS)  
        self.photoimg11=ImageTk.PhotoImage(img11)
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.exit_system,)
        b1.place(x=1020,y=300,width=200,height=200)
    
        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.exit_system,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1020,y=500,width=200,height=30)
        
    def open_image(self):
        os.startfile("data")   

        #####################function buttons##############
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)    
    def detect_faces(self):
        if self.face_detector is None:
            self.face_detector = Toplevel(self.root)  # Create a new window for the face detector
            trained_classifier = cv2.face.LBPHFaceRecognizer_create()
            trained_classifier.read("classifier.xml")  # Load the trained classifier
            self.app = FaceDetector(self.face_detector)  # Initialize the FaceDetector instance with the trained classifier
            self.root.withdraw()  # Hide the main window while the face detector is open
            self.face_detector.protocol("WM_DELETE_WINDOW", self.on_detector_close)  # Set a callback to handle window close
            self.face_detector.protocol("WM_DELETE_WINDOW", self.on_detector_close)
    def on_detector_close(self):
        self.root.deiconify()  # Show the main window when the face detector window is closed
        self.face_detector.destroy()  # Destroy the face detector window
        self.face_detector = None  
    def on_close(self):
        if self.face_detector is not None:
            self.face_detector.destroy()  # Destroy the face detector window if it's open
        self.root.destroy()   
    def open_attendance_page(self):
        self.attendance_window = Toplevel(self.root)
        self.attendance_page = AttendancePage(self.attendance_window)    
    def exit_system(self):
        if self.face_detector is not None:
            self.face_detector.destroy()  # Destroy the face detector window if it's open
        self.root.destroy()  # Destroy the main window    
if __name__ =="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()      