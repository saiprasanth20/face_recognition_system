from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from tkinter import messagebox
import numpy as np
import cv2

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="TRAIN DATASET", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1300, height=35)

        img_top = Image.open(r"C:\Users\saipr\Desktop\sai\win sem 3\information security\face recognition\college_images\facialrecognition.png")
        img_top = img_top.resize((1300, 220), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=40, width=1300, height=220)

        b1_1 = Button(self.root, text="Train Data", command=self.train_classifier, cursor="hand2",
                      font=("times new roman", 25, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=0, y=250, width=1300, height=50)

        img_bottom = Image.open(r"C:\Users\saipr\Desktop\sai\win sem 3\information security\face recognition\college_images\wp2551980.jpg")
        img_bottom = img_bottom.resize((1300, 420), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=300, width=1300, height=420)

    def train_classifier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image_path in path:
            try:
                img = Image.open(image_path).convert('L')  # Convert to grayscale
                image_np = np.array(img, 'uint8')  # Convert PIL image to NumPy array
                id_str = os.path.split(image_path)[1].split('.')[1]  # Extract ID from filename
                try:
                    id = int(id_str)
                    faces.append(image_np)
                    ids.append(id)
                except ValueError:
                    messagebox.showwarning("Warning", f"Skipping file {image_path}: Invalid ID format")
            except Exception as e:
                messagebox.showerror("Error", f"Error in reading image {image_path}: {str(e)}")

        ids = np.array(ids)

        # Train classifier
        try:
            recognizer = cv2.face.LBPHFaceRecognizer_create()  # Create LBPH recognizer
            recognizer.train(faces, ids)  # Train the recognizer
            recognizer.save("classifier.xml")  # Save the trained model
            messagebox.showinfo("Result", "Training dataset completed")
        except Exception as e:
            messagebox.showerror("Error", f"Error in training classifier: {str(e)}")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
