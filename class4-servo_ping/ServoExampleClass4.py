from machine import Pin, PWM
# Pin uses the GPIO value , not the actual pin number 
import utime

AliveLED = Pin(25,machine.Pin.OUT)
AliveLED.value(0)

servo = PWM(Pin(10))# physical pin14

servo.freq(50) # 50 Hz is 20 msec period
# 100% duty of PWM is 65535 counts
# 2 ms of 20 ms is 10% for full spd FWD 6553
# ( 1.5 ms / 20 ms ) * 65535 = 4875 for zero degrees
# 1 ms of 20 ms is full neg  3251 counts 

#AliveLED.value(1)
count=0 


while True:
    ServoDutyCounts=3250
    AliveLED.toggle()
    
    while True:
        AliveLED.toggle()
        ServoDutyCounts=ServoDutyCounts+25
        servo.duty_u16(ServoDutyCounts)
        utime.sleep(.03) # time to reach position
        if (ServoDutyCounts>6553):
            break
    ServoDutyCounts=6553
    
    while True:
        AliveLED.toggle()
        ServoDutyCounts=ServoDutyCounts-25
        servo.duty_u16(ServoDutyCounts)
        utime.sleep(.03) # time to reach position, remember duty cycle is 20 msec, so if write references faster than than, servo cant keep up
        if (ServoDutyCounts<3252):
            break    
 
# What happens of duty cycle in code exceeds servo spec
# There are 2 ways of make the servo swing faster. What are they ?         
        