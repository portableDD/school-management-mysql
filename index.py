from email.mime import application
from tkinter import*
from tkinter import*
from tkinter import*
from tkinter import ttk
import tkinter.messagebox
from turtle import left, width
import pymysql
from requests import delete

class School:

    def __init__(self, root) -> None:
        self.root = root
        self.root.title("School Management System")
        self.root.geometry("1350x800+0+0")
        self.root.configure(background = "gainsboro")

        # =============================================Frames=====================================================

        MainFrame = Frame(self.root, bd=10, width=1350, height=700, relief=RIDGE)
        MainFrame.grid()

        OuterFrame = Frame(MainFrame, bd=10, width=1340, height=500, bg="gainsboro", relief=RIDGE)
        OuterFrame.grid(row=0, column=0)

        InnerMostFrame = Frame(OuterFrame, bd=5, width=600, height=500, padx=0, bg="cadet blue", relief=RIDGE)
        InnerMostFrame.grid(row=0, column=0)

        InnerFrame = Frame(OuterFrame, bd=5, width=700, height=500, padx=0, bg="cadet blue", relief=RIDGE)
        InnerFrame.grid(row=0, column=1)

        BottomInnerFrame = Frame(MainFrame, bd=7, width=1340, height=300, relief=RIDGE)
        BottomInnerFrame.grid(row=2, column=0)

        Records_Frame = Frame(InnerFrame, bd=7, width=800, height=300, relief=RIDGE)
        Records_Frame.grid()

        DisplayFrame = Frame(InnerMostFrame, bd=7, width=400, height=300, relief=RIDGE)
        DisplayFrame.grid()

        Subjcet_Frame_Left = Frame(BottomInnerFrame, bd=5, width=600, height=300, padx=0, bg="cadet blue", relief=RIDGE)
        Subjcet_Frame_Left.grid(row=0, column=0)

        Subjcet_Frame_Right = Frame(BottomInnerFrame, bd=5, width=700, height=300, padx=0, bg="cadet blue", relief=RIDGE)
        Subjcet_Frame_Right.grid(row=0, column=1)

        SubjcetFrame1 = Frame(Subjcet_Frame_Left, bd=5, width=300, height=250, padx=2, bg="gainsboro", relief=RIDGE)
        SubjcetFrame1.grid(row=0, column=0)

        SubjcetFrame2 = Frame(Subjcet_Frame_Left, bd=5, width=400, height=250, padx=2, bg="gainsboro", relief=RIDGE)
        SubjcetFrame2.grid(row=0, column=1)

        GuidanceFrame = Frame(Subjcet_Frame_Right, bd=5, width=400, height=250, padx=2, pady=4, bg="gainsboro", relief=RIDGE)
        GuidanceFrame.grid(row=0, column=0)

        BottomFrame = Frame(Subjcet_Frame_Right, bd=5, width=200, height=250, padx=2, pady=4, bg="gainsboro", relief=RIDGE)
        BottomFrame.grid(row=0, column=1)

        # ==========================================Variables========================================================
        
        self.StudentID = StringVar()
        self.Firstname = StringVar()
        self.Surname = StringVar()
        self.NINumber = StringVar()
        self.Address = StringVar()
        self.Gender = StringVar()
        self.DOB = StringVar()
        self.Mobile = StringVar()
        self.Email = StringVar()
        self.DataScience = StringVar()
        self.EventDrivenPro =  StringVar()
        self.ObjectOriented = StringVar()
        self.Spreadsheet = StringVar()
        self.SystemAnalysis = StringVar()
        self.InformTechnology = StringVar()
        self.DigitalGraphics = StringVar()
        self.English = StringVar()
        self.Games = StringVar()
        self.Amination = StringVar()
        self.Database = StringVar()
        self.Maths = StringVar()
        self.AddMaths = StringVar()
        self.Physics = StringVar()
        self.ParentGuidance = StringVar()
        self.pgFirstname = StringVar()
        self.pgSurname = StringVar()
        self.pgAddress = StringVar()
        self.pgWorkPhone = StringVar()
        self.pgMobile = StringVar()
        self.pgEmail = StringVar()

      
        # ==========================================Student Detail========================================================

        self.lblStudentID = Label(DisplayFrame, font=('arial', 12, 'bold'), text="Student ID", bd=3 )
        self.lblStudentID.grid(row=0, column=0, sticky=W, padx=5, pady=3)
        self.txtStudentID = Entry(DisplayFrame, font=('arial', 12, 'bold'), bd=3, width=29, textvariable=self.StudentID)
        self.txtStudentID.grid(row=0, column=1)

        self.lblFirstname = Label(DisplayFrame, font=('arial', 12, 'bold'), text="Firstname", bd=3 )
        self.lblFirstname.grid(row=1, column=0, sticky=W, padx=5, pady=3)
        self.txtFirstname = Entry(DisplayFrame, font=('arial', 12, 'bold'), bd=3, width=29, textvariable=self.Firstname)
        self.txtFirstname.grid(row=1, column=1)

        self.lblSurname = Label(DisplayFrame, font=('arial', 12, 'bold'), text="Surname", bd=3 )
        self.lblSurname.grid(row=2, column=0, sticky=W, padx=5, pady=3)
        self.txtSurname = Entry(DisplayFrame, font=('arial', 12, 'bold'), bd=3, width=29, textvariable=self.Surname)
        self.txtSurname.grid(row=2, column=1)

        self.lblNINumber = Label(DisplayFrame, font=('arial', 12, 'bold'), text="NI Number", bd=3 )
        self.lblNINumber.grid(row=3, column=0, sticky=W, padx=5, pady=3)
        self.txtNINumber = Entry(DisplayFrame, font=('arial', 12, 'bold'), bd=3, width=29, textvariable=self.NINumber)
        self.txtNINumber.grid(row=3, column=1)

        self.lblAddress = Label(DisplayFrame, font=('arial', 12, 'bold'), text="Address", bd=3 )
        self.lblAddress.grid(row=4, column=0, sticky=W, padx=5, pady=3)
        self.txtAddress = Entry(DisplayFrame, font=('arial', 12, 'bold'), bd=3, width=29, textvariable=self.Address)
        self.txtAddress.grid(row=4, column=1)

        self.lblGender = Label(DisplayFrame, font=('arial', 12, 'bold'), text="Gender", bd=3 )
        self.lblGender.grid(row=5, column=0, sticky=W, padx=5, pady=3)
        self.cboGender=ttk.Combobox(DisplayFrame, font=('arial', 12, 'bold'), width=27, state='readonly', textvariable=self.Gender)
        self.cboGender ['values'] = ('','Female', 'Male')
        self.cboGender.current(0)
        self.cboGender.grid(row=5, column=1)

        self.lblDOB = Label(DisplayFrame, font=('arial', 12, 'bold'), text="DOB", bd=3 )
        self.lblDOB.grid(row=6, column=0, sticky=W, padx=3, pady=3)
        self.txtDOB = Entry(DisplayFrame, font=('arial', 12, 'bold'), bd=3, width=29, textvariable=self.DOB)
        self.txtDOB.grid(row=6, column=1)

        self.lblMobile = Label(DisplayFrame, font=('arial', 12, 'bold'), text="Mobile", bd=3 )
        self.lblMobile.grid(row=7, column=0, sticky=W, padx=5,pady=3)
        self.txtMobile = Entry(DisplayFrame, font=('arial', 12, 'bold'), bd=5, width=29, textvariable=self.Mobile)
        self.txtMobile.grid(row=7, column=1)

        self.lblEmail = Label(DisplayFrame, font=('arial', 12, 'bold'), text="Email", bd=3, justify=LEFT)
        self.lblEmail.grid(row=8, column=0, sticky=W, padx=5,pady=3)
        self.txtEmail = Entry(DisplayFrame, font=('arial', 12, 'bold'), bd=5, width=29, justify='left', textvariable=self.Email)
        self.txtEmail.grid(row=8, column=1)

        # ==========================================Student Records========================================================

        scroll_x = Scrollbar(Records_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Records_Frame, orient=VERTICAL)

        self.student_records = ttk.Treeview(Records_Frame, height=13, columns=("stdid","firstname","surname","ninumber",
        "address","gender","dob","mobile","email"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.student_records.heading("stdid", text="StudentID.")
        self.student_records.heading("firstname", text="Firstname")
        self.student_records.heading("surname", text="Surname")
        self.student_records.heading("ninumber", text="NINumber")
        self.student_records.heading("address", text="Address")
        self.student_records.heading("gender", text="Gender")
        self.student_records.heading("dob", text="DOB")
        self.student_records.heading("mobile", text="Mobile")
        self.student_records.heading("email", text="Email")

        self.student_records["show"] = "headings"

        self.student_records.column("stdid", width=70)
        self.student_records.column("firstname", width=100)
        self.student_records.column("surname", width=100)
        self.student_records.column("ninumber", width=70)
        self.student_records.column("address", width=150)
        self.student_records.column("gender", width=70)
        self.student_records.column("dob", width=70)
        self.student_records.column("mobile", width=100)
        self.student_records.column("email", width=150)

        self.student_records.pack(fill= BOTH, expand=1)
        self.student_records.bind("<ButtonRelease-1>",self.LearnersInfo)

        self.view_data()

        # ========================================Subject=1=========================================================

        self.lblEnglish = Label(SubjcetFrame1, font=('arial', 12, 'bold'), text="English", bd=7, bg="gainsboro")
        self.lblEnglish.grid(row=0, column=0, sticky=W,)
        self.cboEnglish=ttk.Combobox(SubjcetFrame1, font=('arial', 12, 'bold'), width=19, state='readonly', textvariable=self.English)
        self.cboEnglish ['values'] = ('Core unit','Yes', 'No','Completed')
        self.cboEnglish.current(0)
        self.cboEnglish.grid(row=0, column=1)

        self.lblGames = Label(SubjcetFrame1, font=('arial', 12, 'bold'), text="Games", bd=7, bg="gainsboro")
        self.lblGames.grid(row=1, column=0, sticky=W)
        self.cboGames=ttk.Combobox(SubjcetFrame1, font=('arial', 12, 'bold'), width=19, state='readonly', textvariable=self.Games)
        self.cboGames ['values'] = ('Core unit','Yes', 'No','Completed')
        self.cboGames.current(0)
        self.cboGames.grid(row=1, column=1)

        self.lblAmination= Label(SubjcetFrame1, font=('arial', 12, 'bold'), text="Amination", bd=7, bg="gainsboro")
        self.lblAmination.grid(row=2, column=0, sticky=W)
        self.cboAmination=ttk.Combobox(SubjcetFrame1, font=('arial', 12, 'bold'), width=19, state='readonly', textvariable=self.Amination)
        self.cboAmination ['values'] = ('Core unit','Yes', 'No','Completed')
        self.cboAmination.current(0)
        self.cboAmination.grid(row=2, column=1)

        self.lblDatabase= Label(SubjcetFrame1, font=('arial', 12, 'bold'), text="Database", bd=7, bg="gainsboro")
        self.lblDatabase.grid(row=3, column=0, sticky=W)
        self.cboDatabase=ttk.Combobox(SubjcetFrame1, font=('arial', 12, 'bold'), width=19, state='readonly', textvariable=self.Database)
        self.cboDatabase ['values'] = ('Core unit','Yes', 'No','Completed')
        self.cboDatabase.current(0)
        self.cboDatabase.grid(row=3, column=1)

        self.lblMaths = Label(SubjcetFrame1, font=('arial', 12, 'bold'), text="Maths", bd=7, bg="gainsboro")
        self.lblMaths.grid(row=4, column=0, sticky=W)
        self.cboMaths=ttk.Combobox(SubjcetFrame1, font=('arial', 12, 'bold'), width=19, state='readonly', textvariable=self.Maths)
        self.cboMaths['values'] = ('Core unit','Yes', 'No','Completed')
        self.cboMaths.current(0)
        self.cboMaths.grid(row=4, column=1)

        self.lblAddMaths = Label(SubjcetFrame1, font=('arial', 12, 'bold'), text="AddMaths", bd=7, bg="gainsboro")
        self.lblAddMaths.grid(row=5, column=0, sticky=W)
        self.cboAddMaths=ttk.Combobox(SubjcetFrame1, font=('arial', 12, 'bold'), width=19, state='readonly', textvariable=self.AddMaths)
        self.cboAddMaths['values'] = ('Core unit','Yes', 'No','Completed')
        self.cboAddMaths.current(0)
        self.cboAddMaths.grid(row=5, column=1)

        self.lblPhysics = Label(SubjcetFrame1, font=('arial', 12, 'bold'), text="Physics", bd=7, bg="gainsboro")
        self.lblPhysics.grid(row=6, column=0, sticky=W)
        self.cboPhysics=ttk.Combobox(SubjcetFrame1, font=('arial', 12, 'bold'), width=19, state='readonly', textvariable=self.Physics)
        self.cboPhysics['values'] = ('Core unit','Yes', 'No','Completed')
        self.cboPhysics.current(0)
        self.cboPhysics.grid(row=6, column=1)

        # ========================================Subject=2=========================================================

        self.lblDataScience = Label(SubjcetFrame2, font=('arial', 12, 'bold'), text="Data Science", bd=7, bg="gainsboro")
        self.lblDataScience.grid(row=0, column=0, sticky=W,)
        self.cboDataScience=ttk.Combobox(SubjcetFrame2, font=('arial', 12, 'bold'), width=19, state='readonly', textvariable=self.DataScience)
        self.cboDataScience['values'] = ('Core unit','Yes', 'No','Completed')
        self.cboDataScience.current(0)
        self.cboDataScience.grid(row=0, column=1)

        self.lblEventDrivenPro = Label(SubjcetFrame2, font=('arial', 12, 'bold'), text="Event Driven Prog", bd=7, bg="gainsboro")
        self.lblEventDrivenPro.grid(row=1, column=0, sticky=W,)
        self.cboEventDrivenPro=ttk.Combobox(SubjcetFrame2, font=('arial', 12, 'bold'), width=19, state='readonly', textvariable=self.EventDrivenPro)
        self.cboEventDrivenPro['values'] = ('Core unit','Yes', 'No','Completed')
        self.cboEventDrivenPro.current(0)
        self.cboEventDrivenPro.grid(row=1, column=1)

        self.lblObjectOriented = Label(SubjcetFrame2, font=('arial', 12, 'bold'), text="Object Oriented", bd=7, bg="gainsboro")
        self.lblObjectOriented .grid(row=2, column=0, sticky=W,)
        self.cboObjectOriented =ttk.Combobox(SubjcetFrame2, font=('arial', 12, 'bold'), width=19, state='readonly', textvariable=self.ObjectOriented )
        self.cboObjectOriented ['values'] = ('Core unit','Yes', 'No','Completed')
        self.cboObjectOriented .current(0)
        self.cboObjectOriented .grid(row=2, column=1)

        self.lblSpreadsheet = Label(SubjcetFrame2, font=('arial', 12, 'bold'), text="Spreadsheet", bd=7, bg="gainsboro")
        self.lblSpreadsheet.grid(row=3, column=0, sticky=W,)
        self.cboSpreadsheet=ttk.Combobox(SubjcetFrame2, font=('arial', 12, 'bold'), width=19, state='readonly', textvariable=self.Spreadsheet)
        self.cboSpreadsheet['values'] = ('Core unit','Yes', 'No','Completed')
        self.cboSpreadsheet.current(0)
        self.cboSpreadsheet.grid(row=3, column=1)

        self.lblSystemAnalysis = Label(SubjcetFrame2, font=('arial', 12, 'bold'), text="System Analysis", bd=7, bg="gainsboro")
        self.lblSystemAnalysis.grid(row=4, column=0, sticky=W,)
        self.cboSystemAnalysis=ttk.Combobox(SubjcetFrame2, font=('arial', 12, 'bold'), width=19, state='readonly', textvariable=self.SystemAnalysis)
        self.cboSystemAnalysis['values'] = ('Core unit','Yes', 'No','Completed')
        self.cboSystemAnalysis.current(0)
        self.cboSystemAnalysis.grid(row=4, column=1)

        self.lblInformTechnology = Label(SubjcetFrame2, font=('arial', 12, 'bold'), text="Inform Technology", bd=7, bg="gainsboro")
        self.lblInformTechnology.grid(row=5, column=0, sticky=W,)
        self.cboInformTechnology=ttk.Combobox(SubjcetFrame2, font=('arial', 12, 'bold'), width=19, state='readonly', textvariable=self.InformTechnology)
        self.cboInformTechnology['values'] = ('Core unit','Yes', 'No','Completed')
        self.cboInformTechnology.current(0)
        self.cboInformTechnology.grid(row=5, column=1)

        self.lblDigitalGraphics = Label(SubjcetFrame2, font=('arial', 12, 'bold'), text="Digital Graphics", bd=7, bg="gainsboro")
        self.lblDigitalGraphics.grid(row=6, column=0, sticky=W,)
        self.cboDigitalGraphics=ttk.Combobox(SubjcetFrame2, font=('arial', 12, 'bold'), width=19, state='readonly', textvariable=self.DigitalGraphics)
        self.cboDigitalGraphics['values'] = ('Core unit','Yes', 'No','Completed')
        self.cboDigitalGraphics.current(0)
        self.cboDigitalGraphics.grid(row=6, column=1)

        # ========================================Parent or Guidance=========================================================

        self.lblParentGuidance = Label(GuidanceFrame, font=('arial', 12, 'bold'), text="Parent or Guidance", bd=7, bg="gainsboro")
        self.lblParentGuidance.grid(row=0, column=0, sticky=W, padx=5)
        self.cboParentGuidance=ttk.Combobox(GuidanceFrame, font=('arial', 12, 'bold'), width=24, state='readonly', textvariable=self.ParentGuidance)
        self.cboParentGuidance ['values'] = ('Mother','Father', 'Brother','Sister','Guidance')
        self.cboParentGuidance.current(0)
        self.cboParentGuidance.grid(row=0, column=1)

        self.lblFirstname = Label(GuidanceFrame, font=('arial', 12, 'bold'), text="Firstname", bd=7, bg="gainsboro" )
        self.lblFirstname.grid(row=1, column=0, sticky=W, padx=5, pady=3)
        self.txtFirstname = Entry(GuidanceFrame, font=('arial', 12, 'bold'), bd=5, width=25, justify="left", textvariable=self.pgFirstname)
        self.txtFirstname.grid(row=1, column=1)

        self.lblSurname = Label(GuidanceFrame, font=('arial', 12, 'bold'), text="Surname", bd=7, bg="gainsboro", justify=LEFT )
        self.lblSurname.grid(row=2, column=0, sticky=W, padx=5, pady=3)
        self.txtSurname = Entry(GuidanceFrame, font=('arial', 12, 'bold'), bd=5, width=25, justify="left", textvariable=self.pgSurname)
        self.txtSurname.grid(row=2, column=1)

        self.lblAddress = Label(GuidanceFrame, font=('arial', 12, 'bold'), text="Address",  bd=7, bg="gainsboro")
        self.lblAddress.grid(row=3, column=0, sticky=W, padx=5, pady=3)
        self.txtAddress = Entry(GuidanceFrame, font=('arial', 12, 'bold'), bd=5, width=25, justify="left", textvariable=self.pgAddress)
        self.txtAddress.grid(row=3, column=1)

        self.lblWorkPhone = Label(GuidanceFrame, font=('arial', 12, 'bold'), text="Work Phone No.", bd=5, bg="gainsboro" )
        self.lblWorkPhone.grid(row=4, column=0, sticky=W, padx=5)
        self.txtWorkPhone = Entry(GuidanceFrame, font=('arial', 12, 'bold'), bd=5, width=25,textvariable=self.pgWorkPhone)
        self.txtWorkPhone.grid(row=4, column=1)

        self.lblMobile = Label(GuidanceFrame, font=('arial', 12, 'bold'), text="Mobile", bd=5, bg="gainsboro")
        self.lblMobile.grid(row=5, column=0, sticky=W, padx=5)
        self.txtMobile = Entry(GuidanceFrame, font=('arial', 12, 'bold'), bd=5, width=25,textvariable=self.pgMobile)
        self.txtMobile.grid(row=5, column=1)

        self.lblEmail = Label(GuidanceFrame, font=('arial', 12, 'bold'), text="Email", bd=5, bg="gainsboro")
        self.lblEmail.grid(row=6, column=0, sticky=W, padx=5,)
        self.txtEmail = Entry(GuidanceFrame, font=('arial', 12, 'bold'), bd=5, width=25, textvariable=self.pgEmail)
        self.txtEmail.grid(row=6, column=1)

        # =========================================Button=====================================================

        self.btnAddNew = Button(BottomFrame, pady=1, padx=24, bd=4, font=('arial', 16, 'bold'), width=9, text="Add New", command=self.add_student)
        self.btnAddNew.grid(row=0, column=0)

        self.btnUpdate = Button(BottomFrame, pady=1, padx=24, bd=4, font=('arial', 16, 'bold'), width=9, text="Update", command=self.update)
        self.btnUpdate.grid(row=1, column=0)

        self.btnDelete = Button(BottomFrame, pady=1, padx=24, bd=4, font=('arial', 16, 'bold'), width=9, text="Delete", command=self.deleteDB)
        self.btnDelete.grid(row=2, column=0)

        self.btnReset = Button(BottomFrame, pady=1, padx=24, bd=4, font=('arial', 16, 'bold'), width=9, text="Reset", command=self.Reset)
        self.btnReset.grid(row=3, column=0)

        self.btnExit = Button(BottomFrame, pady=1, padx=24, bd=4, font=('arial', 16, 'bold'), width=9, text="Exit", command=self.iExit)
        self.btnExit.grid(row=4, column=0)

        # ===================================================================================================

  # ==========================================Functions========================================================
    def add_student (self) :
        if self.StudentID.get() == "" or self.Firstname.get() == "" or self.Surname.get() == "" :
            tkinter.messagebox.showerror("Enter Student correct details")
        else:
            sqlCon = pymysql.connect(host="localhost", user="debian-sys-maint", password="ZEbfuikfjtZSUaVo", database="schooldb")
            cur = sqlCon.cursor()
            cur.execute("insert into schooldb values(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (self.StudentID.get(),
                                                                                    self.Firstname.get(),
                                                                                    self.Surname.get(),
                                                                                    self.NINumber.get(),
                                                                                    self.Address.get(),
                                                                                    self.Gender.get(),
                                                                                    self.DOB.get(),
                                                                                    self.Mobile.get(),
                                                                                    self.Email.get()
                                                                                    )
                        )
            sqlCon.commit()
            sqlCon.close()
            self.view_data()
            tkinter.messagebox.showinfo("SMS","Records Entered successfully")
    
    def view_data(self) : 
        sqlCon = pymysql.connect(host="localhost", user="debian-sys-maint", password="ZEbfuikfjtZSUaVo", database="schooldb")
        cur = sqlCon.cursor()
        cur.execute("select * from schooldb")
        rows = cur.fetchall()
        if len(rows) != 0 :
            self.student_records.delete(*self.student_records.get_children())
            for row in rows:
                self.student_records.insert("",END,values = row)
                sqlCon.commit()
            sqlCon.close()

    def LearnersInfo (self,ev) :
        veiwInfo = self.student_records.focus()
        learnerData = self.student_records.item(veiwInfo)
        row = learnerData["values"]
        self.StudentID.set(row[0])
        self.Firstname.set(row[1])
        self.Surname.set(row[2])
        self.NINumber.set(row[3])
        self.Address.set(row[4])
        self.Gender.set(row[5])
        self.DOB.set(row[6])
        self.Mobile.set(row[7])
        self.Email.set(row[8])

    def update (self) :
        sqlCon = pymysql.connect(host="localhost", user="debian-sys-maint", password="ZEbfuikfjtZSUaVo", database="schooldb")
        cur = sqlCon.cursor()
        cur.execute("update schooldb set firstname=%s,surname=%s,ninumber=%s,address=%s,gender=%s,dob=%s,mobile=%s, email=%s, where stdid=%s",( 
        self.Firstname.get(),
        self.Surname.get(),
        self.NINumber.get(),
        self.Address.get(),
        self.Gender.get(),
        self.DOB.get(),
        self.Mobile.get(),
        self.Email.get(),
        self.StudentID.get()
        ))

        sqlCon.commit()
        self.view_data()
        sqlCon.close()
        self.Reset()
        tkinter.messagebox.showinfo("Successful","Records Successfully Updated")
    
    def deleteDB (self) :
        sqlCon = pymysql.connect(host="localhost", user="debian-sys-maint", password="ZEbfuikfjtZSUaVo", database="schooldb")
        cur = sqlCon.cursor()
        cur.execute("delete from schooldb where stdid=%s", self.StudentID.get())

        sqlCon.commit()
        self.view_data()
        sqlCon.close()
        # self.Reset()
        tkinter.messagebox.showinfo("Delete","Records Deleted Successfully")
        

    def Reset (self) :
        self.StudentID.set("")
        self.Firstname.set("")
        self.Surname.set("")
        self.NINumber.set("")
        self.Address.set("")
        self.Gender.set("")
        self.DOB.set("")
        self.Mobile.set("")
        self.Email.set("")
        self.DataScience.set("Core Unit")
        self.EventDrivenPro.set("Core Unit")
        self.ObjectOriented.set("Core Unit")
        self.Spreadsheet.set("Core Unit")
        self.SystemAnalysis.set("Core Unit")
        self.InformTechnology.set("Core Unit")
        self.DigitalGraphics.set("Core Unit")
        self.English.set("Core Unit")
        self.Games.set("Core Unit")
        self.Amination.set("Core Unit")
        self.Database.set("Core Unit")
        self.Maths.set("Core Unit")
        self.AddMaths.set("Core Unit")
        self.Physics.set("Core Unit")
        self.ParentGuidance.set("Mother")
        self.pgFirstname.set("")
        self.pgSurname.set("")
        self.pgAddress.set("")
        self.pgWorkPhone.set("")
        self.pgMobile.set("")
        self.pgEmail.set("")

    def iExit (self) :
        iExit = tkinter.messagebox.askyesno("School Management System","Confirm if you want to exit")
        if iExit > 0 :
            root.destroy()
            return


if __name__=="__main__":
    root = Tk()
    application = School(root)
    root.mainloop()