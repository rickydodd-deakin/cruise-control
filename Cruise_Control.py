#IMPORTS
import time
import Fuzzifier


#CONSTANTS
THROTTLE_RATE = 2 #creates speed change of 2km/h per tick
CAR_DRAG = 1 #the car will lose 1km/h per tick if throttle disengaged

#VARIABLES
driving = True
maintainingSpeed = False
setCCSpeed = 0
currentVehicleSpeed = 40 #CC cannot engage below 40km/h
frontVehicle = False
frontVehicleDistance = 0
safedistance = 0
#surfaceAngle = 0


#FUNCTIONS
#while travelling the drag of the car reduces speed by 1 km/h every 2 seconds
#once vehicle speed is below cruise control threshold (outside 5km/h of setCCspeed break)
def MaintainSpeed(currentVehicleSpeed, maintainingSpeed, setCCSpeed): 
    while(maintainingSpeed):
        currentVehicleSpeed -= CAR_DRAG
        time.sleep(2)
        if(currentVehicleSpeed < (setCCSpeed - 5)):
            maintainingSpeed = False

#when the vehicle needs to accelerate, increase speed by 2km/h per second
def Accelerate(currentVehicleSpeed, maintainingSpeed, setCCSpeed):
    #get car back up to Cruise Control speed
    while(currentVehicleSpeed < setCCSpeed):
       currentVehicleSpeed += THROTTLE_RATE
       time.sleep(1)
    #maintaining speed is now true
    maintainingSpeed = True
    
#when the vehicle needs to decelerate, reduce speed by car drag every second
def Decelerate(currentVehicleSpeed, maintainingSpeed, setCCSpeed):
    while(currentVehicleSpeed > setCCSpeed):
        currentVehicleSpeed -= CAR_DRAG
        time.sleep(2)
    #maintaining speed is now true
    maintainingSpeed = True

def DetermineSafeDistance(frontvehicle, frontVehicleDistance, currentVehicleSpeed, setCCSpeed):
    if(frontVehicle):
        if(40 < currentVehicleSpeed <= 50):
            safedistance = 24
        if(50 < currentVehicleSpeed <= 60):
            safedistance = 32
        if(60 < currentVehicleSpeed <= 70):
            safedistance = 40
        if(70 < currentVehicleSpeed <= 80):
            safedistance = 52
        if(80 < currentVehicleSpeed <= 90):
            safedistance = 61
        if(90 < currentVehicleSpeed <= 100):
            safedistance = 76
        if(currentVehicleSpeed > 100):
            safedistance = 90


#the scenario is we are driving at 40km/h, we turn a corner and then wish to engage our cruise control
#set cruise control
setCCSpeed = 50
#check for vehicle in front (lets just say there is one)
frontVehicle = True
#collect distance of front vehicle from our vehicle (in meters)
frontVehicleDistance = 50

while(driving):
    #accelerate up to setCCSpeed
    Accelerate(currentVehicleSpeed, maintainingSpeed, setCCSpeed)
    #not sure about heavily decrease, maybe it should be cruise control disengage? because braking is not used in cruise control systems.
    if(Fuzzifier.R1):
        MaintainSpeed(currentVehicleSpeed, maintainingSpeed, setCCSpeed)
    if(Fuzzifier.R2):
        MaintainSpeed(currentVehicleSpeed, MaintainSpeed, setCCSpeed)
    if(Fuzzifier.R3):
        #unsure how to implement these rules.














#if CVS < setCCSpeed & SA > 0 then Maintain()
#if CVS < setCCSpeed & SA == 0 then Maintain()
#if CVS == setCCSpeed & SA > 0 then Maintain()
#if CVS < setCCSpeed & SA < 0 then Maintain()
#if CVS == setCCSpeed & SA == 0 then Maintain()
#if CVS > setCCSpeed & SA > 0 then Maintain()
#if CVS == setCCSpeed & SA < 0 then Maintain()
#if CVS > setCCSpeed & SA == 0 then Maintain()
#if CVS > setCCSpeed & SA < 0 then Maintain()

#IF (frontVehicle AND 40 < currentVehicleSpeed <= 50) Safe distance is 24 metres 
#IF (frontVehicle AND 50 < currentVehicleSpeed <= 60) Safe distance is 32 metres 
#IF (frontVehicle AND 60 < currentVehicleSpeed <= 70) Safe distance is 40 metres 
#IF (frontVehicle AND 70 < currentVehicleSpeed <= 80) Safe distance is 52 metres 
#IF (frontVehicle AND 80 < currentVehicleSpeed <= 90) Safe distance is 61 metres 
#IF (frontVehicle AND 90 < currentVehicleSpeed <= 100) Safe distance is 76 metres 
#IF (frontVehicle AND 100 < currentVehicleSpeed) Safe distance is 90 metres 
#IF (frontVehicle AND frontVehicleDistance too small)  THEN lower setCCSpeed 
#IF (frontVehicleDistance not too small AND setCCSpeed < original setCCSpeed) THEN restore original setCCSpeed 
#IF (currentVehicleSpeed < setCCSpeed) THEN accelerate to setCCSpeed 
#IF (currentVehicleSpeed > setCCSpeed) THEN decelerate to setCCSpeed 
#IF (currentVehicleSpeed = setCCSpeed) THEN maintain setCCSpeed 