"""
    THIS IS PYTHON GAME CREATED BY YASH SHARMA WHILE LEARNING TKINTER
"""
global Computer,Vs,User

#Importing required packages tkinter, random
from tkinter import *
from tkinter import messagebox
import random

def Final_Score():
    #calculating marks....
    if (marks.get())>(cmarks.get()):
        messagebox.showinfo("YOU WON",("YOU WON BY "+str(marks.get()-cmarks.get())+" POINTS."))
    elif (marks.get())<(cmarks.get()):
        messagebox.showinfo("YOU LOOSE",("COMPUTER WON BY "+str(cmarks.get()-marks.get())+" POINTS."))
    else :
        messagebox.showinfo("DRAW",("MATCH DRAWN WITH "+str(marks.get())+" POINTS."))

def normalise():
    #setting default images
    User.config(image=userImg)
    Computer.config(image=computerImg)

def action(n):
    #action on user's move
    cmp=random.choice([1,2,3])
    if cmp==1:
        Computer.config(image=Stone)
    elif cmp==2:
        Computer.config(image=Paper)
    elif cmp==3:
        Computer.config(image=Scissor)
    if n==2 and cmp==3:
        cmarks.set((cmarks.get())+7)
    elif n==1 and cmp==2:
        cmarks.set((cmarks.get())+7)
    elif n==3 and cmp==1:
        cmarks.set((cmarks.get())+7)
    elif n==cmp:
        cmarks.set((cmarks.get())+0)
    else:
        marks.set((marks.get())+7)
    User.after(500,normalise)
    
    

def start():
    #click of plbut (play button)
    if (game.get()) == "OFF":
        s=messagebox.askyesno("Begin","Instructions & rules :\n1) If you win you will get 7 points.\n2) If you loose computer will get 7 points.\nDo you want to continue ?")
        if s==1:
            plbut.config(text="STOP GAME ABRUPTLY")
            game.set("ON")
            papbut.config(state=NORMAL)
            stnbut.config(state=NORMAL)
            scibut.config(state=NORMAL)
            marks.set(0)
            cmarks.set(0)
    else :
        s=messagebox.askyesno("Stop","Really Want to Stop ?")
        if s==1:
            plbut.config(text="START THE GAME")
            papbut.config(state=DISABLED)
            stnbut.config(state=DISABLED)
            scibut.config(state=DISABLED)
            Final_Score()
            marks.set(0)
            cmarks.set(0)
            game.set("OFF")

                        
def stone():
    if (game.get())=="ON":
        User.config(image=Stone)
        action(1)
        
        
        
def paper():
    if (game.get())=="ON":
        User.config(image=Paper)
        action(2)

def scissor():
    if (game.get())=="ON":
        User.config(image=Scissor)
        action(3)


#GUI BASIC SETUP                      
root=Tk()
root.title("STONE,PAPER,SCISSOR - A WONDERFUL GAME")
root.geometry("1150x600")
root.resizable(0,0)
root.config(bg="Light Blue")

#Variable declarations
marks=IntVar()
marks.initialize(0)
cmarks=IntVar()
cmarks.initialize(0)
game=StringVar()
game.initialize("OFF")

#CREATING PHOTOIMAGE OBJECTS
Stone=PhotoImage(file="stone.png")
Paper=PhotoImage(file="paper.png")
Scissor=PhotoImage(file="scissor.png")
computerImg=PhotoImage(file="computer.png")
vs=PhotoImage(file="vs.png")
userImg=PhotoImage(file="user.png")

#Extra GUI Setup
Heading = Label(root,bg="Light Blue",font=("Monotype Corsiva",27),text="                                           Let's Play !!")
Heading.grid(row=1,columnspan=3)
Computer = Label(root,image=computerImg,bg="Light Blue")
Computer.grid(row=2,column=1,rowspan=3)
Vs = Label(root,image=vs,bg="Light Blue")
Vs.grid(row=2,column=2,rowspan=3)
User = Label(root,image=userImg,bg="Light Blue")
User.grid(row=2,rowspan=3,column=3)

cname = Label(root,text="COMPUTER",bg="Light Blue",font=("Monotype Corsiva",16))
cname.grid(row=5,column=1)
uname = Label(root,text="YOU",bg="Light Blue",font=("Monotype Corsiva",16))
uname.grid(row=5,column=3)

stnbut = Button(root,text="Stone",command=stone,bg="Light Blue",state=DISABLED,font=("Monotype Corsiva",16))
stnbut.grid(row=2,column=4)
papbut = Button(root,text="Paper",command=paper,bg="Light Blue",state=DISABLED,font=("Monotype Corsiva",16))
papbut.grid(row=3,column=4)
scibut = Button(root,text="Scissor",command=scissor,bg="Light Blue",state=DISABLED,font=("Monotype Corsiva",16))
scibut.grid(row=4,column=4)


plbut = Button(root,text="START THE GAME",command=start,bg="Light Blue",font=("Monotype Corsiva",16))
plbut.grid(row=6,column=2)
root.mainloop()
