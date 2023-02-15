# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 21:21:43 2023

@author: ellio
"""

import CommandHandler as command
import time

def engineFire():
    command.valveControl('mainOxidiserValve', 180)
    command.valveControl('mainFuelValve', 180)
    time.sleep(300)
    command.engineIgnition()
    print('boom boom')
    
def engineStop():
    command.valveControl('mainOxidiserValve', 0)
    command.valveControl('mainFuelValve', 0)
    print('no boom boom')