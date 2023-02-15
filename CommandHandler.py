# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 11:03:13 2023

@author: ellio
"""

import json, os

with open(os.path.join("systemAddresses.json"), 'r+') as file:
    systemAddresses = json.load(file)

def valveControl(valveName, arg):
    address = systemAddresses[valveName]
    #function creates valve command packet and sends it
    
def engineIgnition():
    #function commands the ignition of the ignition motor