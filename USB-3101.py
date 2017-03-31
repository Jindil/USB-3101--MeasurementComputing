# -*- coding: utf-8 -*-
"""
This code allows to apply a given voltage to an analog output channel between 0 and 5V with a USB-3101 from Measurement Computing
as well as to apply digital signals (0/+5V) on individual or all digital output channels. 
For the analog output, the code can be modified to deliver a voltage between -10 to 10V.
WARNING : The parameter gain seems to be overwritten by the configuration defined in InstaCal, the default software to test the USB device
Also the BoardNum can be read from InstaCal  
UL.cbVOut(BoardNum,Channel,Gain,5) is not possible with USB-3101
Use cbAOut instead in combination with cbFromEngUnits for conversion Volt to Bytes

tested on Python 2.7 64-bit on a windows machine
"""

import UniversalLibrary as UL # using source code from user u55 on github for python 3/64-bit compatibility

BoardNum     = 1 # refer to the number defined in InstaCal
List_VChan   = [VChan0,VChan1,VChan2,VChan3] = [i for i in range(4)] # 4 analog outputs
List_BitChan = [BitChan0,BitChan1,BitChan2,BitChan3,BitChan4,BitChan5,BitChan6,BitChan7] = [i for i in range(8)] # 8 digital in/output
Gain         = UL.BIP10VOLTS # Bilateral allows to do -10 to 10 V (check with instancal that seems to overwrite this parameter)
PortType     = UL.AUXPORT # default for USB-3101
PortNum      = UL.AUXPORT 


def SetBitOn(BitChanX):
    '''Set a digital channel to 5V output'''
    UL.cbDConfigBit(BoardNum,PortType,BitChanX,UL.DIGITALOUT) # necessary otherwise setting voltage directly does not work
    #Syntax : int cbDConfigBit(int BoardNum, int PortType, int BitNum, int Direction) 
    UL.cbDBitOut(BoardNum,PortType,BitChanX,1)
    #int cbDBitOut(int BoardNum, int PortType, int BitNum, unsigned short BitValue) 


def SetBitOff(BitChanX):
    '''Set a digital channel to 0V output'''
    UL.cbDConfigBit(BoardNum,PortType,BitChanX,UL.DIGITALOUT) # necessary otherwise setting voltage directly does not work
    #Syntax : int cbDConfigBit(int BoardNum, int PortType, int BitNum, int Direction) 
    UL.cbDBitOut(BoardNum,PortType,BitChanX,1)
    #Syntax : int cbDBitOut(int BoardNum, int PortType, int BitNum, unsigned short BitValue)
    

def SetPower(VChanX,Percent):
    '''Set modulation voltage in % from 0 to 5V on a given channel - 100% = 5V'''
    Vout = UL.cbFromEngUnits(BoardNum,Gain, 5 * Percent/100 ,0) # convert from % to volt, and from volt to bytes
    UL.cbAOut(BoardNum,VChanX,Gain,Vout) 


def Reset():
    '''Set all digital channels (the entire port) to 0V output'''
    UL.cbDConfigPort (BoardNum, PortNum, UL.DIGITALOUT)
    UL.cbDOut(BoardNum, PortNum,0)