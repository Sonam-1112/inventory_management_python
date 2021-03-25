import tkinter as tk
from tkinter import *
# from My_Billing_Software import root
from tkinter.ttk import Treeview
from tkinter import ttk
from tkinter import Toplevel,messagebox
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import pymysql
import import_ipynb
from pandas import DataFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# import My_LoginSystem
# import Billing_Software
# from ipynb.fs.full.<My_Billing_Software.ipynb> import *

# Billing_Software.main()
root = Tk()
root.geometry('1174x700+200+50')
root.resizable(False,False)
root.title('Manufacturer Dashboard')
root.configure(bg = 'gold2')

global con,mycursor
try:
    con = pymysql.connect(host='localhost',user='root',password='')
    mycursor = con.cursor()
    query = 'use inventoryDB;'
    mycursor.execute(query)
except:
    messagebox.showerror('Notification','Some error occured in database!!!\nPlease try again...') 

##################################################ShowDataFrame##########################################
ShowDataFrame = Frame(root,bg = 'gold2',relief=GROOVE,borderwidth=5,width=760,height=670)
ShowDataFrame.place(x=410,y=20)

pendingFrame = Frame(ShowDataFrame,bg = 'gold2',relief=GROOVE,borderwidth=5,width=300,height=200)
pendingFrame.place(x=50,y=20)

deliveredFrame = Frame(ShowDataFrame,bg = 'gold2',relief=GROOVE,borderwidth=5,width=300,height=200)
deliveredFrame.place(x=400,y=20)

##################################################################Pending Labels
pendingLabel = Label(pendingFrame,text="Pending : ",bg = 'red',font = ('times',20,'bold italic'),anchor='w',relief=GROOVE
                     ,borderwidth=5)
pendingLabel.place(x=70,y=10)

##################################################################Delivered Labels
deliveredLabel = Label(deliveredFrame,text="Delivered : ",bg = 'green',font = ('times',20,'bold italic'),anchor='w',
                       relief=GROOVE,borderwidth=5)
deliveredLabel.place(x=70,y=10)

###################################################################Home Page - Info Table
homeinfotableFrame = Frame(ShowDataFrame,bg = 'gold2',relief=GROOVE,borderwidth=5)
homeinfotableFrame.place(x=10,y=250,width=730,height=380)

style = ttk.Style()
style.configure('Treeview.Heading',font=('times',15,'italic'),foreground='green')
style.configure('Treeview',font=('times',12,'italic'),foreground='black',background='powder blue')


scroll_x = Scrollbar(homeinfotableFrame,orient = HORIZONTAL)
scroll_y = Scrollbar(homeinfotableFrame,orient = VERTICAL)


homeinfoTable = Treeview(homeinfotableFrame,columns = ('Order ID','Customer Name','Mobile No.','Email','Address','Gender','Order Date'
                        ,'Status'),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.configure(command = homeinfoTable.xview)
scroll_y.configure(command = homeinfoTable.yview)


homeinfoTable.heading('Order ID',text='Order ID')
homeinfoTable.heading('Customer Name',text='Customer Name')
homeinfoTable.heading('Mobile No.',text='Mobile No.')
homeinfoTable.heading('Email',text='Email')
homeinfoTable.heading('Address',text='Address')
homeinfoTable.heading('Gender',text='Gender')
homeinfoTable.heading('Order Date',text='Order Date')
homeinfoTable.heading('Status',text='Status')

homeinfoTable.configure(show='headings')

homeinfoTable.column('Order ID',width=100)
homeinfoTable.column('Customer Name',width=200)
homeinfoTable.column('Mobile No.',width=200)
homeinfoTable.column('Email',width=300)
homeinfoTable.column('Address',width=300)
homeinfoTable.column('Gender',width=100)
homeinfoTable.column('Order Date',width=150)
homeinfoTable.column('Status',width=150)

homeinfoTable.pack(fill=BOTH,expand=1)

query = 'select * from customerinfo;'
mycursor.execute(query)
data = mycursor.fetchall()
homeinfoTable.delete(*homeinfoTable.get_children())
for i in data:
    vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
    homeinfoTable.insert('',END,values=vv)

#########################################################################Show Products Function
def showProducts():
    showProductsroot = Toplevel()
    showProductsroot.geometry('1174x700+200+50')
    showProductsroot.grab_set()                                           ######Untill this window is closed nothing will work
    showProductsroot.resizable(False,False)
    showProductsroot.title('Product Details')   
    
    #########################################################Products Info Table
    productinfotableFrame = Frame(showProductsroot,bg = 'gold2',relief=GROOVE,borderwidth=5)
    productinfotableFrame.place(x=10,y=100,width=1154,height=580)

    style = ttk.Style()
    style.configure('Treeview.Heading',font=('times',15,'italic'),foreground='green')
    style.configure('Treeview',font=('times',12,'italic'),foreground='black',background='powder blue')


    scroll_x = Scrollbar(productinfotableFrame,orient = HORIZONTAL)
    scroll_y = Scrollbar(productinfotableFrame,orient = VERTICAL)


    productinfoTable = Treeview(productinfotableFrame,columns = ('Product ID','Name','Qty Available','Size','Weight','Price','Color','Status'),
                                yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)

    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.configure(command = productinfoTable.xview)
    scroll_y.configure(command = productinfoTable.yview)


    productinfoTable.heading('Product ID',text='Product ID')
    productinfoTable.heading('Name',text='Name')
    productinfoTable.heading('Qty Available',text='Qty Available')
    productinfoTable.heading('Size',text='Size')
    productinfoTable.heading('Weight',text='Weight')
    productinfoTable.heading('Price',text='Price')
    productinfoTable.heading('Color',text='Color')
    productinfoTable.heading('Status',text='Status')

    productinfoTable.configure(show='headings')

    productinfoTable.column('Product ID',width=100)
    productinfoTable.column('Name',width=200)
    productinfoTable.column('Qty Available',width=150)
    productinfoTable.column('Size',width=200)
    productinfoTable.column('Weight',width=200)
    productinfoTable.column('Price',width=100)
    productinfoTable.column('Color',width=150)
    productinfoTable.column('Status',width=150)

    productinfoTable.pack(fill=BOTH,expand=1)

    query = 'select * from productinfo;'
    mycursor.execute(query)
    data = mycursor.fetchall()
    productinfoTable.delete(*productinfoTable.get_children())
    for i in data:
        vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
        productinfoTable.insert('',END,values=vv)
        
    def addProductBtnfunc():
        def on_entersubmitaddbtn(e):
            submitaddbtn.configure(bg='red')
        def on_leavesubmitaddbtn(e):
            submitaddbtn.configure(bg='blue')
            
        addroot = Toplevel()
        addroot.geometry('550x560+300+150')
        addroot.grab_set()                                           ######Untill this window is closed nothing will work
#         addroot.iconbitmap('student.ico')
        addroot.resizable(False,False)
        addroot.title('Add Products')
        addroot.configure(bg = 'powder blue')
        def submitaddfunc():
            a_id = a_idval.get() 
            a_name = a_nameval.get() 
            a_qty = a_qtyval.get()
            a_size = a_sizeval.get() 
            a_weight = a_weightval.get() 
            a_price = a_priceval.get() 
            a_color = a_colorval.get()
            a_status = a_statusval.get()

            try:
                query = 'insert into productinfo values(%s,%s,%s,%s,%s,%s,%s,%s);'
                mycursor.execute(query,(a_id,a_name,a_qty,a_size,a_weight,a_price,a_color,a_status))
                con.commit()
                rr = messagebox.askyesnocancel('Notification','Product added Successfully...\nyou want to add new???'
                                               ,parent=addroot)
                if(rr == True):
                    a_idval.set('')
                    a_nameval.set('')
                    a_qtyval.set('')
                    a_sizeval.set('')
                    a_weightval.set('')
                    a_priceval.set('')
                    a_colorval.set('')
                    a_statusval.set('')   
            except:
                pass

            query = 'select * from productinfo;'
            mycursor.execute(query)
            data = mycursor.fetchall()
            productinfoTable.delete(*productinfoTable.get_children())
            for i in data:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
                productinfoTable.insert('',END,values=vv)    
        
        #################################################Labels
        a_idLabel = Label(addroot,text="Enter ID : ",bg = 'powder blue',font = ('times',20,'bold italic'),anchor='w')
        a_idLabel.place(x=10,y=10)

        a_nameLabel = Label(addroot,text="Enter Name : ",bg = 'powder blue',font = ('times',20,'bold italic'),anchor='w')
        a_nameLabel.place(x=10,y=70)

        a_qtyLabel = Label(addroot,text="Enter Qty. Aval. : ",bg = 'powder blue',font = ('times',20,'bold italic'),anchor='w')
        a_qtyLabel.place(x=10,y=130)

        a_sizeLabel = Label(addroot,text="Enter Size(L,M,S) : ",bg = 'powder blue',font = ('times',20,'bold italic'),anchor='w')
        a_sizeLabel.place(x=10,y=190)

        a_weightLabel = Label(addroot,text="Enter Weight(kg) : ",bg = 'powder blue',font = ('times',20,'bold italic'),anchor='w')
        a_weightLabel.place(x=10,y=250)

        a_priceLabel = Label(addroot,text="Enter Price(Rs.) : ",bg = 'powder blue',font = ('times',20,'bold italic'),anchor='w')
        a_priceLabel.place(x=10,y=310)

        a_colorLabel = Label(addroot,text="Enter Color : ",bg = 'powder blue',font = ('times',20,'bold italic'),anchor='w')
        a_colorLabel.place(x=10,y=370)
        
        a_statusLabel = Label(addroot,text="Enter Status : ",bg = 'powder blue',font = ('times',20,'bold italic'),anchor='w')
        a_statusLabel.place(x=10,y=430)

        #################################################Entry Boxes
        a_idval = StringVar()
        a_nameval = StringVar()
        a_qtyval = StringVar()
        a_sizeval = StringVar()
        a_weightval = StringVar()
        a_priceval = StringVar()
        a_colorval = StringVar()
        a_statusval = StringVar()

        a_idEntry = Entry(addroot,textvariable=a_idval,width=32,font=('arial',12,'italic'),bd=5,bg='light pink')
        a_idEntry.place(x=240,y=10)

        a_nameEntry = Entry(addroot,textvariable=a_nameval,width=32,font=('arial',12,'italic'),bd=5,bg='light pink')
        a_nameEntry.place(x=240,y=70)

        a_qtyEntry = Entry(addroot,textvariable=a_qtyval,width=32,font=('arial',12,'italic'),bd=5,bg='light pink')
        a_qtyEntry.place(x=240,y=130)

        a_sizeEntry = Entry(addroot,textvariable=a_sizeval,width=32,font=('arial',12,'italic'),bd=5,bg='light pink')
        a_sizeEntry.place(x=240,y=190)

        a_weightEntry = Entry(addroot,textvariable=a_weightval,width=32,font=('arial',12,'italic'),bd=5,bg='light pink')
        a_weightEntry.place(x=240,y=250)

        a_priceEntry = Entry(addroot,textvariable=a_priceval,width=32,font=('arial',12,'italic'),bd=5,bg='light pink')
        a_priceEntry.place(x=240,y=310)

        a_colorEntry = Entry(addroot,textvariable=a_colorval,width=32,font=('arial',12,'italic'),bd=5,bg='light pink')
        a_colorEntry.place(x=240,y=370)
        
        a_statusEntry = Entry(addroot,textvariable=a_statusval,width=32,font=('arial',12,'italic'),bd=5,bg='light pink')
        a_statusEntry.place(x=240,y=430)

        ########################################################Buttons
        submitaddbtn = Button(addroot,text='Add Product',font=('Arial',15,'bold'),width=10,bg='blue',activebackground='red'
                          ,activeforeground='white',relief=GROOVE,bd=9,command = submitaddfunc)
        submitaddbtn.place(x=190,y=480)
        submitaddbtn.bind('<Enter>',on_entersubmitaddbtn)
        submitaddbtn.bind('<Leave>',on_leavesubmitaddbtn)

    def deleteProductBtnfunc():
        cc = productinfoTable.focus()
        content = productinfoTable.item(cc)
        pp = content['values'][0]
        query = 'delete from productinfo where productid = %s;'
        rr = messagebox.askyesnocancel("Confirmation","Are you sure you want to delete this product?",parent=showProductsroot)
        if(rr == True):
            mycursor.execute(query,(pp))
            con.commit()
            query = 'select * from productinfo;'
            mycursor.execute(query)
            data = mycursor.fetchall()
            productinfoTable.delete(*productinfoTable.get_children())
            for i in data:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
                productinfoTable.insert('',END,values=vv)
        
    def searchProductBtnfunc():
        searchroot = Toplevel()
        searchroot.geometry('550x560+300+100')
        searchroot.grab_set()                                           ######Untill this window is closed nothing will work
#         searchroot.iconbitmap('student.ico')
        searchroot.resizable(False,False)
        searchroot.title('Search Products')
        searchroot.configure(bg = 'powder blue')

        def on_entersubmitsearchbtn(e):
            submitsearchbtn.configure(bg='red')
        def on_leavesubmitsearchbtn(e):
            submitsearchbtn.configure(bg='blue')
        def submitsearchfunc():
            s_id = s_idval.get() 
            s_name = s_nameval.get() 
            s_qty = s_qtyval.get()
            s_size = s_sizeval.get() 
            s_weight = s_weightval.get() 
            s_price = s_priceval.get() 
            s_color = s_colorval.get()  
            s_status = s_statusval.get()
            if(s_id !=''):
                query = 'select * from productinfo where productid=%s;'
                mycursor.execute(query,(s_id))
                data = mycursor.fetchall()
                productinfoTable.delete(*productinfoTable.get_children())
                for i in data:
                    vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
                    productinfoTable.insert('',END,values=vv)

            if(s_name !=''):
                query = 'select * from productinfo where name=%s;'
                mycursor.execute(query,(s_name))
                data = mycursor.fetchall()
                productinfoTable.delete(*productinfoTable.get_children())
                for i in data:
                    vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
                    productinfoTable.insert('',END,values=vv)

            if(s_qty !=''):
                query = 'select * from productinfo where qty=%s;'
                mycursor.execute(query,(s_qty))
                data = mycursor.fetchall()
                productinfoTable.delete(*productinfoTable.get_children())
                for i in data:
                    vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
                    productinfoTable.insert('',END,values=vv)

            if(s_size !=''):
                query = 'select * from productinfo where size=%s;'
                mycursor.execute(query,(s_size))
                data = mycursor.fetchall()
                productinfoTable.delete(*productinfoTable.get_children())
                for i in data:
                    vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
                    productinfoTable.insert('',END,values=vv)

            if(s_weight !=''):
                query = 'select * from productinfo where weight=%s;'
                mycursor.execute(query,(s_weight))
                data = mycursor.fetchall()
                productinfoTable.delete(*productinfoTable.get_children())
                for i in data:
                    vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
                    productinfoTable.insert('',END,values=vv)

            if(s_price !=''):
                query = 'select * from productinfo where price=%s;'
                mycursor.execute(query,(s_price))
                data = mycursor.fetchall()
                productinfoTable.delete(*productinfoTable.get_children())
                for i in data:
                    vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
                    productinfoTable.insert('',END,values=vv)

            if(s_color !=''):
                query = 'select * from productinfo where color=%s;'
                mycursor.execute(query,(s_color))
                data = mycursor.fetchall()
                productinfoTable.delete(*productinfoTable.get_children())
                for i in data:
                    vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
                    productinfoTable.insert('',END,values=vv)

            if(s_status !=''):
                query = 'select * from productinfo where status=%s;'
                mycursor.execute(query,(s_status))
                data = mycursor.fetchall()
                productinfoTable.delete(*productinfoTable.get_children())
                for i in data:
                    vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
                    productinfoTable.insert('',END,values=vv)
        #################################################Labels
        s_idLabel = Label(searchroot,text="Enter ID : ",bg = 'powder blue',font = ('times',20,'bold italic'),anchor='w')
        s_idLabel.place(x=10,y=10)

        s_nameLabel = Label(searchroot,text="Enter Name : ",bg = 'powder blue',font = ('times',20,'bold italic'),anchor='w')
        s_nameLabel.place(x=10,y=70)

        s_qtyLabel = Label(searchroot,text="Enter Qty. Aval. : ",bg = 'powder blue',font = ('times',20,'bold italic'),anchor='w')
        s_qtyLabel.place(x=10,y=130)

        s_sizeLabel = Label(searchroot,text="Enter Size(L,M,S) : ",bg = 'powder blue',font = ('times',20,'bold italic'),anchor='w')
        s_sizeLabel.place(x=10,y=190)

        s_weightLabel = Label(searchroot,text="Enter Weight(kg) : ",bg = 'powder blue',font = ('times',20,'bold italic'),anchor='w')
        s_weightLabel.place(x=10,y=250)

        s_priceLabel = Label(searchroot,text="Enter Price(Rs.) : ",bg = 'powder blue',font = ('times',20,'bold italic'),anchor='w')
        s_priceLabel.place(x=10,y=310)

        s_colorLabel = Label(searchroot,text="Enter Color : ",bg = 'powder blue',font = ('times',20,'bold italic'),anchor='w')
        s_colorLabel.place(x=10,y=370)
        
        s_statusLabel = Label(searchroot,text="Enter Status : ",bg = 'powder blue',font = ('times',20,'bold italic'),anchor='w')
        s_statusLabel.place(x=10,y=430)

        #################################################Entry Boxes
        s_idval = StringVar()
        s_nameval = StringVar()
        s_qtyval = StringVar()
        s_sizeval = StringVar()
        s_weightval = StringVar()
        s_priceval = StringVar()
        s_colorval = StringVar()
        s_statusval = StringVar()

        a_idEntry = Entry(searchroot,textvariable=s_idval,width=32,font=('arial',12,'italic'),bd=5,bg='light pink')
        a_idEntry.place(x=240,y=10)

        a_nameEntry = Entry(searchroot,textvariable=s_nameval,width=32,font=('arial',12,'italic'),bd=5,bg='light pink')
        a_nameEntry.place(x=240,y=70)

        a_qtyEntry = Entry(searchroot,textvariable=s_qtyval,width=32,font=('arial',12,'italic'),bd=5,bg='light pink')
        a_qtyEntry.place(x=240,y=130)

        a_sizeEntry = Entry(searchroot,textvariable=s_sizeval,width=32,font=('arial',12,'italic'),bd=5,bg='light pink')
        a_sizeEntry.place(x=240,y=190)

        a_weightEntry = Entry(searchroot,textvariable=s_weightval,width=32,font=('arial',12,'italic'),bd=5,bg='light pink')
        a_weightEntry.place(x=240,y=250)

        a_priceEntry = Entry(searchroot,textvariable=s_priceval,width=32,font=('arial',12,'italic'),bd=5,bg='light pink')
        a_priceEntry.place(x=240,y=310)

        a_colorEntry = Entry(searchroot,textvariable=s_colorval,width=32,font=('arial',12,'italic'),bd=5,bg='light pink')
        a_colorEntry.place(x=240,y=370)
        
        a_statusEntry = Entry(searchroot,textvariable=s_statusval,width=32,font=('arial',12,'italic'),bd=5,bg='light pink')
        a_statusEntry.place(x=240,y=430)

        ########################################################Buttons
        submitsearchbtn = Button(searchroot,text='Search',font=('Arial',15,'bold'),width=10,bg='blue',activebackground='red'
                          ,activeforeground='white',relief=GROOVE,bd=9,command = submitsearchfunc)
        submitsearchbtn.place(x=190,y=480)
        submitsearchbtn.bind('<Enter>',on_entersubmitsearchbtn)
        submitsearchbtn.bind('<Leave>',on_leavesubmitsearchbtn)
        
    #########################################################ShowProduct Buttons
    addProductBtn = Button(showProductsroot,text="Add Product",width=15,font=('arial',20,'italic'),bd=6,bg='yellow'
               ,relief=RIDGE,activebackground='red',activeforeground='white',command=addProductBtnfunc)
    addProductBtn.place(x=100,y=20)
    
    deleteProductBtn = Button(showProductsroot,text="Delete Product",width=15,font=('arial',20,'italic'),bd=6,bg='yellow'
               ,relief=RIDGE,activebackground='red',activeforeground='white',command=deleteProductBtnfunc)
    deleteProductBtn.place(x=400,y=20)
    
    searchProductBtn = Button(showProductsroot,text="Search Product",width=15,font=('arial',20,'italic'),bd=6,bg='yellow'
               ,relief=RIDGE,activebackground='red',activeforeground='white',command=searchProductBtnfunc)
    searchProductBtn.place(x=700,y=20)

#########################################################################Show Distribution Function

def showDistribution():
    showDistributionroot = Toplevel()
    showDistributionroot.geometry('1174x700+200+50')
    showDistributionroot.grab_set()                                           ######Untill this window is closed nothing will work
    showDistributionroot.resizable(False,False)
    showDistributionroot.title("Distribution Info")
    showDistributionroot.configure(bg = 'powder blue')
    
    infotableFrame = Frame(showDistributionroot,bg = 'gold2',relief=GROOVE,borderwidth=5)
    infotableFrame.place(x=10,y=100,width=1154,height=580)

    style = ttk.Style()
    style.configure('Treeview.Heading',font=('times',15,'italic'),foreground='green')
    style.configure('Treeview',font=('times',12,'italic'),foreground='black',background='powder blue')

    scroll_x = Scrollbar(infotableFrame,orient = HORIZONTAL)
    scroll_y = Scrollbar(infotableFrame,orient = VERTICAL)

    infoTable = Treeview(infotableFrame,columns = ('Order ID','Customer Name','Mobile No.','Email','Address','Gender','Order Date'
                            ,'Status'),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)

    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.configure(command = infoTable.xview)
    scroll_y.configure(command = infoTable.yview)


    infoTable.heading('Order ID',text='Order ID')
    infoTable.heading('Customer Name',text='Customer Name')
    infoTable.heading('Mobile No.',text='Mobile No.')
    infoTable.heading('Email',text='Email')
    infoTable.heading('Address',text='Address')
    infoTable.heading('Gender',text='Gender')
    infoTable.heading('Order Date',text='Order Date')
    infoTable.heading('Status',text='Status')

    infoTable.configure(show='headings')

    infoTable.column('Order ID',width=100)
    infoTable.column('Customer Name',width=200)
    infoTable.column('Mobile No.',width=200)
    infoTable.column('Email',width=300)
    infoTable.column('Address',width=300)
    infoTable.column('Gender',width=100)
    infoTable.column('Order Date',width=150)
    infoTable.column('Status',width=150)

    infoTable.pack(fill=BOTH,expand=1)

    query = 'select * from customerinfo;'
    mycursor.execute(query)
    data = mycursor.fetchall()
    infoTable.delete(*infoTable.get_children())
    for i in data:
        vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
        infoTable.insert('',END,values=vv)
    
    def showBuyerDetailsBtnfunc():
        pass
    
    def deleteCustomerBtnfunc():
        cc = infoTable.focus()
        content = infoTable.item(cc)
        pp = content['values'][0]
        query = 'delete from customerinfo where orderid = %s;'
        rr = messagebox.askyesnocancel("Confirmation","Are you sure you want to delete this customer?",parent=showDistributionroot)
        if(rr == True):
            mycursor.execute(query,(pp))
            con.commit()
            query = 'select * from customerinfo;'
            mycursor.execute(query)
            data = mycursor.fetchall()
            infoTable.delete(*infoTable.get_children())
            for i in data:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
                infoTable.insert('',END,values=vv)
                
            query = 'select * from customerinfo;'
            mycursor.execute(query)
            data = mycursor.fetchall()
            homeinfoTable.delete(*homeinfoTable.get_children())
            for i in data:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
                homeinfoTable.insert('',END,values=vv) 
                
    def searchCustomerBtnfunc():
        searchroot = Toplevel()
        searchroot.geometry('550x560+300+100')
        searchroot.grab_set()                                           ######Untill this window is closed nothing will work
#         searchroot.iconbitmap('student.ico')
        searchroot.resizable(False,False)
        searchroot.title('Search Products')
        searchroot.configure(bg = 'powder blue')

        def on_entersubmitsearchbtn(e):
            submitsearchbtn.configure(bg='red')
        def on_leavesubmitsearchbtn(e):
            submitsearchbtn.configure(bg='blue')
        def submitsearchfunc():
            s_orderid = s_orderidval.get() 
            s_custname = s_custnameval.get() 
            s_mobile = s_mobileval.get()
            s_email = s_emailval.get() 
            s_address = s_addressval.get() 
            s_gender = s_genderval.get() 
            s_orderdate = s_orderdateval.get()  
            s_status = s_statusval.get()
            if(s_orderid !=''):
                query = 'select * from customerinfo where orderid=%s;'
                mycursor.execute(query,(s_orderid))
                data = mycursor.fetchall()
                infoTable.delete(*infoTable.get_children())
                for i in data:
                    vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
                    infoTable.insert('',END,values=vv)

            if(s_custname !=''):
                query = 'select * from customerinfo where customername=%s;'
                mycursor.execute(query,(s_custname))
                data = mycursor.fetchall()
                infoTable.delete(*infoTable.get_children())
                for i in data:
                    vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
                    infoTable.insert('',END,values=vv)

            if(s_mobile !=''):
                query = 'select * from customerinfo where mobile_no=%s;'
                mycursor.execute(query,(s_mobile))
                data = mycursor.fetchall()
                infoTable.delete(*infoTable.get_children())
                for i in data:
                    vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
                    infoTable.insert('',END,values=vv)

            if(s_email !=''):
                query = 'select * from customerinfo where email=%s;'
                mycursor.execute(query,(s_email))
                data = mycursor.fetchall()
                infoTable.delete(*infoTable.get_children())
                for i in data:
                    vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
                    infoTable.insert('',END,values=vv)

            if(s_address !=''):
                query = 'select * from customerinfo where address=%s;'
                mycursor.execute(query,(s_address))
                data = mycursor.fetchall()
                infoTable.delete(*infoTable.get_children())
                for i in data:
                    vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
                    infoTable.insert('',END,values=vv)

            if(s_gender !=''):
                query = 'select * from customerinfo where gender=%s;'
                mycursor.execute(query,(s_gender))
                data = mycursor.fetchall()
                infoTable.delete(*infoTable.get_children())
                for i in data:
                    vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
                    infoTable.insert('',END,values=vv)

            if(s_orderdate !=''):
                query = 'select * from customerinfo where orderdate=%s;'
                mycursor.execute(query,(s_orderdate))
                data = mycursor.fetchall()
                infoTable.delete(*infoTable.get_children())
                for i in data:
                    vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
                    infoTable.insert('',END,values=vv)

            if(s_status !=''):
                query = 'select * from customerinfo where deliverystatus=%s;'
                mycursor.execute(query,(s_status))
                data = mycursor.fetchall()
                infoTable.delete(*infoTable.get_children())
                for i in data:
                    vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
                    infoTable.insert('',END,values=vv)
        #################################################Labels
        s_orderidLabel = Label(searchroot,text="Enter ID : ",bg = 'powder blue',font = ('times',20,'bold italic'),anchor='w')
        s_orderidLabel.place(x=10,y=10)

        s_custnameLabel = Label(searchroot,text="Enter Name : ",bg = 'powder blue',font = ('times',20,'bold italic'),anchor='w')
        s_custnameLabel.place(x=10,y=70)

        s_mobileLabel = Label(searchroot,text="Enter Mobile No. : ",bg = 'powder blue',font = ('times',20,'bold italic'),anchor='w')
        s_mobileLabel.place(x=10,y=130)

        s_emailLabel = Label(searchroot,text="Enter Email : ",bg = 'powder blue',font = ('times',20,'bold italic'),anchor='w')
        s_emailLabel.place(x=10,y=190)

        s_addressLabel = Label(searchroot,text="Enter Address : ",bg = 'powder blue',font = ('times',20,'bold italic'),anchor='w')
        s_addressLabel.place(x=10,y=250)

        s_genderLabel = Label(searchroot,text="Enter Gender : ",bg = 'powder blue',font = ('times',20,'bold italic'),anchor='w')
        s_genderLabel.place(x=10,y=310)

        s_orderdateLabel = Label(searchroot,text="Enter Order Date : ",bg = 'powder blue',font = ('times',20,'bold italic'),anchor='w')
        s_orderdateLabel.place(x=10,y=370)
        
        s_statusLabel = Label(searchroot,text="Enter Status : ",bg = 'powder blue',font = ('times',20,'bold italic'),anchor='w')
        s_statusLabel.place(x=10,y=430)

        #################################################Entry Boxes
        s_orderidval = StringVar()
        s_custnameval = StringVar()
        s_mobileval = StringVar()
        s_emailval = StringVar()
        s_addressval = StringVar()
        s_genderval = StringVar()
        s_orderdateval = StringVar()
        s_statusval = StringVar()

        s_orderidEntry = Entry(searchroot,textvariable=s_orderidval,width=32,font=('arial',12,'italic'),bd=5,bg='light pink')
        s_orderidEntry.place(x=240,y=10)

        s_custnameEntry = Entry(searchroot,textvariable=s_custnameval,width=32,font=('arial',12,'italic'),bd=5,bg='light pink')
        s_custnameEntry.place(x=240,y=70)

        s_mobileEntry = Entry(searchroot,textvariable=s_mobileval,width=32,font=('arial',12,'italic'),bd=5,bg='light pink')
        s_mobileEntry.place(x=240,y=130)

        s_emailEntry = Entry(searchroot,textvariable=s_emailval,width=32,font=('arial',12,'italic'),bd=5,bg='light pink')
        s_emailEntry.place(x=240,y=190)

        s_addressEntry = Entry(searchroot,textvariable=s_addressval,width=32,font=('arial',12,'italic'),bd=5,bg='light pink')
        s_addressEntry.place(x=240,y=250)

        s_genderEntry = Entry(searchroot,textvariable=s_genderval,width=32,font=('arial',12,'italic'),bd=5,bg='light pink')
        s_genderEntry.place(x=240,y=310)

        s_orderdateEntry = Entry(searchroot,textvariable=s_orderdateval,width=32,font=('arial',12,'italic'),bd=5,bg='light pink')
        s_orderdateEntry.place(x=240,y=370)
        
        s_statusEntry = Entry(searchroot,textvariable=s_statusval,width=32,font=('arial',12,'italic'),bd=5,bg='light pink')
        s_statusEntry.place(x=240,y=430)

        ########################################################Buttons
        submitsearchbtn = Button(searchroot,text='Search',font=('Arial',15,'bold'),width=10,bg='blue',activebackground='red'
                          ,activeforeground='white',relief=GROOVE,bd=9,command = submitsearchfunc)
        submitsearchbtn.place(x=190,y=480)
        submitsearchbtn.bind('<Enter>',on_entersubmitsearchbtn)
        submitsearchbtn.bind('<Leave>',on_leavesubmitsearchbtn)
    
    ##########################################################################Distribution Root Buttons
    showBuyerDetailsBtn = Button(showDistributionroot,text="Show Details",width=15,font=('arial',20,'italic'),bd=6,bg='yellow'
               ,relief=RIDGE,activebackground='red',activeforeground='white',command=showBuyerDetailsBtnfunc)
    showBuyerDetailsBtn.place(x=100,y=20)
    
    deleteProductBtn = Button(showDistributionroot,text="Delete Buyer",width=15,font=('arial',20,'italic'),bd=6,bg='yellow'
               ,relief=RIDGE,activebackground='red',activeforeground='white',command=deleteCustomerBtnfunc)
    deleteProductBtn.place(x=400,y=20)
    
    searchProductBtn = Button(showDistributionroot,text="Search Buyer",width=15,font=('arial',20,'italic'),bd=6,bg='yellow'
               ,relief=RIDGE,activebackground='red',activeforeground='white',command=searchCustomerBtnfunc)
    searchProductBtn.place(x=700,y=20)

#########################################################################Show Analysis Function
    
def showAnalysis():
    showAnalysisroot = Toplevel()
    showAnalysisroot.geometry('1174x700+200+50')
    showAnalysisroot.grab_set()                                           ######Untill this window is closed nothing will work
    showAnalysisroot.resizable(False,False)
    showAnalysisroot.title("Analysis Panel")
    showAnalysisroot.configure(bg = 'powder blue')
#     td = pd.read_excel('Sample.xlsx', engine='openpyxl')
#     sns.countplot(x='Product',data=td)
    data1 = {'Country': ['US','CA','GER','UK','FR'],
         'GDP_Per_Capita': [45000,42000,52000,49000,47000]
        }
    df1 = DataFrame(data1,columns=['Country','GDP_Per_Capita'])
    figure1 = plt.Figure(figsize=(3,6), dpi=100)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, showAnalysisroot)
    bar1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)
    df1 = df1[['Country','GDP_Per_Capita']].groupby('Country').sum()
    df1.plot(kind='bar', legend=True, ax=ax1)
    ax1.set_title('Country Vs. GDP Per Capita')

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
######################################################FrontPageButtonsFrame#################################
DataEntryFrame = Frame(root,bg = 'gold2',relief=GROOVE,borderwidth=5,width=400,height=670)
DataEntryFrame.place(x=10,y=20)

frontLabel = Label(DataEntryFrame,text='--------------Welcome-----------',width=21,font=('arial',22,'italic bold')
                   ,bg='gold2')
frontLabel.place(x=0,y=0)

homeBtn = Button(DataEntryFrame,text="1. Home",width=20,font=('arial',20,'italic'),bd=6,bg='red'
               ,relief=RIDGE,activebackground='red',activeforeground='white')
homeBtn.place(x=25,y=40)

productBtn = Button(DataEntryFrame,text="2. Products",width=20,font=('arial',20,'italic'),bd=6,bg='light blue'
               ,relief=RIDGE,activebackground='red',activeforeground='white',command=showProducts)
productBtn.place(x=25,y=120)

distributionBtn = Button(DataEntryFrame,text="3. Distribution",width=20,font=('arial',20,'italic'),bd=6,bg='light blue'
               ,relief=RIDGE,activebackground='red',activeforeground='white',command=showDistribution)
distributionBtn.place(x=25,y=200)


analysisBtn = Button(DataEntryFrame,text="4. Analysis",width=20,font=('arial',20,'italic'),bd=6,bg='light blue'
               ,relief=RIDGE,activebackground='red',activeforeground='white',command=showAnalysis)
analysisBtn.place(x=25,y=280)

userinfoBtn = Button(DataEntryFrame,text="5. User Info",width=20,font=('arial',20,'italic'),bd=6,bg='light blue'
               ,relief=RIDGE,activebackground='red',activeforeground='white',command=showUserInfo)
userinfoBtn.place(x=25,y=360)

logoutBtn = Button(DataEntryFrame,text="6. Logout",width=20,font=('arial',20,'italic'),bd=6,bg='light blue'
               ,relief=RIDGE,activebackground='red',activeforeground='white',command=logout)
logoutBtn.place(x=25,y=440)

root.mainloop()
