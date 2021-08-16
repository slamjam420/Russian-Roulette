# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 14:58:52 2021

@author: asus
"""

def end_death():
    return "you are dead !! thanks for playing"
def end_alive():
    return "congrats you won russian roulette"
import random
def RR():
    print("please enter 1 to load and shot the bullet")
    chance=int(input())
    LL=[0,0,0,0,0,1]
    if chance==1:
        shot=random.choice(LL)
        if shot==1:
            print(end_death())
        if shot==0:
            print(end_alive())       
RR()   
    