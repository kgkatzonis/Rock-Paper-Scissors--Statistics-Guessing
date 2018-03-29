# -*- coding: utf-8 -*-
"""
Rock Paper Scissors with statistic probability guessing 
Written by Konstantinos Gkatzonis
"""
import random as rnd
from tkinter import *

logic = [[1,1,1],[1,1,1],[1,1,1]] #Three different statistic sets: rock = 0
                                       #Paper = 1 and Scisors = 2

global score
score = 0    #Player Score variable
prevai = rnd.randint(0,2)
def new():
    global prevai
    global score
    global game
    game = Toplevel()
    Complab = Label(game, text = "Computer:").grid(row = 0, column = 0)
    Complab = Label(game, text = "Score:").grid(row = 0, column = 1)

    Comp = Label(game, text = "-").grid(row = 1, column = 0)
    Score = Label(game, text = score).grid(row = 1, column = 1)

    r = Button(game, text = "Rock", command = lambda *args: AI(0)).grid(row = 2,column = 0)   #Rock button
    p = Button(game, text = "Paper", command = lambda *args: AI(1)).grid(row = 2,column = 1)  #Paper button
    s = Button(game, text = "Scissors", command = lambda *args: AI(2)).grid(row = 2,column = 2)   #Scissors button
    game.mainloop()
    
def des():
    top.destroy()

def AI(answ):
    global score
    global prevai
    global game
    maxnum = logic[prevai][0] + logic[prevai][1] + logic[prevai][2] #Sets the max random number to the sum of all the players answers in the logic[prevai] space
    pick = rnd.randint(0,maxnum)    
    logic[prevai][answ] = logic[prevai][answ] + 1 #I placed the readjustment line here to make it more fair for the player.
                                                #Instead of increasing the probability of him losing when he enters his move, the program takes his input into account after it has made its guess
    
    if (pick <= logic[prevai][0]):    #Prediction guesses that the player will play rock
        Comp = Label(game, text = "Paper").grid(row = 1, column = 0)
        prevai = 1
    elif(pick >= logic[prevai][0] and pick <= logic[prevai][0]+logic[prevai][1]): #Prediction guesses that the player will play paper
        Comp = Label(game, text = "Scissors").grid(row = 1, column = 0)
        prevai = 2
    else:
        Comp = Label(game, text = "Rock").grid(row = 1, column = 0)   #Prediction guesses that the player will play scissors
        prevai = 0
    if((prevai == 0 and answ == 2) or (prevai == 1 and answ == 0) or (prevai == 2 and answ == 1)):
        score = score - 1
        Score = Label(game, text = score).grid(row = 1, column = 1)
    if((prevai == 2 and answ == 0) or (prevai == 0 and answ == 1) or (prevai == 1 and answ == 2)):
        score = score + 1
        Score = Label(game, text = score).grid(row = 1, column = 1)
    if(score == 5 or score == -5):
        game.destroy()
        score = 0

top = Tk()


n = Button(top, text = "New Game", command = new).pack()
q = Button(top, text = "Quit", command = des).pack()

top.mainloop()
