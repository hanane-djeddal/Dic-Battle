#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 20:09:03 2019

@author: h_djeddal
"""
from tkinter import * 


#============== Contre Ordinateur
N=20
inst="TRY TO REACH "+str(N)+" POINTS FIRST!" 
score='0'
score_comp='0'
result='0'
d = StringVar(Agent_Frame, "1")
d2=1
comp_dice="Your Turn"
fenetre = Tk()
fenetre.geometry('450x400')
fenetre.title('DICE BATTLE')

Setting_Frame = Frame(fenetre, borderwidth=1, relief=GROOVE)
Setting_Frame.pack(side=BOTTOM, padx=1, pady=1)

BoutonRestart = Button(Setting_Frame, text ='Restart', command = fenetre.destroy)
BoutonRestart.pack(side = LEFT, padx = 80, pady = 5)

BoutonQuitter = Button(Setting_Frame, text ='Quit', command = fenetre.destroy)
BoutonQuitter.pack(side = RIGHT, padx = 70, pady = 5)



Head_Frame=Frame(fenetre, width=440, height=350,borderwidth=1, relief=GROOVE)
Head_Frame.pack(side=TOP, padx=1, pady=1)

Label(Head_Frame,text=inst).pack(side=TOP,padx=5,pady=5)

Score_Frame=Frame(Head_Frame, borderwidth=1)
Score_Frame.pack(side=TOP, padx=1, pady=1)

AgentScore_Frame=Frame(Score_Frame, borderwidth=1)
AgentScore_Frame.pack(side=LEFT, padx=50, pady=1)
Label(AgentScore_Frame,text="SCORE : ").pack(side=LEFT,padx=5,pady=5)
Label(AgentScore_Frame,text=score).pack(side=LEFT,padx=5,pady=5)

CompScore_Frame=Frame(Score_Frame, borderwidth=1)
CompScore_Frame.pack(side=RIGHT, padx=40, pady=1)
Label(CompScore_Frame,text=score_comp).pack(side=RIGHT,padx=5,pady=5)
Label(CompScore_Frame,text="COMPUTER SCORE : ").pack(side=RIGHT,padx=5,pady=5)


Control_Frame=Frame(fenetre, width=440, height=350,borderwidth=0, relief=GROOVE)
Control_Frame.pack(side=TOP, padx=1, pady=1)
Label(Control_Frame,text=result).pack(side=RIGHT,padx=5,pady=5)
Label(Control_Frame,text="Result : ").pack(side=RIGHT,padx=5,pady=5)
BoutonLancer = Button(Control_Frame, text ='Throw', command = fenetre.destroy)
BoutonLancer.pack(side = LEFT, padx = 60, pady = 5)

Game_Frame=Frame(fenetre, width=440, height=350,borderwidth=0, relief=GROOVE)
Game_Frame.pack(side=LEFT, padx=5, pady=5)
Agent_Frame=Frame(Game_Frame, width=440, height=350,borderwidth=1, relief=GROOVE)
Agent_Frame.pack(side=LEFT, padx=1, pady=1)
Label(Agent_Frame,text="Choose your dice").pack(side=TOP,padx=5,pady=5)

dice = {"1 Dices" : "1", 
          "2 Dice" : "2", 
          "3 Dice" : "3", 
          "4 Dice" : "4", 
          "5 Dice" : "5"} 

for (text, value) in dice.items(): 
    Radiobutton(Agent_Frame, text = text, variable = d,  value = value).pack(side=TOP,ipadx=5, ipady=5)
Computer_Frame=Frame(Game_Frame, width=440, height=350,borderwidth=0, relief=GROOVE)
Computer_Frame.pack(side=TOP, padx=120, pady=1)
Label(Computer_Frame,text=comp_dice).pack(side=TOP,padx=1,pady=1)
fenetre.mainloop()
