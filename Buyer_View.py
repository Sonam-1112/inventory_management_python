from tkinter import *
# from My_Billing_Software import root
from tkinter.ttk import Treeview
from tkinter import ttk
from tkinter import Toplevel,messagebox
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import pymysql
import import_ipynb
# import My_LoginSystem
# import Billing_Software
# from ipynb.fs.full.<My_Billing_Software.ipynb> import *

# Billing_Software.main()
root = Tk()
root.geometry('1174x700+200+50')
root.resizable(False,False)
root.title('Buyer Dashboard')
root.configure(bg = 'gold2')

global con,mycursor
try:
    con = pymysql.connect(host='localhost',user='root',password='')
    mycursor = con.cursor()
    query = 'use inventoryDB;'
    mycursor.execute(query)
except:
    messagebox.showerror('Notification','Some error occured in database!!!\nPlease try again...') 

    
def showUserInfo():
    showUserInforoot = Toplevel()
    showUserInforoot.geometry('1220x700+200+50')
    showUserInforoot.grab_set()                                        ######Untill this window is closed nothing will work
    showUserInforoot.resizable(False,False)
    showUserInforoot.title("User Information")
    showUserInforoot.configure(bg = 'powder blue')
    
    def on_entersavenewbtn(e):    
        savenewbtn.configure(bg='red')
    def on_leavesavenewbtn(e):
        savenewbtn.configure(bg='blue')
        
    def on_entersavechangesbtn(e):    
        savechangesbtn.configure(bg='red')
    def on_leavesavechangesbtn(e):
        savechangesbtn.configure(bg='blue')
        
    def savenewfunc():
        pass
    
    def savechangesfunc():
        pass
    ##################################################SubFrame-1
    frame1 = Frame(showUserInforoot,bg = 'powder blue',relief=GROOVE,borderwidth=5,width=400,height=670)
    frame1.place(x=10,y=20)
    heading1 = Label(frame1,text='Address & Financial  ',width=21,font=('arial',22,'italic bold'),bg='powder blue')
    heading1.place(x=0,y=0)
    #################################################SubFrame-1 Labels
    titleLabel = Label(frame1,text="Title : ",bg = 'powder blue',font = ('times',16,'italic'),anchor='w')
    titleLabel.place(x=10,y=60)

    nameLabel = Label(frame1,text="Name : ",bg = 'powder blue',font = ('times',16,'italic'),anchor='w')
    nameLabel.place(x=10,y=120)
    
    emailLabel = Label(frame1,text="Email : ",bg = 'powder blue',font = ('times',16,'italic'),anchor='w')
    emailLabel.place(x=10,y=180)

    addressLabel = Label(frame1,text="Address : ",bg = 'powder blue',font = ('times',16,'italic'),anchor='w')
    addressLabel.place(x=10,y=240)

    countryLabel = Label(frame1,text="Country : ",bg = 'powder blue',font = ('times',16,'italic'),anchor='w')
    countryLabel.place(x=10,y=300)

    phoneLabel = Label(frame1,text="Phone No. : ",bg = 'powder blue',font = ('times',16,'italic'),anchor='w')
    phoneLabel.place(x=10,y=360)

    accountLabel = Label(frame1,text="Bank Acc. No.: ",bg = 'powder blue',font = ('times',16,'italic'),anchor='w')
    accountLabel.place(x=10,y=420)
    
    #################################################SubFrame-1 Entry Boxes
    titleval = StringVar()
    nameval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    countryval = StringVar()
    phoneval = StringVar()
    accountval = StringVar()

    titlechoosen = ttk.Combobox(frame1, width = 27, textvariable = titleval) 
    titlechoosen['values'] = ('Mr.','Mrs.','Miss.','Other')
    titlechoosen.place(x=150,y=60)

    nameEntry = Entry(frame1,textvariable=nameval,width=25,font=('arial',12,'italic'),bd=5,bg='light pink')
    nameEntry.place(x=150,y=120)

    emailEntry = Entry(frame1,textvariable=emailval,width=25,font=('arial',12,'italic'),bd=5,bg='light pink')
    emailEntry.place(x=150,y=180)

    addressEntry = Entry(frame1,textvariable=addressval,width=25,font=('arial',12,'italic'),bd=5,bg='light pink')
    addressEntry.place(x=150,y=240)

    countryEntry = Entry(frame1,textvariable=countryval,width=25,font=('arial',12,'italic'),bd=5,bg='light pink')
    countryEntry.place(x=150,y=300)

    phoneEntry = Entry(frame1,textvariable=phoneval,width=25,font=('arial',12,'italic'),bd=5,bg='light pink')
    phoneEntry.place(x=150,y=360)

    accountEntry = Entry(frame1,textvariable=accountval,width=25,font=('arial',12,'italic'),bd=5,bg='light pink')
    accountEntry.place(x=150,y=420)

    ##################################################SubFrame-2
    frame2 = Frame(showUserInforoot,bg = 'powder blue',relief=GROOVE,borderwidth=5,width=400,height=670)
    frame2.place(x=410,y=20)
    heading2 = Label(frame2,text='Other Information',width=21,font=('arial',22,'italic bold'),bg='powder blue')
    heading2.place(x=0,y=0)
    #################################################SubFrame-2 Labels
    dobLabel = Label(frame2,text="DOB : ",bg = 'powder blue',font = ('times',16,'italic'),anchor='w')
    dobLabel.place(x=10,y=60)

    placeofbirthLabel = Label(frame2,text="Place of Birth : ",bg = 'powder blue',font = ('times',16,'italic'),anchor='w')
    placeofbirthLabel.place(x=10,y=120)
    
    nationalityLabel = Label(frame2,text="Nationality : ",bg = 'powder blue',font = ('times',16,'italic'),anchor='w')
    nationalityLabel.place(x=10,y=180)

    maritalstatusLabel = Label(frame2,text="Marital Status : ",bg = 'powder blue',font = ('times',16,'italic'),anchor='w')
    maritalstatusLabel.place(x=10,y=240)
    
    #################################################SubFrame-2 Entry Boxes
    dobval = StringVar()
    placeofbirthval = StringVar()
    nationalityval = StringVar()
    maritalstatusval = StringVar()

    dobEntry = Entry(frame2,textvariable=dobval,width=25,font=('arial',12,'italic'),bd=5,bg='light pink')
    dobEntry.place(x=150,y=60)

    placeofbirthEntry = Entry(frame2,textvariable=placeofbirthval,width=25,font=('arial',12,'italic'),bd=5,bg='light pink')
    placeofbirthEntry.place(x=150,y=120)

    nationalityEntry = Entry(frame2,textvariable=nationalityval,width=25,font=('arial',12,'italic'),bd=5,bg='light pink')
    nationalityEntry.place(x=150,y=180)

    maritalstatuschoosen = ttk.Combobox(frame2, width = 27, textvariable = maritalstatusval) 
    maritalstatuschoosen['values'] = ('Married','Unmarried','Seperated')
    maritalstatuschoosen.place(x=150,y=240)
    
    ##################################################SubFrame-3
    frame3 = Frame(showUserInforoot,bg = 'powder blue',relief=GROOVE,borderwidth=5,width=400,height=670)
    frame3.place(x=810,y=20)
    heading3 = Label(frame3,text='Sensitive Information',width=21,font=('arial',22,'italic bold'),bg='powder blue')
    heading3.place(x=0,y=0)
    #################################################SubFrame-3 Labels
    aadharLabel = Label(frame3,text="Aadhar No. : ",bg = 'powder blue',font = ('times',16,'italic'),anchor='w')
    aadharLabel.place(x=10,y=60)

    ssnLabel = Label(frame3,text="SSN No. : ",bg = 'powder blue',font = ('times',16,'italic'),anchor='w')
    ssnLabel.place(x=10,y=120)
    
    #################################################SubFrame-3 Entry Boxes
    aadharval = StringVar()
    ssnval = StringVar()
    
    aadharEntry = Entry(frame3,textvariable=aadharval,width=25,font=('arial',12,'italic'),bd=5,bg='light pink')
    aadharEntry.place(x=150,y=60)

    ssnEntry = Entry(frame3,textvariable=ssnval,width=25,font=('arial',12,'italic'),bd=5,bg='light pink')
    ssnEntry.place(x=150,y=120)
    
    ################################################SubFrame-3 Buttons
    savenewbtn = Button(frame3,text='Save New',font=('Arial',15,'bold'),width=10,bg='blue',activebackground='red'
                          ,activeforeground='white',relief=GROOVE,bd=9,command = savenewfunc)
    savenewbtn.place(x=30,y=250)
    savenewbtn.bind('<Enter>',on_entersavenewbtn)
    savenewbtn.bind('<Leave>',on_leavesavenewbtn)
    
    savechangesbtn = Button(frame3,text='Save Changes',font=('Arial',15,'bold'),width=13,bg='blue',activebackground='red'
                          ,activeforeground='white',relief=GROOVE,bd=9,command = savechangesfunc)
    savechangesbtn.place(x=200,y=250)
    savechangesbtn.bind('<Enter>',on_entersavechangesbtn)
    savechangesbtn.bind('<Leave>',on_leavesavechangesbtn)
    
#########################################################################Logout Button Function
def logout():
    rr = messagebox.askyesnocancel("Confirmation","Are you sure you want to exit?",parent=DataEntryFrame)
    if(rr == True):
        root.destroy() 
##################################################ShowDataFrame##########################################
ShowDataFrame = Frame(root,bg = 'gold2',relief=GROOVE,borderwidth=5,width=760,height=670)
ShowDataFrame.place(x=410,y=20)

######################################################FrontPageButtonsFrame#################################
DataEntryFrame = Frame(root,bg = 'gold2',relief=GROOVE,borderwidth=5,width=400,height=670)
DataEntryFrame.place(x=10,y=20)

frontLabel = Label(DataEntryFrame,text='--------------Welcome-----------',width=21,font=('arial',22,'italic bold')
                   ,bg='gold2')
frontLabel.place(x=0,y=0)

homeBtn = Button(DataEntryFrame,text="1. Home",width=20,font=('arial',20,'italic'),bd=6,bg='red'
               ,relief=RIDGE,activebackground='red',activeforeground='white')
homeBtn.place(x=25,y=40)

productBtn = Button(DataEntryFrame,text="2. Buy Products",width=20,font=('arial',20,'italic'),bd=6,bg='light blue'
               ,relief=RIDGE,activebackground='red',activeforeground='white')
productBtn.place(x=25,y=120)

userinfoBtn = Button(DataEntryFrame,text="3. User Info",width=20,font=('arial',20,'italic'),bd=6,bg='light blue'
               ,relief=RIDGE,activebackground='red',activeforeground='white',command=showUserInfo)
userinfoBtn.place(x=25,y=200)

logoutBtn = Button(DataEntryFrame,text="4. Logout",width=20,font=('arial',20,'italic'),bd=6,bg='light blue'
               ,relief=RIDGE,activebackground='red',activeforeground='white',command=logout)
logoutBtn.place(x=25,y=280)

root.mainloop()