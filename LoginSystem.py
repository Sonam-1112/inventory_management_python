from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
from tkinter.ttk import Treeview
from tkinter import ttk
import import_ipynb
from datetime import datetime
# import Manufacturer_View
# import Buyer_View
# import Billing_Software

root = Tk()
root.title('Login Page')
root.geometry('600x400+470+170')
root.resizable(False,False)
root.configure(bg="powder blue")

# ############################################################Images
# bgimg = ImageTk.PhotoImage(file='bgimg.jpg')

# logoimg = PhotoImage(file='logo.png')
# logoimg = logoimg.subsample(3,3)

# usernameimg = PhotoImage(file='usernameicon.png')
# usernameimg = usernameimg.subsample(15,15)

# passwordimg = PhotoImage(file='passwordicon.png')
# passwordimg = passwordimg.subsample(25,25)

#############################################################Hover Effect
def on_enterloginbtn(e):
    loginbtn.configure(bg='cyan')
def on_leaveloginbtn(e):
    loginbtn.configure(bg='blue')
    
def on_enterregisterbtn(e):
    registerbtn.configure(bg='cyan')
def on_leaveregisterbtn(e):
    registerbtn.configure(bg='blue')

def loginBtnfunc():
    username = usernameval.get()
    passw = passwordval.get()
    if(username =="" or passw == ""):
        messagebox.showinfo("Notification","All fields are required...!!!",parent=root)
    else:
        try:
            con = pymysql.connect(host='localhost',user='root',password='')
            mycursor = con.cursor()
            query = 'use inventoryDB;'
            mycursor.execute(query)
            query = 'select * from login_info where username = %s and password=%s;'
            t = mycursor.execute(query,(username,passw))
            if(t == True):
                data = mycursor.fetchall()
                for i in data:
                    if(i[3] == 'Manufacturer'):
                        print("True")
                        root.destroy()
                        Manufacturer_View.mains()
                    else:
                        print("Buyer Login")
                        root.destroy()
                        Buyer_View.mains()
            else:
                messagebox.showerror('Notification','Incorrect Username or Password!!!\nPlease try again...')
        except:
            messagebox.showerror('Notification','Something is wrong!!!\nPlease try again...')
            return 
def registerBtnfunc():
    registerroot = Toplevel()
    registerroot.geometry("600x600+470+100")
    registerroot.resizable(False,False)
    registerroot.configure(bg="powder blue")
    registerroot.title("Register Page")
    registerroot.grab_set()
    def on_enterregisterbtn(e):
        registerbtn.configure(bg='cyan')
    def on_leaveregisterbtn(e):
        registerbtn.configure(bg='blue')
    def registerregisterBtnfunc():
        username = usernameval.get()
        passw = passwordval.get()
        conpassw = confirmpasswordval.get()
        role = roleval.get()
        custname = custnameval.get()
        mobile = mobileval.get()
        address = addressval.get()
        if(custname.strip()=="" or mobile.strip()=="" or address.strip()=="" or username =="" or passw == "" or conpassw == ""):
            messagebox.showinfo("Error","All fields are required",parent=registerroot)
        elif(len(mobile.strip()) != 10):
            messagebox.showinfo("Error","Invalid Phone Number",parent=registerroot)
        elif(passw != conpassw):
            messagebox.showinfo("Error","Both password fields should be same...!!!",parent=registerroot)
        else:
            try:
                con = pymysql.connect(host='localhost',user='root',password='')
                mycursor = con.cursor()
                query = 'use inventoryDB;'
                mycursor.execute(query)
                query = 'insert into login_info values(%s,%s,%s,%s,%s,%s,%s);'
                t = mycursor.execute(query,(username,passw,conpassw,role,custname,mobile,address))
                if(t == True):
                    messagebox.showinfo('Notification','Registered Successfully...!!!',parent=registerroot)
                    if(role == "Manufacturer"):
                        print("Manufacturer Login")
                        Manufacturer_View.mains()
                    else:
                        print("Buyer Login")
                        Manufacturer_View.mains()
                else:
                    messagebox.showerror('Notification','Some Error occured while registering!!!\nPlease try again...',parent=registerroot)
            except:
                messagebox.showerror('Notification','Something is wrong!!!\nPlease try again...',parent=registerroot)
                return 

    #############################################################Labels

    usernameLabel = Label(registerroot,text = "Username",font=('times',15,'italic bold'),bg='powder blue')
    usernameLabel.place(x=70,y=70)

    passwordLabel = Label(registerroot,text = "Password",font=('times',15,'italic bold'),bg='powder blue')
    passwordLabel.place(x=70,y=130)
        
    confirmpasswordLabel = Label(registerroot,text = "Confirm Password",font=('times',15,'italic bold'),bg='powder blue')
    confirmpasswordLabel.place(x=70,y=190)

    roleLabel = Label(registerroot,text = "Choose Role",font=('times',15,'italic bold'),bg='powder blue')
    roleLabel.place(x=70,y=250)

    custnameLabel = Label(registerroot,text="Enter Name ",bg = 'powder blue',font = ('times',15,'bold italic'),anchor='w')
    custnameLabel.place(x=70,y=310)

    mobileLabel = Label(registerroot,text="Enter Mobile No. ",bg = 'powder blue',font = ('times',15,'bold italic'),anchor='w')
    mobileLabel.place(x=70,y=370)

    addressLabel = Label(registerroot,text="Enter Address ",bg = 'powder blue',font = ('times',15,'bold italic'),anchor='w')
    addressLabel.place(x=70,y=430)
    
    ############################################################Entry Boxes
    usernameval = StringVar()
    passwordval = StringVar()
    confirmpasswordval = StringVar()
    roleval = StringVar()
    custnameval = StringVar()
    mobileval = StringVar()
    addressval = StringVar()

    usernameEntry = Entry(registerroot,textvariable=usernameval,width=32,font=('arial',12,'italic'),bd=5,bg='light pink')
    usernameEntry.place(x=250,y=70)

    passwordEntry = Entry(registerroot,show="*",textvariable=passwordval,width=32,font=('arial',12,'italic'),bd=5,bg='light pink')
    passwordEntry.place(x=250,y=130)
    
    confirmpasswordEntry = Entry(registerroot,show="*",textvariable=confirmpasswordval,width=32,font=('arial',12,'italic'),bd=5,bg='light pink')
    confirmpasswordEntry.place(x=250,y=190)

    rolechoosen = ttk.Combobox(registerroot, width = 27, textvariable = roleval) 
    rolechoosen['values'] = ('Buyer','Manufacturer')
    rolechoosen.place(x=250,y=250)
    
    custnameEntry = Entry(registerroot,textvariable=custnameval,width=32,font=('arial',12,'italic'),bd=5,bg='light pink')
    custnameEntry.place(x=250,y=310)

    mobileEntry = Entry(registerroot,textvariable=mobileval,width=32,font=('arial',12,'italic'),bd=5,bg='light pink')
    mobileEntry.place(x=250,y=370)

    addressEntry = Entry(registerroot,textvariable=addressval,width=32,font=('arial',12,'italic'),bd=5,bg='light pink')
    addressEntry.place(x=250,y=430)

    registerbtn = Button(registerroot,text='Register Now',font=('times',15,'italic bold'),bg='blue',bd=10,activebackground = 'red',
                   activeforeground='white',command = registerregisterBtnfunc)
    registerbtn.place(x=230,y=490)
    registerbtn.bind('<Enter>',on_enterregisterbtn)
    registerbtn.bind('<Leave>',on_leaveregisterbtn)

#############################################################Labels
 
usernameLabel = Label(root,text = "Username",font=('times',15,'italic bold'),bg='powder blue')
usernameLabel.place(x=90,y=70)

passwordLabel = Label(root,text = "Password",font=('times',15,'italic bold'),bg='powder blue')
passwordLabel.place(x=90,y=130)

############################################################Entry Boxes
usernameval = StringVar()
passwordval = StringVar()

usernameEntry = Entry(root,textvariable=usernameval,width=32,font=('arial',12,'italic'),bd=5,bg='light pink')
usernameEntry.place(x=230,y=70)

passwordEntry = Entry(root,show="*",textvariable=passwordval,width=32,font=('arial',12,'italic'),bd=5,bg='light pink')
passwordEntry.place(x=230,y=130)

##############################################################BUtton
loginbtn = Button(root,text='Login',font=('times',15,'italic bold'),bg='blue',bd=10,activebackground = 'red',
                   activeforeground='white',command = loginBtnfunc)
loginbtn.place(x=270,y=190)
loginbtn.bind('<Enter>',on_enterloginbtn)
loginbtn.bind('<Leave>',on_leaveloginbtn)

orLabel = Label(root,text = "OR...Not yet Registered!!! Register Below",font=('times',15,'italic bold'),bg='powder blue')
orLabel.place(x=150,y=260)

registerbtn = Button(root,text='Register Now',font=('times',15,'italic bold'),bg='blue',bd=10,activebackground = 'red',
                   activeforeground='white',command = registerBtnfunc)
registerbtn.place(x=240,y=310)
registerbtn.bind('<Enter>',on_enterregisterbtn)
registerbtn.bind('<Leave>',on_leaveregisterbtn)

root.mainloop()