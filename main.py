# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 20:17:03 2023

@author: ellio
"""

################### TO DO LIST ######################
# Figure out how to send commands on RNP
# Get an actual switch rather than using a knife
# Figure out a system overview
# Steal a board and a valve to practice with




import pygame
import json, os
import systemControls
import time
import numpy as np



pygame.init()
joysticks = []
for i in range(pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
for joystick in joysticks:
    joystick.init()

with open(os.path.join("buttons.json"), 'r+') as file:
    button_keys = json.load(file)
    
previousPressTime = np.zeros(64)
standardButtonPressDelay = 0.3

def timeCheck(prev_time, delay):
    if (time.time()*1000 - prev_time) <= delay:
        return 0
    else:
        return 1



while True:
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == button_keys['B-1']:
                if timeCheck(previousPressTime[0], 1) == 1:
                    systemControls.engineFire()
                else:
                    continue
            if event.button == button_keys['B-2']:
                if timeCheck(previousPressTime[0], standardButtonPressDelay) == 1:
                    print('B_2 Pressed')
                else:
                    continue
            if event.button == button_keys['B-3']:
                print('B_3 Pressed')
        if event.type == pygame.JOYBUTTONUP:
            if event.button == button_keys['B-1']:
                systemControls.engineStop()
                
                

