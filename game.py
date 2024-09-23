from tkinter import *
import random

window = Tk()

window.geometry("800x400")
window.title("Rock, Paper, Scissors")

Frame = Frame(window)
Frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

name = Label(Frame, text="Rock, Paper, Scissors - Player vc Computer", font = "100")
name.place(x=250, y=20)

label1 = Label(Frame, text="Player", font = "normal 15")

label2 = Label(Frame, text="vs", font = "normal 15")

label3 = Label(Frame, text="Computer", font = "normal 15")

label1.place(x=80, y = 50, width=100)
label2.place(x=350, y = 50, width=100)
label3.place(x=600, y = 50, width=100)

rock_png = PhotoImage(file="rock.png")
paper_png = PhotoImage(file="paper.png")
scissors_png = PhotoImage(file="scissors.png")

rock_png = rock_png.subsample(4, 4)
paper_png = paper_png.subsample(4, 4)
scissors_png = scissors_png.subsample(4, 4)

user_img = Label(Frame, image= "")
user_img.place(x=80, y=100)

comp_img = Label(Frame, image= "")
comp_img.place(x=600, y=100)

label4 = Label(Frame, text="", font="normal 20", width=15, borderwidth=2, relief="solid")
label4.place(x=275, y=250)


def Rock():
    user = "Rock"
    computer = random.choice(["Rock", "Paper", "Scissors"])
    user_img.configure(image=rock_png)
    if user == computer:
        label4.configure(text="Tie")
        comp_img.configure(image=rock_png)
    elif computer == "Paper":
        label4.configure(text="Computer Wins")
        comp_img.configure(image=paper_png)
    else:
        label4.configure(text="U Win!")
        comp_img.configure(image=scissors_png)

b1 = Button(Frame, text="Rock", font="10", width=20, command=Rock)
b1.place(x=100, y=300)

def Paper():
    user = "Paper"
    computer = random.choice(["Rock", "Paper", "Scissors"])
    user_img.configure(image=paper_png)
    if user == computer:
        label4.configure(text="Tie")
        comp_img.configure(image=paper_png)
    elif computer == "Scissors":
        label4.configure(text="Computer Wins")
        comp_img.configure(image=scissors_png)
    else:
        label4.configure(text="U Win!")
        comp_img.configure(image=rock_png)

b2 = Button(Frame, text="Paper", font="10", width=20, command=Paper)
b2.place(x=300, y=300)

def Scissors():
    user = "Scissors"
    computer = random.choice(["Rock", "Paper", "Scissors"])
    user_img.configure(image=scissors_png)
    if user == computer:
        label4.configure(text="Tie")
        comp_img.configure(image=scissors_png)
    elif computer == "Rock":
        label4.configure(text="Computer Wins")
        comp_img.configure(image=rock_png)
    else:
        label4.configure(text="U Win!")
        comp_img.configure(image=paper_png)

b3 = Button(Frame, text="Scissors", font="10", width=20, command=Scissors)
b3.place(x=500, y=300)

window.mainloop()