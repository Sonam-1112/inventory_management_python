from tkinter import *
from tkinter import messagebox
import math
import random
import os

root = Tk()
bg_color = "#074463"
root.title("Billing System")
root.geometry('1525x800+0+0')
root.configure(bg=bg_color)
root.resizable(False,False)

#############################################################################Bill Area Frame
F5 = Frame(root,bd=15,relief=GROOVE)
F5.place(x=1010,y=170,width=500,height=380)

bill_title = Label(F5,text = 'Bill Area',font=('times',15,'italic'),bd=10,relief=GROOVE)
bill_title.pack(fill=X)

scroll_y = Scrollbar(F5,orient=VERTICAL)
billarea = Text(F5,yscrollcommand = scroll_y.set)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_y.configure(command = billarea.yview)
billarea.pack(fill=BOTH,expand=1)
# billarea.configure(state='disabled')

cnameval = StringVar()
cphoneval = StringVar()
cbillval = StringVar()
bill_no = StringVar()
x = random.randint(1000,9999)
bill_no.set(str(x))

bathsoapval = IntVar()
facecreamval = IntVar()
facewashval = IntVar()
hairsprayval = IntVar()
hairgelval = IntVar()
bodylotionval = IntVar()

riceval = IntVar()
foodoilval = IntVar()
daalval = IntVar()
wheatval = IntVar()
sugarval = IntVar()
teaval = IntVar()

mazaval = IntVar()
cokeval = IntVar()
frootival = IntVar()
thumbsupval = IntVar()
limcaval = IntVar()
spriteval = IntVar()

totcosmeticval = StringVar()
totgroceryval = StringVar()
totcolddrinkval = StringVar()
taxcosmeticval = StringVar()
taxgroceryval = StringVar()
taxcolddrinkval = StringVar()

def main():
    ########################################################################Labels
    titleLabel = Label(root,text='Billing Software',bd=12,relief=GROOVE,fg='white',font=('Arial',20,'italic bold'),bg=bg_color)
    titleLabel.place(x=0,y=0,relwidth=1)

    ######################################################################Customer Detail Frame

    F1 = LabelFrame(root,text='Customer Details',font=('times',15,'bold'),fg='gold2',bg=bg_color,bd=12,relief=GROOVE)
    F1.place(x=0,y=59,relwidth=1)

    cnameLabel = Label(F1,text='Customer Name',bg=bg_color,fg='white',font=('times',18,'bold'),padx=40,pady=5)
    cnameLabel.grid(row=0,column=0)
    cnameEntry = Entry(F1,width=20,bd=5,font=('times',15,'italic'),textvariable=cnameval)
    cnameEntry.grid(row=0,column=1,padx=10,pady=5)


    cphoneLabel = Label(F1,text='Phone No.',bg=bg_color,fg='white',font=('times',18,'bold'),padx=40,pady=5)
    cphoneLabel.grid(row=0,column=2)
    cphoneEntry = Entry(F1,width=20,bd=5,font=('times',15,'italic'),textvariable=cphoneval)
    cphoneEntry.grid(row=0,column=3,padx=10,pady=5)


    cbillLabel = Label(F1,text='Bill No.',bg=bg_color,fg='white',font=('times',18,'bold'),padx=40,pady=5)
    cbillLabel.grid(row=0,column=4)
    cbillEntry = Entry(F1,width=20,bd=5,font=('times',15,'italic'),textvariable=cbillval)
    cbillEntry.grid(row=0,column=5,padx=10,pady=5)

    searchbtn = Button(F1,text='Search',bg='cadetblue',font=('times',15,'bold'),bd=12,width=10,command=searchfunc)
    searchbtn.grid(row=0,column=8,padx=10)


    #####################################################################Cosmetics Detail Frame
    

    F2 = LabelFrame(root,text='Cosmetics',font=('times',15,'bold'),fg='gold2',bg=bg_color,bd=15,relief=GROOVE)
    F2.place(x=5,y=170,width=325,height=380)

    bathLabel = Label(F2,text='Bath Soap',bg=bg_color,fg='light green',font=('times',18,'bold'))
    bathLabel.grid(row=0,column=0,sticky='w',padx=10,pady=10)
    bathEntry = Entry(F2,width=10,textvariable=bathsoapval,bd=5,font=('times',15,'italic'))
    bathEntry.grid(row=0,column=1,padx=10,pady=10)

    facecreamLabel = Label(F2,text='Face Cream',bg=bg_color,fg='light green',font=('times',18,'bold'))
    facecreamLabel.grid(row=1,column=0,sticky='w',padx=10,pady=10)
    facecreamEntry = Entry(F2,width=10,textvariable=facecreamval,bd=5,font=('times',15,'italic'))
    facecreamEntry.grid(row=1,column=1,padx=10,pady=10)

    facewashLabel = Label(F2,text='Face Wash',bg=bg_color,fg='light green',font=('times',18,'bold'))
    facewashLabel.grid(row=2,column=0,sticky='w',padx=10,pady=10)
    facewashEntry = Entry(F2,width=10,textvariable=facewashval,bd=5,font=('times',15,'italic'))
    facewashEntry.grid(row=2,column=1,padx=10,pady=10)

    hairsprayLabel = Label(F2,text='Hair Spray',bg=bg_color,fg='light green',font=('times',18,'bold'))
    hairsprayLabel.grid(row=3,column=0,sticky='w',padx=10,pady=10)
    hairsprayEntry = Entry(F2,width=10,textvariable=hairsprayval,bd=5,font=('times',15,'italic'))
    hairsprayEntry.grid(row=3,column=1,padx=10,pady=10)

    hairgelLabel = Label(F2,text='Hair Gel',bg=bg_color,fg='light green',font=('times',18,'bold'))
    hairgelLabel.grid(row=4,column=0,sticky='w',padx=10,pady=10)
    hairgelEntry = Entry(F2,width=10,textvariable=hairgelval,bd=5,font=('times',15,'italic'))
    hairgelEntry.grid(row=4,column=1,padx=10,pady=10)

    bodylotionLabel = Label(F2,text='Body lotion',bg=bg_color,fg='light green',font=('times',18,'bold'))
    bodylotionLabel.grid(row=5,column=0,sticky='w',padx=10,pady=10)
    bodylotionEntry = Entry(F2,width=10,textvariable=bodylotionval,bd=5,font=('times',15,'italic'))
    bodylotionEntry.grid(row=5,column=1,padx=10,pady=10)


    #####################################################################Grocery Detail Frame
    


    F3 = LabelFrame(root,text='Groceries',font=('times',15,'bold'),fg='gold2',bg=bg_color,bd=15,relief=GROOVE)
    F3.place(x=340,y=170,width=325,height=380)

    riceLabel = Label(F3,text='Rice',bg=bg_color,fg='light green',font=('times',18,'bold'))
    riceLabel.grid(row=0,column=0,sticky='w',padx=10,pady=10)
    riceEntry = Entry(F3,width=10,textvariable=riceval,bd=5,font=('times',15,'italic'))
    riceEntry.grid(row=0,column=1,padx=10,pady=10)

    foodoilLabel = Label(F3,text='Food oil',bg=bg_color,fg='light green',font=('times',18,'bold'))
    foodoilLabel.grid(row=1,column=0,sticky='w',padx=10,pady=10)
    foodoilEntry = Entry(F3,width=10,textvariable=foodoilval,bd=5,font=('times',15,'italic'))
    foodoilEntry.grid(row=1,column=1,padx=10,pady=10)

    daalLabel = Label(F3,text='Daal',bg=bg_color,fg='light green',font=('times',18,'bold'))
    daalLabel.grid(row=2,column=0,sticky='w',padx=10,pady=10)
    daalEntry = Entry(F3,width=10,textvariable=daalval,bd=5,font=('times',15,'italic'))
    daalEntry.grid(row=2,column=1,padx=10,pady=10)

    wheatLabel = Label(F3,text='Wheat',bg=bg_color,fg='light green',font=('times',18,'bold'))
    wheatLabel.grid(row=3,column=0,sticky='w',padx=10,pady=10)
    wheatEntry = Entry(F3,width=10,textvariable=wheatval,bd=5,font=('times',15,'italic'))
    wheatEntry.grid(row=3,column=1,padx=10,pady=10)

    sugarLabel = Label(F3,text='Sugar',bg=bg_color,fg='light green',font=('times',18,'bold'))
    sugarLabel.grid(row=4,column=0,sticky='w',padx=10,pady=10)
    sugarEntry = Entry(F3,width=10,textvariable=sugarval,bd=5,font=('times',15,'italic'))
    sugarEntry.grid(row=4,column=1,padx=10,pady=10)

    teaLabel = Label(F3,text='Tea',bg=bg_color,fg='light green',font=('times',18,'bold'))
    teaLabel.grid(row=5,column=0,sticky='w',padx=10,pady=10)
    teaEntry = Entry(F3,width=10,textvariable=teaval,bd=5,font=('times',15,'italic'))
    teaEntry.grid(row=5,column=1,padx=10,pady=10)


    #####################################################################Cold Drink Detail Frame
    


    F4 = LabelFrame(root,text='Cold Drinks',font=('times',15,'bold'),fg='gold2',bg=bg_color,bd=15,relief=GROOVE)
    F4.place(x=670,y=170,width=325,height=380)

    mazaLabel = Label(F4,text='Maza',bg=bg_color,fg='light green',font=('times',18,'bold'))
    mazaLabel.grid(row=0,column=0,sticky='w',padx=10,pady=10)
    mazaEntry = Entry(F4,width=10,textvariable=mazaval,bd=5,font=('times',15,'italic'))
    mazaEntry.grid(row=0,column=1,padx=10,pady=10)

    cokeLabel = Label(F4,text='Coke',bg=bg_color,fg='light green',font=('times',18,'bold'))
    cokeLabel.grid(row=1,column=0,sticky='w',padx=10,pady=10)
    cokeEntry = Entry(F4,width=10,textvariable=cokeval,bd=5,font=('times',15,'italic'))
    cokeEntry.grid(row=1,column=1,padx=10,pady=10)

    frootiLabel = Label(F4,text='Frooti',bg=bg_color,fg='light green',font=('times',18,'bold'))
    frootiLabel.grid(row=2,column=0,sticky='w',padx=10,pady=10)
    frootiEntry = Entry(F4,width=10,textvariable=frootival,bd=5,font=('times',15,'italic'))
    frootiEntry.grid(row=2,column=1,padx=10,pady=10)

    thumbsupLabel = Label(F4,text='Thumbs up',bg=bg_color,fg='light green',font=('times',18,'bold'))
    thumbsupLabel.grid(row=3,column=0,sticky='w',padx=10,pady=10)
    thumbsupEntry = Entry(F4,width=10,textvariable=thumbsupval,bd=5,font=('times',15,'italic'))
    thumbsupEntry.grid(row=3,column=1,padx=10,pady=10)

    limcaLabel = Label(F4,text='Limca',bg=bg_color,fg='light green',font=('times',18,'bold'))
    limcaLabel.grid(row=4,column=0,sticky='w',padx=10,pady=10)
    limcaEntry = Entry(F4,width=10,textvariable=limcaval,bd=5,font=('times',15,'italic'))
    limcaEntry.grid(row=4,column=1,padx=10,pady=10)

    spriteLabel = Label(F4,text='Sprite',bg=bg_color,fg='light green',font=('times',18,'bold'))
    spriteLabel.grid(row=5,column=0,sticky='w',padx=10,pady=10)
    spriteEntry = Entry(F4,width=10,textvariable=spriteval,bd=5,font=('times',15,'italic'))
    spriteEntry.grid(row=5,column=1,padx=10,pady=10)

    ##############################################################################Billing Menu Frame
    

    F6 = LabelFrame(root,text='Bill Menu',font=('times',15,'bold'),fg='gold2',bg=bg_color,bd=15,relief=GROOVE)
    F6.place(x=0,y=560,relwidth=1,height=220)

    cosmeticpriceLabel = Label(F6,text='Total Cosmetic Price',bg=bg_color,fg='light green',font=('times',18,'bold'))
    cosmeticpriceLabel.grid(row=0,column=0,sticky='w',padx=10,pady=10)
    cosmeticpriceEntry = Entry(F6,width=10,textvariable=totcosmeticval,bd=5,font=('times',15,'italic'))
    cosmeticpriceEntry.grid(row=0,column=1,padx=10,pady=10)

    grocerypriceLabel = Label(F6,text='Total Grocery Price',bg=bg_color,fg='light green',font=('times',18,'bold'))
    grocerypriceLabel.grid(row=1,column=0,sticky='w',padx=10,pady=10)
    grocerypriceEntry = Entry(F6,width=10,textvariable=totgroceryval,bd=5,font=('times',15,'italic'))
    grocerypriceEntry.grid(row=1,column=1,padx=10,pady=10)

    colddrinkpriceLabel = Label(F6,text='Total Cold Drink Price',bg=bg_color,fg='light green',font=('times',18,'bold'))
    colddrinkpriceLabel.grid(row=2,column=0,sticky='w',padx=10,pady=10)
    colddrinkpriceEntry = Entry(F6,width=10,textvariable=totcolddrinkval,bd=5,font=('times',15,'italic'))
    colddrinkpriceEntry.grid(row=2,column=1,padx=10,pady=10)

    cosmetictaxLabel = Label(F6,text='Cosmetic Tax',bg=bg_color,fg='light green',font=('times',18,'bold'))
    cosmetictaxLabel.grid(row=0,column=2,sticky='w',padx=10,pady=10)
    cosmetictaxEntry = Entry(F6,width=10,bd=5,textvariable=taxcosmeticval,font=('times',15,'italic'))
    cosmetictaxEntry.grid(row=0,column=3,padx=10,pady=10)

    grocerytaxLabel = Label(F6,text='Grocery Tax',bg=bg_color,fg='light green',font=('times',18,'bold'))
    grocerytaxLabel.grid(row=1,column=2,sticky='w',padx=10,pady=10)
    grocerytaxEntry = Entry(F6,width=10,bd=5,textvariable=taxgroceryval,font=('times',15,'italic'))
    grocerytaxEntry.grid(row=1,column=3,padx=10,pady=10)

    colddrinktaxLabel = Label(F6,text='Cold Drink Tax',bg=bg_color,fg='light green',font=('times',18,'bold'))
    colddrinktaxLabel.grid(row=2,column=2,sticky='w',padx=10,pady=10)
    colddrinktaxEntry = Entry(F6,width=10,textvariable=taxcolddrinkval,bd=5,font=('times',15,'italic'))
    colddrinktaxEntry.grid(row=2,column=3,padx=10,pady=10)

    ###############################################################################Buttons Frame

    F7 = Frame(F6,bd=15,relief=GROOVE)
    F7.place(x=750,y=27,width=720,height=105)

    totalbtn = Button(F7,text="Total",bd=12,font=('times',15,'italic bold'),bg='cadetblue',width=10,command=totalfunc)
    totalbtn.grid(row=0,column=0,padx=14,pady=8)

    genbillbtn = Button(F7,text="Generate Bill",bd=12,font=('times',15,'italic bold'),bg='cadetblue',width=10,command=genbillfunc)
    genbillbtn.grid(row=0,column=1,padx=14,pady=8)

    clearbtn = Button(F7,text="Clear",bd=12,font=('times',15,'italic bold'),bg='cadetblue',width=10,command=clearfunc)
    clearbtn.grid(row=0,column=2,padx=14,pady=8)

    exitbtn = Button(F7,text="Exit",bd=12,font=('times',15,'italic bold'),bg='cadetblue',width=10,command=exitfunc)
    exitbtn.grid(row=0,column=3,padx=14,pady=8)

    root.mainloop()

def welcome_bill():
    billarea.delete('1.0',END)
    billarea.insert(END,"\t\tWelcome Dear Customer\n")
    billarea.insert(END,f"\n\nBill Number    : {bill_no.get()}")
    billarea.insert(END,f"\nCustomer Name  : {cnameval.get()}")
    billarea.insert(END,f"\nCustomer Phone : {cphoneval.get()}")
    billarea.insert(END,f"\n========================================================")
    billarea.insert(END,f"\nProducts\t\t\tQTY\t\t\tPrice")
    billarea.insert(END,f"\n========================================================")
   
    if(bathsoapval.get()!=0):
        billarea.insert(END,f"\nBath Soap\t\t\t{bathsoapval.get()}\t\t\t{a_bs}")
    if(facecreamval.get()!=0):
        billarea.insert(END,f"\nFace Cream\t\t\t{facecreamval.get()}\t\t\t{a_fc}")
    if(facewashval.get()!=0):
        billarea.insert(END,f"\nFace Wash\t\t\t{facewashval.get()}\t\t\t{a_fw}")
    if(hairsprayval.get()!=0):
        billarea.insert(END,f"\nHair Spray\t\t\t{hairsprayval.get()}\t\t\t{a_hs}")
    if(hairgelval.get()!=0):
        billarea.insert(END,f"\nHair Gel\t\t\t{hairgelval.get()}\t\t\t{a_hg}")
    if(bodylotionval.get()!=0):
        billarea.insert(END,f"\nBody Lotion\t\t\t{bodylotionval.get()}\t\t\t{a_bl}")
    
    
    if(riceval.get()!=0):
        billarea.insert(END,f"\nRice\t\t\t{riceval.get()}\t\t\t{a_ri}")
    if(foodoilval.get()!=0):
        billarea.insert(END,f"\nFood Oil\t\t\t{foodoilval.get()}\t\t\t{a_fo}")
    if(daalval.get()!=0):
        billarea.insert(END,f"\nDaal\t\t\t{daalval.get()}\t\t\t{a_da}")
    if(wheatval.get()!=0):
        billarea.insert(END,f"\nWheat\t\t\t{wheatval.get()}\t\t\t{a_wh}")
    if(sugarval.get()!=0):
        billarea.insert(END,f"\nSugar\t\t\t{sugarval.get()}\t\t\t{a_su}")
    if(teaval.get()!=0):
        billarea.insert(END,f"\nTea\t\t\t{teaval.get()}\t\t\t{a_te}")
    
   
    if(mazaval.get()!=0):
        billarea.insert(END,f"\nMaza\t\t\t{mazaval.get()}\t\t\t{a_ma}")
    if(cokeval.get()!=0):
        billarea.insert(END,f"\nCoke\t\t\t{cokeval.get()}\t\t\t{a_co}")
    if(frootival.get()!=0):
        billarea.insert(END,f"\nFrooti\t\t\t{frootival.get()}\t\t\t{a_fr}")
    if(thumbsupval.get()!=0):
        billarea.insert(END,f"\nThumbs Up\t\t\t{thumbsupval.get()}\t\t\t{a_tu}")
    if(limcaval.get()!=0):
        billarea.insert(END,f"\nLimca\t\t\t{limcaval.get()}\t\t\t{a_li}")
    if(spriteval.get()!=0):
        billarea.insert(END,f"\nSprite\t\t\t{spriteval.get()}\t\t\t{a_sp}")
    
    billarea.insert(END,f"\n========================================================")
    if(taxcosmeticval.get()!='Rs.0.0'):
        billarea.insert(END,f"\nCosmetic Tax\t\t\t\t\t\t{taxcosmeticval.get()}")
    if(taxgroceryval.get()!='Rs.0.0'):
        billarea.insert(END,f"\nGrocery Tax\t\t\t\t\t\t{taxgroceryval.get()}")
    if(taxcolddrinkval.get()!='Rs.0.0'):
        billarea.insert(END,f"\nCold Drink Tax\t\t\t\t\t\t{taxcolddrinkval.get()}")
    billarea.insert(END,f"\n========================================================")
    billarea.insert(END,f"\nTotal Bill\t\t\t\t\t\t{'Rs.'+str(float(totcosmeticprice)+float(totgroceryprice)+float(totcolddrinkprice)+float(totcosmeticprice*0.05)+float(totgroceryprice*0.05)+float(totcolddrinkprice*0.05))}")

def savebill():
    rr = messagebox.askyesnocancel("Save Bill","Do you want to save bill?",parent = root)
    if(rr == True):
        bill_data = billarea.get('1.0',END)
        f1 = open("C:\\Users\\DELL\\Desktop\\Billing_recipts\\"+str(bill_no.get())+".txt","w")
        f1.write(bill_data)
        f1.close()
        messagebox.showinfo('Notification',f'Bill No:{bill_no.get()} saved successfully',parent = root)
    else:
        return

def bill_calcy():
    if(cnameval.get() == "" or cphoneval.get() == ""):
        messagebox.showerror('Notification','Customer Details are required!!!',parent = root)
    elif(totcosmeticprice==0 and totgroceryprice==0 and totcolddrinkprice==0):
        messagebox.showerror('Notification','No Product has been selected!!!',parent = root)  
    else:
        welcome_bill()
        savebill()
    
    
def totalfunc():
    global a_bs,a_fc,a_fw,a_hs,a_hg,a_bl,a_ri,a_fo,a_da,a_wh,a_su,a_te,a_ma,a_co,a_fr,a_tu,a_li,a_sp,totcosmeticprice,totgroceryprice,totcolddrinkprice
    #####################Cosmetics############
    a_bs = bathsoapval.get()*40
    a_fc = facecreamval.get()*120
    a_fw = facewashval.get()*60
    a_hs = hairsprayval.get()*180
    a_hg = hairgelval.get()*140
    a_bl = bodylotionval.get()*180
    
    totcosmeticprice = (a_bs+a_fc+a_fw+a_hs+a_hg+a_bl)
    totcosmeticval.set('Rs.'+str(totcosmeticprice))
    taxcosmeticval.set('Rs.'+str(totcosmeticprice*0.05))
    
    #####################Groceries############
    a_ri = riceval.get()*80
    a_fo = foodoilval.get()*180
    a_da = daalval.get()*60
    a_wh = wheatval.get()*240
    a_su = sugarval.get()*45
    a_te = teaval.get()*150
    
    totgroceryprice = (a_ri+a_fo+a_da+a_wh+a_su+a_te)
    totgroceryval.set('Rs.'+str(totgroceryprice))
    taxgroceryval.set('Rs.'+str(totgroceryprice*0.05))
    
    
    #####################Cold Drinks############
    a_ma = mazaval.get()*60
    a_co = cokeval.get()*60
    a_fr = frootival.get()*50
    a_tu = thumbsupval.get()*45
    a_li = limcaval.get()*40
    a_sp = spriteval.get()*60
    
    totcolddrinkprice = (a_ma+a_co+a_fr+a_tu+a_li+a_sp)
    totcolddrinkval.set('Rs.'+str(totcolddrinkprice))
    taxcolddrinkval.set('Rs.'+str(totcolddrinkprice*0.05))

def genbillfunc():
     bill_calcy()

def clearfunc():
    cnameval.set('')
    cphoneval.set('')
    cbillval.set('')
    bathsoapval.set(0)
    facecreamval.set(0)
    facewashval.set(0)
    hairsprayval.set(0)
    hairgelval.set(0)
    bodylotionval.set(0)
    riceval.set(0)
    foodoilval.set(0)
    daalval.set(0)
    wheatval.set(0)
    sugarval.set(0)
    teaval.set(0)
    mazaval.set(0)
    cokeval.set(0)
    frootival.set(0)
    thumbsupval.set(0)
    limcaval.set(0)
    spriteval.set(0)
    totcosmeticval.set('')
    totgroceryval.set('')
    totcolddrinkval.set('')
    taxcosmeticval.set('')
    taxgroceryval.set('')
    taxcolddrinkval.set('')
    
def exitfunc():
    rr = messagebox.askyesnocancel("Notification","Are you sure you want to exit?",parent=root)
    if(rr == True):
        root.destroy()

def searchfunc():
    present = "No"
    for i in os.listdir("C:\\Users\\DELL\\Desktop\\Billing_recipts\\"):
        if i.split('.')[0] == cbillval.get():
            f1 = open("C:\\Users\\DELL\\Desktop\\Billing_recipts\\"+str(cbillval.get())+".txt","r")
            billarea.delete('1.0',END)
            for d in f1:
                billarea.insert(END,d)
            f1.close()
            present ="Yes"
    if(present == "No"):
        messagebox.showerror("Error","Bill No. Not Found!!!")