from tkinter import *
from tkinter import messagebox
import math
import random
import os
import pymysql
from tkinter.ttk import Treeview
from tkinter import ttk
# import Manufacturer_View
# import Buyer_View


root = Tk()
bg_color = "powder blue"
root.title("Buy Products")
root.geometry('1525x800+0+0')
root.configure(bg=bg_color)
root.resizable(False,False)

billingFrame = Frame(root,bd=15,relief=GROOVE)
billingFrame.place(x=0,y=170,width=399,height=380)

bill_title = Label(billingFrame,text = 'Bill Area',font=('times',15,'italic'),bd=10,relief=GROOVE)
bill_title.pack(fill=X)

def on_entersearchbtn(e):
    searchbtn.configure(bg='red')
def on_leavesearchbtn(e):
    searchbtn.configure(bg='blue')

def on_enterplaceorderbtn(e):
    placeorderbtn.configure(bg='red')
def on_leaveplaceorderbtn(e):
    placeorderbtn.configure(bg='blue')

def placeorderfunc():
    custname = custnameval.get()
    custphone = custphoneval.get()
    if(custname.strip()==""):
        messagebox.showinfo("Info","Please fill your name...!!!",parent=popupWin)
    elif(custphone==""):
        messagebox.showinfo("Info","Please fill your phone number...!!!",parent=popupWin)
    elif(len(custphone) != 10):
        messagebox.showinfo("Info","Not a valid phone number...!!!",parent=popupWin)
    else:
        bill_no = StringVar()
        x = random.randint(1000,9999)
        bill_no.set(str(x))
        billarea.delete('1.0',END)
        billarea.insert(END,"\tWelcome Dear Customer\n")
        billarea.insert(END,f"\n\nBill Number    : {bill_no.get()}")
        billarea.insert(END,f"\nCustomer Name  : {custnameval.get()}")
        billarea.insert(END,f"\nCustomer Phone : {custphoneval.get()}")
        billarea.insert(END,f"\n===========================================")
        billarea.insert(END,f"\nProducts\t\tSize\t\tPrice")
        billarea.insert(END,f"\n===========================================")
        billarea.insert(END,f"\n{a.column(1).get()}\t\t\t{a.column(3).get()}\t\t\t{a.column(5).get()}")

placeorderbtn = Button(root,text='Place Order',font=('Arial',15,'bold'),width=10,bg='blue',foreground="white",activebackground='red'
                            ,activeforeground='white',relief=GROOVE,bd=9,command = placeorderfunc)
placeorderbtn.place(x=130,y=600)
placeorderbtn.bind('<Enter>',on_enterplaceorderbtn)
placeorderbtn.bind('<Leave>',on_leaveplaceorderbtn)

scroll_y = Scrollbar(billingFrame,orient=VERTICAL)
billarea = Text(billingFrame,yscrollcommand = scroll_y.set)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_y.configure(command = billarea.yview)
billarea.pack(fill=BOTH,expand=1)
# billarea.configure(state='disabled')

def searchfunc():
    searchproduct = searchproductnameval.get()
    if(searchproduct !=''):
        query = 'select * from productinfo where name=%s;'
        mycursor.execute(query,(searchproduct))
        data = mycursor.fetchall()
        productsTable.delete(*productsTable.get_children())
        for i in data:
            vv = [i[0],i[1],i[5],i[3]]
            productsTable.insert('',END,values=vv)
    else:
        query = 'select * from productinfo;'
        mycursor.execute(query)
        data = mycursor.fetchall()
        productsTable.delete(*productsTable.get_children())
        for i in data:
            vv = [i[0],i[1],i[5],i[3]]
            productsTable.insert('',END,values=vv)

searchproductnameval = StringVar()
custnameval = StringVar()
custphoneval = StringVar()

searchproductEntry = Entry(root,textvariable=searchproductnameval,width=38,font=('arial',12,'italic'),bd=5,bg='light pink')
searchproductEntry.place(x=20,y=50)

searchbtn = Button(root,text='Search Product',font=('Arial',15,'bold'),width=14,bg='blue',foreground="white",activebackground='red'
                            ,activeforeground='white',relief=GROOVE,bd=9,command = searchfunc)
searchbtn.place(x=100,y=100)
searchbtn.bind('<Enter>',on_entersearchbtn)
searchbtn.bind('<Leave>',on_leavesearchbtn)

####################################################################Customer Entry Details
custnameLabel = Label(root,text="Your Name : ",bg = 'powder blue',font = ('times',20,'bold italic'),anchor='w')
custnameLabel.place(x=400,y=10)

custphoneLabel = Label(root,text="Your Phone No.: ",bg = 'powder blue',font = ('times',20,'bold italic'),anchor='w')
custphoneLabel.place(x=950,y=10)

custnameEntry = Entry(root,textvariable=custnameval,width=32,font=('arial',12,'italic'),bd=5,bg='light pink')
custnameEntry.place(x=580,y=10)

custphoneEntry = Entry(root,textvariable=custphoneval,width=32,font=('arial',12,'italic'),bd=5,bg='light pink')
custphoneEntry.place(x=1180,y=10)

#####################################################################ProductsInfo Table
productstableFrame = Frame(root,bg = 'gold2',relief=GROOVE,borderwidth=5)
productstableFrame.place(x=400,y=50,width=1120,height=730)

style = ttk.Style()
style.configure('Treeview.Heading',font=('times',15,'italic'),foreground='green')
style.configure('Treeview',font=('times',12,'italic'),foreground='black',background='powder blue')

scroll_x = Scrollbar(productstableFrame,orient = HORIZONTAL)
scroll_y = Scrollbar(productstableFrame,orient = VERTICAL)

productsTable = Treeview(productstableFrame,columns = ('Product ID','Name','Price','Size'),yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
def select_item(a):
    popupWin = Toplevel()
    popupWin.geometry('550x500+500+150')
    popupWin.grab_set()                                          ######Untill this window is closed nothing will work
    popupWin.resizable(False,False)
    popupWin.title("Product Details")
    popupWin.configure(bg = 'powder blue')
    def on_enteraddtocartbtn(e):
        addtocartbtn.configure(bg='red')
    def on_leaveaddtocartbtn(e):
        addtocartbtn.configure(bg='blue')
    def addtocartbtnfunc():
        custname = custnameval.get()
        custphone = custphoneval.get()
        if(custname.strip()==""):
            messagebox.showinfo("Info","Please fill your name...!!!",parent=popupWin)
        elif(custphone==""):
            messagebox.showinfo("Info","Please fill your phone number...!!!",parent=popupWin)
        elif(len(custphone) != 10):
            messagebox.showinfo("Info","Not a valid phone number...!!!",parent=popupWin)
        else:
            billarea.delete('1.0',END)
            billarea.insert(END,"\tWelcome Dear Customer\n")
            billarea.insert(END,f"\n\nBill Number    : {bill_no.get()}")
            billarea.insert(END,f"\nCustomer Name  : {custnameval.get()}")
            billarea.insert(END,f"\nCustomer Phone : {custphoneval.get()}")
            billarea.insert(END,f"\n===========================================")
            billarea.insert(END,f"\nProducts\t\tSize\t\tPrice")
            billarea.insert(END,f"\n===========================================")
            billarea.insert(END,f"\n{a.column(1).get()}\t\t\t{a.column(3).get()}\t\t\t{a.column(5).get()}")
            # if(s_id !=''):
            #     query = 'select * from productinfo where productid=%s;'
            #     mycursor.execute(query,(s_id))
            #     data = mycursor.fetchall()
            #     productinfoTable.delete(*productinfoTable.get_children())
            #     for i in data:
            #         vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
            #         productinfoTable.insert('',END,values=vv)

    #################################################Labels
    s_idLabel = Label(popupWin,text="Product ID : ",bg = 'powder blue',font = ('times',20,'bold italic'),anchor='w')
    s_idLabel.place(x=10,y=10)

    s_nameLabel = Label(popupWin,text="Name : ",bg = 'powder blue',font = ('times',20,'bold italic'),anchor='w')
    s_nameLabel.place(x=10,y=70)

    s_sizeLabel = Label(popupWin,text="Size : ",bg = 'powder blue',font = ('times',20,'bold italic'),anchor='w')
    s_sizeLabel.place(x=10,y=130)

    s_weightLabel = Label(popupWin,text="Weight(kg) : ",bg = 'powder blue',font = ('times',20,'bold italic'),anchor='w')
    s_weightLabel.place(x=10,y=190)

    s_priceLabel = Label(popupWin,text="Price(Rs.) : ",bg = 'powder blue',font = ('times',20,'bold italic'),anchor='w')
    s_priceLabel.place(x=10,y=250)

    s_colorLabel = Label(popupWin,text="Color : ",bg = 'powder blue',font = ('times',20,'bold italic'),anchor='w')
    s_colorLabel.place(x=10,y=310)
            
    s_statusLabel = Label(popupWin,text="Status : ",bg = 'powder blue',font = ('times',20,'bold italic'),anchor='w')
    s_statusLabel.place(x=10,y=370)

    #################################################Labels as Entry Boxes
    a_idEntry = Label(popupWin,width=32,font=('arial',12,'italic'),bd=5,bg='light pink')
    a_idEntry.place(x=240,y=10)

    a_nameEntry = Label(popupWin,width=32,font=('arial',12,'italic'),bd=5,bg='light pink')
    a_nameEntry.place(x=240,y=70)

    a_sizeEntry = Label(popupWin,width=32,font=('arial',12,'italic'),bd=5,bg='light pink')
    a_sizeEntry.place(x=240,y=130)

    a_weightEntry = Label(popupWin,width=32,font=('arial',12,'italic'),bd=5,bg='light pink')
    a_weightEntry.place(x=240,y=190)

    a_priceEntry = Label(popupWin,width=32,font=('arial',12,'italic'),bd=5,bg='light pink')
    a_priceEntry.place(x=240,y=250)

    a_colorEntry = Label(popupWin,width=32,font=('arial',12,'italic'),bd=5,bg='light pink')
    a_colorEntry.place(x=240,y=310)

    s_statusEntry = Label(popupWin,width=32,font=('arial',12,'italic'),bd=5,bg='light pink')
    s_statusEntry.place(x=240,y=370)

    ########################################################Buttons
    addtocartbtn = Button(popupWin,text='Add To Cart',font=('Arial',15,'bold'),width=10,bg='blue',foreground="white",activebackground='red'
                    ,activeforeground='white',relief=GROOVE,bd=9,command = addtocartbtnfunc)
    addtocartbtn.place(x=190,y=430)
    addtocartbtn.bind('<Enter>',on_enteraddtocartbtn)
    addtocartbtn.bind('<Leave>',on_leaveaddtocartbtn)

    test_str_library = productsTable.item(productsTable.selection())# gets all the values of the selected row
    print ('The test_str = ', type(test_str_library), test_str_library,  '\n')  # prints a dictionay of the selected row
    item = productsTable.selection()[0] # which row did you click on
    print ('item clicked ', item) # variable that represents the row you clicked on
    # print (productsTable.item(item)['values'][0]) # prints the first value of the values (the id value)

    selectedItemId = test_str_library['values'][0]
    query = "select * from productinfo where productid=%s"
    mycursor.execute(query,(selectedItemId))
    data = mycursor.fetchall()
    for i in data:
        a_idEntry.configure(text=i[0])
        a_nameEntry.configure(text=i[1])
        a_sizeEntry.configure(text=i[3])
        a_weightEntry.configure(text=i[4])
        a_priceEntry.configure(text=i[5])
        a_colorEntry.configure(text=i[6])
        s_statusEntry.configure(text=i[7])

productsTable.bind('<ButtonRelease-1>', select_item) 

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.configure(command = productsTable.xview)
scroll_y.configure(command = productsTable.yview)

productsTable.heading('Product ID',text='Product ID')
productsTable.heading('Name',text='Name')
productsTable.heading('Price',text='Price')
productsTable.heading('Size',text='Size')

productsTable.configure(show='headings')

productsTable.column('Product ID',width=100,anchor="center")
productsTable.column('Name',width=200,anchor="center")
productsTable.column('Price',width=200,anchor="center")
productsTable.column('Size',width=300,anchor="center")

productsTable.pack(fill=BOTH,expand=1)

con = pymysql.connect(host='localhost',user='root',password='')
mycursor = con.cursor()
query = 'use inventoryDB;'
mycursor.execute(query)
query = 'select * from productinfo;'
mycursor.execute(query)
data = mycursor.fetchall()
productsTable.delete(*productsTable.get_children())

for i in data:
    vv = [i[0],i[1],i[5],i[3]]
    productsTable.insert('',END,values=vv)

root.mainloop()