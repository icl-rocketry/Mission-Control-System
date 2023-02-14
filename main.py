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
import EngineControls

pygame.init()
joysticks = []
for i in range(pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
for joystick in joysticks:
    joystick.init()

with open(os.path.join("buttons.json"), 'r+') as file:
    button_keys = json.load(file)
    
    

while True:
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == button_keys['B-1']:
                EngineControls.engineFire()
            if event.button == button_keys['B-2']:
                print('B_2 Pressed')
            if event.button == button_keys['B-3']:
                print('B_3 Pressed')
        if event.type == pygame.JOYBUTTONUP:
            if event.button == button_keys['B-1']:
                EngineControls.engineStop()
                
                

