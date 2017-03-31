# USB-3101--MeasurementComputing
Simple Python script to control analog and digital outputs for a USB-3101 from Measurement Computing 

This code allows to apply a given voltage to an analog output channel between 0 and 5V as well as to apply digital signals (0/+5V) on individual or all digital output channels. 
For the analog output, the code can be modified to deliver a voltage between -10 to 10V.
WARNING : The parameter gain seems to be overwritten by the configuration defined in InstaCal (the default software to test the USB device)
Also the BoardNum should be read from InstaCal
UL.cbVOut(BoardNum,Channel,Gain,5) is not supported by the USB-3101.
Use UL.cbAOut instead in combination with cbFromEngUnits for conversion Volt to Bytes.

tested on Python 2.7 64-bit on a windows machine
