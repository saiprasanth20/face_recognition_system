from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import os
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")

        self.root.title("face Recogntion system")
        
        #=================variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_registration_no=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        
         #1st image
        img=Image.open(r"C:\Users\saipr\Desktop\sai\win sem 3\information security\face recognition\college_images\facial_recognition_action.jpg")
        img = img.resize((400, 130), Image.LANCZOS)  

        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=400,height=130)
        
        #2nd image
        img1=Image.open(r"C:\Users\saipr\Desktop\sai\win sem 3\information security\face recognition\college_images\smart-attendance.jpg")
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
        
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1300,height=35)
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=45,width=1400,height=600)
        #left label
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=600,height=580)
        
        img_left=Image.open(r"C:\Users\saipr\Desktop\sai\win sem 3\information security\face recognition\college_images\AdobeStock_303989091.jpeg")
        img_left = img_left.resize((720, 130), Image.LANCZOS)  

        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=580,height=130)
        
        #cureent course
        Current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        Current_course_frame.place(x=5,y=135,width=580,height=130)
        #department
        dep_label=Label(Current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=5)
        dep_combo=ttk.Combobox(Current_course_frame,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","SENSE","SCOPE","VISH","LAW")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        #course
        course_label=Label(Current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=5)
        course_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        course_combo["values"]=("Select Course","CSE","ECE","MGT","LAW")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        #Year
        year_label=Label(Current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=5)
        year_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly")
        year_combo["values"]=("Select Year","1st year","2nd year","3rd year","4th year")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
           #semester
        semester_label=Label(Current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=5)
        semester_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly")
        semester_combo["values"]=("Select Semester","1st sem","2nd sem")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        #Class student information
        Class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        Class_Student_frame.place(x=5,y=265,width=580,height=250)
        #student id
        studentId_label=Label(Class_Student_frame,text="StudentId:",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        studentId_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_registration_no,width=15,font=("times new roman",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=5,sticky=W)
        
        #student name
        
        studentName_label=Label(Class_Student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)
        studentName_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_std_name,width=15,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=5,sticky=W)
        
        ##################
        #class division
        class_div_label=Label(Class_Student_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)
        #class_div_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_div,width=15,font=("times new roman",12,"bold"))
        #class_div_entry.grid(row=1,column=1,padx=10,sticky=W)
        class_div_combo=ttk.Combobox(Class_Student_frame,textvariable=self.var_div,width=15,font=("times new roman",12,"bold"),state="readonly")
        class_div_combo["values"]=("Select Division","A","B","C","D")
        class_div_combo.current(0)
        class_div_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)
        
        #ROLL NO
        
        roll_no_label=Label(Class_Student_frame,text="Roll No :",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)
        roll_no_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_roll,width=15,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=5,sticky=W)
        
        ##################
        #gender
        gender_label=Label(Class_Student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)
        #gender_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_gender,width=15,font=("times new roman",12,"bold"))
        #gender_entry.grid(row=2,column=1,padx=10,sticky=W)
        gender_combo=ttk.Combobox(Class_Student_frame,textvariable=self.var_gender,width=15,font=("times new roman",12,"bold"),state="readonly")
        gender_combo["values"]=("Select Gender","Male","Female","Other","Not to say")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=5,sticky=W)
        
        #dob
        
        dob_label=Label(Class_Student_frame,text="DOB :",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)
        dob_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_dob,width=15,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=5,sticky=W)
        
        
        #####################
        #email
        email_label=Label(Class_Student_frame,text="Email ID:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)
        email_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_email,width=15,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=5,sticky=W)
        
        #phone number
        
        phoneNo_label=Label(Class_Student_frame,text="Phone number :",font=("times new roman",12,"bold"),bg="white")
        phoneNo_label.grid(row=3,column=2,padx=5,pady=5,sticky=W)
        phoneNo_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_phone,width=15,font=("times new roman",12,"bold"))
        phoneNo_entry.grid(row=3,column=3,padx=5,sticky=W)
        
        
        #radio button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1,text="Take photo sample",value="Yes",width=15)
        radiobtn1.grid(row=5,column=0)
        
        radiobtn2=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1,text="No photo sample",value="No",width=15)
        radiobtn2.grid(row=5,column=1)
        
        #buttons frame
        btn_frame=Frame(Class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=170,width=570,height=50)
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        update_btn=Button(btn_frame,text="Update",width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        Take_photo_sample_btn=Button(btn_frame,text="Take photo sample",command=self.generate_dataset,width=15,font=("times new roman",12,"bold"),bg="red",fg="white")
        Take_photo_sample_btn.grid(row=1,column=0)
        update_photo_sample_btn=Button(btn_frame,text="Update photo sample",command=self.update_data,width=15,font=("times new roman",12,"bold"),bg="red",fg="white")
        update_photo_sample_btn.grid(row=1,column=2)
        
        
        #rightlabel
        RIGHT_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        RIGHT_frame.place(x=620,y=10,width=620,height=580)
        
       
        
        img_right=Image.open(r"C:\Users\saipr\Desktop\sai\win sem 3\information security\face recognition\college_images\student.jpeg")
        img_right = img_right.resize((720, 130), Image.LANCZOS)  

        self.photoimg_right=ImageTk.PhotoImage(img_right)
        
        f_lbl=Label(RIGHT_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=580,height=130)
         ########### search system
        Search_frame=LabelFrame(RIGHT_frame,bd=2,bg="white",relief=RIDGE,text="Search system",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=135,width=580,height=70) 
        
        search_label=Label(Search_frame,text="Search By:",font=("times new roman",13,"bold"),bg="red",fg="White")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        search_combo=ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),state="readonly",width=10)
        search_combo["values"]=("Select","Roll no","Phone no")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        search_entry=ttk.Entry(Search_frame,width=10,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,sticky=W)
        
        
        search_btn=Button(Search_frame,text="Search",width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)
        showAll_btn=Button(Search_frame,text="Show All",width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)
        
        ###table frame
        table_frame=Frame(RIGHT_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=580,height=280)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL) 
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=("department","course","year","semester","registration no","name","div","roll","gender","phone","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

# Corrected the heading lines
        self.student_table.heading("department", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("semester", text="Semester")  # corrected spelling
        self.student_table.heading("registration no", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("photo", text="PhotoSampleStatus")

        self.student_table["show"] = "headings"
        self.student_table.column("department", width=100)  # corrected column identifier
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    
    ##################function declaration###########
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_registration_no.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="123456789",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                            self.var_dep.get(),
                                                                            self.var_year.get(),
                                                                            self.var_course.get(),
                                                                            self.var_semester.get(),
                                                                            self.var_registration_no.get(),
                                                                            self.var_std_name.get(),
                                                                            self.var_div.get(),
                                                                            self.var_roll.get(),
                                                                            self.var_gender.get(),
                                                                            self.var_dob.get(),
                                                                            self.var_email.get(),
                                                                            self.var_phone.get(),
                                                                            self.var_radio1.get()
                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been addes successfuly",parent=self.root)   
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
            
    ############## fetch
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="123456789",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()  
    ###############get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_dep.set(data[0]),            
        self.var_year.set(data[1]),
        self.var_course.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_registration_no.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_radio1.set(data[12])
        
        
        ####update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="123456789",database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set department=%s,course=%s,year=%s,semester=%s,registration_no=%s,name=%s,division=%s,roll=%s,gender=%s,dob=%s,email=%s,phone_no=%s,photosample=%s where registraion_no=%s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_radio1.get(),
                        self.var_registration_no.get()
                        
                        ))
                else:
                    if  not Update:
                         return   
                messagebox.showinfo("Success","Student details successfully updated completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    ##########delete function
    def delete_data(self):
        if self.var_registration_no.get()=="":
            messagebox.showerror("Error ","student id must be require",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("student details page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="123456789",database="face_recognition")
                    my_cursor=conn.cursor()
                    sql="delete from student where registration_no=%s"
                    val=(self.var_registration_no.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","successfully deleted student details",parent=self.root)    
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)            
             ##########reset function
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_year.set("select Course"),
        self.var_course.set("select Year"),
        self.var_semester.set("Select semester"),
        self.var_registration_no.set(""),
        self.var_std_name.set(""),
        self.var_div.set("select division"),
        self.var_roll.set(""),
        self.var_gender.set("select gender"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_radio1.set("")
       #========================== generate data set and take a photo sample ============
    def generate_dataset(self):
        if self.var_registration_no.get() == "":
            messagebox.showerror("Error", "Registration number is required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="123456789", database="face_recognition")
                my_cursor = conn.cursor()   
                my_cursor.execute("select * from student where registration_no=%s", (self.var_registration_no.get(),))
                data = my_cursor.fetchone()
            
                if data is not None:
                    registration_no = data[4]  # Get the registration number from the database
                    face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
                    cap = cv2.VideoCapture(0)
                    img_id = 0
                
                    while True:
                        ret, my_frame = cap.read()
                        if self.face_cropped(my_frame, face_classifier) is not None:  # Call to face_cropped function
                            img_id += 1
                            face = cv2.resize(self.face_cropped(my_frame, face_classifier), (450, 450))  # Call to face_cropped function
                            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                            file_name_path = f"data/user.{registration_no}.{img_id}.jpg"  # Change the filename format
                            cv2.imwrite(file_name_path, face)
                            cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                            cv2.imshow("Cropped Face", face)

                        if cv2.waitKey(1) == 13 or int(img_id) == 100:
                            break
                        
                    cap.release()
                    cv2.destroyAllWindows()
                
                    messagebox.showinfo("Result", "Generating Datasets completed")
                
                else:
                    messagebox.showerror("Error", "Student with this registration number does not exist", parent=self.root)
            
                conn.close()  
            
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    def face_cropped(self, img, face_classifier):  # Define the face_cropped function
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            face_cropped = img[y:y+h, x:x+w]
            return face_cropped
                                     
if __name__ =="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()  