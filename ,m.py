from tkinter import*
from tkinter import Tk
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import filedialog
from pygame import mixer
import os
root=Tk()
root.title("mplay")
root.geometry('1920x1080')
root.wm_iconbitmap("D:\python\music player\logo.ico")
root.config(bg='#0D7F0D')
mixer.init()
       
def jpop():

    jpop.t = Toplevel(root)
    jpop.t.title("Jpop")
    jpop.t.geometry('1920x1080')
    jpop.t.config(bg='#0D7F0D')
    jpop.t.wm_iconbitmap('./logo.ico')
    current_song = StringVar()

    def play_song():
            music=playlist.curselection()
            music_name=playlist.get(ACTIVE)
            mixer.music.load(os.path.join(path, music_name))
            mixer.music.play()
            current_song.set(music_name)
            song_label = Label(jpop.t,textvariable=current_song,bg='#0D7F0D',font=("ARIAL",28,"italic")).place(x=1080,y=700)

    def next_():
        next_one = playlist.curselection()
        next_one = next_one[0]+1
        next_song = playlist.get(next_one)
        mixer.music.load(os.path.join(path, next_song))
        mixer.music.play()
        playlist.selection_clear(0, END)
        playlist.activate(next_one)
        playlist.selection_set(next_one, last=None)
        current_song.set(next_song)
        
    def back_():
        back_one = playlist.curselection()
        back_one = back_one[0]-1
        back_song = playlist.get(back_one)
        mixer.music.load(os.path.join(path, back_song))
        mixer.music.play()
        playlist.selection_clear(0, END)
        playlist.activate(back_one)
        playlist.selection_set(back_one, last=None)
        current_song.set(back_song)


    Label(jpop.t,text="J-POP",bd=0,font=("forte",60),fg="black",bg='#0D7F0D').place(x=1200,y=20)
    #frame
    f=Frame(jpop.t,bd=2,bg='white',relief=SUNKEN)
    f.place(x=0,y=0,width=700,height=700)

    #scrollbar and playlist
    scroll=Scrollbar(f)
    playlist=Listbox(f,fg="grey",height=1920,width=800,font=("arial",20,"italic"),bg="#333333",selectbackground="lightblue",cursor="hand2",bd=0,yscrollcommand=scroll.set)
    scroll.config(command=playlist.yview)
    scroll.pack(side=RIGHT,fill=Y)
    playlist.pack(side=LEFT,fill=BOTH)
    
    path="D:/python/music player/Music/jpop"
    songs=os.listdir(path)
    for song in songs:
        if song.endswith(".mp3"):
            playlist.insert(END,song)
            
    #showing name of music playing
    music=Label(jpop.t,text='',font=("arial",30),fg="white",bg="#0D7F0D")
    music.place(x=900,y=700)
    
            
        #buttons
    i=PhotoImage(file="D:/python/music player/ply.png")
    Button(jpop.t,image=i,bg='#0D7F0D',bd=0,command=play_song).place(x=1300,y=800)
    i1=PhotoImage(file="D:/python/music player/bck.png")
    Button(jpop.t,image=i1,bg='#0D7F0D',bd=0,command=back_).place(x=1000,y=800)
    i2=PhotoImage(file='D:/python/music player/nxt.png')
    Button(jpop.t,image=i2,bg='#0D7F0D',bd=0,command=next_).place(x=1450,y=800)
    i3=PhotoImage(file='D:/python/music player/stp.png')
    Button(jpop.t,image=i3,bg='#0D7F0D',bd=0,command=mixer.music.stop).place(x=1150,y=800)



    img4=PhotoImage(file="D:\python\music player\music_logo.png")
    l=Label(jpop.t,text="",image=img4,bd=0)
    l.place(x=1085,y=200)

    jpop.t.mainloop()

def kpop():

    kpop.t = Toplevel(root)
    kpop.t.title("K-pop")
    kpop.t.geometry('1920x1080')
    kpop.t.config(bg='#0D7F0D')
    kpop.t.wm_iconbitmap('./logo.ico')
    current_song = StringVar()

    def play_song():
            music=playlist.curselection()
            music_name=playlist.get(ACTIVE)
            mixer.music.load(os.path.join(path, music_name))
            mixer.music.play()
            current_song.set(music_name)
            song_label = Label(kpop.t,textvariable=current_song,bg='#0D7F0D',font=("ARIAL",28,"italic")).place(x=1080,y=700)

    def next_():
        next_one = playlist.curselection()
        next_one = next_one[0]+1
        next_song = playlist.get(next_one)
        mixer.music.load(os.path.join(path, next_song))
        mixer.music.play()
        playlist.selection_clear(0, END)
        playlist.activate(next_one)
        playlist.selection_set(next_one, last=None)
        current_song.set(next_song)
        
    def back_():
        back_one = playlist.curselection()
        back_one = back_one[0]-1
        back_song = playlist.get(back_one)
        mixer.music.load(os.path.join(path, back_song))
        mixer.music.play()
        playlist.selection_clear(0, END)
        playlist.activate(back_one)
        playlist.selection_set(back_one, last=None)
        current_song.set(back_song)


    Label(kpop.t,text="K-POP",bd=0,font=("forte",60),fg="black",bg='#0D7F0D').place(x=1200,y=20)
    #frame
    f=Frame(kpop.t,bd=2,bg='white',relief=SUNKEN)
    f.place(x=0,y=0,width=700,height=700)

    #scrollbar and playlist
    scroll=Scrollbar(f)
    playlist=Listbox(f,fg="grey",height=1920,width=800,font=("arial",20,"italic"),bg="#333333",selectbackground="lightblue",cursor="hand2",bd=0,yscrollcommand=scroll.set)
    scroll.config(command=playlist.yview)
    scroll.pack(side=RIGHT,fill=Y)
    playlist.pack(side=LEFT,fill=BOTH)
    
    path="D:/python/music player/Music/kpop"
    songs=os.listdir(path)
    for song in songs:
        if song.endswith(".mp3"):
            playlist.insert(END,song)
            
    #showing name of music playing
    music=Label(kpop.t,text='',font=("arial",30),fg="white",bg="#0D7F0D")
    music.place(x=900,y=700)
    
            
        #buttons
    i=PhotoImage(file="D:/python/music player/ply.png")
    Button(kpop.t,image=i,bg='#0D7F0D',bd=0,command=play_song).place(x=1300,y=800)
    i1=PhotoImage(file="D:/python/music player/bck.png")
    Button(kpop.t,image=i1,bg='#0D7F0D',bd=0,command=back_).place(x=1000,y=800)
    i2=PhotoImage(file='D:/python/music player/nxt.png')
    Button(kpop.t,image=i2,bg='#0D7F0D',bd=0,command=next_).place(x=1450,y=800)
    i3=PhotoImage(file='D:/python/music player/stp.png')
    Button(kpop.t,image=i3,bg='#0D7F0D',bd=0,command=mixer.music.stop).place(x=1150,y=800)



    img4=PhotoImage(file="D:\python\music player\music_logo.png")
    l=Label(kpop.t,text="",image=img4,bd=0)
    l.place(x=1085,y=200)

    kpop.t.mainloop()

def pop():

    pop.t = Toplevel(root)
    pop.t.title("Pop")
    pop.t.geometry('1920x1080')
    pop.t.config(bg='#0D7F0D')
    pop.t.wm_iconbitmap('./logo.ico')
    current_song = StringVar()

    def play_song():
            music=playlist.curselection()
            music_name=playlist.get(ACTIVE)
            mixer.music.load(os.path.join(path, music_name))
            mixer.music.play()
            current_song.set(music_name)
            song_label = Label(pop.t,textvariable=current_song,bg='#0D7F0D',font=("ARIAL",28,"italic")).place(x=1080,y=700)

    def next_():
        next_one = playlist.curselection()
        next_one = next_one[0]+1
        next_song = playlist.get(next_one)
        mixer.music.load(os.path.join(path, next_song))
        mixer.music.play()
        playlist.selection_clear(0, END)
        playlist.activate(next_one)
        playlist.selection_set(next_one, last=None)
        current_song.set(next_song)
        
    def back_():
        back_one = playlist.curselection()
        back_one = back_one[0]-1
        back_song = playlist.get(back_one)
        mixer.music.load(os.path.join(path, back_song))
        mixer.music.play()
        playlist.selection_clear(0, END)
        playlist.activate(back_one)
        playlist.selection_set(back_one, last=None)
        current_song.set(back_song)


    Label(pop.t,text="POP",bd=0,font=("forte",60),fg="black",bg='#0D7F0D').place(x=1200,y=20)
    #frame
    f=Frame(pop.t,bd=2,bg='white',relief=SUNKEN)
    f.place(x=0,y=0,width=700,height=700)

    #scrollbar and playlist
    scroll=Scrollbar(f)
    playlist=Listbox(f,fg="grey",height=1920,width=800,font=("arial",20,"italic"),bg="#333333",selectbackground="lightblue",cursor="hand2",bd=0,yscrollcommand=scroll.set)
    scroll.config(command=playlist.yview)
    scroll.pack(side=RIGHT,fill=Y)
    playlist.pack(side=LEFT,fill=BOTH)
    
    path="D:/python/music player/Music/pop"
    songs=os.listdir(path)
    for song in songs:
        if song.endswith(".mp3"):
            playlist.insert(END,song)
            
    #showing name of music playing
    music=Label(pop.t,text='',font=("arial",30),fg="white",bg="#0D7F0D")
    music.place(x=900,y=700)
    
            
        #buttons
    i=PhotoImage(file="D:/python/music player/ply.png")
    Button(pop.t,image=i,bg='#0D7F0D',bd=0,command=play_song).place(x=1300,y=800)
    i1=PhotoImage(file="D:/python/music player/bck.png")
    Button(pop.t,image=i1,bg='#0D7F0D',bd=0,command=back_).place(x=1000,y=800)
    i2=PhotoImage(file='D:/python/music player/nxt.png')
    Button(pop.t,image=i2,bg='#0D7F0D',bd=0,command=next_).place(x=1450,y=800)
    i3=PhotoImage(file='D:/python/music player/stp.png')
    Button(pop.t,image=i3,bg='#0D7F0D',bd=0,command=mixer.music.stop).place(x=1150,y=800)



    img4=PhotoImage(file="D:\python\music player\music_logo.png")
    l=Label(pop.t,text="",image=img4,bd=0)
    l.place(x=1085,y=200)

    pop.t.mainloop()

def rap():

    rap.t = Toplevel(root)
    rap.t.title("Rap")
    rap.t.geometry('1920x1080')
    rap.t.config(bg='#0D7F0D')
    rap.t.wm_iconbitmap('./logo.ico')
    current_song = StringVar()

    def play_song():
            music=playlist.curselection()
            music_name=playlist.get(ACTIVE)
            mixer.music.load(os.path.join(path, music_name))
            mixer.music.play()
            current_song.set(music_name)
            song_label = Label(rap.t,textvariable=current_song,bg='#0D7F0D',font=("ARIAL",28,"italic")).place(x=1080,y=700)

    def next_():
        next_one = playlist.curselection()
        next_one = next_one[0]+1
        next_song = playlist.get(next_one)
        mixer.music.load(os.path.join(path, next_song))
        mixer.music.play()
        playlist.selection_clear(0, END)
        playlist.activate(next_one)
        playlist.selection_set(next_one, last=None)
        current_song.set(next_song)
        
    def back_():
        back_one = playlist.curselection()
        back_one = back_one[0]-1
        back_song = playlist.get(back_one)
        mixer.music.load(os.path.join(path, back_song))
        mixer.music.play()
        playlist.selection_clear(0, END)
        playlist.activate(back_one)
        playlist.selection_set(back_one, last=None)
        current_song.set(back_song)


    Label(rap.t,text="RAP",bd=0,font=("forte",60),fg="black",bg='#0D7F0D').place(x=1200,y=20)
    #frame
    f=Frame(rap.t,bd=2,bg='white',relief=SUNKEN)
    f.place(x=0,y=0,width=700,height=700)

    #scrollbar and playlist
    scroll=Scrollbar(f)
    playlist=Listbox(f,fg="grey",height=1920,width=800,font=("arial",20,"italic"),bg="#333333",selectbackground="lightblue",cursor="hand2",bd=0,yscrollcommand=scroll.set)
    scroll.config(command=playlist.yview)
    scroll.pack(side=RIGHT,fill=Y)
    playlist.pack(side=LEFT,fill=BOTH)
    
    path="D:/python/music player/Music/rap"
    songs=os.listdir(path)
    for song in songs:
        if song.endswith(".mp3"):
            playlist.insert(END,song)
            
    #showing name of music playing
    music=Label(rap.t,text='',font=("arial",30),fg="white",bg="#0D7F0D")
    music.place(x=900,y=700)
    
            
        #buttons
    i=PhotoImage(file="D:/python/music player/ply.png")
    Button(rap.t,image=i,bg='#0D7F0D',bd=0,command=play_song).place(x=1300,y=800)
    i1=PhotoImage(file="D:/python/music player/bck.png")
    Button(rap.t,image=i1,bg='#0D7F0D',bd=0,command=back_).place(x=1000,y=800)
    i2=PhotoImage(file='D:/python/music player/nxt.png')
    Button(rap.t,image=i2,bg='#0D7F0D',bd=0,command=next_).place(x=1450,y=800)
    i3=PhotoImage(file='D:/python/music player/stp.png')
    Button(rap.t,image=i3,bg='#0D7F0D',bd=0,command=mixer.music.stop).place(x=1150,y=800)



    img4=PhotoImage(file="D:\python\music player\music_logo.png")
    l=Label(rap.t,text="",image=img4,bd=0)
    l.place(x=1085,y=200)

    rap.t.mainloop()

def bollywood():

    bollywood.t = Toplevel(root)
    bollywood.t.title("Bollywood")
    bollywood.t.geometry('1920x1080')
    bollywood.t.config(bg='#0D7F0D')
    bollywood.t.wm_iconbitmap('./logo.ico')
    current_song = StringVar()

    def play_song():
            music=playlist.curselection()
            music_name=playlist.get(ACTIVE)
            mixer.music.load(os.path.join(path, music_name))
            mixer.music.play()
            current_song.set(music_name)
            song_label = Label(bollywood.t,textvariable=current_song,bg='#0D7F0D',font=("ARIAL",28,"italic")).place(x=1080,y=700)

    def next_():
        next_one = playlist.curselection()
        next_one = next_one[0]+1
        next_song = playlist.get(next_one)
        mixer.music.load(os.path.join(path, next_song))
        mixer.music.play()
        playlist.selection_clear(0, END)
        playlist.activate(next_one)
        playlist.selection_set(next_one, last=None)
        current_song.set(next_song)
        
    def back_():
        back_one = playlist.curselection()
        back_one = back_one[0]-1
        back_song = playlist.get(back_one)
        mixer.music.load(os.path.join(path, back_song))
        mixer.music.play()
        playlist.selection_clear(0, END)
        playlist.activate(back_one)
        playlist.selection_set(back_one, last=None)
        current_song.set(back_song)


    Label(bollywood.t,text="BOLLYWOOD",bd=0,font=("forte",60),fg="black",bg='#0D7F0D').place(x=1200,y=20)
    #frame
    f=Frame(bollywood.t,bd=2,bg='white',relief=SUNKEN)
    f.place(x=0,y=0,width=700,height=700)

    #scrollbar and playlist
    scroll=Scrollbar(f)
    playlist=Listbox(f,fg="grey",height=1920,width=800,font=("arial",20,"italic"),bg="#333333",selectbackground="lightblue",cursor="hand2",bd=0,yscrollcommand=scroll.set)
    scroll.config(command=playlist.yview)
    scroll.pack(side=RIGHT,fill=Y)
    playlist.pack(side=LEFT,fill=BOTH)
    
    path="D:/python/music player/Music/bollywood"
    songs=os.listdir(path)
    for song in songs:
        if song.endswith(".mp3"):
            playlist.insert(END,song)
            
    #showing name of music playing
    music=Label(bollywood.t,text='',font=("arial",30),fg="white",bg="#0D7F0D")
    music.place(x=900,y=700)
    
            
        #buttons
    i=PhotoImage(file="D:/python/music player/ply.png")
    Button(bollywood.t,image=i,bg='#0D7F0D',bd=0,command=play_song).place(x=1300,y=800)
    i1=PhotoImage(file="D:/python/music player/bck.png")
    Button(bollywood.t,image=i1,bg='#0D7F0D',bd=0,command=back_).place(x=1000,y=800)
    i2=PhotoImage(file='D:/python/music player/nxt.png')
    Button(bollywood.t,image=i2,bg='#0D7F0D',bd=0,command=next_).place(x=1450,y=800)
    i3=PhotoImage(file='D:/python/music player/stp.png')
    Button(bollywood.t,image=i3,bg='#0D7F0D',bd=0,command=mixer.music.stop).place(x=1150,y=800)



    img4=PhotoImage(file="D:\python\music player\music_logo.png")
    l=Label(bollywood.t,text="",image=img4,bd=0)
    l.place(x=1085,y=200)

    bollywood.t.mainloop()

def spanish():

    spanish.t = Toplevel(root)
    spanish.t.title("Spanish")
    spanish.t.geometry('1920x1080')
    spanish.t.config(bg='#0D7F0D')
    spanish.t.wm_iconbitmap('./logo.ico')
    current_song = StringVar()

    def play_song():
            music=playlist.curselection()
            music_name=playlist.get(ACTIVE)
            mixer.music.load(os.path.join(path, music_name))
            mixer.music.play()
            current_song.set(music_name)
            song_label = Label(spanish.t,textvariable=current_song,bg='#0D7F0D',font=("ARIAL",28,"italic")).place(x=1080,y=700)

    def next_():
        next_one = playlist.curselection()
        next_one = next_one[0]+1
        next_song = playlist.get(next_one)
        mixer.music.load(os.path.join(path, next_song))
        mixer.music.play()
        playlist.selection_clear(0, END)
        playlist.activate(next_one)
        playlist.selection_set(next_one, last=None)
        current_song.set(next_song)
        
    def back_():
        back_one = playlist.curselection()
        back_one = back_one[0]-1
        back_song = playlist.get(back_one)
        mixer.music.load(os.path.join(path, back_song))
        mixer.music.play()
        playlist.selection_clear(0, END)
        playlist.activate(back_one)
        playlist.selection_set(back_one, last=None)
        current_song.set(back_song)


    Label(spanish.t,text="SPANISH",bd=0,font=("forte",60),fg="black",bg='#0D7F0D').place(x=1200,y=20)
    #frame
    f=Frame(spanish.t,bd=2,bg='white',relief=SUNKEN)
    f.place(x=0,y=0,width=700,height=700)

    #scrollbar and playlist
    scroll=Scrollbar(f)
    playlist=Listbox(f,fg="grey",height=1920,width=800,font=("arial",20,"italic"),bg="#333333",selectbackground="lightblue",cursor="hand2",bd=0,yscrollcommand=scroll.set)
    scroll.config(command=playlist.yview)
    scroll.pack(side=RIGHT,fill=Y)
    playlist.pack(side=LEFT,fill=BOTH)
    
    path="D:/python/music player/Music/spanish"
    songs=os.listdir(path)
    for song in songs:
        if song.endswith(".mp3"):
            playlist.insert(END,song)
            
    #showing name of music playing
    music=Label(spanish.t,text='',font=("arial",30),fg="white",bg="#0D7F0D")
    music.place(x=900,y=700)
    
            
        #buttons
    i=PhotoImage(file="D:/python/music player/ply.png")
    Button(spanish.t,image=i,bg='#0D7F0D',bd=0,command=play_song).place(x=1300,y=800)
    i1=PhotoImage(file="D:/python/music player/bck.png")
    Button(spanish.t,image=i1,bg='#0D7F0D',bd=0,command=back_).place(x=1000,y=800)
    i2=PhotoImage(file='D:/python/music player/nxt.png')
    Button(spanish.t,image=i2,bg='#0D7F0D',bd=0,command=next_).place(x=1450,y=800)
    i3=PhotoImage(file='D:/python/music player/stp.png')
    Button(spanish.t,image=i3,bg='#0D7F0D',bd=0,command=mixer.music.stop).place(x=1150,y=800)



    img4=PhotoImage(file="D:\python\music player\music_logo.png")
    l=Label(spanish.t,text="",image=img4,bd=0)
    l.place(x=1085,y=200)

    spanish.t.mainloop()

def latin():

    latin.t = Toplevel(root)
    latin.t.title("Latin")
    latin.t.geometry('1920x1080')
    latin.t.config(bg='#0D7F0D')
    latin.t.wm_iconbitmap('./logo.ico')
    current_song = StringVar()

    def play_song():
            music=playlist.curselection()
            music_name=playlist.get(ACTIVE)
            mixer.music.load(os.path.join(path, music_name))
            mixer.music.play()
            current_song.set(music_name)
            song_label = Label(latin.t,textvariable=current_song,bg='#0D7F0D',font=("ARIAL",28,"italic")).place(x=1080,y=700)

    def next_():
        next_one = playlist.curselection()
        next_one = next_one[0]+1
        next_song = playlist.get(next_one)
        mixer.music.load(os.path.join(path, next_song))
        mixer.music.play()
        playlist.selection_clear(0, END)
        playlist.activate(next_one)
        playlist.selection_set(next_one, last=None)
        current_song.set(next_song)
        
    def back_():
        back_one = playlist.curselection()
        back_one = back_one[0]-1
        back_song = playlist.get(back_one)
        mixer.music.load(os.path.join(path, back_song))
        mixer.music.play()
        playlist.selection_clear(0, END)
        playlist.activate(back_one)
        playlist.selection_set(back_one, last=None)
        current_song.set(back_song)


    Label(latin.t,text="LATIN",bd=0,font=("forte",60),fg="black",bg='#0D7F0D').place(x=1200,y=20)
    #frame
    f=Frame(latin.t,bd=2,bg='white',relief=SUNKEN)
    f.place(x=0,y=0,width=700,height=700)

    #scrollbar and playlist
    scroll=Scrollbar(f)
    playlist=Listbox(f,fg="grey",height=1920,width=800,font=("arial",20,"italic"),bg="#333333",selectbackground="lightblue",cursor="hand2",bd=0,yscrollcommand=scroll.set)
    scroll.config(command=playlist.yview)
    scroll.pack(side=RIGHT,fill=Y)
    playlist.pack(side=LEFT,fill=BOTH)
    
    path="D:/python/music player/Music/latin"
    songs=os.listdir(path)
    for song in songs:
        if song.endswith(".mp3"):
            playlist.insert(END,song)
            
    #showing name of music playing
    music=Label(latin.t,text='',font=("arial",30),fg="white",bg="#0D7F0D")
    music.place(x=900,y=700)
    
            
        #buttons
    i=PhotoImage(file="D:/python/music player/ply.png")
    Button(latin.t,image=i,bg='#0D7F0D',bd=0,command=play_song).place(x=1300,y=800)
    i1=PhotoImage(file="D:/python/music player/bck.png")
    Button(latin.t,image=i1,bg='#0D7F0D',bd=0,command=back_).place(x=1000,y=800)
    i2=PhotoImage(file='D:/python/music player/nxt.png')
    Button(latin.t,image=i2,bg='#0D7F0D',bd=0,command=next_).place(x=1450,y=800)
    i3=PhotoImage(file='D:/python/music player/stp.png')
    Button(latin.t,image=i3,bg='#0D7F0D',bd=0,command=mixer.music.stop).place(x=1150,y=800)



    img4=PhotoImage(file="D:\python\music player\music_logo.png")
    l=Label(latin.t,text="",image=img4,bd=0)
    l.place(x=1085,y=200)

    latin.t.mainloop()

def fbase():

    fbase.t = Toplevel(root)
    fbase.t.title("FUTURE BASE")
    fbase.t.geometry('1920x1080')
    fbase.t.config(bg='#0D7F0D')
    fbase.t.wm_iconbitmap('./logo.ico')
    current_song = StringVar()

    def play_song():
            music=playlist.curselection()
            music_name=playlist.get(ACTIVE)
            mixer.music.load(os.path.join(path, music_name))
            mixer.music.play()
            current_song.set(music_name)
            song_label = Label(fbase.t,textvariable=current_song,bg='#0D7F0D',font=("ARIAL",28,"italic")).place(x=1080,y=700)

    def next_():
        next_one = playlist.curselection()
        next_one = next_one[0]+1
        next_song = playlist.get(next_one)
        mixer.music.load(os.path.join(path, next_song))
        mixer.music.play()
        playlist.selection_clear(0, END)
        playlist.activate(next_one)
        playlist.selection_set(next_one, last=None)
        current_song.set(next_song)
        
    def back_():
        back_one = playlist.curselection()
        back_one = back_one[0]-1
        back_song = playlist.get(back_one)
        mixer.music.load(os.path.join(path, back_song))
        mixer.music.play()
        playlist.selection_clear(0, END)
        playlist.activate(back_one)
        playlist.selection_set(back_one, last=None)
        current_song.set(back_song)


    Label(fbase.t,text="FUTURE BASE",bd=0,font=("forte",60),fg="black",bg='#0D7F0D').place(x=1200,y=20)
    #frame
    f=Frame(fbase.t,bd=2,bg='white',relief=SUNKEN)
    f.place(x=0,y=0,width=700,height=700)

    #scrollbar and playlist
    scroll=Scrollbar(f)
    playlist=Listbox(f,fg="grey",height=1920,width=800,font=("arial",20,"italic"),bg="#333333",selectbackground="lightblue",cursor="hand2",bd=0,yscrollcommand=scroll.set)
    scroll.config(command=playlist.yview)
    scroll.pack(side=RIGHT,fill=Y)
    playlist.pack(side=LEFT,fill=BOTH)
    
    path="D:/python/music player/Music/fbase"
    songs=os.listdir(path)
    for song in songs:
        if song.endswith(".mp3"):
            playlist.insert(END,song)
            
    #showing name of music playing
    music=Label(fbase.t,text='',font=("arial",30),fg="white",bg="#0D7F0D")
    music.place(x=900,y=700)
    
            
        #buttons
    i=PhotoImage(file="D:/python/music player/ply.png")
    Button(fbase.t,image=i,bg='#0D7F0D',bd=0,command=play_song).place(x=1300,y=800)
    i1=PhotoImage(file="D:/python/music player/bck.png")
    Button(fbase.t,image=i1,bg='#0D7F0D',bd=0,command=back_).place(x=1000,y=800)
    i2=PhotoImage(file='D:/python/music player/nxt.png')
    Button(fbase.t,image=i2,bg='#0D7F0D',bd=0,command=next_).place(x=1450,y=800)
    i3=PhotoImage(file='D:/python/music player/stp.png')
    Button(fbase.t,image=i3,bg='#0D7F0D',bd=0,command=mixer.music.stop).place(x=1150,y=800)



    img4=PhotoImage(file="D:\python\music player\music_logo.png")
    l=Label(fbase.t,text="",image=img4,bd=0)
    l.place(x=1085,y=200)

    fbase.t.mainloop()

def elec():

    elec.t = Toplevel(root)
    elec.t.title("ELECTRONIC")
    elec.t.geometry('1920x1080')
    elec.t.config(bg='#0D7F0D')
    elec.t.wm_iconbitmap('./logo.ico')
    current_song = StringVar()

    def play_song():
            music=playlist.curselection()
            music_name=playlist.get(ACTIVE)
            mixer.music.load(os.path.join(path, music_name))
            mixer.music.play()
            current_song.set(music_name)
            song_label = Label(elec.t,textvariable=current_song,bg='#0D7F0D',font=("ARIAL",28,"italic")).place(x=1080,y=700)

    def next_():
        next_one = playlist.curselection()
        next_one = next_one[0]+1
        next_song = playlist.get(next_one)
        mixer.music.load(os.path.join(path, next_song))
        mixer.music.play()
        playlist.selection_clear(0, END)
        playlist.activate(next_one)
        playlist.selection_set(next_one, last=None)
        current_song.set(next_song)
        
    def back_():
        back_one = playlist.curselection()
        back_one = back_one[0]-1
        back_song = playlist.get(back_one)
        mixer.music.load(os.path.join(path, back_song))
        mixer.music.play()
        playlist.selection_clear(0, END)
        playlist.activate(back_one)
        playlist.selection_set(back_one, last=None)
        current_song.set(back_song)


    Label(elec.t,text="ELECTRONIC",bd=0,font=("forte",60),fg="black",bg='#0D7F0D').place(x=1200,y=20)
    #frame
    f=Frame(elec.t,bd=2,bg='white',relief=SUNKEN)
    f.place(x=0,y=0,width=700,height=700)

    #scrollbar and playlist
    scroll=Scrollbar(f)
    playlist=Listbox(f,fg="grey",height=1920,width=800,font=("arial",20,"italic"),bg="#333333",selectbackground="lightblue",cursor="hand2",bd=0,yscrollcommand=scroll.set)
    scroll.config(command=playlist.yview)
    scroll.pack(side=RIGHT,fill=Y)
    playlist.pack(side=LEFT,fill=BOTH)
    
    path="D:/python/music player/Music/elec"
    songs=os.listdir(path)
    for song in songs:
        if song.endswith(".mp3"):
            playlist.insert(END,song)
            
    #showing name of music playing
    music=Label(elec.t,text='',font=("arial",30),fg="white",bg="#0D7F0D")
    music.place(x=900,y=700)
    
            
        #buttons
    i=PhotoImage(file="D:/python/music player/ply.png")
    Button(elec.t,image=i,bg='#0D7F0D',bd=0,command=play_song).place(x=1300,y=800)
    i1=PhotoImage(file="D:/python/music player/bck.png")
    Button(elec.t,image=i1,bg='#0D7F0D',bd=0,command=back_).place(x=1000,y=800)
    i2=PhotoImage(file='D:/python/music player/nxt.png')
    Button(elec.t,image=i2,bg='#0D7F0D',bd=0,command=next_).place(x=1450,y=800)
    i3=PhotoImage(file='D:/python/music player/stp.png')
    Button(elec.t,image=i3,bg='#0D7F0D',bd=0,command=mixer.music.stop).place(x=1150,y=800)



    img4=PhotoImage(file="D:\python\music player\music_logo.png")
    l=Label(elec.t,text="",image=img4,bd=0)
    l.place(x=1085,y=200)

    elec.t.mainloop()

def bhj():

    bhj.t = Toplevel(root)
    bhj.t.title("BHAJAN")
    bhj.t.geometry('1920x1080')
    bhj.t.config(bg='#0D7F0D')
    bhj.t.wm_iconbitmap('./logo.ico')
    current_song = StringVar()

    def play_song():
            music=playlist.curselection()
            music_name=playlist.get(ACTIVE)
            mixer.music.load(os.path.join(path, music_name))
            mixer.music.play()
            current_song.set(music_name)
            song_label = Label(bhj.t,textvariable=current_song,bg='#0D7F0D',font=("ARIAL",28,"italic")).place(x=1080,y=700)

    def next_():
        next_one = playlist.curselection()
        next_one = next_one[0]+1
        next_song = playlist.get(next_one)
        mixer.music.load(os.path.join(path, next_song))
        mixer.music.play()
        playlist.selection_clear(0, END)
        playlist.activate(next_one)
        playlist.selection_set(next_one, last=None)
        current_song.set(next_song)
        
    def back_():
        back_one = playlist.curselection()
        back_one = back_one[0]-1
        back_song = playlist.get(back_one)
        mixer.music.load(os.path.join(path, back_song))
        mixer.music.play()
        playlist.selection_clear(0, END)
        playlist.activate(back_one)
        playlist.selection_set(back_one, last=None)
        current_song.set(back_song)


    Label(bhj.t,text="BHAJAN",bd=0,font=("forte",60),fg="black",bg='#0D7F0D').place(x=1200,y=20)
    #frame
    f=Frame(bhj.t,bd=2,bg='white',relief=SUNKEN)
    f.place(x=0,y=0,width=700,height=700)

    #scrollbar and playlist
    scroll=Scrollbar(f)
    playlist=Listbox(f,fg="grey",height=1920,width=800,font=("arial",20,"italic"),bg="#333333",selectbackground="lightblue",cursor="hand2",bd=0,yscrollcommand=scroll.set)
    scroll.config(command=playlist.yview)
    scroll.pack(side=RIGHT,fill=Y)
    playlist.pack(side=LEFT,fill=BOTH)
    
    path="D:/python/music player/Music/bhj"
    songs=os.listdir(path)
    for song in songs:
        if song.endswith(".mp3"):
            playlist.insert(END,song)
            
    #showing name of music playing
    music=Label(bhj.t,text='',font=("arial",30),fg="white",bg="#0D7F0D")
    music.place(x=900,y=700)
    
            
        #buttons
    i=PhotoImage(file="D:/python/music player/ply.png")
    Button(bhj.t,image=i,bg='#0D7F0D',bd=0,command=play_song).place(x=1300,y=800)
    i1=PhotoImage(file="D:/python/music player/bck.png")
    Button(bhj.t,image=i1,bg='#0D7F0D',bd=0,command=back_).place(x=1000,y=800)
    i2=PhotoImage(file='D:/python/music player/nxt.png')
    Button(bhj.t,image=i2,bg='#0D7F0D',bd=0,command=next_).place(x=1450,y=800)
    i3=PhotoImage(file='D:/python/music player/stp.png')
    Button(bhj.t,image=i3,bg='#0D7F0D',bd=0,command=mixer.music.stop).place(x=1150,y=800)



    img4=PhotoImage(file="D:\python\music player\music_logo.png")
    l=Label(bhj.t,text="",image=img4,bd=0)
    l.place(x=1085,y=200)

    bhj.t.mainloop()

def ip():

    ip.t = Toplevel(root)
    ip.t.title("Indie-Pop")
    ip.t.geometry('1920x1080')
    ip.t.config(bg='#0D7F0D')
    ip.t.wm_iconbitmap('./logo.ico')
    current_song = StringVar()

    def play_song():
            music=playlist.curselection()
            music_name=playlist.get(ACTIVE)
            mixer.music.load(os.path.join(path, music_name))
            mixer.music.play()
            current_song.set(music_name)
            song_label = Label(ip.t,textvariable=current_song,bg='#0D7F0D',font=("ARIAL",28,"italic")).place(x=1080,y=700)

    def next_():
        next_one = playlist.curselection()
        next_one = next_one[0]+1
        next_song = playlist.get(next_one)
        mixer.music.load(os.path.join(path, next_song))
        mixer.music.play()
        playlist.selection_clear(0, END)
        playlist.activate(next_one)
        playlist.selection_set(next_one, last=None)
        current_song.set(next_song)
        
    def back_():
        back_one = playlist.curselection()
        back_one = back_one[0]-1
        back_song = playlist.get(back_one)
        mixer.music.load(os.path.join(path, back_song))
        mixer.music.play()
        playlist.selection_clear(0, END)
        playlist.activate(back_one)
        playlist.selection_set(back_one, last=None)
        current_song.set(back_song)


    Label(ip.t,text="INDIE-POP",bd=0,font=("forte",60),fg="black",bg='#0D7F0D').place(x=1200,y=20)
    #frame
    f=Frame(ip.t,bd=2,bg='white',relief=SUNKEN)
    f.place(x=0,y=0,width=700,height=700)

    #scrollbar and playlist
    scroll=Scrollbar(f)
    playlist=Listbox(f,fg="grey",height=1920,width=800,font=("arial",20,"italic"),bg="#333333",selectbackground="lightblue",cursor="hand2",bd=0,yscrollcommand=scroll.set)
    scroll.config(command=playlist.yview)
    scroll.pack(side=RIGHT,fill=Y)
    playlist.pack(side=LEFT,fill=BOTH)
    
    path="D:/python/music player/Music/ip"
    songs=os.listdir(path)
    for song in songs:
        if song.endswith(".mp3"):
            playlist.insert(END,song)
            
    #showing name of music playing
    music=Label(ip.t,text='',font=("arial",30),fg="white",bg="#0D7F0D")
    music.place(x=900,y=700)
    
            
        #buttons
    i=PhotoImage(file="D:/python/music player/ply.png")
    Button(ip.t,image=i,bg='#0D7F0D',bd=0,command=play_song).place(x=1300,y=800)
    i1=PhotoImage(file="D:/python/music player/bck.png")
    Button(ip.t,image=i1,bg='#0D7F0D',bd=0,command=back_).place(x=1000,y=800)
    i2=PhotoImage(file='D:/python/music player/nxt.png')
    Button(ip.t,image=i2,bg='#0D7F0D',bd=0,command=next_).place(x=1450,y=800)
    i3=PhotoImage(file='D:/python/music player/stp.png')
    Button(ip.t,image=i3,bg='#0D7F0D',bd=0,command=mixer.music.stop).place(x=1150,y=800)



    img4=PhotoImage(file="D:\python\music player\music_logo.png")
    l=Label(ip.t,text="",image=img4,bd=0)
    l.place(x=1085,y=200)

    ip.t.mainloop()

def classic():

    classic.t = Toplevel(root)
    classic.t.title("Classic")
    classic.t.geometry('1920x1080')
    classic.t.config(bg='#0D7F0D')
    classic.t.wm_iconbitmap('./logo.ico')
    current_song = StringVar()

    def play_song():
            music=playlist.curselection()
            music_name=playlist.get(ACTIVE)
            mixer.music.load(os.path.join(path, music_name))
            mixer.music.play()
            current_song.set(music_name)
            song_label = Label(classic.t,textvariable=current_song,bg='#0D7F0D',font=("ARIAL",28,"italic")).place(x=1080,y=700)

    def next_():
        next_one = playlist.curselection()
        next_one = next_one[0]+1
        next_song = playlist.get(next_one)
        mixer.music.load(os.path.join(path, next_song))
        mixer.music.play()
        playlist.selection_clear(0, END)
        playlist.activate(next_one)
        playlist.selection_set(next_one, last=None)
        current_song.set(next_song)
        
    def back_():
        back_one = playlist.curselection()
        back_one = back_one[0]-1
        back_song = playlist.get(back_one)
        mixer.music.load(os.path.join(path, back_song))
        mixer.music.play()
        playlist.selection_clear(0, END)
        playlist.activate(back_one)
        playlist.selection_set(back_one, last=None)
        current_song.set(back_song)


    Label(classic.t,text="CLASSIC",bd=0,font=("forte",60),fg="black",bg='#0D7F0D').place(x=1200,y=20)
    #frame
    f=Frame(classic.t,bd=2,bg='white',relief=SUNKEN)
    f.place(x=0,y=0,width=700,height=700)

    #scrollbar and playlist
    scroll=Scrollbar(f)
    playlist=Listbox(f,fg="grey",height=1920,width=800,font=("arial",20,"italic"),bg="#333333",selectbackground="lightblue",cursor="hand2",bd=0,yscrollcommand=scroll.set)
    scroll.config(command=playlist.yview)
    scroll.pack(side=RIGHT,fill=Y)
    playlist.pack(side=LEFT,fill=BOTH)
    
    path="D:/python/music player/Music/classic"
    songs=os.listdir(path)
    for song in songs:
        if song.endswith(".mp3"):
            playlist.insert(END,song)
            
    #showing name of music playing
    music=Label(classic.t,text='',font=("arial",30),fg="white",bg="#0D7F0D")
    music.place(x=900,y=700)
    
            
        #buttons
    i=PhotoImage(file="D:/python/music player/ply.png")
    Button(classic.t,image=i,bg='#0D7F0D',bd=0,command=play_song).place(x=1300,y=800)
    i1=PhotoImage(file="D:/python/music player/bck.png")
    Button(classic.t,image=i1,bg='#0D7F0D',bd=0,command=back_).place(x=1000,y=800)
    i2=PhotoImage(file='D:/python/music player/nxt.png')
    Button(classic.t,image=i2,bg='#0D7F0D',bd=0,command=next_).place(x=1450,y=800)
    i3=PhotoImage(file='D:/python/music player/stp.png')
    Button(classic.t,image=i3,bg='#0D7F0D',bd=0,command=mixer.music.stop).place(x=1150,y=800)



    img4=PhotoImage(file="D:\python\music player\music_logo.png")
    l=Label(classic.t,text="",image=img4,bd=0)
    l.place(x=1085,y=200)

    classic.t.mainloop()


    
Label(root,text="GENRE",bg='#0D7F0D',bd=0,font=("ARIAL",80,"bold")).place(x=800,y=50)
Label(root,text="Select your favourite genre",bg='#0D7F0D',bd=0,font=("ARIAL",20,"italic")).place(x=830,y=190)
#button
img=PhotoImage(file='./folder.png')
Button(root,image=img,bg='#0D7F0D',bd=0,command=jpop).place(x=1700,y=250)
l=Label(root,text="J-pop",bd=0,font=("forte",30),fg="black",bg='#0D7F0D')
l.place(x=1750,y=430)
img1=PhotoImage(file='./folder.png')
Button(root,image=img1,bg='#0D7F0D',bd=0,command=kpop).place(x=1700,y=550)
l1=Label(root,text="K-pop",bd=0,font=("forte",30),fg="black",bg='#0D7F0D')
l1.place(x=1750,y=730)
img2=PhotoImage(file='./folder.png')
Button(root,image=img2,bg='#0D7F0D',bd=0,command=pop).place(x=1400,y=250)
l2=Label(root,text="Pop",bd=0,font=("forte",30),fg="black",bg='#0D7F0D')
l2.place(x=1450,y=430)
img3=PhotoImage(file='./folder.png')
Button(root,image=img3,bg='#0D7F0D',bd=0,command=rap).place(x=1400,y=550)
l3=Label(root,text="Rap",bd=0,font=("forte",30),fg="black",bg='#0D7F0D')
l3.place(x=1450,y=730)
img4=PhotoImage(file='./folder.png')
Button(root,image=img4,bg='#0D7F0D',bd=0,command=bollywood).place(x=1100,y=250)
l4=Label(root,text="Bollywood",bd=0,font=("forte",30),fg="black",bg='#0D7F0D')
l4.place(x=1100,y=430)
img5=PhotoImage(file='./folder.png')
Button(root,image=img5,bg='#0D7F0D',bd=0,command=spanish).place(x=1100,y=550)
l5=Label(root,text="Spanish",bd=0,font=("forte",30),fg="black",bg='#0D7F0D')
l5.place(x=1100,y=730)
img6=PhotoImage(file='./folder.png')
Button(root,image=img6,bg='#0D7F0D',bd=0,command=latin).place(x=800,y=250)
l6=Label(root,text="Latin",bd=0,font=("forte",30),fg="black",bg='#0D7F0D')
l6.place(x=850,y=430)
img7=PhotoImage(file='./folder.png')
Button(root,image=img7,bg='#0D7F0D',bd=0,command=fbase).place(x=800,y=550)
l7=Label(root,text="Future base",bd=0,font=("forte",30),fg="black",bg='#0D7F0D')
l7.place(x=800,y=730)
img9=PhotoImage(file='./folder.png')
Button(root,image=img9,bg='#0D7F0D',bd=0,command=elec).place(x=500,y=250)
l9=Label(root,text="Electronic",bd=0,font=("forte",30),fg="black",bg='#0D7F0D')
l9.place(x=500,y=430)
img10=PhotoImage(file='./folder.png')
Button(root,image=img10,bg='#0D7F0D',bd=0,command=bhj).place(x=500,y=550)
l10=Label(root,text="Bhajan",bd=0,font=("forte",30),fg="black",bg='#0D7F0D')
l10.place(x=500,y=730)
img11=PhotoImage(file='./folder.png')
Button(root,image=img11,bg='#0D7F0D',bd=0,command=ip).place(x=200,y=250)
l11=Label(root,text="Indie-pop",bd=0,font=("forte",30),fg="black",bg='#0D7F0D')
l11.place(x=200,y=430)
img12=PhotoImage(file='./folder.png')
Button(root,image=img12,bg='#0D7F0D',bd=0,command=classic).place(x=200,y=550)
l12=Label(root,text="Classic",bd=0,font=("forte",30),fg="black",bg='#0D7F0D')
l12.place(x=200,y=730)










root.mainloop()



