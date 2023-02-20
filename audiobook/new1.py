import os
from tkinter import * #std gui library
import pyttsx3
import PyPDF2
from tkinter.filedialog import askopenfilename
import pywhatkit as kt
from PIL import ImageTk, Image  #Python Imaging Library 
from translate import Translator

book=askopenfilename()
speaker=pyttsx3.init()
pdfReader=PyPDF2.PdfFileReader(book,strict=False)
pages = pdfReader.numPages
window = Tk()
window.title("My Audiobook")
window.geometry("1800x1000")
greet = Label(window,text=os.path.basename(book),font='Helvetica 15',pady=20).pack()

f=Frame(window)
lb=Label(f,text=" ",height=1).pack()
img=Image.open("audiobook.png")
newimg=img.resize((950,500))
img1=ImageTk.PhotoImage(newimg)
label=Label(f,image=img1)
label.pack()
lb=Label(f,text=" ",height=3).pack(side=LEFT)

def male():
    voice=speaker.getProperty('voices')
    speaker.setProperty('voice',voice[0].id)
def female():
    voice=speaker.getProperty('voices')
    speaker.setProperty('voice',voice[1].id)
def ispeed():
    speed = speaker.getProperty('rate')
    speaker.setProperty('rate',speed+20)
def dspeed():
    speed = speaker.getProperty('rate')
    speaker.setProperty('rate',speed-20)

def ivol1():
    vol=speaker.getProperty('volume')
    speaker.setProperty('volume',vol+0.2)

def ivol2():
    vol=speaker.getProperty('volume')
    speaker.setProperty('volume',vol+0.4)

def ivol3():
    vol=speaker.getProperty('volume')
    speaker.setProperty('volume',vol+0.6)

def ivol4():
    vol=speaker.getProperty('volume')
    speaker.setProperty('volume',vol+0.8)

def dvol1():
    vol=speaker.getProperty('volume')
    speaker.setProperty('volume',vol-0.2)

def dvol2():
    vol=speaker.getProperty('volume')
    speaker.setProperty('volume',vol-0.4)

def dvol3():
    vol=speaker.getProperty('volume')
    speaker.setProperty('volume',vol-0.6)

def dvol4():
    
    vol=speaker.getProperty('volume')
    speaker.setProperty('volume',vol-0.8)
def main():
    def play():
        speaker.runAndWait()
    def pause():
        speaker.stop

    for i in range(int(t1.get())-1,int(t2.get())):
        page = pdfReader.getPage(i)
        txt = page.extractText(page)
        speaker.say(txt)
        speaker.runAndWait()
def translator_fun():
       translator=Translator(to_lang=t5.get())
       translation=translator.translate(t4.get())
       lb8.config(text=translation)
def search():
        kt.search(t3.get("1.0","end-1c"))





lb1=Label(f,text="Start page no. : ")
lb1.pack(side=LEFT)
t1=Entry(f,width=15)
t1.pack(side=LEFT)
lb=Label(f,text=" ",height=2,width=3).pack(side=LEFT)

lb2=Label(f,text="End page no. : ").pack(side=LEFT)
t2=Entry(f,width=15)
t2.pack(side=LEFT)
lb=Label(f,text=" ",height=2,width=3).pack(side=LEFT)

bt7=Button(f,text="Set",command=main,height=1,width=20,bg='#FCD12A').pack(side=LEFT)
lb=Label(f,text=" ",height=2,width=3).pack(side=LEFT)

lb3=Label(f,text="Unknown word : ").pack(side=LEFT)
t3=Text(f,height=1.5,width=15)
t3.pack(side=LEFT)
lb=Label(f,text=" ",width=3).pack(side=LEFT)
bt8=Button(f,text="Search",command=search,height=1,width=20,bg='#FCD12A').pack(side=LEFT)
f.pack()


f2=Frame(window)
lb7=Label(f2,text="Enter word : ")
lb7.pack(side=LEFT)
t4=Entry(f2,width=15)
t4.pack(side=LEFT)
lb=Label(f2,text=" ",height=2,width=3).pack(side=LEFT)
lb7=Label(f2,text="Enter language with first letter in capitals : ").pack(side=LEFT)
t5=Entry(f2,width=15)
t5.pack(side=LEFT)
lb=Label(f2,text=" ",width=3).pack(side=LEFT)

bt8=Button(f2,text="Translate",command=translator_fun,height=1,width=20,bg='#FCD12A').pack(side=LEFT)
lb=Label(f2,text=" ",width=3).pack(side=LEFT)

lb8=Label(f2,text="Translated text")
lb8.pack(side=LEFT)
f2.pack()


f3=Frame(window)
lb4=Label(f3,text="NOTE : Please do enter the settings before the audio starts to enjoy uninterupted listening!! ",bg='#FCD12A').pack()
f3.pack()


f4=Frame(window)
lb=Label(f4,text=" ",height=2,width=3).pack(side=LEFT)
bt1=Button(f4,text="speed >>",height=1,width=20,command=ispeed).pack(side=RIGHT)
bt2=Button(f4,text="<< speed",height=1,width=20,command=dspeed).pack(side=LEFT)
bt5=Button(f4,text="female",height=1,width=20,command=female).pack(side=RIGHT)
bt6=Button(f4,text="male",height=1,width=20,command=male).pack(side=LEFT)
f4.pack()

f5=Frame(window)
bt3=Button(f5,text="vol + 80%",height=1,width=20,command=ivol4).pack(side=RIGHT)
bt4=Button(f5,text="vol - 80%",height=1,width=20,command=dvol4).pack(side=LEFT)
bt3=Button(f5,text="vol + 60%",height=1,width=20,command=ivol3).pack(side=RIGHT)
bt4=Button(f5,text="vol - 60%",height=1,width=20,command=dvol3).pack(side=LEFT)
bt3=Button(f5,text="vol + 40%",height=1,width=20,command=ivol2).pack(side=RIGHT)
bt4=Button(f5,text="vol - 40%",height=1,width=20,command=dvol2).pack(side=LEFT)
bt3=Button(f5,text="vol + 20%",height=1,width=20,command=ivol1).pack(side=RIGHT)
bt4=Button(f5,text="vol - 20%",height=1,width=20,command=dvol1).pack(side=LEFT)
f5.pack()

window.mainloop()