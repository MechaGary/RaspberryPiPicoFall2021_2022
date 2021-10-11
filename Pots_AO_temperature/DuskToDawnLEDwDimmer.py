from machine import Pin, ADC, PWM
import utime
#import constant  # wierd 

PotWiperCounts=ADC(Pin(26))
LDR_Counts=ADC(Pin(27))

u16_to_volts = 3.3/(65535)
#volts_2_U16 = (65535)/3.3

# DuskToDawnLED= Pin(25, machine.Pin.OUT)#GP25 is the Pico mounted LED
# DuskToDawnLED.value(0)
DuskToDawnLED= PWM(Pin(2))# physical pin 4    
DuskToDawnLED.freq(100)

LightOnAdjust=1.5 ## in volts at GPIO  
# volts_to_U16 = (65535)/LightOnAdjust


volts_to_U16 = (65535)/LightOnAdjust

while True:
    #print(PotWiperCounts.read_u16())
    #print(LDR_Counts.read_u16())
    LDR_Volts=(LDR_Counts.read_u16())*u16_to_volts
    print(LDR_Volts)
    if ((LDR_Volts) < (LightOnAdjust)):   ## floating point value of volts
        DimmerDutyCounts=65535
    if ((LDR_Volts) < ((LightOnAdjust)*.8)):   ## floating point value of volts
        DimmerDutyCounts=52400
    if ((LDR_Volts) < ((LightOnAdjust)*.6)):   ## floating point value of volts
        DimmerDutyCounts=39000
    if ((LDR_Volts) < ((LightOnAdjust)*.4)):   ## floating point value of volts
        DimmerDutyCounts=26200
    if ((LDR_Volts) < ((LightOnAdjust)*.2)):   ## floating point value of volts
        DimmerDutyCounts=13000
    if ((LDR_Volts) > ((LightOnAdjust))):   ## floating point value of volts
        DimmerDutyCounts=0        
    DuskToDawnLED.duty_u16(DimmerDutyCounts) 
            
    utime.sleep(2)