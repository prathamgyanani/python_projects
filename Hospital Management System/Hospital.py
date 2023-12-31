from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
class Hospital:
    def __init__(self,root,tab_control):
        self.root=root
        #self.root.title("Hospital Management System")
        #self.root.geometry("1540x800+0+0")
        self.tab_control=tab_control
        self.nameoftablet=StringVar()
        self.refno=IntVar()
        self.dose=StringVar()
        self.nooftablet=StringVar()
        self.lot = StringVar()
        self.issuedate=StringVar()
        self.expirydate=StringVar()
        self.dailydose=StringVar()
        self.sideeffect=StringVar()
        self.futherinfo=StringVar()
        self.storageadvice=StringVar()
        self.drivingusingmachine=StringVar()
        self.howtousemedication=StringVar()
        self.patientid=StringVar()
        self.nhsno=StringVar()
        self.patientname=StringVar()
        self.dob=StringVar()
        self.patientaddress=StringVar()
        self.updaterefno=IntVar()

        #self.refno_count=1000



        lbtitle = Label(self.root, bd=20, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", fg="red", bg="white",
                        font=("times new roman",50,"bold"))
        lbtitle.pack(side=TOP, fill=X)
        #============================DATA Frame=========================================

        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=100,width=1530,height=400)

        Dataframeleft=LabelFrame(Dataframe, bd=10 , relief=RIDGE,padx=10,font=("arial",12,"bold"),text="Patient Information")
        Dataframeleft.place(x=5,y=5,width=980,heigh=350)

        Dataframeright=LabelFrame(Dataframe,relief=RIDGE,bd=10,padx=10,font=("arial",12,"bold"),text="Prescription")
        Dataframeright.place(x=990,y=5,width=500,height=350)

        #============================Buttons frame==============================================
        Buttonframe=Frame(self.root,bd=15,relief=RIDGE)
        Buttonframe.place(x=5,y=500,width=1530,height=80)
        Buttonframe.grid_columnconfigure(0,weight=1)

        # ============================Details frame==============================================
        Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=580, width=1530, height=210)


        #=============================Dataframeleft=========================
        lblNameTablet=Label(Dataframeleft,text="Name of Tablet",font=("arial",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)

        #combo Box
        self.comNametablet=ttk.Combobox(Dataframeleft,textvariable=self.nameoftablet,state="readonly",font=("arial",12,"bold"),width=33)
        self.comNametablet["values"]=("Nice","Corona Vacine","Acetainophen","Adderall","Amlodipine","Ativan")
        self.comNametablet.current(0)
        self.comNametablet.grid(row=0,column=1)
        #self.refno.set(self.refno_count)
        lblref = Label(Dataframeleft, text="Reference No : ", font=("arial", 12, "bold"), padx=2,
                              pady=6)
        lblref.grid(row=1, column=0,sticky=W)
        txtref=Entry(Dataframeleft,textvariable=self.refno,font=("arial",12,"bold"),width=35)
        txtref.grid(row=1,column=1)

        lbldose=Label(Dataframeleft,text="Dose :",font=(("arial",12,"bold")),padx=2,pady=6)
        lbldose.grid(row=2,column=0,sticky=W)
        txtdose=Entry(Dataframeleft,textvariable=self.dose,font=("arial",12,"bold"),width=35)
        txtdose.grid(row=2,column=1)

        lblnoofTablet = Label(Dataframeleft, text="No of Tablets :", font=(("arial", 12, "bold")), padx=2, pady=6)
        lblnoofTablet.grid(row=3, column=0, sticky=W)
        txtnoofTablet = Entry(Dataframeleft, textvariable=self.nooftablet,font=("arial", 12, "bold"), width=35)
        txtnoofTablet.grid(row=3, column=1)

        lblLot = Label(Dataframeleft, text="Lot:", font=(("arial", 12, "bold")), padx=2, pady=6)
        lblLot.grid(row=4, column=0, sticky=W)
        txtLot = Entry(Dataframeleft, textvariable=self.lot,font=("arial", 12, "bold"), width=35)
        txtLot.grid(row=4, column=1)

        lblissueDate = Label(Dataframeleft, text="Issue Date :", font=(("arial", 12, "bold")), padx=2, pady=6)
        lblissueDate.grid(row=5, column=0, sticky=W)
        txtissueDate = Entry(Dataframeleft, textvariable=self.issuedate,font=("arial", 12, "bold"), width=35)
        txtissueDate.grid(row=5, column=1)

        lblExpDate = Label(Dataframeleft, text="Exp Date :", font=(("arial", 12, "bold")), padx=2, pady=6)
        lblExpDate.grid(row=6, column=0, sticky=W)
        txtExpDate = Entry(Dataframeleft, textvariable=self.expirydate,font=("arial", 12, "bold"), width=35)
        txtExpDate.grid(row=6, column=1)

        lblDailyDose = Label(Dataframeleft, text="Daily Dose :", font=(("arial", 12, "bold")), padx=2, pady=6)
        lblDailyDose.grid(row=7, column=0, sticky=W)
        txtDailyDose = Entry(Dataframeleft, textvariable=self.dailydose,font=("arial", 12, "bold"), width=35)
        txtDailyDose.grid(row=7, column=1)

        lblSideEffects = Label(Dataframeleft, text="Side Effects :", font=(("arial", 12, "bold")), padx=2, pady=6)
        lblSideEffects.grid(row=8, column=0, sticky=W)
        txtSideEffects = Entry(Dataframeleft, textvariable=self.sideeffect,font=("arial", 12, "bold"), width=35)
        txtSideEffects.grid(row=8, column=1)

        lblfutherInfo = Label(Dataframeleft, text="Further Information :", font=(("arial", 12, "bold")), padx=5, pady=6)
        lblfutherInfo.grid(row=0, column=2, sticky=W)
        txtfutherInfo = Entry(Dataframeleft,textvariable=self.futherinfo, font=("arial", 12, "bold"), width=35)
        txtfutherInfo.grid(row=0, column=3)

        lblbloodPressure = Label(Dataframeleft, text="Blood Pressure :", font=(("arial", 12, "bold")), padx=5, pady=6)
        lblbloodPressure.grid(row=1, column=2, sticky=W)
        txtbloodPressure = Entry(Dataframeleft,textvariable=self.drivingusingmachine, font=("arial", 12, "bold"), width=35)
        txtbloodPressure.grid(row=1, column=3)

        lblStorageAdvice = Label(Dataframeleft, text="Storage Advice :", font=(("arial", 12, "bold")), padx=5, pady=6)
        lblStorageAdvice.grid(row=2, column=2, sticky=W)
        txtStorageAdvice = Entry(Dataframeleft,textvariable=self.storageadvice, font=("arial", 12, "bold"), width=35)
        txtStorageAdvice.grid(row=2, column=3)

        lblMedication = Label(Dataframeleft, text="Medication :", font=(("arial", 12, "bold")), padx=5, pady=6)
        lblMedication.grid(row=3, column=2, sticky=W)
        txtMedication = Entry(Dataframeleft, textvariable=self.howtousemedication,font=("arial", 12, "bold"), width=35)
        txtMedication.grid(row=3, column=3)

        lblPatientId = Label(Dataframeleft, text="Patient Id :", font=(("arial", 12, "bold")), padx=5, pady=6)
        lblPatientId.grid(row=4, column=2, sticky=W)
        txtPatientId = Entry(Dataframeleft, textvariable=self.patientid,font=("arial", 12, "bold"), width=35)
        txtPatientId.grid(row=4, column=3)

        lblNhsno = Label(Dataframeleft, text="NHS Number :", font=(("arial", 12, "bold")), padx=5, pady=6)
        lblNhsno.grid(row=5, column=2, sticky=W)
        txtNhsno = Entry(Dataframeleft, textvariable=self.nhsno,font=("arial", 12, "bold"), width=35)
        txtNhsno.grid(row=5, column=3)

        lblPatientname = Label(Dataframeleft, text="Patient Name :", font=(("arial", 12, "bold")), padx=5, pady=6)
        lblPatientname.grid(row=6, column=2, sticky=W)
        txtPatientname = Entry(Dataframeleft, textvariable=self.patientname,font=("arial", 12, "bold"), width=35)
        txtPatientname.grid(row=6, column=3)

        lblDOB = Label(Dataframeleft, text="Date of Birth :", font=(("arial", 12, "bold")), padx=5, pady=6)
        lblDOB.grid(row=7, column=2, sticky=W)
        txtDOB = Entry(Dataframeleft, textvariable=self.dob,font=("arial", 12, "bold"), width=35)
        txtDOB.grid(row=7, column=3)

        txtPatientaddress = Label(Dataframeleft, text="Patient Address :", font=(("arial", 12, "bold")), padx=5, pady=6)
        txtPatientaddress.grid(row=8, column=2, sticky=W)
        txtPatientaddress = Entry(Dataframeleft, textvariable=self.patientaddress,font=("arial", 12, "bold"), width=35)
        txtPatientaddress.grid(row=8, column=3)

        #================================== Data Frame Right==================================

        self.txtPrescription=Text(Dataframeright,font=("arial",12,"bold"),width=50,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)



        # =============================== BUTTONS ==============================
        btnprescription = Button(Buttonframe, text="Prescription",command=self.iprescription, fg="white", bg="green",width=24,padx=2,height=2,pady=1,font=("arial",12,"bold"))
        btnprescription.grid(row=0, column=0)

        btnprescriptiondata = Button(Buttonframe, text="Prescription Data",command=self.iprescriptionData , fg="white", bg="green",width=24,height=2, padx=2, pady=1,
                                 font=("arial", 12, "bold"))
        btnprescriptiondata.grid(row=0, column=1)

        btnupdate = Button(Buttonframe, text="Update",command=self.update, fg="white", bg="green",width=24,height=2, padx=2, pady=1,
                                 font=("arial", 12, "bold"))
        btnupdate.grid(row=0, column=2)

        btnDelete = Button(Buttonframe, text="Delete", command=self.idelete, fg="white", bg="green", width=24, height=2,
                           padx=2, pady=1,
                           font=("arial", 12, "bold"))
        btnDelete.grid(row=0, column=3)

        btnReset = Button(Buttonframe, text="Reset", fg="white",command=self.reset, bg="green",width=24,height=2, padx=2, pady=1,
                                 font=("arial", 12, "bold"))
        btnReset.grid(row=0, column=4)

        btnExit = Button(Buttonframe, text="Exit", fg="white",command=self.iExit, bg="green",width=24,height=2, padx=2, pady=1,
                                 font=("arial", 12, "bold"))
        btnExit.grid(row=0, column=5)

        # ===========================Table================================================

        # ==========================Scroll bar ====================================
        scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)

        # Create the Treeview widget and configure its xscrollcommand and yscrollcommand
        self.hospital_table = ttk.Treeview(
            Detailsframe,
            columns=(
            "nameoftablet", "refno", "dose", "nooftablet", "lot", "idate", "edate", "ddose", "storage", "nhsno",
            "pname", "dob", "address"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        # Configure the horizontal scrollbar to work with the xview method of the Treeview
        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        # Pack the scrollbars (assuming you want them at the bottom and right)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.hospital_table.heading("nameoftablet",text="Name of Tablets")
        self.hospital_table.heading("refno",text="Ref No.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablet",text="No of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("idate",text="Issue Date")
        self.hospital_table.heading("edate",text="Expiry Date")
        self.hospital_table.heading("ddose",text="Daily Dose")
        self.hospital_table.heading("storage",text="Storage Advice")
        self.hospital_table.heading("nhsno",text="NHS No.")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("address",text="Patient Address")

        self.hospital_table["show"]="headings"


        self.hospital_table.column("nameoftablet",width=100)
        self.hospital_table.column("refno",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftablet",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("idate",width=100)
        self.hospital_table.column("edate",width=100)
        self.hospital_table.column("ddose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsno",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)
        self.hospital_table.pack(fill=BOTH, expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fatch_data()


        #================Functionality==========================
    def iprescriptionData(self):
        if self.nameoftablet.get()=="" or self.refno.get()=="":
            messagebox.showerror(("Error","All Fields are Required"))
        else:
            #self.refno_count+=1
            #self.refno.set(self.refno_count)


            conn=mysql.connector.connect(
                host="localhost",
                user="root",
                password="Seriseri.1906",
                database="mydata"
            )

            my_cursor=conn.cursor()
            my_cursor.execute("insert into hospital VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.nameoftablet.get(),self.refno.get(),self.dose.get(),
                                                                                                    self.nooftablet.get(),
                                                                                                        self.lot.get(),
                                                                                                        self.issuedate.get(),
                                                                                                        self.expirydate.get(),
                                                                                                        self.dailydose.get(),
                                                                                                        self.storageadvice.get(),
                                                                                                        self.nhsno.get(),
                                                                                                        self.patientname.get(),
                                                                                                        self.dob.get(),
                                                                                                        self.patientaddress.get()))

            conn.commit()
            self.fatch_data()
            my_cursor.close()

            conn.close()
            messagebox.showinfo("Succes","Data is Stored")

    def update(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Seriseri.1906",
            database="mydata"
        )
        my_cursor = conn.cursor()
        if self.refno.get()==self.updaterefno:
            my_cursor.execute("update hospital set Name_of_Tablets=%s,Dose=%s,No_of_Tablets=%s,Lot=%s,Issue_Date=%s,Expiry_Date=%s,Daily_Dose=%s,Storage=%s,NHS_No=%s,Patient_Name=%s,DOB=%s,Patient_Address=%s where Ref_no=%s" ,(self.nameoftablet.get(),self.dose.get(),
                                                                                                        self.nooftablet.get(),
                                                                                                            self.lot.get(),
                                                                                                            self.issuedate.get(),
                                                                                                            self.expirydate.get(),
                                                                                                            self.dailydose.get(),
                                                                                                            self.storageadvice.get(),
                                                                                                            self.nhsno.get(),
                                                                                                            self.patientname.get(),
                                                                                                            self.dob.get(),
                                                                                                            self.patientaddress.get(),self.refno.get()))
        else:
            my_cursor.execute(
                "update hospital set Name_of_Tablets=%s,Ref_no=%s,Dose=%s,No_of_Tablets=%s,Lot=%s,Issue_Date=%s,Expiry_Date=%s,Daily_Dose=%s,Storage=%s,NHS_No=%s,Patient_Name=%s,DOB=%s,Patient_Address=%s where Ref_no=%s",
                (self.nameoftablet.get(), self.refno.get(), self.dose.get(),
                 self.nooftablet.get(),
                 self.lot.get(),
                 self.issuedate.get(),
                 self.expirydate.get(),
                 self.dailydose.get(),
                 self.storageadvice.get(),
                 self.nhsno.get(),
                 self.patientname.get(),
                 self.dob.get(),
                 self.patientaddress.get(), self.updaterefno))

        conn.commit()
        self.fatch_data()
        my_cursor.close()
        conn.close()

        messagebox.showinfo("Update","Record has Been Updated Successfully")
        self.reset()

    def iprescription(self):

        self.txtPrescription.insert(END,"Name of Tablets :\t\t\t"+self.nameoftablet.get()+"\n")
        self.txtPrescription.insert(END,"Reference No. :\t\t\t"+str(self.refno.get())+"\n")
        self.txtPrescription.insert(END,"Dose :\t\t\t"+self.dose.get()+"\n")
        self.txtPrescription.insert(END,"Number of Tablets:\t\t\t"+self.nooftablet.get()+"\n")
        self.txtPrescription.insert(END,"Lot :\t\t\t"+self.lot.get()+"\n")
        self.txtPrescription.insert(END,"Issue Date :\t\t\t"+self.issuedate.get()+"\n")
        self.txtPrescription.insert(END,"Expiry Date :\t\t\t"+self.expirydate.get()+"\n")
        self.txtPrescription.insert(END,"Daily Dose :\t\t\t"+self.dailydose.get()+"\n")
        self.txtPrescription.insert(END,"Side Effects :\t\t\t"+self.sideeffect.get()+"\n")
        self.txtPrescription.insert(END,"Further Information :\t\t\t"+self.futherinfo.get()+"\n")
        self.txtPrescription.insert(END,"Storage Advice :\t\t\t"+self.storageadvice.get()+"\n")
        self.txtPrescription.insert(END,"Driving Using Machine :\t\t\t"+self.drivingusingmachine.get()+"\n")
        self.txtPrescription.insert(END,"Patient Id :\t\t\t"+self.patientid.get()+"\n")
        self.txtPrescription.insert(END,"NHS No :\t\t\t"+self.nhsno.get()+"\n")
        self.txtPrescription.insert(END,"Patient Name :\t\t\t"+self.patientname.get()+"\n")
        self.txtPrescription.insert(END,"Date of Birth :\t\t\t"+self.dob.get()+"\n")
        self.txtPrescription.insert(END,"Patient Address :\t\t\t"+self.patientaddress.get()+"\n")




    def fatch_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Seriseri.1906",
            database="mydata"
        )
        my_cursor = conn.cursor()
        my_cursor.execute("Select *from hospital")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("", END, values=i)
            conn.commit()
            my_cursor.close()
            conn.close()
    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]

        self.nameoftablet.set(row[0])
        self.refno.set(row[1])
        self.dose.set(row[2])
        self.nooftablet.set(row[3])
        self.lot.set(row[4])
        self.issuedate.set(row[5])
        self.expirydate.set(row[6])
        self.dailydose.set(row[7])
        self.storageadvice.set(row[8])
        self.nhsno.set(row[9])
        self.patientname.set(row[10])
        self.dob.set(row[11])
        self.patientaddress.set(row[12])
        self.updaterefno = self.refno.get()

    def idelete(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Seriseri.1906",
            database="mydata"
        )
        my_cursor = conn.cursor()
        query = "Delete from Hospital where Ref_No=%s"
        value = (self.refno.get(),)
        my_cursor.execute(query, value)

        conn.commit()
        my_cursor.close()
        self.fatch_data()
        conn.close()
        messagebox.showinfo("Deleted", "Ref No: " + str(value) + " Query is Deleted", )
        self.reset()

    def reset(self):
        self.nameoftablet.set(self.comNametablet['values'][0])
        self.refno.set(0)
        self.dose.set("")
        self.nooftablet.set("")
        self.lot.set("")
        self.issuedate.set("")
        self.expirydate.set("")
        self.dailydose.set("")
        self.sideeffect.set("")
        self.futherinfo.set("")
        self.storageadvice.set("")
        self.drivingusingmachine.set("")
        self.howtousemedication.set("")
        self.patientid.set("")
        self.nhsno.set("")
        self.patientname.set("")
        self.dob.set("")
        self.patientaddress.set("")
        self.txtPrescription.delete("1.0",END)

    def iExit(self):
        iExit=messagebox.askyesno("Hospital Management System","Confirm You Want to Exit")
        if iExit>0:
            self.tab_control.hide(self.tab_control.select())
            return


        '''def reffetch(self):
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Seriseri.1906",
                database="mydata"
            )

            # Create a cursor object
            cursor = conn.cursor()

            # Define the column you want to retrieve
            column_name = "Ref_no"

            # Create and execute the SQL query to get the value of the specified column from the last row
            query = f"SELECT {column_name} FROM hospital ORDER BY your_primary_key_column DESC LIMIT 1"
            cursor.execute(query)

            # Fetch the result
            result = cursor.fetchone()

            # Check if a result was retrieved
            if result:
                last_value = result[0]
                print(f"The value of {column_name} in the last row is: {last_value}")
            else:
                print(f"No rows found in the table {your_table_name}")'''
