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
#print(h.get_input_report(100,100))
#h.close()


while True:
    time.sleep(1)
    print(h.read(100, 1))