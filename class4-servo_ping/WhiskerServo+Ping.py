# This code has the BeetleBot run FWD at top spped.
# If the LHS side whisker bumps an object, Beetbot backs up and makes a righthand turn to avoid it.
# The time BeetleBot backs up is random, from 1.5 seconds to 6 seconds,.
# It will stop backing up if an object is detected 7 inches from the
# HC-SR04 ping sensor in the reat of BeetleBot.
# If the RHS whisker encounters an object, the behavior is the same except Beetlebot turns left after backing up.


from machine import Pin, PWM
# Pin uses the GPIO value , not the actual pin number 
import utime
import random

LHSWhisker= Pin(14, machine.Pin.IN,machine.Pin.PULL_DOWN)
RHSWhisker= Pin(13, machine.Pin.IN,machine.Pin.PULL_DOWN)

LHSWhiskerLED= Pin(12, machine.Pin.OUT)
RHSWhiskerLED= Pin(11, machine.Pin.OUT)
AliveLED = Pin(25,machine.Pin.OUT)


LHSservo = PWM(Pin(16))
RHSservo = PWM(Pin(17))
# 50 Hz is 20 msec period
LHSservo.freq(50)
RHSservo.freq(50) 
# 100% duty of PWM is 65200 counts
# 2 ms of 20 ms is 10% for full spd FWD
# ( 1.5 ms / 20 ms ) * 65200 = 4875 for servo zerospeed
# 1 ms of 20 ms is full spd rev , .05* 65200 
zerospd = 4875
LHS_FullSpd = 3250 # LHS side servo is mounted opposite so gets a reversed reference 
RHS_FullSpd = 6500
LHS_TopSpdRev = 6500
RHS_TopSpdRev = 3250
AliveLED.value(1)

PingTrigger=Pin(9,Pin.OUT)
PingEcho=Pin(8,Pin.IN)

def Ping():
    echotries=0
    PingTrigger.low()
    utime.sleep_us(2)  # note sleep_us is for microsecs
    PingTrigger.high()
    utime.sleep_us(10)
    PingTrigger.low()
    while ((PingEcho.value() == 0) and (echotries<30)):
        EchoStartTime = utime.ticks_us()
        echotries=echotries+1
         # This check bails out of the loop on a problem with a long echo  or failed echo, I havent been able to prove its needed.
         
    while PingEcho.value()==1:
        EchoHeard = utime.ticks_us()
    PingDeltaTime=EchoHeard-EchoStartTime
    PingDistance_cm =(PingDeltaTime*.0343)/2  # sound is 343.2 m/s .0343 cm/usec
    PingDistance_in=(PingDistance_cm)/2.54
    #print ("Measured distance is ",PingDistance_cm, "cm"  )
    print ("Measured distance is ",PingDistance_in, "inches"  )
    #print ("Echotries =", echotries)
    return PingDistance_in

def backup():
    LHSservo.duty_u16(LHS_TopSpdRev)  #top speed rev on LHS
    RHSservo.duty_u16(RHS_TopSpdRev) # top spd rev on RHS



while True:  #this is start of the main loop routine
    AliveLED.toggle()
     # if no action on the whiakers go straight
    LHSservo.duty_u16(LHS_FullSpd)  #top speed forward on LHS
    RHSservo.duty_u16(RHS_FullSpd) # top spd fwd on RHS
                            # zerospeed = 4875
    
    # if no action on the whiakers go straight, clear LEDs
    
    if ((LHSWhisker.value() ==0) & (RHSWhisker.value() ==0)):
        LHSWhiskerLED.value(0)
        RHSWhiskerLED.value(0)
      
      
      ################ LHS whisker routine, backup and turn right   
          
    if LHSWhisker.value() ==1: #gotta latch this operation
        LHSWhiskerLED.value(1)
        count=1
        while True:  # using break to exit the loop
            backup()
            #Ping()
            PingDistance=Ping()
            utime.sleep(.2)
            count=count+1
            backuptime=random.randint(8,30)  # backuptime is comprised as the number of 200msec cycles before breaking out of the backup loop
            #print ("backuptime = ",backuptime)
            print ("count = ",count)
            print ("backuptime = ",backuptime)
            #print ("LoopCycles= ",Loopcycles)
            if (PingDistance<6):
                break        
            if (count>backuptime):
                break
           # print ("ping distance = ",PingDistance)
            
    # back up tthen right turn
        RHturntime=random.uniform(.5,3)
        LHSservo.duty_u16(LHS_FullSpd)  #top speed forward on LHS
        RHSservo.duty_u16(zerospd) # zerospeed on RHS
        utime.sleep(RHturntime)
        
        #on exit of LHS Whisker routine, go staright again
    LHSservo.duty_u16(LHS_FullSpd)  #top speed forward on LHS
    RHSservo.duty_u16(RHS_FullSpd) # top spd fwd on RHS
        
        ## start RHS side whisker behavior definition 
        
    if RHSWhisker.value() ==0:
        RHSWhiskerLED.value(0)
        
    if RHSWhisker.value() ==1:
        RHSWhiskerLED.value(1)
        count=1
        while True:  # using break to exit the loop
            backup()
            #Ping()
            PingDistance=Ping()
            utime.sleep(.2)
            count=count+1
            backuptime=random.randint(8,30)  # backuptime is comprised as the number of 200msec cycles before breaking out of the backup loop
            #print ("backuptime = ",backuptime)
            print ("RHScount = ",count)
            print ("RHSbackuptime = ",backuptime)
            if (PingDistance<6):
                break        
            if (count>backuptime):
                break
           # print ("ping distance = ",PingDistance)
        
    # turn left
        LHturntime=random.uniform(.5,3)
        
        LHSservo.duty_u16(zerospd)  # zerospeed on LHS
        RHSservo.duty_u16(RHS_FullSpd) # top spd fwd on RHS
        utime.sleep(LHturntime)
      
        LHSservo.duty_u16(LHS_FullSpd)  #top speed forward on LHS
        RHSservo.duty_u16(RHS_FullSpd) # top spd fwd on RHS
    