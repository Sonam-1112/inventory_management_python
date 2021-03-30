from tkinter import *
# from My_Billing_Software import root
from tkinter.ttk import Treeview
from tkinter import ttk
from tkinter import Toplevel,messagebox
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import pymysql
from datetime import datetime
import import_ipynb
import Manufacturer_View
import Billing_Software

def mains(usename):
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

    def buyProduct():
        Billing_Software.mains()
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
                ,relief=RIDGE,activebackground='red',activeforeground='white',command=buyProduct)
    productBtn.place(x=25,y=120)

    logoutBtn = Button(DataEntryFrame,text="4. Logout",width=20,font=('arial',20,'italic'),bd=6,bg='light blue'
                ,relief=RIDGE,activebackground='red',activeforeground='white',command=logout)
    logoutBtn.place(x=25,y=200)

    root.mainloop()