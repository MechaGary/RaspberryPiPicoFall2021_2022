from machine import Pin, ADC
import utime

PotWiperCounts=ADC(Pin(26))

while True:
    print(PotWiperCounts.read_u16())
    utime.sleep(.5)