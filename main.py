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

import time
import hid


h = hid.device()
h.open(0x1dd2, 0x2010)

button_array = [1,1,2,3,5,8,1,3]

# button_bitfield = sum([(value << (8*index)) for index,value in enumerate(button_array) if index < 8])
# print(button_bitfield)
# print("{0:b}".format(button_bitfield))
# #check if button 8 is pressed
# button_id = 8
# print(button_bitfield & (1<<button_id))
# print(bool(button_bitfield & (1<<button_id)))
# print("{0:b}".format(button_bitfield& (1<< button_id)))

def check_buttons(buttons_to_check,button_array) -> bool:
    #generate button bitfield
    button_bitfield:int = sum([(value << (8*index)) for index,value in enumerate(button_array) if index < 8])

    result = 1
    #convert single int to list with single element
    if type(buttons_to_check) is int:
        buttons_to_check = [buttons_to_check]
    
    for button in buttons_to_check:
        result *= button_bitfield & (1<<button)
    return bool(result)


while True:
    time.sleep(1)
    x = h.read(100, 1)
    print(check_buttons(x[0], [1]))


