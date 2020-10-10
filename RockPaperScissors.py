# -*- coding: utf-8 -*-
"""
Rock Paper Scissors with statistic probability guessing 
Written by Konstantinos Gkatzonis

Description:
    A rock-paper-scissors game that uses statistics to predict the winning move on each round
    judging from the player's response to what was played previously.
"""


import random as rnd
from tkinter import *

class gameAction(): # Class to distinguish between the different game actions and increase code readabiity
    Rock = 0
    Paper = 1
    Scissors = 2


logic = [[1,1,1],[1,1,1],[1,1,1]] #Three different statistic sets: 0 = Responses to rock, 1 = Responses to paper, 2 = Responses to scissors
score = 0    #Player Score variable
prevAI = -1 # Initialize the previous AI value to -1 so that the first round isn't logged (there's no previous round to go off of)
MAX_SCORE = 5 # Define maximum score

# This function is the main game loop. It creates and preserves the UI elements
def new():
    global gameUI
    global score
    global prevAI
    gameUI = Toplevel()
    compTextLabel = Label(gameUI, text = "Computer:").grid(row = 0, column = 0) # "Computer" label
    scoreTextLabel = Label(gameUI, text = "Score:").grid(row = 0, column = 1) # "Score" label

    compLabel = Label(gameUI, text = "-").grid(row = 1, column = 0)# Computer decision for this round text label
    scoreLabel = Label(gameUI, text = score).grid(row = 1, column = 1)# Current Score

    rButton = Button(gameUI, text = "Rock", command = lambda *args: AI(gameAction.Rock)).grid(row = 2,column = 0)   #Rock button
    pButton = Button(gameUI, text = "Paper", command = lambda *args: AI(gameAction.Paper)).grid(row = 2,column = 1)  #Paper button
    sButton = Button(gameUI, text = "Scissors", command = lambda *args: AI(gameAction.Scissors)).grid(row = 2,column = 2)   #Scissors button
    gameUI.mainloop()
    
def des():
    top.destroy()

def AI(answ):
    global gameUI
    global score
    global prevAI

    maxNum = logic[prevAI][gameAction.Rock] + logic[prevAI][1] + logic[prevAI][2] #Sets the max random number to the total number of player answers in the logic[prevAI] space
    randomPick = rnd.randint(0,maxNum)

    # Adjust logic table only if this is not the first round of the game (in which case there's no previous round to start with
    if (prevAI != -1):
        logic[prevAI][answ] = logic[prevAI][answ] + 1 # Adjust logic matrix to the player's new response
                                                      # I placed the readjustment line here to make it more fair for the player.
                                                      # Instead of increasing the probability of him losing when he enters his move, the program takes his input into account after it has made its guess

    # Declare AI action
    if (randomPick <= logic[prevAI][0]):    #Prediction guesses that the player will play rock
        compLabel = Label(gameUI, text = "Paper").grid(row = 1, column = 0) # The AI chooses paper to beat rock
        AIAction = gameAction.Paper
        
    elif(randomPick >= logic[prevAI][0] and randomPick <= logic[prevAI][0]+logic[prevAI][1]): #Prediction guesses that the player will play paper
        compLabel = Label(gameUI, text = "Scissors").grid(row = 1, column = 0)# The AI chooses scissors to beat paper
        AIAction = gameAction.Scissors
        
    else: # Prediction guesses that the player will play scissors
        compLabel = Label(gameUI, text = "Rock").grid(row = 1, column = 0) # The AI chooses rock to beat scissors
        AIAction = gameAction.Rock

    # Adjust score
    if((AIAction == gameAction.Rock and answ == gameAction.Scissors) or (AIAction == gameAction.Paper and answ == gameAction.Rock) or (AIAction == gameAction.Scissors and answ == gameAction.Paper)): 
        score = score - 1
        scoreLabel = Label(gameUI, text = score).grid(row = 1, column = 1)
        
    elif((AIAction == gameAction.Scissors and answ == gameAction.Rock) or (AIAction == gameAction.Rock and answ == gameAction.Paper) or (AIAction == gameAction.Paper and answ == gameAction.Scissors)):
        score = score + 1
        scoreLabel = Label(gameUI, text = score).grid(row = 1, column = 1)

    prevAI = AIAction # Set the previous action of the AI to the current action to prepare for the next round

    # Check for Game Over
    if(score == MAX_SCORE or score == -MAX_SCORE):
        gameUI.destroy()
        gameOverWindow = Toplevel()

        if (score == -5):
            compTextLabel = Label(gameOverWindow, text = "Game Over: Computer Wins").grid(row = 0, column = 0) # Computer Wins label
            
        else:
            compTextLabel = Label(gameOverWindow, text = "Game Over: Player Wins").grid(row = 0, column = 0) # Player Wins label
        
        score = 0 # Reset score
        gameOverWindow.mainloop()

# MAIN
top = Tk() # Main game loop


newButton = Button(top, text = "New Game", command = new).pack() # New game button
quitButton = Button(top, text = "Quit", command = des).pack() # Quit button

top.mainloop()
