from tkinter import *
import tkinter as tk
import random
from functools import partial
win=0
tie=0
lost=0
play=0
bwin=0
blost=0

#make picture popup, which shows who won!  
#Functions/Tasks
def main():
    bot = ("Rock","Paper","Scissors","Spock","Lizard")
    def close():
        window.destroy()

    def click1():
        global bwin
        global blost
        global win
        global lost
        global tie
        global play
        botChoice=random.choice(bot)
        user=(lb1.configure(text="Rock"))
        user="Rock"
        if(user==botChoice):
            outcome.configure(text="You Tied!")
            final.configure(text="You both chose Rock")
            tie=tie+1
            play=play+1
        elif(botChoice=="Paper"):
            outcome.configure(text="You Lost!")
            final.configure(text="Rock is covered by Paper")
            lost=lost+1
            play=play+1
            bwin=bwin+1
        elif(botChoice=="Scissors"):
            outcome.configure(text="You Won!")
            final.configure(text="Rock Crushes Scissors")
            win=win+1
            play=play+1
            blost=blost+1
        elif(botChoice=="Lizard"):
            outcome.configure(text="You Won!")
            final.configure(text="Rock Crushes Lizard")
            win=win+1
            play=play+1
            blost=blost+1
        elif (botChoice=="Spock"):
            lost=lost+1
            play=play+1
            bwin=bwin+1
            outcome.configure(text="You Lost!")
            final.configure(text= "Rock is vapourised by Spock")

        win2.configure(text=win)
        lost2.configure(text=lost)
        tie2.configure(text=tie)
        play2.configure(text=play)
        winn1.configure(text=bwin)
        lostt1.configure(text=blost)
    
            
    def click2():
        global bwin
        global blost
        global win
        global lost
        global tie
        global play
        botChoice=random.choice(bot)
        user=lb2.configure(text="Paper")
        user="Paper"
        if(user==botChoice):
            outcome.configure(text="You Tied!")
            final.configure(text="You both chose Paper")
            tie=tie+1
            play=play+1
        elif(botChoice=="Rock"):
            outcome.configure(text="You Won!")
            final.configure(text="Paper covers Rock")
            win=win+1
            play=play+1
            blost1=blost+1
        elif(botChoice=="Scissors"):
            outcome.configure(text="You Lost!")
            final.configure(text= "Paper is cut by Scissors")
            lost=lost+1
            play=play+1
            bwin=bwin+1
        elif(botChoice=="Lizard"):
            outcome.configure(text="You Lost!")
            final.configure(text="Lizard eats paper")
            lost=lost+1
            play=play+1
            bwin=bwin+1
        elif (botChoice=="Spock"):
            outcome.configure(text="You Won!")
            final.configure(text="Paper disaproves Spock")
            win=win+1
            play=play+1
            blost=blost+1
            
        win2.configure(text=win)
        lost2.configure(text=lost)
        tie2.configure(text=tie)
        play2.configure(text=play)
        winn1.configure(text=bwin)
        lostt1.configure(text=blost)
    
        
    def click3():
        global bwin
        global blost
        global win
        global lost
        global tie
        global play
        botChoice=random.choice(bot)
        user=lb3.configure(text="Scissors")
        user="Scissors"
        if(user==botChoice):
            outcome.configure(text="You Tied!")
            final.configure(text="You both chose Scissors")
            tie=tie+1
            play=play+1
        elif(botChoice=="Rock"):
            outcome.configure(text="You Lost!")
            final.configure(text="Rock crushes Scissors")
            lost=lost+1
            play=play+1
            bwin=bwin+1
        elif(botChoice=="Paper"):
            outcome.configure(text="You Won!")
            final.configure(text="Scissors cuts Paper")
            win=win+1
            play=play+1
            blost=blost+1
        elif(botChoice=="Lizard"):
            outcome.configure(text="You Won!")
            final.configure(text="Scissors decapitates Lizard")
            win=win+1
            play=play+1
            blost=blost+1
        elif (botChoice=="Spock"):
            outcome.configure(text="You Lost!")
            final.configure(text="Spock smashed Scissors")
            lost=lost+1
            play=play+1
            bwin=bwin+1
            
        win2.configure(text=win)
        lost2.configure(text=lost)
        tie2.configure(text=tie)
        play2.configure(text=play)
        winn1.configure(text=bwin)
        lostt1.configure(text=blost)

    
    def click4():
        global bwin
        global blost
        global win
        global lost
        global tie
        global play
        botChoice=random.choice(bot)
        user=lb4.configure(text="Spock")
        user="Spock"
        if(user==botChoice):
            outcome.configure(text="You Tied!")
            final.configure(text="You both chose spock")
            tie=tie+1
            play=play+1
        elif(botChoice=="Rock"):
            outcome.configure(text="You Won!")
            final.configure(text="Spock vapourises Rock ")
            win=win+1
            play=play+1
            blost=blost+1
        elif(botChoice=="Paper"):
            outcome.configure(text="You Lost!")
            final.configure(text="Paper disproves Spock")
            lost=lost+1
            play=play+1
            bwin=bwin+1
        elif(botChoice=="Lizard"):
            outcome.configure(text="You Lost!")
            final.configure(text="Lizard poisons Spock")
            lost=lost+1
            play=play+1
            bwin=bwin+1
        elif (botChoice=="Scissors"):
            outcome.configure(text="You Won!")
            final.configure(text="Spock smashes Scissors")
            win=win+1
            play=play+1
            blost=blost+1
            
        win2.configure(text=win)
        lost2.configure(text=lost)
        tie2.configure(text=tie)             
        play2.configure(text=play)
        winn1.configure(text=bwin)
        lostt1.configure(text=blost)
    

    def click5():
        global bwin
        global blost
        global win
        global lost
        global tie
        global play
        botChoice=random.choice(bot)
        user=lb5.configure(text="Lizard")
        user="Lizard"
        if(user==botChoice):
            outcome.configure(text="You Tied!")
            final.configure(text="You both chose Lizard")
            tie=tie+1
            play=play+1
        elif(botChoice=="Rock"):
            outcome.configure(text="You Lost!")
            final.configure(text="Rock crushed Lizard")
            lost=lost+1
            play=play+1
            bwin=bwin+1
        elif(botChoice=="Paper"):
            outcome.configure(text="You Won!")
            final.configure(text="Lizard eats Paper")
            win=win+1
            play=play+1
            blost=blost+1
        elif(botChoice=="Scissors"):
            outcome.configure(text="You Lost!")
            final.configure(text="Scissors decapitates Lizard")
            lost=lost+1
            bwin=bwin+1
        elif (botChoice=="Spock"):
            outcome.configure(text="You Won!")
            final.configure(text="Lizard poisons Spock")
            win=win+1
            play=play+1
            blost=blost+1

        win2.configure(text=win)
        lost2.configure(text=lost)
        tie2.configure(text=tie)
        play2.configure(text=play)
        winn1.configure(text=bwin)
        lostt1.configure(text=blost)
            
       

        
#window
    window=Tk()
    window.title("Magic Games")
    window.geometry("1000x1000")
    window.configure(bg="white")
#pictures
    img1=PhotoImage(file='rock1.png')
    img2=PhotoImage(file='paper2.png')
    img3=PhotoImage(file='scissors.png')
    img4=PhotoImage(file='spock.png')
    img5=PhotoImage(file='lizard.png')
    
#buttons/labels/grid
    
#wins    
    win1= Label(text="Wins:",font=("Arial bold",30),bg="white",fg="green1")
    win1.place(y=300,x=850)
    win2= Label(text= win , font=("Arial bold",30),bg="white",fg="green")
    win2.place(y=302,x=985)
    
    winn= Label(text="Wins:",font=("Arial bold",30),bg="white",fg="green1")
    winn.place(y=460,x=850)
    winn1= Label(text= win , font=("Arial bold",30),bg="white",fg="green")
    winn1.place(y=462,x=985)
#loses 
    lost1= Label(text="Loses:", font=("Arial bold",30),bg="white",fg="red3")
    lost1.place(y=350,x=850)
    lost2= Label(text= lost,font=("Arial bold",30),bg="white",fg="red")
    lost2.place(y=352,x=985)

    lostt= Label(text="Loses:", font=("Arial bold",30),bg="white",fg="red3")
    lostt.place(y=510,x=850)
    lostt1= Label(text= lost,font=("Arial bold",30),bg="white",fg="red")
    lostt1.place(y=512,x=985)
#ties 
    tie1=Label(text="Ties:", font=("Arial bold",30),bg="white",fg="grey")
    tie1.place(y=605,x=850)
    tie2=Label(text= tie,font=("Arial bold",30),bg="white",fg="darkgrey") 
    tie2.place(y=607,x=985)
    
#plays
    play1=Label(text="Plays:",font=("Arial bold",30),bg="white",fg="steelblue1")
    play1.place(y=655,x=850)
    play2=Label(text= play,font=("Arial bold",30),bg="white",fg="PaleTurquoise3") 
    play2.place(y=657,x=985)
    
#label for score
    score=Label(text="Player Score",font=("Arial bold",40),bg="white",fg="black")
    score.place(y=240,x=800)

    score1=Label(text="Computer Score",font=("Arial bold",40),bg="white",fg="black")
    score1.place(y=400,x=800)

#button/label for rock
    bttn1=Button(window,fg="white",bg="coral1",image=img1,command= click1)
    bttn1.grid(row=0, column=1)
    lb1=Label(window,fg="black",bg="white",  text="Rock",font=("Arial",15))
    lb1.grid(row=1,column=1)

#button/label for paper
    bttn2=Button(window,fg="white",bg="coral1",image=img2,command= click2)
    bttn2.grid(row=0, column=2)
    lb2=Label(window,fg="black", bg="white", text="Paper",font=("Arial",15))
    lb2.grid(row=1,column=2)
    
#button/label for scissors
    bttn3=Button(window,fg="white", bg="coral1",image=img3,command=click3)
    bttn3.grid(row=0, column=3)
    lb3=Label(window,fg="black",bg="white",  text="Scissors",font=("Arial",15))
    lb3.grid(row=1,column=3)

#button/label for spock
    bttn4=Button(window,fg="white",bg="coral1", image=img4,command=click4)
    bttn4.grid(row=0, column=4)
    lb4=Label(window,fg="black",bg="white",  text="Spock",font=("Arial",15))
    lb4.grid(row=1,column=4)
    
#button/label for lizard
    bttn5=Button(window,fg="white",bg="coral1", image=img5,command=click5)
    bttn5.grid(row=0, column=5)
    lb5=Label(window,fg="black",bg="white", text="Lizard",font=("Arial",15))
    lb5.grid(row=1,column=5)
    
#label for what the computer chose
    final=Label(window,fg="black",bg="white",font=("Arial bold",40))
    final.place(y=400 ,x=50)
    
#label for if you won,lost or tied   
    outcome=Label(window,fg="black",bg="white",font=("Arial bold",70))
    outcome.place(y=275,x=120)
    
#button/label for exit button
    quit = Button(text="EXIT",fg="red", command= close,font=("Arial Bold",50))    
    quit.place(relx=1.0, rely=1.0, anchor='se')

  
    window.mainloop()


main()
