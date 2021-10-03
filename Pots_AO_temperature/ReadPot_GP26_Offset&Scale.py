from machine import Pin, ADC, PWM
import utime
#PWM1A=PWM(Pin(2)) # GP2  pin 4 
#PWM1A.freq(1000)


PotWiperCounts=ADC(Pin(26)) # can also call machine.ADC(3) 
GP2OFFSET=288  # The PotWiperCounts when the pot is full CCW
GP2GAIN=1.004 # GP2 read 65535 at full cw, however once 288 counts are
# subtracted from it, it needs multiplied by the ratio to make it back to 65535 full scale

while True:
    print(PotWiperCounts.read_u16())
    PotWiperCountsTUNED=((PotWiperCounts.read_u16())-GP2OFFSET)*GP2GAIN
    print("PotWiperCounts TUNED=", PotWiperCountsTUNED)
# BONUS POINTS ! How many volts is 30 counts of offset ?
# Hint 3.3V = 65535 counts . In reality the resolution is still 4096 12 bits
    utime.sleep(1)
#    print("Adjusted GP2 value is:", PotWiperCountsReal)
    
# MAKE a NOTE what the PotWiperCounts are at full CW - full up________
# MAKE a NOTE what the PotWiperCounts are at full CCW - full down________
# The value at full CCW should be zero. The value it really shows is called OFFSET !!
# The next program you will correct the OFFSET and then also the gain error - The value at full CW !