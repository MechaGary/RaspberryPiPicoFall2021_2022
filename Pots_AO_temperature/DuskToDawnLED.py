from machine import Pin, ADC
import utime
#import constant  # wierd 

PotWiperCounts=ADC(Pin(26))
LDR_Counts=ADC(Pin(27))

u16_2_volts = 3.3/(65535)

DuskToDawnLED= Pin(25, machine.Pin.OUT)#GP25 is the Pico mounted LED
DuskToDawnLED.value(0)
    
LightOnAdjust=1.1 ## in volts at GPIO  

while True:
    #print(PotWiperCounts.read_u16())
    #print(LDR_Counts.read_u16())
    LDR_Volts=(LDR_Counts.read_u16())*u16_2_volts
    print(LDR_Volts)
    if ((LDR_Volts) < (LightOnAdjust)):
        DuskToDawnLED.value(1)
    else:
        DuskToDawnLED.value(0)
            
    utime.sleep(2)