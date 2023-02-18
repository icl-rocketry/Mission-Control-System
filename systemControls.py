# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 21:21:43 2023

@author: ellio
"""

import functions as command
import time

#---------------------Read Me---------------------------#

#controls are broken down in this file
#subprocesses are executed by the functions.py
#these processes should check that the function has been successfully fulfilled (ie pressure checks)

#------------------Emergency Stop-----------------------#


def emergencyStop():
    command.valveControl('mainOxidiserValve', 0)
    command.valveControl('mainFuelValve', 0)
    command.valveControl('oxidiserVentValve', 0)
    command.valveControl('fuelVentValve', 0)
    command.valveControl('nitrogenVentValve', 0)
    command.valveControl('nitrogenFillValve', 0)
    command.valveControl('oxidiserFillValve', 0)
    command.valveControl('nitrogenPressuriseValve', 0)


#------------------Engine Controls----------------------#


def engineFire():
    command.valveControl('mainOxidiserValve', 90)
    command.valveControl('mainFuelValve', 90)
    time.sleep(0.3)
    command.engineIgnition()
    time.sleep(0.2)
    command.valveControl('mainOxidiserValve', 180)
    command.valveControl('mainFuelValve', 180)
    print('boom boom')
    
def engineStop():
    command.valveControl('mainOxidiserValve', 0)
    command.valveControl('mainFuelValve', 0)
    print('no boom boom')


#------------------Oxidiser Valves----------------------#

    
def oxidiserFillOpen():
    command.valveControl('oxidiserFillValve', 180)
    
def oxidiserFillClose():
    command.valveControl('oxidiserFillValve', 0)
    
def oxidiserVentOpen():
    command.valveControl('oxidiserVentValve', 180)

def oxidiserVentSlow():
    command.valveControl('oxidiserVentValve', 90)

def oxidiserVentClose():
    command.valveControl('oxidiserVentValve', 0)
    
    
#---------------------Fuel Valves-----------------------#


def fuelVentOpen():
    command.valveControl('fuelVentValve', 180)

def fuelVentSlow():
    command.valveControl('fuelVentValve', 90)

def fuelVentClose():
    command.valveControl('fuelVentValve', 0)


#------------------Nitrogen Valves----------------------#

def nitogenFillOpen():
    command.valveControl('nitrogenFillValve', 180)
    
def nitogenFillClose():
    command.valveControl('nitrogenFillValve', 0)
   
def propellantPressuriseValveOpen():
    command.valveControl('nitrogenPressuriseValve', 180)
    
def propellantPressuriseValveClose():
    command.valveControl('nitrogenPressuriseValve', 0)
    
def nitrogenVentOpen():
    command.valveControl('nitrogenVentValve', 180)

def nitrogenVentSlow():
    command.valveControl('nitrogenVentValve', 90)

def nitrogenVentClose():
    command.valveControl('nitrogenVentValve', 0)