#!/usr/bin/env python
# coding: utf-8

# In[90]:


from tkinter import * 
from tkinter import messagebox
import psycopg2
from tkinter import ttk
from tkinter.ttk import Style,Treeview


# In[91]:


try:
    # conn = psycopg2.connect("dbname='pyapp' user='kali' password='kali'")
    
    conn = psycopg2.connect(
            dbname='pyapp',
            host='localhost',
            user='kali',
            password='kali'
    )
    print("database is connected ")
    cur = conn.cursor()
    
    conn.close()
        
except:
    print("Error: database couldn't connect!") 


# In[162]:


win = Tk()
win.call("wm","attributes",".","-zoomed","True")
win.attributes('-zoomed',True)
win.wm_attributes("-zoomed",True)
win.configure(bg="powder blue")
# win.resizable(width=False,height=False)

title=Label(win,text="Bank Account Automation",font=("Arial",30,"bold",'underline'),bg="powder blue")
title.pack()
#------------------------------------------------------------------------------------------------------------------------------
def home_screen():
    frm = Frame(win)
    frm.configure(bg="green")
    frm.place(x=.0,y=70,relwidth=1,relheight=1)
    
    def fp():
        frm.destroy()
        forget_pass_scr()
        
    def wlcm():
        AcNo = e_acn.get()
        AcPss = e_pass.get()
        if(len(AcNo) == 0 or len(AcPss) ==0):
            messagebox.showwarning("Validation","Fill the details to login")
            return 
        elif(not AcNo.isdigit()):
            messagebox.showwarning("Validation","Account Number must be in digits! ")
            return 
        
        else:
            conn = psycopg2.connect(
                dbname='pyapp',
                host='localhost',
                user='kali',
                password='kali')

            cur = conn.cursor()
            cur.execute("SELECT * FROM accounts where acc_no=%s and password=%s",(AcNo,AcPss))
            global row
            row = cur.fetchone()
            cur.close()
            conn.close()
            if (row ==None):
                messagebox.showwarning("Validation","Invalid Acc/Pass ")
            else:
                # print(row)
                frm.destroy()
                wlcm_scr()
        
    def new_acc():
        frm.destroy()
        new_acn_scr()
        
    
    lab_ace=Label(frm,text="Account No : " ,font=('Arial',20,'bold'), bg='green')
    lab_ace.place(relx=.3,rely=.2)
    
    e_acn = Entry(frm,font=('Arial',20,'bold'),bd=1)
    e_acn.place(relx=.4,rely=.2)
    e_acn.focus()
        
    lab_pass=Label(frm,text="Password : " ,font=('Arial',20,'bold'), bg='green')
    lab_pass.place(relx=.3,rely=.26)
    
    e_pass = Entry(frm,font=('Arial',20,'bold'),bd=1,show="*")
    e_pass.place(relx=.4,rely=.26)
    
    btn_login=Button(frm,text="Login",font=('Arial',20,'bold'),command=wlcm)
    btn_login.place(relx=.5,rely=.33)
    
    btn_sinup=Button(frm,text="SinUP",font=('Arial',20,'bold'),command=new_acc)
    btn_sinup.place(relx=.4,rely=.33)
    
    btn_fpass=Button(frm,text="Forget_Password",font=('Arial',20,'bold'),command=fp)
    btn_fpass.place(relx=.001,rely=.88)
    
    
#--------------------------------------------------CREAT NEW ACCOUNT SCREEN ----------------------------------------------------------------------------




def new_acn_scr():
    frm = Frame(win)
    frm.configure(bg="blue")
    frm.place(x=.0,y=70,relwidth=1,relheight=1)
    
    def home_scr():
        frm.destroy()
        home_screen()
    def new_usr():
        name =e_acn.get()
        mob =e_mob.get()
        mail =e_mail.get()
        paswd = e_pass.get()
        
        if(len(name)==0 or len(mob)==0 or len(mail)==0 or len(paswd)==0):
            messagebox.showwarning("Validation","you must have to fill all the details!\nin order to acreate your account")
            return
        if(len(mob)>13):
            messagebox.showwarning("Validation","Invalid mobile number")
            return           
        elif(not mob.isdigit()):
            messagebox.showwarning("Validation","Enter Valid Mobile Number!")
            return
        
        # connecting to database 
        
        conn = psycopg2.connect(
            dbname='pyapp',
            host='localhost',
            user='kali',
            password='kali')
        
        cur = conn.cursor()


        cur.execute(f"INSERT INTO accounts(name,mail,mob_no,password,balance) VALUES ('{name}','{mail}','{mob}','{paswd}',{1000})")
        cur.execute("select max(acc_no) from accounts")
        tup=cur.fetchone()
        messagebox.showwarning("Success",f"you Account has already created\nwith ACN:{tup[0]}")
        # cur.execute(f"INSERT INTO recoades(acc_no,balance) VALUES ({tup[0]},1000)")

        conn.commit()
        cur.close()
        conn.close()

        e_acn.delete(0,'end')
        e_mob.delete(0,'end')
        e_mail.delete(0,'end')
        e_pass.delete(0,'end')
        e_acn.focus()
    
    
    btn_back=Button(frm,text=" Home ",font=('Arial',20,'bold'),command=home_scr)
    btn_back.place(relx=0,rely=0)
    
    ac_name=Label(frm,text="Enter your Name : " ,font=('Arial',20,'bold'), bg='blue')
    ac_name.place(relx=.25,rely=.2)    
    e_acn = Entry(frm,font=('Arial',20,'bold'),bd=1)
    e_acn.place(relx=.4,rely=.2)
    e_acn.focus()
    
    lab_pass=Label(frm,text="Password : " ,font=('Arial',20,'bold'), bg='blue')
    lab_pass.place(relx=.28,rely=.26)
    e_pass = Entry(frm,font=('Arial',20,'bold'),bd=1,show="*")
    e_pass.place(relx=.4,rely=.26)
        
    lab_mob=Label(frm,text="Mobile no : " ,font=('Arial',20,'bold'), bg='blue')
    lab_mob.place(relx=.28,rely=.32)
    e_mob = Entry(frm,font=('Arial',20,'bold'),bd=1)
    e_mob.place(relx=.4,rely=.32)
 
    lab_Mail=Label(frm,text="Mail id : " ,font=('Arial',20,'bold'), bg='blue')
    lab_Mail.place(relx=.28,rely=.38)
    e_mail = Entry(frm,font=('Arial',20,'bold'),bd=1)
    e_mail.place(relx=.4,rely=.38)
    
    btn_login=Button(frm,text="Create Account",font=('Arial',20,'bold'),command=new_usr)
    btn_login.place(relx=.5,rely=.44)
    
#----------------------------------------------------- welcome window -------------------------------------------------------------------------


def wlcm_scr():
    frm = Frame(win)
    frm.configure(bg="yellow")
    frm.place(x=.0,y=70,relwidth=1,relheight=1)
    lab_ace=Label(frm,text=f"Hey  {row[1]} \nWelcome to the F Bank ;) " ,font=('Arial',30,'bold'), bg='yellow')
    lab_ace.place(relx=.36,rely=.04)
    
    def home_scr():
        frm.destroy()
        home_screen()
    
    btn_fpass=Button(frm,text="Logout",font=('Arial',20,'bold'),command=home_scr)
    btn_fpass.place(relx=.9,rely=0)
    
    def withraw():
        ifrm = Frame(frm)
        ifrm.configure(bg="green")
        ifrm.place(relx=.18,rely=0.17,relwidth=.81,relheight=.75)
        
        def txn_wit():
            txn_amt = wit_amt.get()
            
            if(txn_amt == '' or (float(wit_amt.get() ==0)) ):
                messagebox.showwarning("Error","You must enter valid Amount")
                return
            amt =float(wit_amt.get())
            print(type(amt),amt)
            
            conn = psycopg2.connect(
                dbname='pyapp',
                host='localhost',
                user='kali',
                password='kali')

            cur = conn.cursor()
            cur.execute(f"select balance from accounts where acc_no={row[0]}")
            bal = cur.fetchone()
            bal = list(bal)
            print(bal,type(bal))
            bal = bal[0]
            print(bal,type(bal))
            flamt=bal-amt
            print(flamt)

            
            if(bal<amt):
                messagebox.showwarning("Error",f"You don't have {amt} lol :) ")
                return
            
            cur.execute(f"select balance from accounts where acc_no={row[0]}")
            bal = cur.fetchone()

            cur.execute("INSERT INTO txn VALUES (%s,%s,%s) ",(row[0],amt,"Db."))
            cur.execute(f"update accounts set balance={flamt} where acc_no={row[0]} ")
            conn.commit()
            conn.close()
            messagebox.showinfo("Success",f"{amt} Amount Withraw ") 
            wit_amt.delete(0,'end')
            return
            
            
        lab_txt=Label(ifrm,text="This is Withraw",font=('Arial',20,'bold','underline'),fg="red",bg="green")
        lab_txt.place(relx=.1,rely=.02)
         
        
        lab_wit=Label(frm,text="Withraw Amount:  " ,font=('Arial',20,'bold'), bg='green',fg="red")
        lab_wit.place(relx=.28,rely=.26)
        wit_amt = Entry(frm,font=('Arial',20,'bold'),bd=1)
        wit_amt.place(relx=.42,rely=.26) 
        wit_amt.focus()
         
        a_wit=Button(frm,text="Submit",font=('Arial',20,'bold'),command=txn_wit)
        a_wit.place(relx=.6,rely=.32)

    def deposit():
        ifrm = Frame(frm)
        ifrm.configure(bg="green") 
        ifrm.place(relx=.18,rely=0.17,relwidth=.81,relheight=.75) 
         
        def txn_dep():
            amt = dep_amt.get() 
            if(amt=="" or (float(dep_amt.get() ==0))): 
                messagebox.showwarning("Error","You must enter valid Amount") 
                return
            amt = float(dep_amt.get()) 
            print(type(amt),amt)
            
            conn = psycopg2.connect(
                dbname='pyapp', 
                host='localhost',
                user='kali',
                password='kali')

            cur = conn.cursor()
            cur.execute(f"select balance from accounts where acc_no={row[0]}")
            bal = cur.fetchone()
            bal = list(bal)
            bal = bal[0]
               
            cur.execute("INSERT INTO txn VALUES (%s,%s,%s) ",(row[0],amt,"Cr"))
            cur.execute(f"update accounts set balance={bal+amt} where acc_no={row[0]} ")
            conn.commit()
            conn.close()
            messagebox.showinfo("Success",f"{amt} Amount deposited ")
            dep_amt.delete(0,"end")
            return
            
            
        lab_txt=Label(ifrm,text="This is Deposit",font=('Arial',20,'bold','underline'),fg="red",bg="green")
        lab_txt.place(relx=.1,rely=.02)
        
        
        lab_dep=Label(frm,text="Deposit Amount:  " ,font=('Arial',20,'bold'), bg='green',fg="red")
        lab_dep.place(relx=.28,rely=.26)
        dep_amt = Entry(frm,font=('Arial',20,'bold'),bd=1)
        dep_amt.place(relx=.42,rely=.26)
        dep_amt.focus()
        
        a_dep=Button(frm,text="Submit",font=('Arial',20,'bold'),command=txn_dep)
        a_dep.place(relx=.6,rely=.32)
        
    def trnsfr():
        ifrm = Frame(frm)
        ifrm.configure(bg="green")
        ifrm.place(relx=.18,rely=0.17,relwidth=.81,relheight=.75)

        lab_txt=Label(ifrm,text="This is Transfer",font=('Arial',20,'bold','underline'),fg="red",bg="green")
        lab_txt.place(relx=.1,rely=.02)
        
        def Amt_tsf():
            txn_amt = a_tsf.get()
            to = a_tacn.get()
            
            conn = psycopg2.connect(
                dbname='pyapp',
                host='localhost',
                user='kali',
                password='kali')

            cur = conn.cursor()
            cur.execute(f"select balance from accounts where acc_no={to}")
            tup = cur.fetchone() # tup of reciving ac balance
                
#             conn.commit()
#             conn.close()
            
            if(tup==None):
                messagebox.showerror("Error","T Acn doesn't exiest! ")
                return
            else:
                if(a_tsf == '' or (float(a_tsf.get() ==0)) ):
                    messagebox.showwarning("Error","You must enter valid Amount")
                    return
                amt =float(a_tsf.get()) # amount to transfer

                conn = psycopg2.connect(
                    dbname='pyapp',
                    host='localhost',
                    user='kali',
                    password='kali')
                cur = conn.cursor()
                
                
                cur.execute(f"select balance from accounts where acc_no={row[0]}")
                bal = cur.fetchone()
                snd = list(bal)
                snd = snd[0]  # sender's acount balance 
                
                if(snd<amt):
                    messagebox.showwarning("Error",f"You don't have {amt} lol :) ")
                    return

                cur.execute(f"select balance from accounts where acc_no={to}")
                rcv = cur.fetchone()
                rcv = list(tup)
                rcv = rcv[0]
                
                print(f"\n\nsender bal : {snd} -  {type(snd)}")
                print(f" recever bal : {rcv} - {type(rcv)}")
                print(f" amount to transfer : {amt} - {type(amt)}\n\n")
                
                sndbal = snd-amt
                rcvbal = rcv+amt
                
                
                cur.execute("INSERT INTO txn VALUES (%s,%s,%s) ",(row[0],amt,"Db."))
                cur.execute("INSERT INTO txn VALUES (%s,%s,%s) ",(to,amt,"Cr."))

                cur.execute(f"update accounts set balance={sndbal} where acc_no={row[0]} ")
                cur.execute(f"update accounts set balance={rcvbal} where acc_no={to} ")

                conn.commit()
                conn.close()
                messagebox.showinfo("Success",f"{amt} Amount Transfered Successfully :)  ") 
                a_tsf.delete(0,'end')
                return
        
        
        lab_tacn=Label(frm,text="To Acn:  " ,font=('Arial',20,'bold'), bg='green',fg="red")
        lab_tacn.place(relx=.28,rely=.26)
        a_tacn = Entry(frm,font=('Arial',20,'bold'),bd=1)
        a_tacn.place(relx=.42,rely=.26)
        a_tacn.focus()

        lab_tsf=Label(frm,text="Transfer Amount:  " ,font=('Arial',20,'bold'), bg='green',fg="red")
        lab_tsf.place(relx=.28,rely=.31)
        a_tsf = Entry(frm,font=('Arial',20,'bold'),bd=1)
        a_tsf.place(relx=.42,rely=.31)
        
        b_tsf=Button(frm,text="Submit",font=('Arial',20,'bold'),command=Amt_tsf)
        b_tsf.place(relx=.6,rely=.32)
    
    def profile():
        ifrm = Frame(frm)
        ifrm.configure(bg="green")
        ifrm.place(relx=.18,rely=0.17,relwidth=.71,relheight=.7)

        lab_txt=Label(ifrm,text="This is Profile",font=('Arial',20,'bold','underline'),fg="red",bg="green")
        lab_txt.place(relx=.1,rely=.02)
            
        # we have user information in row varable 
        
        conn = psycopg2.connect(
                dbname='pyapp', 
                host='localhost',
                user='kali',
                password='kali')

        cur = conn.cursor()
        cur.execute(f"select balance from accounts where acc_no={row[0]}")
        bal = cur.fetchone()
        conn.commit()
        conn.close()
        bal = list(bal)
        bal = bal[0]

        
        tv=Treeview(ifrm)
        tv.place(x=100,y=100,height=300,width=1000)
        
        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Arial',15,'bold'),foreground='brown')


        tv['columns']=('ACN','Name','Email','Mob','Bal','Creation_Date')
        
        #defining columns here 
        
        tv.column('ACN',width=50,anchor='c')
        tv.column('Name',width=120,anchor='c')
        tv.column('Email',width=150,anchor='c')
        tv.column('Mob',width=100,anchor='c')
        tv.column('Bal',width=120,anchor='c')
        tv.column('Creation_Date',width=125,anchor='c')
      
    #definging headings here 
    
        tv.heading('ACN',text='ACN')
        tv.heading('Name',text='Name')
        tv.heading('Email',text='Email')
        tv.heading('Mob',text='Mob')
        tv.heading('Bal',text='Bal')
        tv.heading('Creation_Date',text='Creation_Date')
        
        tv['show']='headings'
        
        tv.insert("","end",values=(row[0],row[1],row[2],row[3],bal,str(row[6])[:18]))
        
    def Logs():
        ifrm = Frame(frm)
        ifrm.configure(bg="green")
        ifrm.place(relx=.18,rely=0.17,relwidth=.71,relheight=.7)

        lab_txt=Label(ifrm,text="Balance Information",font=('Arial',20,'bold','underline'),fg="red",bg="green")
        lab_txt.place(relx=.1,rely=.02)
            
        # we have user information in row varable 
        
        tv=Treeview(ifrm)
        tv.place(x=100,y=100,height=300,width=1000)
        
        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Arial',15,'bold'),foreground='brown')


        
        
        
        
        tv['columns']=('ACN','Amt','Type','DateTime')
        
        #defining columns here 
        
        tv.column('ACN',width=50,anchor='c')
        tv.column('Amt',width=10,anchor='c')
        tv.column('Type',width=150,anchor='c')
        tv.column('DateTime',width=100,anchor='c')
 
    #definging headings here 
    
        tv.heading('ACN',text='ACN')
        tv.heading('Amt',text='Amt')
        tv.heading('Type',text='Type')
        tv.heading('DateTime',text='DateTime')
      
        tv['show']='headings'
        
        
        conn = psycopg2.connect(
            dbname='pyapp',
            host='localhost',
            user='kali',
            password='kali')

        cur = conn.cursor()
        cur.execute(f"SELECT * FROM txn where acc_no={row[0]}")
        tup = cur.fetchall()
        logs = []
        for i in tup:
            time = str(i[3])
            logs.append(f"{i[0]} {i[1]} {i[2]} {time[:18]} ")
        for log in logs:
            tv.insert("","end",values=(log))

        cur.close()
        conn.close()

        

        
    def update():
        ifrm = Frame(frm)
        ifrm.configure(bg="green")
        ifrm.place(relx=.18,rely=0.17,relwidth=.71,relheight=.7)
        
        lab_txt=Label(ifrm,text="Update Profile",font=('Arial',20,'bold','underline'),fg="red",bg="green")
        lab_txt.place(relx=.7,rely=.02)
                
        def Apply():
            name=e_acn.get()
            mail=e_mail.get()
            mob=e_mob.get()
            pwd=e_pass.get()
            chpwd=e_chpass.get()
            
            conn = psycopg2.connect(
            dbname='pyapp',
            host='localhost',
            user='kali',
            password='kali')
            cur = conn.cursor()
            def fp():
                frm.destroy()
                forget_pass_scr()
                
            if(pwd != row[0]):
                messagebox.showwarning("Error","your password is Wrong!")
                btn_fpass=Button(frm,text="Forget_Password",font=('Arial',20,'bold'),command=fp)
                btn_fpass.place(relx=.001,rely=.88)
                return
            
            if(chpwd != '' and pwd ==row[4]):
                cur.execute("update accounts set password=%s where acc_no=%s",(chpwd,row[0]))
                messagebox.showinfo("Success","your Password has Successfully Changed ")
                return
                
            if(name != '' and pwd == row[4]):
                cur.execute("update accounts set name=%s where acc_no=%s",(name,row[0]))
                messagebox.showinfo("Success","your Name has Successfully Changed ")
                return
                
            if(mail != '' and pwd ==row[4]):
                cur.execute("update accounts set mail=%s where acc_no=%s",(mail,row[0]))
                messagebox.showinfo("Success","your Mail Id has Successfully Changed ")
                return
                
            if(mob != '' and pwd ==row[4]):
                cur.execute("update accounts set mob_no=%s where acc_no=%s",(mob,row[0]))
                messagebox.showinfo("Success","your Mobil Number has Successfully Changed ")
                return

            else:
                messagebox.showwarning("Error","Enter your password to change your details")

            
            
            
        
        ac_name=Label(frm,text="Enter your Name : " ,font=('Arial',20,'bold'), bg='green',fg='blue')
        ac_name.place(relx=.25,rely=.2)    
        e_acn = Entry(frm,font=('Arial',20,'bold'),bd=1)
        e_acn.place(relx=.4,rely=.2)
        e_acn.focus()
        e_acn.insert(0,row[1])

        lab_mob=Label(frm,text="Mobile no : " ,font=('Arial',20,'bold'), bg='green',fg='blue')
        lab_mob.place(relx=.28,rely=.32)
        e_mob = Entry(frm,font=('Arial',20,'bold'),bd=1)
        e_mob.place(relx=.4,rely=.32)
        e_mob.insert(0,row[3])


        lab_Mail=Label(frm,text="Mail id : " ,font=('Arial',20,'bold'), bg='green',fg='blue')
        lab_Mail.place(relx=.28,rely=.26)
        e_mail = Entry(frm,font=('Arial',20,'bold'),bd=1)
        e_mail.place(relx=.4,rely=.26)
        e_mail.insert(0,row[2])
        
        lab_chpass=Label(frm,text="ChPasswd : " ,font=('Arial',20,'bold'), bg='green',fg='blue')
        lab_chpass.place(relx=.28,rely=.38)
        e_chpass = Entry(frm,font=('Arial',20,'bold'),bd=1,show="*")
        e_chpass.place(relx=.4,rely=.38)        

        
        lab_pass=Label(frm,text="Password : " ,font=('Arial',20,'bold'), bg='green',fg='blue')
        lab_pass.place(relx=.28,rely=.44)
        e_pass = Entry(frm,font=('Arial',20,'bold'),bd=1,show="*")
        e_pass.place(relx=.4,rely=.44)

        
        btn_login=Button(frm,text="Apply",font=('Arial',20,'bold'),command=Apply)
        btn_login.place(relx=.5,rely=.5)
        
        
        
        
        
    
    #welcome
    btn_pfp=Button(frm,text="profile",font=('Arial',20,'bold'),command=profile)
    btn_pfp.place(relx=.9,rely=.05)
    
    btn_chk=Button(frm,text="TF History",font=('Arial',20,'bold'),command=Logs)
    btn_chk.place(relx=.05,rely=.15)
    
    btn_wed=Button(frm,text="widrow",font=('Arial',20,'bold'),command=withraw)
    btn_wed.place(relx=.05,rely=.05)
    
    btn_dep=Button(frm,text="deposit",font=('Arial',20,'bold'),command=deposit)
    btn_dep.place(relx=.05,rely=.1)
    
    btn_trnsf=Button(frm,text="Transfer",font=('Arial',20,'bold'),command=trnsfr)
    btn_trnsf.place(relx=.05,rely=.2)
    
    btn_update=Button(frm,text="Update",font=('Arial',20,'bold'),command=update)
    btn_update.place(relx=.05,rely=.25)
    
#--------------------------------------------FORGET PASSWORD SCREEN ----------------------------------------------------------------------------------
    
    
def forget_pass_scr():
    frm = Frame(win)
    frm.configure(bg="red")
    frm.place(x=.0,y=70,relwidth=1,relheight=1)
    
    def home_scr():
        frm.destroy()
        home_screen()
    
    def get_pass(): 
        Acn=e_acn.get()
        Mob=e_mob.get()
        Mail=e_mail.get()
        
        if(len(Acn)==0 or len(Mob)==0 or len(Mail)==0):
            messagebox.showwarning("Validation","you must have to fill all the details!\nin order to get your account password")
            return
        
        conn = psycopg2.connect(
            dbname='pyapp',
            host='localhost',
            user='kali',
            password='kali')
        
        cur = conn.cursor()
        cur.execute("SELECT * FROM accounts where acc_no=%s and mail=%s and mob_no=%s ",(Acn,Mail,Mob))
        pwd = cur.fetchone()
        cur.close()
        conn.close()
        if (pwd == None):
            messagebox.showwarning("Validation","Invalid Information !! ")
        else:
            messagebox.showinfo("hmm keeping a strong password is good but don't forget it ",f"you password: {pwd[4]}")
            print(pwd[4])        
            frm.destroy()
            get_pass_scr()
    
    btn_back=Button(frm,text=" Home ",font=('Arial',20,'bold'),command=home_scr)
    btn_back.place(relx=0,rely=0)
    
    lab_ace=Label(frm,text="Account No : " ,font=('Arial',20,'bold'), bg='red')
    lab_ace.place(relx=.3,rely=.2)    
    e_acn = Entry(frm,font=('Arial',20,'bold'),bd=1)
    e_acn.place(relx=.4,rely=.2)
    e_acn.focus()
        
        
    lab_mob=Label(frm,text="Mobile no : " ,font=('Arial',20,'bold'), bg='red')
    lab_mob.place(relx=.3,rely=.26)
    e_mob = Entry(frm,font=('Arial',20,'bold'),bd=1)
    e_mob.place(relx=.4,rely=.26)
 
    lab_Mail=Label(frm,text="Mail id : " ,font=('Arial',20,'bold'), bg='red')
    lab_Mail.place(relx=.3,rely=.32)
    e_mail = Entry(frm,font=('Arial',20,'bold'),bd=1)
    e_mail.place(relx=.4,rely=.32)
    
    btn_login=Button(frm,text="get password",font=('Arial',20,'bold'),command=get_pass)
    btn_login.place(relx=.5,rely=.38)
    
    
#------------------------------------------------passWORD RECOVERY SCREEN ------------------------------------------------------------------------------
    
def get_pass_scr():
    frm = Frame(win)
    frm.configure(bg="blue")
    frm.place(x=.0,y=70,relwidth=1,relheight=1)
    
    def home_scr():
        frm.destroy()
        home_screen()
    
    lab_ace=Label(frm,text="Welcome to F Bank \n\n\t\tyou will get your password on you main or on your mobile ;) " ,font=('Arial',35,'bold'), bg='blue')
    lab_ace.place(relx=0,rely=.2)
    
    btn_back=Button(frm,text="Home",font=('Arial',20,'bold'),command=home_scr)
    btn_back.place(relx=0,rely=0)
    
home_screen()


win.mainloop()


# In[157]:



#testing

# conn = psycopg2.connect(
#     dbname='pyapp',
#     host='localhost',
#     user='kali',
#     password='kali')

# cur = conn.cursor()
# cur.execute(f"SELECT * FROM txn where acc_no={2}")
# tup = cur.fetchall()
# log = []
# for i in tup:
#     time = str(i[3])
#     log.append(f"{i[0]} {i[1]} {i[2]} {time[:18]} ")
# print(log)
# cur.close()
# conn.close()


# # In[ ]:




