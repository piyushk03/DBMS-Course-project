from tkinter import * #to import the functions of all the classes
from tkinter import ttk #to show availabilites in that specific textbox like in gender textbox here
import pymysql
from tkinter import messagebox #TO display different messages 
class Student:
    #Constructor in python called evertime when object is created 
    def __init__(self,root): #Self keyword is used to access all the instances in a class like methods and attributes and  It binds the         attributes with the given arguments.
        self.root = root #It will create a class level variable root and initialize with root variable
        self.root.title("Student Management System") 
        self.root.geometry("1350x700+0+0")

        title = Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="Black",fg="Blue") #Styles of button
        title.pack(side = TOP,fill=X)#fill=x to fully cover the head with title

        #Widget - a component of GUI that is used to perform some specific operations
        #-------All Variables-------Declaring variables of student
        self.Roll_No_var=StringVar()
        self.Name_var=StringVar()
        self.Email_var=StringVar()
        self.Gender_var=StringVar()
        self.Contact_var=StringVar()
        self.DOB_var=StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()

        #-------Manage_Frame--------
        Manage_frame = Frame(self.root,bd =4 ,relief=GROOVE,bg="crimson")#crimson colour similar to red 
        Manage_frame.place(x=20,y=100,width=450,height=600)
        m_title = Label(Manage_frame,text="Fill Student Details",bg="crimson",fg="white",font=("times new roman",20,"bold"),)
        m_title.grid(row=0,columnspan=3,pady=20)#pady-to separate roll no from student details label


        #column = To put the widget in the specified column and columnspan = To fix the columns widget will occupy.
        lbl_roll = Label(Manage_frame,text="Roll No.",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=10,sticky="w")

        txt_roll = Entry(Manage_frame,textvariable=self.Roll_No_var,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=10,padx=10,sticky="w")#sticky -basically stick the textbox to left after each label here,AFTER ROLL no

        lbl_name = Label(Manage_frame,text="Name",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=10,sticky="w ")

        txt_name = Entry(Manage_frame,textvariable=self.Name_var,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=10,sticky="w ")

        lbl_email = Label(Manage_frame,text="Email",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_email.grid(row=3,column=0,pady=10,padx=10,sticky="w ")

        txt_email = Entry(Manage_frame,textvariable=self.Email_var,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
        txt_email.grid(row=3,column=1,pady=10,padx=10,sticky="w ")

        lbl_gender = Label(Manage_frame,text="Gender",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_gender.grid(row=4,column=0,pady=10,padx=10,sticky="w ")

        combo_gender = ttk.Combobox(Manage_frame,textvariable=self.Gender_var,font=("times new roman",19,"bold"),state='readonly')#Readonly state means user cannot enter it's values only it can select the  available values like here
        combo_gender['values'] = ('Male','Female')
        combo_gender.grid(row=4,column=1,padx=20,pady=10)

        lbl_contact = Label(Manage_frame,text="Contact",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_contact.grid(row=5,column=0,pady=10,padx=10,sticky="w ")

        txt_contact = Entry(Manage_frame,textvariable=self.Contact_var,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
        txt_contact.grid(row=5,column=1,pady=10,padx=10,sticky="w ")

        lbl_DOB = Label(Manage_frame,text="DOB",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_DOB.grid(row=6,column=0,pady=10,padx=10,sticky="w ")

        txt_DOB = Entry(Manage_frame,textvariable=self.DOB_var,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
        txt_DOB.grid(row=6,column=1,pady=10,padx=10,sticky="w ")

        lbl_Add = Label(Manage_frame,text="Address",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_Add.grid(row=7,column=0,pady=10,padx=10,sticky="w ")

        self.txt_Add = Text(Manage_frame,width=40,height=5,font=("times new roman",10))
        self.txt_Add.grid(row=7,column=1,pady=10,padx=20,sticky="w")

        #-----ButtonFrame-----
        btn_frame = Frame(Manage_frame,bd=4,relief=RIDGE,bg="crimson")
        btn_frame.place(x=10,y=540,width=420) #width gives total horixzontal distance of the button frame 

        Addbtn = Button(btn_frame,text="ADD",width=10,command=self.add_student).grid(row=0,column=0,padx=10,pady=10)
        Updabtn = Button(btn_frame,text="UPDATE",width=10,command=self.update_data ).grid(row=0,column=1,padx=10,pady=10)
        delbtn = Button(btn_frame,text="DELETE",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        Clrbtn = Button(btn_frame,text="CLEAR",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)


        #-------Detail_Frame--------
        Detail_frame = Frame(self.root,bd =4 ,relief=RIDGE,bg="crimson")
        Detail_frame.place(x=500,y=100,width=800,height=580)

        lbl_search = Label(Detail_frame,text="Search By",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=10,sticky="w")

        combo_search = ttk.Combobox(Detail_frame,textvariable = self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly ')
        combo_search['values'] = ('Roll_no','Name','Contact')
        combo_search.grid(row=0,column=1,padx=20,pady=10)

        txt_search = Entry(Detail_frame ,textvariable = self.search_txt,width=20,font=("times new roman",14 ,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w ")

        searchbtn = Button(Detail_frame,text="SEARCH",width=10,pady=5,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        showallbtn = Button(Detail_frame,text="SHOWALL",width=10,pady=5,command=self.fetch_data).grid(row=0,column=4 ,padx=10,pady=10)

        #--------Table_Frame-----------
        Tbl_frame = Frame(Detail_frame,bd =4 ,relief=RIDGE,bg="crimson")
        Tbl_frame.place(x=10,y=70,width=760,height=495)

        scroll_x = Scrollbar(Tbl_frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Tbl_frame,orient=VERTICAL)
        self.Student_table = ttk.Treeview(Tbl_frame,columns=("Roll","Name","Email","Gender","Contact","DOB","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)#Tkinter Treeview widget is used to display the data in a hierarchical structure. In this structure, each row can represent a file or a directory. 
        scroll_x.pack(side=BOTTOM,fill=X)#Scroll bar appears in bottom and completely appears in whole bottom line
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("Roll",text="Roll No.")
        self.Student_table.heading("Name",text="Name")
        self.Student_table.heading("Email",text="Email")
        self.Student_table.heading("Gender",text="Gender")
        self.Student_table.heading("Contact",text="Contact")
        self.Student_table.heading("DOB",text="D.O.B")
        self.Student_table.heading("Address",text="Address")

        self.Student_table['show'] = 'headings'#to start the table from top left 

        self.Student_table.column("Roll",width=100)#width-Horizontal(size) distance of each column
        self.Student_table.column("Name",width=100)
        self.Student_table.column("Email",width=150)
        self.Student_table.column("Gender",width=100)
        self.Student_table.column("Contact",width=100)
        self.Student_table.column("DOB",width=100)
        self.Student_table.column("Address",width=150)
        self.Student_table.pack(fill=BOTH,expand=1)#to expand the student bottom of window  

        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data() #to get and display the values inside data from database whenever we start the execution

    def add_student(self):
        if self.Roll_No_var.get()=="" or self.Name_var.get()=="":
            messagebox.showerror("Error","All fields are required !!!")
        else:
                    con =  pymysql.connect(host="localhost",user="root",password="",database="SMS")
                    cur = con.cursor()
                    cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),self.Name_var.get(),self.Email_var.get(),self.Gender_var.get(),self.Contact_var.get(),self.DOB_var.get(),self.txt_Add.get('1.0',END)))
                    con.commit()
                    self.fetch_data() #It basically fetch the all the content from the table after addition of one row
                    self.clear()
                    con.close()
                    messagebox.showinfo("Success","Record has been inserted")

    def fetch_data(self):
        con =  pymysql.connect(host="localhost",user="root",password="",database="SMS")
        cur = con.cursor()
        cur.execute("select * from student")
        rows = cur.fetchall()#to store all the data from table
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())#to delete all the children elements (values) in row
            for row in rows:
                self.Student_table.insert('',END,values=row)#to store the fetch data into the our table from begining
            con.commit()
        con.close()

    def search_data(self):
        con =  pymysql.connect(host="localhost",user="root",password="",database="SMS")
        cur = con.cursor()
        cur.execute("select * from student where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()

    def clear(self):
        self.Roll_No_var.set("")
        self.Name_var.set("")
        self.Email_var.set("")
        self.Gender_var.set("")
        self.Contact_var.set("")
        self.DOB_var.set("")
        self.txt_Add.delete('1.0',END) #Delete all the text right from starting to end

    def get_cursor(self,ev):
        cursor_row = self.Student_table.focus() #fetch the row where cursor points
        content = self.Student_table.item(cursor_row) #stores the data in content for that row
        row = content['values'] #return list of values inside that row
        #print(row)
        self.Roll_No_var.set(row[0])
        self.Name_var.set(row[1])
        self.Email_var.set(row[2])
        self.Gender_var.set(row[3])
        self.Contact_var.set(row[4])
        self.DOB_var.set(row[5])
        self.txt_Add.delete('1.0',END)#Not append the address if I fetch that info 2 times -Basiically deletes all the content in addresss block and after that adds the new fetched info
        self.txt_Add.insert(END,row[6])

    def update_data(self):
        con =  pymysql.connect(host="localhost",user="root",password="",database="SMS")
        cur = con.cursor()
        cur.execute("update student set Name=%s,Email=%s,Gender=%s,Contact=%s,DOB=%s,Address=%s where Roll_no=%s ",(self.Name_var.get(),self.Email_var.get(),self.Gender_var.get(),self.Contact_var.get(),self.DOB_var.get(),self.txt_Add.get('1.0',END),self.Roll_No_var.get()))#DML Query
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con =  pymysql.connect(host="localhost",user="root",password="",database="SMS")
        cur = con.cursor()# It is an object to make the connection for executing SQL queries.
        cur.execute("delete from student where Roll_no=%s",self.Roll_No_var.get())#DML Query
        con.commit()# Whenever any change is made to the database using update or any other statements, it is necessary to commit the changes. If we donot use the commit() method after making any changes to the database, the database will not not be updated and changes will not be reflected.
        con.close()#Removing the alloted space in memory of con named object 
        self.fetch_data()
        self.clear()
        messagebox.showinfo("Success","Record has been Deleted")

root = Tk() #to create a tkinter application, we generally create an instance of tkinter frame Tk() It helps to display the root window and manages all the other components of the tkinter application 
ob = Student(root) #We are creating object of student class which can create different GUI
root.mainloop()# As the name implies it will loop forever until the user exits the window or waits for any events from the user . The mainloop automatically receives events from the window system and deliver them to the application widgets. This gets quit when we click on the close button of the title bar. So, any code after this mainloop() method will not run.

