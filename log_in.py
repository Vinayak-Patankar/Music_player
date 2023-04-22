from captcha.image import ImageCaptcha
import random
from tkinter import*
from tkinter import ttk,messagebox
from PIL import*
from PIL import Image,ImageTk
from tkinter import filedialog
from pygame import mixer
import os
from pymysql import*
root=Tk()
root.title("music_player")
root.geometry('700x700')
root.config(bg='#0D7F0D')
root.wm_iconbitmap('./logo.ico')
img=PhotoImage(file='logo_in_login.png')
l1=Label(root,text='image',image=img,bd=0)
l1.place(x=480,y=10)
l=Label(root,text='Music player',fg='black',bg='#0D7F0D',font=('cooper black',30,'italic'))
l.place(x=180,y=30)
def login():
    d=connect(host='localhost',user='root',password='root',database='log_')
    cur=d.cursor()
    a=e.get()
    b=e1.get()
    cur.execute("select username,password from log_in;")
    data=dict(cur.fetchall())
    print(data)
    if a in data and data[a]==b:
        print('Login successful!')
        from subprocess import call
        def open_py_file():
            call(['python',',m.py'])
        open_py_file()

    elif a==''or b=='': 
            messagebox.showwarning('space','Fill the whitespace')
    else:
        messagebox.showwarning('warning','Passwords or username is wrong')
def register():
    def signup():
        d=connect(host='localhost',user='root',password='root',database='log_')
        cur=d.cursor()
        a=ef.get()
        b=ef1.get()
        c=ef2.get()
        x=r.get()
        if b==c and a!='' and entry.get() == code_label['text']:
            cur.execute("insert into log_in values('{}','{}','{}');".format(a,b,x))
            messagebox.showinfo('Signup','You are successfully signed up')
            t.destroy()
        else:
            messagebox.showwarning('Captcha','Fill the correct Captcha')
        d.commit()
        d.close()
        if a==''or b==''or c=='': 
            messagebox.showwarning('space','Fill the whitespace')
        elif b!=c:
            messagebox.showwarning('warning','Passwords are not matching')

    t=Toplevel(root)
    t.title("music_player")
    t.geometry('700x700')
    t.config(bg='#0D7F0D')
    t.wm_iconbitmap('./logo.ico')

    #frame
    f=Frame(t,bd=2,bg='white',relief=SUNKEN)
    f.place(x=50,y=230,width=600,height=350)

    #captcha
    def generate_captcha():
        code = str(random.randint(1000, 9999))
        return code

    code = generate_captcha()
    Label(f, text="Captcha",fg='white',bg='#0D7F0D', font=("Helvetica", 17)).place(x=70,y=220)
    code_label = Label(f, text=code, font=("Helvetica", 17))
    code_label.place(x=170,y=220)

    entry = Entry(f, font=("Helvetica", 17))
    entry.place(x=250,y=220)


    
    #txt
    sign_up=Label(t,text='Sign-Up',fg='white',bg='#0D7F0D',font=('cooper black',30,'italic'))
    sign_up.place(x=250,y=100)
    r=Label(f,text='Name                     :',fg='black',bg='white',font=('arial',17))
    r.place(x=20,y=20)
    r1=Label(f,text='Password               :',fg='black',bg='white',font=('arial',17))
    r1.place(x=20,y=120)
    r2=Label(f,text='Confirm Password :',fg='black',bg='white',font=('arial',17))
    r2.place(x=20,y=170)
    r3=Label(f,text='Gender                   :',fg='black',bg='white',font=('arial',17))
    r3.place(x=20,y=70)
    
    #entry box
    ef=Entry(f,bg="white",fg='#0D7F0D',font=('arial',17))
    ef.place(x=250,y=20)
    ef1=Entry(f,bg="white",fg='#0D7F0D',font=('arial',17))
    ef1.place(x=250,y=120)
    ef2=Entry(f,bg="white",fg='#0D7F0D',font=('arial',17))
    ef2.place(x=250,y=170)
    
    #button
    r=StringVar()
    rb=Radiobutton(f,text="Male",variable=r,bg='white',fg='black',relief=SUNKEN,value="Male",font='aharoni')
    rb.place(x=250,y=70)
    rb1=Radiobutton(f,text="Female",variable=r,bg='white',fg='black',relief=SUNKEN,font='aharoni',value="Female")
    rb1.place(x=330,y=70)
    b=Button(f,text="Signup",bg="blue",fg="red",font=("algerian",15),command=signup)
    b.place(x=230,y=300)

    
#frame
frame=Frame(root,bd=2,bg='white',relief=SUNKEN)
frame.place(x=100,y=230,width=500,height=300)
#text
l3=Label(root,text='Sign-in',fg='white',bg='#0D7F0D',font=('cooper black',30,'italic'))
l3.place(x=250,y=150)
l4=Label(root,text='Sign in to Music player to acess Music',fg='white',bg='#0D7F0D',font=('arial',15))
l4.place(x=180,y=200)
l2=Label(frame,text='Username :',fg='black',bg='white',font=('arial',17))
l2.place(x=20,y=50)
l5=Label(frame,text='Password  :',fg='black',bg='white',font=('arial',17))
l5.place(x=20,y=100)
l6=Label(frame,text="If u don't have account register here :- ",fg='black',bg='white',font=('arial',10))
l6.place(x=10,y=260)
#entry box
e=Entry(frame,bg="white",fg='#0D7F0D',font=('arial',17))
e.place(x=150,y=50)
e1=Entry(frame,bg="white",fg='#0D7F0D',font=('arial',17))
e1.place(x=150,y=100)
#button
but=Button(frame,text="login",bg="blue",fg="red",font=("algerian",15),command=login)
but.place(x=200,y=150)
but1=Button(frame,text="Register",bg="blue",fg="red",font=("algerian",10),command=register)
but1.place(x=240,y=260)



root.mainloop()

