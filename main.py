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

import hid

try:
    print("Opening the device")

    h = hid.device()
    h.open(0x1dd2, 0x2010)  # TREZOR VendorID/ProductID

    print("Feature Report: %s" % h.read(100, 1))
    print("Closing the device")
    h.close()

except IOError as ex:
    print(ex)
    print("You probably don't have the hard-coded device.")
    print("Update the h.open() line in this script with the one")
    print("from the enumeration list output above and try again.")

print("Done")  

