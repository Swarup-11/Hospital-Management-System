from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from fpdf import FPDF
from tkinter import filedialog
import random
import time
import datetime
import mysql.connector


class Hospital:
    def __init__(self,root):
        self.root = root
        self.root.title("HOSPITAL MANAGEMENT SYSTEM")
        self.root.geometry("1280x800+0+0")
        self.root.state('zoomed')
 

        #Variable Create=====
        self.PatientId=StringVar()
        self.PatientName=StringVar()
        self.DOB=StringVar()
        self.Age=StringVar()
        self.Gender=StringVar()
        self.BloodGroup=StringVar()
        self.ContactNumber=StringVar()
        self.SideEffect=StringVar()
        self.BP=StringVar()
        self.HR=StringVar()
        self.weight=StringVar()
        self.TabletName=StringVar()
        self.Address=StringVar()
        self.NoofTablet=StringVar()
        self.height=StringVar()
        self.furtherInfo=StringVar()

        

        label_title = Label(self.root,bd=15,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white",font=("times new roman",50,"bold"))
        label_title.pack(side=TOP,fill=X)

        #*********DataFrame*********
        Dataframe = Frame(self.root,bd=15,relief=RIDGE)
        Dataframe.place(x=0,y=110,width=1280,height=340)

        DataFrameLeft = LabelFrame(Dataframe,bd=8,relief=RIDGE,padx=10,
                                                        font=("times new roman",12,"bold"),text="Patient Information:")
        DataFrameLeft.place(x=7,y=5,width=700,height=290)

        DataFrameRight=LabelFrame(Dataframe,bd=8,relief=RIDGE,padx=10,
                                                        font=("times new roman",12,"bold"),text="Prescription:")
        DataFrameRight.place(x=720,y=5,width=520,height=290)


        #***********Buttons Frame**********************
        Buttonframe = Frame(self.root,bd=15,relief=RIDGE)
        Buttonframe.place(x=0,y=450,width=1280,height=60)

        #***********Details Frame**********************
        Detailsframe = Frame(self.root,bd=15,relief=RIDGE)
        Detailsframe.place(x=0,y=510,width=1280,height=182)

        #===============DataFrameLeft=================
        labelPatientId = Label(DataFrameLeft,font=("arial",10,"bold"),text="Patient ID:",padx=2,pady=6)
        labelPatientId.grid(row=0,column=0,sticky=W)
        txtpatientid = Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.PatientId,width=25)
        txtpatientid.grid(row=0,column=1)

        labelName = Label(DataFrameLeft,font=("arial",10,"bold"),text="Name of Patient:",padx=2,pady=6)
        labelName.grid(row=1,column=0,sticky=W)
        txtName = Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.PatientName,width=25)
        txtName.grid(row=1,column=1)

        labeldob = Label(DataFrameLeft,font=("arial",10,"bold"),text="Date of birth:",padx=2,pady=6)
        labeldob.grid(row=2,column=0,sticky=W)
        txtdob = Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.DOB,width=25)
        txtdob.grid(row=2,column=1) 

        labelAge = Label(DataFrameLeft,font=("arial",10,"bold"),text="Patient Age:",padx=2,pady=6)
        labelAge.grid(row=3,column=0,sticky=W)
        txtAge = Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.Age,width=25)
        txtAge.grid(row=3,column=1)

        labelGender = Label(DataFrameLeft,font=("arial",10,"bold"),text="Patient Gender:",padx=2,pady=6)
        labelGender.grid(row=4,column=0,sticky=W)
        comGender=ttk.Combobox(DataFrameLeft,textvariable=self.Gender,state="randonly",font=("arial",10,"bold"),width=23)
        comGender['value']=("Male","Female","Transgender")
        comGender.set('')
        comGender.grid(row=4,column=1)

        labelBloodGroup = Label(DataFrameLeft,font=("arial",10,"bold"),text="Blood Group:",padx=2,pady=6)
        labelBloodGroup.grid(row=5,column=0,sticky=W)
        comBloodGroup=ttk.Combobox(DataFrameLeft,textvariable=self.BloodGroup,state="randonly",font=("arial",10,"bold"),width=23)
        comBloodGroup['value']=("O+","O","A+","A-","B+","B-","AB+","AB-")
        comBloodGroup.set('')
        comBloodGroup.grid(row=5,column=1)

        labelContactNUmber = Label(DataFrameLeft,font=("arial",10,"bold"),text="Contact Number:",padx=2,pady=6)
        labelContactNUmber.grid(row=6,column=0,sticky=W)
        txtContactNumber = Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.ContactNumber,width=25)
        txtContactNumber.grid(row=6,column=1)

        labelSideEffect = Label(DataFrameLeft,font=("arial",10,"bold"),text="Side Effects:",padx=2,pady=6)
        labelSideEffect.grid(row=7,column=0,sticky=W)
        txtSideEffect = Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.SideEffect,width=25)
        txtSideEffect.grid(row=7,column=1)

        


        labelBP= Label(DataFrameLeft,font=("arial",10,"bold"),text="Blood Pressure:",padx=10,pady=6)
        labelBP.grid(row=0,column=2,sticky=W)
        txtBP = Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.BP,width=25)
        txtBP.grid(row=0,column=3)

        labelHeartRate= Label(DataFrameLeft,font=("arial",10,"bold"),text="Heart Rate:",padx=10,pady=6)
        labelHeartRate.grid(row=1,column=2,sticky=W)
        txtHeartRate = Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.HR,width=25)
        txtHeartRate.grid(row=1,column=3)

        labelWeight= Label(DataFrameLeft,font=("arial",10,"bold"),text="Weight:",padx=10,pady=6)
        labelWeight.grid(row=2,column=2,sticky=W)
        txtWeight = Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.weight,width=25)
        txtWeight.grid(row=2,column=3)

        labelTabletName= Label(DataFrameLeft,font=("arial",10,"bold"),text="Tablet Names:",padx=10,pady=6)
        labelTabletName.grid(row=3,column=2,sticky=W)
        txtTabletName = Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.TabletName,width=25)
        txtTabletName.grid(row=3,column=3)

        labelAddress = Label(DataFrameLeft,font=("arial",10,"bold"),text="Address:",padx=10,pady=6)
        labelAddress.grid(row=4,column=2,sticky=W)
        txtAddress = Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.Address,width=25)
        txtAddress.grid(row=4,column=3)

        labelNoOfTablet = Label(DataFrameLeft,font=("arial",10,"bold"),text="No Of Tablet:",padx=10,pady=6)
        labelNoOfTablet.grid(row=5,column=2,sticky=W)
        txtAddress = Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.NoofTablet,width=25)
        txtAddress.grid(row=5,column=3)

        labelHeight = Label(DataFrameLeft,font=("arial",10,"bold"),text="Height:",padx=10,pady=6)
        labelHeight.grid(row=6,column=2,sticky=W)
        txtHeight = Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.height,width=25)
        txtHeight.grid(row=6,column=3)

        labelFInfo = Label(DataFrameLeft,font=("arial",10,"bold"),text="Further Information:",padx=10,pady=6)
        labelFInfo.grid(row=7,column=2,sticky=W)
        txtFInfo = Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.furtherInfo,width=25)
        txtFInfo.grid(row=7,column=3)

        #======================DataFrameRight======================
        self.txtPrescription=Text(DataFrameRight,font=("arial",10,"bold"),width=68,height=15,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0) 

        #=========Buttons=====================
        btnPrescription = Button(Buttonframe,text="Prescription",command=self.prescription,bg="purple",fg="white",font=("arial",10,"bold"),width=19,height=1,padx=10,pady=2)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData = Button(Buttonframe,text="Prescription Data",command=self.insert_prescription_data,bg="purple",fg="white",font=("arial",10,"bold"),width=19,height=1,padx=10,pady=2)
        btnPrescriptionData.grid(row=0,column=1)

        btnUpdate = Button(Buttonframe,text="Update",command=self.update_data,bg="purple",fg="white",font=("arial",10,"bold"),width=19,height=1,padx=10,pady=2)
        btnUpdate.grid(row=0,column=2)

        btnDelete = Button(Buttonframe,text="Delete",command=self.delete_data,bg="purple",fg="white",font=("arial",10,"bold"),width=19,height=1,padx=10,pady=2)
        btnDelete.grid(row=0,column=3)

        btnClear = Button(Buttonframe,text="Clear",command=self.clear_data,bg="purple",fg="white",font=("arial",10,"bold"),width=19,height=1,padx=10,pady=2)
        btnClear.grid(row=0,column=4)

        btnExit = Button(Buttonframe,text="Exit",command=self.exit,bg="purple",fg="white",font=("arial",10,"bold"),width=19,height=1,padx=10,pady=2)
        btnExit.grid(row=0,column=5)

        btnPrint = Button(Buttonframe,text="Print",command=self.print_data,bg="purple",fg="white",font=("arial",10,"bold"),width=17,height=1,padx=10,pady=2)
        btnPrint.grid(row=0,column=6)

        #=========Table==========================
           #=========ScrollBar======================
        
        self.hospital_table=ttk.Treeview(Detailsframe,column=("Patient ID","Name of patient","Date of Birth","Patient Age",
                                        "Patient Gender","Blood Group","Contact Number","Side Effects","Blood Pressure",
                                        "Heart Rate","Weight","Tablet Name","Address","No of Tablets","Height",
                                        "Further Information"))
        
        scroll_x=ttk.Scrollbar(Detailsframe,orient="horizontal",command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(Detailsframe,orient="vertical",command=self.hospital_table.yview)
        
        self.hospital_table.configure(xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("Patient ID",text="Patient ID")
        self.hospital_table.heading("Name of patient",text="Patient Name")
        self.hospital_table.heading("Date of Birth",text="DOB")
        self.hospital_table.heading("Patient Age",text="Age of Patient")
        self.hospital_table.heading("Patient Gender",text="Gender of Patient")
        self.hospital_table.heading("Blood Group",text="Blood Group")
        self.hospital_table.heading("Contact Number",text="Contact Number")
        self.hospital_table.heading("Side Effects",text="Side Effects")
        self.hospital_table.heading("Blood Pressure",text="BP")
        self.hospital_table.heading("Heart Rate",text="Heart Rate")
        self.hospital_table.heading("Weight",text="Patient Weight")
        self.hospital_table.heading("Tablet Name",text="Name of Tablet")
        self.hospital_table.heading("Address",text="Patient Address")
        self.hospital_table.heading("No of Tablets",text="No of Tablets")
        self.hospital_table.heading("Height",text="Patient Height")
        self.hospital_table.heading("Further Information",text="Patient Info")
        
        self.hospital_table["show"]="headings"
        
        self.hospital_table.column("Patient ID",width=100)
        self.hospital_table.column("Name of patient",width=100)
        self.hospital_table.column("Date of Birth",width=100)
        self.hospital_table.column("Patient Age",width=100)
        self.hospital_table.column("Patient Gender",width=100)
        self.hospital_table.column("Blood Group",width=100)
        self.hospital_table.column("Contact Number",width=100)
        self.hospital_table.column("Side Effects",width=100)
        self.hospital_table.column("Blood Pressure",width=100)
        self.hospital_table.column("Heart Rate",width=100)
        self.hospital_table.column("Weight",width=100)
        self.hospital_table.column("Tablet Name",width=100)
        self.hospital_table.column("Address",width=100)
        self.hospital_table.column("No of Tablets",width=100)
        self.hospital_table.column("Height",width=100)
        self.hospital_table.column("Further Information",width=400)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    # ===========Functionality Declaration====================
    def insert_prescription_data(self):
        if (self.PatientId.get()=="" or 
            self.PatientName.get()=="" or 
            self.Age.get()=="" or
            not self.Age.get().isdigit()):
            messagebox.showerror("Error","All fields are required and Age must be a valid number")
            return 
        try:
            conn = mysql.connector.connect(host="localhost",username="root",password="root",database="hospital_db")
            my_cursor = conn.cursor()
            # Execute the SQL insert query
            my_cursor.execute("""
                INSERT INTO prescription (
                    Patient_id, Patient_name, DOB, Age, Gender, Blood_group, contact_number,
                    side_effect, Blood_pressure, Heart_rate, weight,tablet_name, address, NoofTablet, height, further_info
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                self.PatientId.get(),
                self.PatientName.get(),
                self.DOB.get(),
                self.Age.get(),
                self.Gender.get(),
                self.BloodGroup.get(),
                self.ContactNumber.get(),
                self.SideEffect.get(),
                self.BP.get(),
                self.HR.get(),
                self.weight.get(),
                self.TabletName.get(),
                self.Address.get(),
                self.NoofTablet.get(),
                self.height.get(),
                self.furtherInfo.get()
            ))

            conn.commit()  
            self.fetch_data()
            messagebox.showinfo("Success", "Record has been inserted successfully!")
        except mysql.connector.Error as err:
            print("MySQL Error:", err)  
            messagebox.showerror("Database Error", f"An error occurred: {err}")
        except Exception as e:
            print("Error:", e)  
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            conn.close() 

    #=========Update Function=============
    def update_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="root",database="hospital_db")
        my_cursor = conn.cursor()
        my_cursor.execute("""update prescription set Patient_name=%s, DOB=%s, Age=%s, Gender=%s, Blood_group=%s,
                          contact_number=%s, side_effect=%s, Blood_pressure=%s, Heart_rate=%s, weight=%s, 
                          tablet_name=%s, address=%s, NoofTablet=%s, height=%s, further_info=%s 
                          where Patient_id=%s""",(
                            self.PatientName.get(),
                            self.DOB.get(),
                            self.Age.get(),
                            self.Gender.get(),
                            self.BloodGroup.get(),
                            self.ContactNumber.get(),
                            self.SideEffect.get(),
                            self.BP.get(),
                            self.HR.get(),
                            self.weight.get(),
                            self.TabletName.get(),
                            self.Address.get(),
                            self.NoofTablet.get(),
                            self.height.get(),
                            self.furtherInfo.get(),
                            self.PatientId.get()
            ))
        conn.commit()
        self.fetch_data()
        conn.close() 

    #===============Prescription Function Button====================
    def prescription(self):
        self.txtPrescription.delete('1.0',END)

        self.txtPrescription.insert(END,"Patient ID:\t\t\t" +self.PatientId.get() + "\n")
        self.txtPrescription.insert(END,"Patient Name:\t\t\t" +self.PatientName.get() + "\n")
        self.txtPrescription.insert(END,"DOB:\t\t\t" +self.DOB.get() + "\n")
        self.txtPrescription.insert(END,"Patient Age:\t\t\t" +self.Age.get() + "\n")
        self.txtPrescription.insert(END,"Patient Gender:\t\t\t" +self.Gender.get() + "\n")
        self.txtPrescription.insert(END,"Blood Group:\t\t\t" +self.BloodGroup.get() + "\n")
        self.txtPrescription.insert(END,"Contact Number:\t\t\t" +self.ContactNumber.get() + "\n")
        self.txtPrescription.insert(END,"Side Effect:\t\t\t" +self.SideEffect.get() + "\n")
        self.txtPrescription.insert(END,"Blood Pressure:\t\t\t" +self.BP.get() + "\n")
        self.txtPrescription.insert(END,"Heart Rate:\t\t\t" +self.HR.get() + "\n")
        self.txtPrescription.insert(END,"Weight:\t\t\t" +self.weight.get() + "\n")
        self.txtPrescription.insert(END,"Tablet Names:\t\t\t" +self.TabletName.get() + "\n")
        self.txtPrescription.insert(END,"Address:\t\t\t" +self.Address.get() + "\n")
        self.txtPrescription.insert(END,"No of Tablets:\t\t\t" +self.NoofTablet.get() + "\n")
        self.txtPrescription.insert(END,"Height:\t\t\t" +self.height.get() + "\n")
        self.txtPrescription.insert(END,"Further Info:\t\t\t" +self.furtherInfo.get() + "\n")

    
    #=======Delete Button Function===========
    def delete_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="root",database="hospital_db")
        my_cursor = conn.cursor()
        query="delete from prescription where Patient_id=%s"
        value=(self.PatientId.get(),)
        my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete","Patient has been deleted.")

    #=======Clear button function=========
    def clear_data(self):
        self.PatientId.set("")
        self.PatientName.set("")
        self.DOB.set("")
        self.Age.set("")
        self.Gender.set("")
        self.BloodGroup.set("")
        self.ContactNumber.set("")
        self.SideEffect.set("")
        self.BP.set("")
        self.HR.set("")
        self.weight.set("")
        self.TabletName.set("")
        self.Address.set("")
        self.NoofTablet.set("")
        self.height.set("")
        self.furtherInfo.set("")
        self.txtPrescription.delete("1.0",END)


    #========Exit button Function===========
    def exit(self):
        exit=messagebox.askyesno("Hospital Management System","Confirm you want to exit?")
        if exit>0:
            root.destroy()
            return 

    #==========Print button Function============
    def print_data(self):
        try:
            #Creating new pdf instance
            pdf=FPDF()
            pdf.add_page()
            pdf.set_font("Arial",size=12)

            #Add a title
            pdf.set_font("Arial",style="B",size=16)
            pdf.cell(0,10,"Prescription Details:",ln=True,align='C')
            pdf.ln(10)

            prescription_data=self.txtPrescription.get("1.0",END)

            pdf.set_font("Arial",size=12)
            for line in prescription_data.split('\n'):
                pdf.cell(0,10,line,ln=True)

            file_path=filedialog.asksaveasfilename(defaultextension=".pdf",filetypes=[("PDF files","*.pdf")])
            if file_path:
                pdf.output(file_path)
                messagebox.showinfo("Success",f"Prescription saved as {file_path}")
            else:
                messagebox.showwarning("Cancelled","Save operation cancelled.")

            #pdf_file_name="Prescription Data.pdf"
            #pdf.output(pdf_file_name)

            

        except Exception as e:
            messagebox.showerror("Error",f"An error occured while saving the prescription: {e}")





    #======Function for fetching data from database=================
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="root",database="hospital_db")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from prescription")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #==========Function for showing data while we move cursor to data================
    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.PatientId.set(row[0])
        self.PatientName.set(row[1])
        self.DOB.set(row[2])
        self.Age.set(row[3])
        self.Gender.set(row[4])
        self.BloodGroup.set(row[5])
        self.ContactNumber.set(row[6])
        self.SideEffect.set(row[7])
        self.BP.set(row[8])
        self.HR.set(row[9])
        self.weight.set(row[10])
        self.TabletName.set(row[11])
        self.Address.set(row[12])
        self.NoofTablet.set(row[13])
        self.height.set(row[14])
        self.furtherInfo.set(row[15])

     
















root=Tk()
ob=Hospital(root)
root.mainloop()