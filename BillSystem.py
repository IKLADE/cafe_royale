from tkinter import*
from tkinter import messagebox
import random
import time;
import datetime

root=Tk()
root.geometry("1350x750+0+0")
root.title("IK Billing System")
root.configure(background='black')

Tops=Frame(root,width=1350,height=100,bd=14,relief="raise")
Tops.pack(side=TOP)

f1=Frame(root,width=900,height=650,bd=8,relief="raise")
f1.pack(side=LEFT)
f2=Frame(root,width=440,height=650,bd=8,relief="raise")
f2.pack(side=RIGHT)

f1a=Frame(f1,width=900,height=330,bd=8,relief="raise")
f1a.pack(side=TOP)
f2a=Frame(f1,width=900,height=320,bd=6,relief="raise")
f2a.pack(side=BOTTOM)

ft2=Frame(f2,width=440,height=450,bd=12,relief="raise")
ft2.pack(side=TOP)
fb2=Frame(f2,width=440,height=250,bd=16,relief="raise")
fb2.pack(side=BOTTOM)

f1aa=Frame(f1a,width=400,height=330,bd=16,relief="raise")
f1aa.pack(side=LEFT)
f1ab=Frame(f1a,width=400,height=330,bd=16,relief="raise")
f1ab.pack(side=RIGHT)

f2aa=Frame(f2a,width=450,height=330,bd=14,relief="raise")
f2aa.pack(side=LEFT)
f2ab=Frame(f2a,width=450,height=330,bd=14,relief="raise")
f2ab.pack(side=RIGHT)

Tops.configure(background='black')
f1.configure(background='black')
f2.configure(background='black')

def Receipt():
	txtReceipt.delete("1.0",END)
	x=random.randint(100000,999999)
	randomRef=str(x)
	Receipt_Ref.set("BILL"+randomRef)

	txtReceipt.insert(END,'Receipt Ref:\t\t'+Receipt_Ref.get()+"\t\t"+Date.get()+"\n")
	txtReceipt.insert(END,'Items\t\t\t'+"Number of Items\n\n")
	txtReceipt.insert(END,'Filter Coffee\t\t\t'+E_FC.get()+"\n")
	txtReceipt.insert(END,'White Coffee\t\t\t'+E_WC.get()+"\n")
	txtReceipt.insert(END,'Black Coffee\t\t\t'+E_BC.get()+"\n")
	txtReceipt.insert(END,'Cappucino\t\t\t'+E_Cap.get()+"\n")
	txtReceipt.insert(END,'Latte\t\t\t'+E_La.get()+"\n")
	txtReceipt.insert(END,'Espresso\t\t\t'+E_Esp.get()+"\n")
	txtReceipt.insert(END,'Cold Coffee\t\t\t'+E_CC.get()+"\n")
	txtReceipt.insert(END,'Custom Coffee\t\t\t'+E_Cus.get()+"\n")
	txtReceipt.insert(END,'Club Sandwich\t\t\t'+E_CS.get()+"\n")
	txtReceipt.insert(END,'Lava Cake\t\t\t'+E_Lava.get()+"\n")
	txtReceipt.insert(END,'Doughnut\t\t\t'+E_Dou.get()+"\n")
	txtReceipt.insert(END,'Mousse Cake\t\t\t'+E_MC.get()+"\n")
	txtReceipt.insert(END,'French Fries\t\t\t'+E_FF.get()+"\n")
	txtReceipt.insert(END,'Hot Dog\t\t\t'+E_HD.get()+"\n")
	txtReceipt.insert(END,'Hamburger\t\t\t'+E_Ham.get()+"\n")
	txtReceipt.insert(END,'Chocolate Brownie\t\t\t'+E_ChocB.get()+"\n")
	txtReceipt.insert(END,'Cost of Drinks:\t'+Drinks.get()+'\tTax Paid:\t'+PaidTax.get()+"\n")
	txtReceipt.insert(END,'Cost of Snacks:\t'+Snacks.get()+'\tSub Total:\t'+Sub.get()+"\n")
	txtReceipt.insert(END,'Service Charge:\t'+Service.get()+'\tTotal Cost:\t'+Total.get()+"\n")

#========================================================================================================

lblinfo=Label(Tops,font=('Lucida Fax',70,'bold'),text='            Cafe Royale           ',bd=10)
lblinfo.grid(row=0,column=0)

#=================Functions===========================

def qExit():
	qExit=messagebox.askyesno("Quit System","Do You Want To Quit?")
	if qExit>0:
		root.destroy()
		return

def Reset():
	PaidTax.set("")
	Sub.set("")
	Total.set("")
	Drinks.set("")
	Snacks.set("")
	Service.set("")
	txtReceipt.delete("1.0",END)

	E_FC.set("0")
	E_WC.set("0")
	E_BC.set("0")
	E_Cap.set("0")
	E_La.set("0")
	E_Esp.set("0")
	E_CC.set("0")
	E_Cus.set("0")
	E_CS.set("0")
	E_Lava.set("0")
	E_Dou.set("0")
	E_MC.set("0")
	E_FF.set("0")
	E_HD.set("0")
	E_Ham.set("0")
	E_ChocB.set("0")

#=====================ChkButton==============

def chkbutton_value():
	if(var1.get()==1):
		txtFC.configure(state=NORMAL)
	elif var1.get()==0:
		txtFC.configure(state=DISABLED)
		E_FC.set("0")
	if(var2.get()==1):
		txtWC.configure(state=NORMAL)
	elif var2.get()==0:
		txtWC.configure(state=DISABLED)
		E_WC.set("0")
	if(var3.get()==1):
		txtBC.configure(state=NORMAL)
	elif var3.get()==0:
		txtBC.configure(state=DISABLED)
		E_BC.set("0")
	if(var4.get()==1):
		txtCap.configure(state=NORMAL)
	elif var4.get()==0:
		txtCap.configure(state=DISABLED)
		E_Cap.set("0")
	if(var5.get()==1):
		txtLa.configure(state=NORMAL)
	elif var5.get()==0:
		txtLa.configure(state=DISABLED)
		E_La.set("0")
	if(var6.get()==1):
		txtEsp.configure(state=NORMAL)
	elif var6.get()==0:
		txtEsp.configure(state=DISABLED)
		E_Esp.set("0")
	if(var7.get()==1):
		txtCC.configure(state=NORMAL)
	elif var7.get()==0:
		txtCC.configure(state=DISABLED)
		E_CC.set("0")
	if(var8.get()==1):
		txtCus.configure(state=NORMAL)
	elif var8.get()==0:
		txtCus.configure(state=DISABLED)
		E_Cus.set("0")
	if(var9.get()==1):
		txtCS.configure(state=NORMAL)
	elif var9.get()==0:
		txtCS.configure(state=DISABLED)
		E_CS.set("0")
	if(var10.get()==1):
		txtLava.configure(state=NORMAL)
	elif var10.get()==0:
		txtLava.configure(state=DISABLED)
		E_Lava.set("0")
	if(var11.get()==1):
		txtDou.configure(state=NORMAL)
	elif var11.get()==0:
		txtDou.configure(state=DISABLED)
		E_Dou.set("0")
	if(var12.get()==1):
		txtMC.configure(state=NORMAL)
	elif var12.get()==0:
		txtMC.configure(state=DISABLED)
		E_MC.set("0")
	if(var13.get()==1):
		txtFF.configure(state=NORMAL)
	elif var13.get()==0:
		txtFF.configure(state=DISABLED)
		E_FF.set("0")
	if(var14.get()==1):
		txtHD.configure(state=NORMAL)
	elif var14.get()==0:
		txtHD.configure(state=DISABLED)
		E_HD.set("0")
	if(var15.get()==1):
		txtHam.configure(state=NORMAL)
	elif var15.get()==0:
		txtHam.configure(state=DISABLED)
		E_Ham.set("0")
	if(var16.get()==1):
		txtChocB.configure(state=NORMAL)
	elif var16.get()==0:
		txtChocB.configure(state=DISABLED)
		E_ChocB.set("0")
	

#==================CostofItem=========================

def costofitem():
	Item1=float(E_FC.get())
	Item2=float(E_WC.get())
	Item3=float(E_BC.get())
	Item4=float(E_Cap.get())
	Item5=float(E_La.get())
	Item6=float(E_Esp.get())
	Item7=float(E_CC.get())
	Item8=float(E_Cus.get())
	Item9=float(E_CS.get())
	Item10=float(E_Lava.get())
	Item11=float(E_Dou.get())
	Item12=float(E_MC.get())
	Item13=float(E_FF.get())
	Item14=float(E_HD.get())
	Item15=float(E_Ham.get())
	Item16=float(E_ChocB.get())

	priceofdrinks=(Item1*50)+(Item2*60)+(Item3*60)+(Item4*75)+(Item5*90)+(Item6*95)+(Item7*70)+(Item8*100)

	priceofsnacks=(Item9*50)+(Item10*80)+(Item11*40)+(Item12*50)+(Item13*35)+(Item14*50)+(Item15*60)+(Item16*35)

	drinksprice="Rs",str('%.2f'%(priceofdrinks))
	snacksprice="Rs",str('%.2f'%(priceofsnacks))
	Snacks.set(snacksprice)
	Drinks.set(drinksprice)
	SC="Rs",str('%.2f'%(0.005*(priceofsnacks+priceofdrinks)))
	Service.set(SC)

	subtotalofITEMS="Rs",str('%.2f'%(priceofdrinks+priceofsnacks))
	Sub.set(subtotalofITEMS)

	Tax="Rs",str((priceofdrinks + priceofsnacks )*0.12)
	PaidTax.set(Tax)
	TT=((priceofdrinks+priceofsnacks)*0.12)
	TC="Rs",str((priceofdrinks+priceofsnacks+(0.005*(priceofsnacks+priceofdrinks))+TT))
	Total.set(TC)	



	var1.set("0")
	var2.set("0")
	var3.set("0")
	var4.set("0")
	var5.set("0")
	var6.set("0")
	var7.set("0")
	var8.set("0")
	var9.set("0")
	var10.set("0")
	var11.set("0")
	var12.set("0")
	var13.set("0")
	var14.set("0")
	var15.set("0")
	var16.set("0")

	txtFC.configure(state=DISABLED)
	txtWC.configure(state=DISABLED)
	txtBC.configure(state=DISABLED)
	txtCap.configure(state=DISABLED)
	txtLa.configure(state=DISABLED)
	txtEsp.configure(state=DISABLED)
	txtCC.configure(state=DISABLED)
	txtCus.configure(state=DISABLED)
	txtCS.configure(state=DISABLED)
	txtLava.configure(state=DISABLED)
	txtDou.configure(state=DISABLED)
	txtMC.configure(state=DISABLED)
	txtFF.configure(state=DISABLED)
	txtHD.configure(state=DISABLED)
	txtHam.configure(state=DISABLED)
	txtChocB.configure(state=DISABLED)

#===============Variables===============

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()

Date=StringVar()
Receipt_Ref=StringVar()
PaidTax=StringVar()
Sub=StringVar()
Total=StringVar()
Snacks=StringVar()
Drinks=StringVar()
Service=StringVar()

E_FC=StringVar()
E_WC=StringVar()
E_BC=StringVar()
E_Cap=StringVar()
E_La=StringVar()
E_Esp=StringVar()
E_CC=StringVar()
E_Cus=StringVar()

E_CS=StringVar()
E_Lava=StringVar()
E_Dou=StringVar()
E_MC=StringVar()
E_FF=StringVar()
E_HD=StringVar()
E_Ham=StringVar()
E_ChocB=StringVar()

E_FC.set("0")
E_WC.set("0")
E_BC.set("0")
E_Cap.set("0")
E_La.set("0")
E_Esp.set("0")
E_CC.set("0")
E_Cus.set("0")

E_CS.set("0")
E_Lava.set("0")
E_Dou.set("0")
E_MC.set("0")
E_FF.set("0")
E_HD.set("0")
E_Ham.set("0")
E_ChocB.set("0")

Date.set(time.strftime("%d/%m/%Y"))

var1.set("0")
var2.set("0")
var3.set("0")
var4.set("0")
var5.set("0")
var6.set("0")
var7.set("0")
var8.set("0")
var9.set("0")
var10.set("0")
var11.set("0")
var12.set("0")
var13.set("0")
var14.set("0")
var15.set("0")
var16.set("0")


FC=Checkbutton(f1aa,text="Filter Coffee \t",variable=var1,onvalue=1,offvalue=0,font=('Lucida Fax',18,'bold'),command=chkbutton_value).grid(row=0,sticky=W)
WC=Checkbutton(f1aa,text="White Coffee \t",variable=var2,onvalue=1,offvalue=0,font=('Lucida Fax',18,'bold'),command=chkbutton_value).grid(row=1,sticky=W)
BC=Checkbutton(f1aa,text="Black Coffee \t",variable=var3,onvalue=1,offvalue=0,font=('Lucida Fax',18,'bold'),command=chkbutton_value).grid(row=2,sticky=W)
Cap=Checkbutton(f1aa,text="Cappucino \t",variable=var4,onvalue=1,offvalue=0,font=('Lucida Fax',18,'bold'),command=chkbutton_value).grid(row=3,sticky=W)
La=Checkbutton(f1aa,text="Latte \t",variable=var5,onvalue=1,offvalue=0,font=('Lucida Fax',18,'bold'),command=chkbutton_value).grid(row=4,sticky=W)
Esp=Checkbutton(f1aa,text="Espresso \t",variable=var6,onvalue=1,offvalue=0,font=('Lucida Fax',18,'bold'),command=chkbutton_value).grid(row=5,sticky=W)
CC=Checkbutton(f1aa,text="Cold Coffee \t",variable=var7,onvalue=1,offvalue=0,font=('Lucida Fax',18,'bold'),command=chkbutton_value).grid(row=6,sticky=W)
Cus=Checkbutton(f1aa,text="Custom Coffee \t",variable=var8,onvalue=1,offvalue=0,font=('Lucida Fax',18,'bold'),command=chkbutton_value).grid(row=7,sticky=W)

#===============Drinks==============

CS=Checkbutton(f1ab,text="Club Sandwich \t",variable=var9,onvalue=1,offvalue=0,font=('Lucida Fax',18,'bold'),command=chkbutton_value).grid(row=0,sticky=W)
Lava=Checkbutton(f1ab,text="Lava Cake \t",variable=var10,onvalue=1,offvalue=0,font=('Lucida Fax',18,'bold'),command=chkbutton_value).grid(row=1,sticky=W)
Dou=Checkbutton(f1ab,text="Doughnut \t",variable=var11,onvalue=1,offvalue=0,font=('Lucida Fax',18,'bold'),command=chkbutton_value).grid(row=2,sticky=W)
MC=Checkbutton(f1ab,text="Mousse Cake \t",variable=var12,onvalue=1,offvalue=0,font=('Lucida Fax',18,'bold'),command=chkbutton_value).grid(row=3,sticky=W)
FF=Checkbutton(f1ab,text="French Fries \t",variable=var13,onvalue=1,offvalue=0,font=('Lucida Fax',18,'bold'),command=chkbutton_value).grid(row=4,sticky=W)
HD=Checkbutton(f1ab,text="Hot Dog \t",variable=var14,onvalue=1,offvalue=0,font=('Lucida Fax',18,'bold'),command=chkbutton_value).grid(row=5,sticky=W)
Ham=Checkbutton(f1ab,text="Hamburger \t",variable=var15,onvalue=1,offvalue=0,font=('Lucida Fax',18,'bold'),command=chkbutton_value).grid(row=6,sticky=W)
ChocB=Checkbutton(f1ab,text="Chocolate Brownie \t",variable=var16,onvalue=1,offvalue=0,font=('Lucida Fax',18,'bold'),command=chkbutton_value).grid(row=7,sticky=W)


#================Others============

txtFC=Entry(f1aa,font=('Lucida Fax',16,'bold'),bd=8,width=6,justify='left',textvariable=E_FC,state=DISABLED)
txtFC.grid(row=0,column=1)
txtWC=Entry(f1aa,font=('Lucida Fax',16,'bold'),bd=8,width=6,justify='left',textvariable=E_WC,state=DISABLED)
txtWC.grid(row=1,column=1)
txtBC=Entry(f1aa,font=('Lucida Fax',16,'bold'),bd=8,width=6,justify='left',textvariable=E_BC,state=DISABLED)
txtBC.grid(row=2,column=1)
txtCap=Entry(f1aa,font=('Lucida Fax',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Cap,state=DISABLED)
txtCap.grid(row=3,column=1)
txtLa=Entry(f1aa,font=('Lucida Fax',16,'bold'),bd=8,width=6,justify='left',textvariable=E_La,state=DISABLED)
txtLa.grid(row=4,column=1)
txtEsp=Entry(f1aa,font=('Lucida Fax',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Esp,state=DISABLED)
txtEsp.grid(row=5,column=1)
txtCC=Entry(f1aa,font=('Lucida Fax',16,'bold'),bd=8,width=6,justify='left',textvariable=E_CC,state=DISABLED)
txtCC.grid(row=6,column=1)
txtCus=Entry(f1aa,font=('Lucida Fax',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Cus,state=DISABLED)
txtCus.grid(row=7,column=1)

#===================Drinks===============

txtCS=Entry(f1ab,font=('Lucida Fax',16,'bold'),bd=8,width=6,justify='left',textvariable=E_CS,state=DISABLED)
txtCS.grid(row=0,column=1)
txtLava=Entry(f1ab,font=('Lucida Fax',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Lava,state=DISABLED)
txtLava.grid(row=1,column=1)
txtDou=Entry(f1ab,font=('Lucida Fax',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Dou,state=DISABLED)
txtDou.grid(row=2,column=1)
txtMC=Entry(f1ab,font=('Lucida Fax',16,'bold'),bd=8,width=6,justify='left',textvariable=E_MC,state=DISABLED)
txtMC.grid(row=3,column=1)
txtFF=Entry(f1ab,font=('Lucida Fax',16,'bold'),bd=8,width=6,justify='left',textvariable=E_FF,state=DISABLED)
txtFF.grid(row=4,column=1)
txtHD=Entry(f1ab,font=('Lucida Fax',16,'bold'),bd=8,width=6,justify='left',textvariable=E_HD,state=DISABLED)
txtHD.grid(row=5,column=1)
txtHam=Entry(f1ab,font=('Lucida Fax',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Ham,state=DISABLED)
txtHam.grid(row=6,column=1)
txtChocB=Entry(f1ab,font=('Lucida Fax',16,'bold'),bd=8,width=6,justify='left',textvariable=E_ChocB,state=DISABLED)
txtChocB.grid(row=7,column=1)

#=================Others============
#==================Info=============

lblr=Label(ft2,font=('Lucida Fax',12,'bold'),text="RECEIPT",bd=2).grid(row=0,column=0,sticky=W)
txtReceipt=Text(ft2,font=('Lucida Fax',11,'bold'),bd=8,width=59)
txtReceipt.grid(row=1,column=0)

#===============Cost================

lblCostD=Label(f2aa,font=('Lucida Fax',12,'bold'),text='Cost of Drinks',bd=8,anchor='w')
lblCostD.grid(row=2,column=0,sticky=W)
txtCostD=Entry(f2aa,font=('Lucida Fax',12,'bold'),bd=8,insertwidth=2,justify='left',textvariable=Drinks)
txtCostD.grid(row=2,column=1)

lblCostC=Label(f2aa,font=('Lucida Fax',12,'bold'),text='Cost of Snacks',bd=8,anchor='w')
lblCostC.grid(row=3,column=0,sticky=W)
txtCostC=Entry(f2aa,font=('Lucida Fax',12,'bold'),bd=8,insertwidth=2,justify='left',textvariable=Snacks)
txtCostC.grid(row=3,column=1)

lblService=Label(f2aa,font=('Lucida Fax',12,'bold'),text='Service Charges',bd=8,anchor='w')
lblService.grid(row=4,column=0,sticky=W)
txtService=Entry(f2aa,font=('Lucida Fax',12,'bold'),bd=8,insertwidth=2,justify='left',textvariable=Service)
txtService.grid(row=4,column=1)

#==============Payment==============

lblPaidTax=Label(f2ab,font=('Lucida Fax',12,'bold'),text='Paid Tax',bd=8)
lblPaidTax.grid(row=2,column=0,sticky=W)
txtPaidTax=Entry(f2ab,font=('Lucida Fax',12,'bold'),bd=8,insertwidth=2,justify='left',textvariable=PaidTax)
txtPaidTax.grid(row=2,column=1)

lblSub=Label(f2ab,font=('Lucida Fax',12,'bold'),text='Sub Total',bd=8)
lblSub.grid(row=3,column=0,sticky=W)
txtSub=Entry(f2ab,font=('Lucida Fax',12,'bold'),bd=8,insertwidth=2,justify='left',textvariable=Sub)
txtSub.grid(row=3,column=1)

lblTotal=Label(f2ab,font=('Lucida Fax',12,'bold'),text='Total',bd=8)
lblTotal.grid(row=4,column=0,sticky=W)
txtTotal=Entry(f2ab,font=('Lucida Fax',12,'bold'),bd=8,insertwidth=2,justify='left',textvariable=Total)
txtTotal.grid(row=4,column=1)

#===================Buttons==========
bTotal=Button(fb2,padx=16,pady=1,bd=4,fg='black',font=("Lucida Fax",10,'bold'),width=5,text='TOTAL',command=costofitem).grid(row=0,column=0)
breceipt=Button(fb2,padx=16,pady=1,bd=4,fg='black',font=("Lucida Fax",10,'bold'),width=5,text='RECEIPT',command=Receipt).grid(row=0,column=1)
breset=Button(fb2,padx=16,pady=1,bd=4,fg='black',font=("Lucida Fax",10,'bold'),width=5,text='RESET',command=Reset).grid(row=0,column=2)
bexit=Button(fb2,padx=16,pady=1,bd=4,fg='black',font=("Lucida Fax",10,'bold'),width=5,text='EXIT', command=qExit).grid(row=0,column=3)

root.mainloop()