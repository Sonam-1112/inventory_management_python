from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
from tkinter.ttk import Treeview
from tkinter import ttk
import import_ipynb
# import Manufacturer_View
# import Buyer_View
# import Billing_Software

root = Tk()
root.title('Login Page')
root.geometry('650x650+450+100')
root.resizable(False,False)
root.configure(bg="gold")

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
    user = username.get()
    passw = password.get()
    if(user =="" or passw == ""):
        messagebox.showinfo("Notification","All fields are required...!!!",parent=root)
    else:
        try:
            con = pymysql.connect(host='localhost',user='root',password='')
            mycursor = con.cursor()
            query = 'use inventoryDB;'
            mycursor.execute(query)
            query = 'select * from login_info where username = %s and password=%s;'
            t = mycursor.execute(query,(user,passw))
            if(t == True):
                data = mycursor.fetchall()
                for i in data:
                    if(i[3] == 'Manufacturer'):
                        print("True")
                        root.destroy()
                        Manufacturer_View.root.mainloop()
                    else:
                        print("Buyer Login")
            else:
                messagebox.showerror('Notification','Incorrect Username or Password!!!\nPlease try again...')
        except:
            messagebox.showerror('Notification','Something is wrong!!!\nPlease try again...')
            return 
def registerBtnfunc():
    registerroot = Toplevel()
    registerroot.geometry("650x650+450+100")
    registerroot.resizable(False,False)
    registerroot.configure(bg="gold2")
    registerroot.title("Library Management System")
    registerroot.grab_set()
    def on_enterregisterbtn(e):
        registerbtn.configure(bg='cyan')
    def on_leaveregisterbtn(e):
        registerbtn.configure(bg='blue')
    def registerregisterBtnfunc():
        user = username.get()
        passw = password.get()
        conpassw = confirmpassword.get()
        role = roleval.get()
        if(user =="" or passw == "" or conpassw == ""):
            messagebox.showinfo("Error","All fields are required",parent=registerroot)
        elif(passw != conpassw):
            messagebox.showinfo("Error","Both password fields should be same...!!!",parent=registerroot)
        else:
            try:
                con = pymysql.connect(host='localhost',user='root',password='')
                mycursor = con.cursor()
                query = 'use inventoryDB;'
                mycursor.execute(query)
                query = 'insert into login_info values(%s,%s,%s,%s);'
                t = mycursor.execute(query,(user,passw,conpassw,role))
                if(t == True):
                    messagebox.showinfo('Notification','Registered Successfully...!!!',parent=registerroot)
                    if(role == "Manufacturer"):
                        Manufacturer_View.root.mainloop()
                    else:
                        print("Buyer Login")
                else:
                    messagebox.showerror('Notification','Some Error occured while registering!!!\nPlease try again...',parent=registerroot)
            except:
                messagebox.showerror('Notification','Something is wrong!!!\nPlease try again...',parent=registerroot)
                return 

    #############################################################Labels
    titleLabel = Label(registerroot,text='Register Page',font=('times',20,'italic bold'),bg='gold',fg='red')
    titleLabel.place(x=0,y=0,relwidth=1)
    
#     logoLabel = Label(registerroot) #,image = logoimg)
#     logoLabel.place(x=250,y=50)

    usernameLabel = Label(registerroot,text = "Username",font=('times',15,'italic bold'),bg='gold2')
    usernameLabel.place(x=100,y=270)

    passwordLabel = Label(registerroot,text = "Password",font=('times',15,'italic bold'),bg='gold2')
    passwordLabel.place(x=100,y=350)
        
    confirmpasswordLabel = Label(registerroot,text = "Confirm Password",font=('times',15,'italic bold'),bg='gold2')
    confirmpasswordLabel.place(x=100,y=430)
    
    roleLabel = Label(registerroot,text = "Choose Role",font=('times',15,'italic bold'),bg='gold2')
    roleLabel.place(x=100,y=510)
    
    ############################################################Entry Boxes
    username = StringVar()
    password = StringVar()
    confirmpassword = StringVar()
    roleval = StringVar()

    usernameEntry = Entry(registerroot,textvariable=username,width=30,font=('times',15,'italic'),bd=10,bg='yellow')
    usernameEntry.place(x=270,y=270)

    passwordEntry = Entry(registerroot,width=30,show='*',textvariable=password,font=('times',15,'italic'),bd=10,bg='yellow')
    passwordEntry.place(x=270,y=350)
    
    confirmpasswordEntry = Entry(registerroot,width=30,show='*',textvariable=confirmpassword,font=('times',15,'italic'),bd=10,bg='yellow')
    confirmpasswordEntry.place(x=270,y=430)
    
    rolechoosen = ttk.Combobox(registerroot, width = 27, textvariable = roleval) 
    rolechoosen['values'] = ('Buyer','Manufacturer')
    rolechoosen.place(x=270,y=510)
    
    registerbtn = Button(registerroot,text='Register Now',font=('times',15,'italic bold'),bg='blue',bd=10,activebackground = 'red',
                   activeforeground='white',command = registerregisterBtnfunc)
    registerbtn.place(x=250,y=560)
    registerbtn.bind('<Enter>',on_enterregisterbtn)
    registerbtn.bind('<Leave>',on_leaveregisterbtn)


############################################################Background Image Setting
# bg_label = Label(root,image = bgimg).pack() 

dashboardframe=Frame(root,bg="#009999")
dashboardframe.place(x=0,y=120,relwidth=1)

#############################################################Labels
titleLabel = Label(root,text='Login Page',font=('times',20,'italic bold'),bg='gold2',fg='red')
titleLabel.place(x=0,y=0,relwidth=1)
       
logoLabel = Label(root) #,image = logoimg)
logoLabel.place(x=250,y=50)
 
usernameLabel = Label(root,text = "Username",font=('times',15,'italic bold'),bg='gold2')
usernameLabel.place(x=90,y=270)

passwordLabel = Label(root,text = "Password",font=('times',15,'italic bold'),bg='gold2')
passwordLabel.place(x=90,y=350)

############################################################Entry Boxes
username = StringVar()
password = StringVar()

usernameEntry = Entry(root,textvariable=username,width=30,font=('times',15,'italic'),bd=10,bg='yellow')
usernameEntry.place(x=230,y=270)

passwordEntry = Entry(root,width=30,show='*',textvariable=password,font=('times',15,'italic'),bd=10,bg='yellow')
passwordEntry.place(x=230,y=350)

##############################################################BUtton
loginbtn = Button(root,text='Login',font=('times',15,'italic bold'),bg='blue',bd=10,activebackground = 'red',
                   activeforeground='white',command = loginBtnfunc)
loginbtn.place(x=250,y=420)
loginbtn.bind('<Enter>',on_enterloginbtn)
loginbtn.bind('<Leave>',on_leaveloginbtn)

orLabel = Label(root,text = "OR...Not yet Registered!!! Register Below",font=('times',15,'italic bold'),bg='gold2')
orLabel.place(x=150,y=500)

registerbtn = Button(root,text='Register Now',font=('times',15,'italic bold'),bg='blue',bd=10,activebackground = 'red',
                   activeforeground='white',command = registerBtnfunc)
registerbtn.place(x=230,y=550)
registerbtn.bind('<Enter>',on_enterregisterbtn)
registerbtn.bind('<Leave>',on_leaveregisterbtn)

root.mainloop()