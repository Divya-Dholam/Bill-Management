#Importing the required modules
from tkinter import *
from tkinter import messagebox
import os
from PIL import Image,ImageTk
from pymysql import *
import mysql.connector



def login():
    user=username.get()
    code=password.get()

    if user=="Divya" and code=="1234":
        root=Toplevel(screen)
        root.title("Bill Management")
        root.geometry("1280x720+150+80")
        root.configure(bg="lawngreen")
        root.resizable(False,False)
        

         #copy and paste your code here
                                                                                       

        def Reset():
            entry_holybasil.delete(0,END)
            entry_hibiscus.delete(0,END)
            entry_moneyplant.delete(0,END)
            entry_snakeplant.delete(0,END)
            entry_aloevera.delete(0,END)
            entry_jasmine.delete(0,END)
            entry_roseplant.delete(0,END)
            
            print("hello6")


        def Total():

            totalcost=IntVar()

            try:a1=int(holybasil.get())
            except: a1=0

            try:a2=int(hibiscus.get())
            except: a2=0

            try:a3=int(moneyplant.get())
            except: a3=0

            try:a4=int(snakeplant.get())
            except: a4=0

            try:a5=int(aloevera.get())
            except: a5=0

            try:a6=int(jasmine.get())
            except: a6=0

            try:a7=int(roseplant.get())
            except: a7=0
            
        
        

            #define cost of each item per quantity
            c1=110*a1
            c2=150*a2
            c3=70*a3
            c4=100*a4
            c5=120*a5
            c6=25*a6
            c7=50*a7



            
            lbl_total=Label(f2,font=("aria",20,"bold"),text="Total",width=22,fg="aqua",bg="black")
            lbl_total.place(x=0,y=50)
            entry_total=Entry(f2,font=("aria",20,"bold"),textvariable=Total_bill,bd=6,width=14,bg="burlywood")
            entry_total.place(x=80,y=100)
            print("hello3",Total_bill)
            print("hello4",Total_bill.get())

            mydb = connect(host="localhost",user ="root",passwd ="div@1512",database ="plantsdb")

            my_cur = mydb.cursor()
            
            print("hello2")
        
            my_cur.execute("use plantsdb;")
            my_cur.execute("select * from nursery1;")

          

            totalcost=c1+c2+c3+c4+c5+c6+c7
            string_bill="Rs.",str('%.2f'%totalcost)
            Total_bill.set(string_bill)
            print("hello5",totalcost)

            
            my_cur.execute("insert into nursery1 (Total) values ({});".format(totalcost))
    ##        print(Total_bill,"ggjg")
    ##        print(Total_bill.get(),"hfjgj")
            
            mydb.commit()                                            
            mydb.close()
            print("hello7")
            print("Total is",totalcost)
        


                                                                                       
        ##    select * from Nursery;
            for x in my_cur:
                print('{}'.format(totalcost))
           


##            ##        ## SQL
##              
##    
##        mydb = connect(host="localhost",user ="root",passwd ="div@1512",database ="plantsdb")
##    
##        my_cur = mydb.cursor()
##        
##        print("hello2")
##    
##        my_cur.execute("use plantsdb;")
##        my_cur.execute("insert into nursery1 (Total) values ({});".format(totalcost.get()))
####        print(Total_bill,"ggjg")
####        print(Total_bill.get(),"hfjgj")
##        my_cur.execute("select * from nursery1;")
##        mydb.commit()                                            
##        mydb.close()
##        print("hello7")


        Label(root,text="Mini Nursery",bg="violet",fg="darkgreen",font=("calibri",37,'bold'),width="300",height="2").pack()


        #MENU CARD
        f=Frame(root,bg="hotpink",highlightbackground="purple",highlightthickness=4,width=300,height=370)
        f.place(x=10,y=158)

        Label(f,text="Plants",font=("Gabriola",40,"bold"),fg="black",bg="hotpink").place(x=100,y=0)

        Label(f,font=("Lucida",15,'bold'),text="Holy Basil-----Rs.110",fg="black",bg="hotpink").place(x=10,y=80)
        Label(f,font=("Lucida",15,'bold'),text="Hibiscus-------Rs.150",fg="black",bg="hotpink").place(x=10,y=110)
        Label(f,font=("Lucida",15,'bold'),text="Money Plant----Rs.70",fg="black",bg="hotpink").place(x=10,y=140)
        Label(f,font=("Lucida",15,'bold'),text="Snake Plant----Rs.100",fg="black",bg="hotpink").place(x=10,y=170)
        Label(f,font=("Lucida",15,'bold'),text="Aloe vera------Rs.120",fg="black",bg="hotpink").place(x=10,y=200)
        Label(f,font=("Lucida",15,'bold'),text="Jasmine--------Rs.25",fg="black",bg="hotpink").place(x=10,y=230)
        Label(f,font=("Lucida",15,'bold'),text="Roseplant------Rs.50",fg="black",bg="hotpink").place(x=10,y=260)
        
        #BILL
        f2=Frame(root,bg="khaki",highlightbackground="peru",highlightthickness=1,width=370,height=400)
        f2.place(x=880,y=150)

        Bill=Label(f2,text="Bill",font=('calibri',24),bg="Khaki")
        Bill.place(x=160,y=10)
   

        #ENTRY WORK
        f1=Frame(root,bd=5,height=400,width=450,relief=RAISED)
        f1.pack(pady=30)

        holybasil=IntVar()
        hibiscus=IntVar()
        moneyplant=IntVar()
        snakeplant=IntVar()
        aloevera=IntVar()
        jasmine=IntVar()
        roseplant=IntVar()
        Total_bill=IntVar()
        

        
        #Label
        lbl_holybasil=Label(f1,font=("aria",20,'bold'),text="Holy Basil",width=12,fg="crimson",bg="black")
        lbl_hibiscus=Label(f1,font=("aria",20,'bold'),text="Hibiscus",width=12,fg="crimson",bg="black")
        lbl_moneyplant=Label(f1,font=("aria",20,'bold'),text="Money Plant",width=12,fg="crimson",bg="black")
        lbl_snakeplant=Label(f1,font=("aria",20,'bold'),text="Snake Plant",width=12,fg="crimson",bg="black")
        lbl_aloevera=Label(f1,font=("aria",20,'bold'),text="Aloe Vera",width=12,fg="crimson",bg="black")
        lbl_jasmine=Label(f1,font=("aria",20,'bold'),text="Jasmine",width=12,fg="crimson",bg="black")
        lbl_roseplant=Label(f1,font=("aria",20,'bold'),text="Rose Plant",width=12,fg="crimson",bg="black")

        lbl_holybasil.grid(row=1,column=0)
        lbl_hibiscus.grid(row=2,column=0)
        lbl_moneyplant.grid(row=3,column=0)
        lbl_snakeplant.grid(row=4,column=0)
        lbl_aloevera.grid(row=5,column=0)
        lbl_jasmine.grid(row=6,column=0)
        lbl_roseplant.grid(row=7,column=0)

        #Entry
        entry_holybasil=Entry(f1,font=("aria",20,'bold'),textvariable=holybasil,bd=6,width=8,bg="lightcoral")
        entry_hibiscus=Entry(f1,font=("aria",20,'bold'),textvariable=hibiscus,bd=6,width=8,bg="lightcoral")
        entry_moneyplant=Entry(f1,font=("aria",20,'bold'),textvariable=moneyplant,bd=6,width=8,bg="lightcoral")
        entry_snakeplant=Entry(f1,font=("aria",20,'bold'),textvariable=snakeplant,bd=6,width=8,bg="lightcoral")
        entry_aloevera=Entry(f1,font=("aria",20,'bold'),textvariable=aloevera,bd=6,width=8,bg="lightcoral")
        entry_jasmine=Entry(f1,font=("aria",20,'bold'),textvariable=jasmine,bd=6,width=8,bg="lightcoral")
        entry_roseplant=Entry(f1,font=("aria",20,'bold'),textvariable=roseplant,bd=6,width=8,bg="lightcoral")
        

        entry_holybasil.grid(row=1,column=1)
        entry_hibiscus.grid(row=2,column=1)
        entry_moneyplant.grid(row=3,column=1)
        entry_snakeplant.grid(row=4,column=1)
        entry_aloevera.grid(row=5,column=1)
        entry_jasmine.grid(row=6,column=1)
        entry_roseplant.grid(row=7,column=1)

        print("hello1")


                #buttons       
        btn_reset=Button(f1,bd=5,fg="black",bg="aquamarine",font=("ariel",16,"bold"),width=10,text="Reset",command=Reset)
        btn_reset.grid(row=8,column=0)
        print("hello8")

        btn_total=Button(f1,bd=5,fg="black",bg="aquamarine",font=("ariel",16,"bold"),width=10,text="Total",command=Total)
        btn_total.grid(row=8,column=1)
        print("hello9")


                            ## SQL
              






            


        

  
         #end of code
        
    elif user=="" and code=="":
        messagebox.showerror("Invalid","Please enter username and password")
    elif user=="":
        messagebox.showerror("Invalid","Please enter username")
    elif code=="":
        messagebox.showerror("Invalid","Please enter password")
    elif user=="Divya" and code!="1234":
        messagebox.showerror("Invalid","Invalid password")
    elif user!="Divya" and code=="1234":
        messagebox.showerror("Invalid","Invalid username")
    elif user!="Divya" and code!="1234":
        messagebox.showerror("Invalid","Invalid username and password")

        

def main_screen():

    global screen
    global username
    global password
    
    screen=Tk()
    screen.geometry("1280x720+150+80")
    screen.configure(bg="mediumorchid")

    image_icon=PhotoImage(file="login.png")
    screen.iconphoto(False,image_icon)
    screen.title("Login System")

    lblTitle=Label(text="Login System",font=("arial",50,"bold"),fg="black",bg="mediumorchid")
    lblTitle.pack(pady=50)

    bordercolor=Frame(screen,bg="mediumorchid",width=800,height=400)
    bordercolor.pack()

    mainframe=Frame(bordercolor,bg="mediumorchid",width=800,height=400)
    mainframe.pack(padx=20,pady=20)

    Label(mainframe,text="Username",font=("arial",30,"bold"),bg="mediumorchid").place(x=100,y=50)
    Label(mainframe,text="Password",font=("arial",30,"bold"),bg="mediumorchid").place(x=100,y=150)

    username=StringVar()
    password=StringVar()

    entry_username=Entry(mainframe,textvariable=username,width=12,bd=2,font=("arial",30))
    entry_username.place(x=400,y=50)
    entry_password=Entry(mainframe,textvariable=password,width=12,bd=2,font=("arial",30),show="*")
    entry_password.place(x=400,y=150)
    
    def reset():
        entry_username.delete(0,END)
        entry_password.delete(0,END)
    

    Button(mainframe,text="Login",height="2",width=23,bg="lavender",fg="black",bd=0,command=login).place(x=100,y=250)
    Button(mainframe,text="Reset",height="2",width=23,bg="lavender",fg="black",bd=0,command=reset).place(x=300,y=250)
    Button(mainframe,text="Exit",height="2",width=23,bg="lavender",fg="black",bd=0,command=screen.destroy).place(x=500,y=250)

        
 
main_screen()
screen.mainloop()


    
    
    




