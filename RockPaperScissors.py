# -*- coding: utf-8 -*-
"""
Spyder Editor

Rock Paper Scissors program
Written by Konstantinos Gkatzonis
"""
import random as rnd
from tkinter import *

logic = [[1,1,1],[1,1,1],[1,1,1]] #Three different statistic sets: rock = 0
                                       #Paper = 1 and Scisors = 2
global score
score = 0    #Player Score variable
prevai = rnd.randint(0,2)
def AI(answ):
    global score
    global prevai
    maxnum = logic[prevai][0] + logic[prevai][1] + logic[prevai][2] #Sets the max random number to the sum of all the players answers in the logic[prevai] space
    pick = rnd.randint(0,maxnum)    
    logic[prevai][answ] = logic[prev][answ] + 1 #I placed the readjustment line here to make it more fair for the player.
                                                #Instead of increasing the probability of him losing when he enters his move, the program takes his input into account after it has made its guess
    
    if (pick <= logic[prevai][0]):    #Prediction guesses that the player will play rock
        Comp = Label(text = "Paper").grid(row = 1, column = 0)
        prevai = 1
    elif(pick >= logic[prevai][0] and pick <= logic[prevai][0]+logic[prevai][1]): #Prediction guesses that the player will play paper
        Comp = Label(text = "Scissors").grid(row = 1, column = 0)
        prevai = 2
    else:
        Comp = Label(text = "Rock").grid(row = 1, column = 0)   #Prediction guesses that the player will play scissors
        prevai = 0
    if((prevai == 0 and answ == 2) or (prevai == 1 and answ == 0) or (prevai == 2 and answ == 1)):
        score = score - 10
        Score = Label(text = score).grid(row = 1, column = 1)
    if((prevai == 2 and answ == 0) or (prevai == 0 and answ == 1) or (prevai == 1 and answ == 2)):
        score = score + 10
        Score = Label(text = score).grid(row = 1, column = 1)

top = Tk()

Complab = Label(text = "Computer:").grid(row = 0, column = 0)
Complab = Label(text = "Score:").grid(row = 0, column = 1)

Comp = Label(text = "-").grid(row = 1, column = 0)
Score = Label(text = score).grid(row = 1, column = 1)

r = Button(text = "Rock", command = lambda *args: AI(0)).grid(row = 2,column = 0)   #Rock button
p = Button(text = "Paper", command = lambda *args: AI(1)).grid(row = 2,column = 1)  #Paper button
s = Button(text = "Scissors", command = lambda *args: AI(2)).grid(row = 2,column = 2)   #Scissors button

top.mainloop()