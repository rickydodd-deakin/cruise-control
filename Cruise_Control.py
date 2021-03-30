#created by Patrick Wright ID: 217530505

#IMPORTS
import time
import Fuzzifier
import Defuzzifier


#CONSTANTS
THROTTLE_RATE = 2 #creates speed change of 2km/h per tick
CAR_DRAG = 1 #the car will lose 1km/h per tick if throttle disengaged

#VARIABLES
#driving = True
#maintainingSpeed = False

#FUNCTION

#while travelling the drag of the car reduces speed by 1 km/h every 2 seconds
#once vehicle speed is below cruise control threshold (outside 5km/h of setCCspeed break)
def MaintainSpeed(currentVehicleSpeed, maintainingSpeed, setCCSpeed): 
    while(maintainingSpeed):
        currentVehicleSpeed -= CAR_DRAG
        time.sleep(2)
        if(currentVehicleSpeed < (setCCSpeed - 5)):
            maintainingSpeed = False
    return currentVehicleSpeed, maintainingSpeed



#when the vehicle needs to accelerate, increase speed by 2km/h per second
def Accelerate(currentVehicleSpeed, maintainingSpeed, setCCSpeed):
    #get car back up to Cruise Control speed
    while(currentVehicleSpeed < setCCSpeed):
       currentVehicleSpeed += THROTTLE_RATE
       time.sleep(1)
    #maintaining speed is now true
    maintainingSpeed = True
    return currentVehicleSpeed, maintainingSpeed

    
    
#when the vehicle needs to decelerate, reduce speed by car drag every second
def Decelerate(currentVehicleSpeed, maintainingSpeed, setCCSpeed):
    while(currentVehicleSpeed > setCCSpeed):
        currentVehicleSpeed -= CAR_DRAG
        time.sleep(2)
    #maintaining speed is now true
    maintainingSpeed = True
    return currentVehicleSpeed, maintainingSpeed

#check for vehicle in front (lets just say there is one)


#driving
def Driving(setCCSpeed, currentVehicleSpeed, frontVehicleDistance, maintainingSpeed):
    #while(driving):
    #this stores an int which is the change of speed we need to make
    safeSpeedCheck = Defuzzifier.Defuzzify(frontVehicleDistance, currentVehicleSpeed)
    setCCSpeed = currentVehicleSpeed + safeSpeedCheck
    #if we are too close, slow down
    if(safeSpeedCheck < 0):
    #if(currentVehicleSpeed > setCCSpeed):
        print('Decelerating')
        currentVehicleSpeed, maintainingSpeed = Decelerate(currentVehicleSpeed, maintainingSpeed, setCCSpeed)
    #if we are safe distance for our current speed, maintain
    elif(safeSpeedCheck == 0):
    #elif(currentVehicleSpeed == setCCSpeed):
        print('Maintaining Speed')
        currentVehicleSpeed, maintainingSpeed = MaintainSpeed(currentVehicleSpeed, maintainingSpeed, setCCSpeed)
    #if we are too far away but below CCspeed, accelerate
    elif(safeSpeedCheck > 0): 
    #elif(currentVehicleSpeed < setCCSpeed):
        print('Accelerating')
        currentVehicleSpeed, maintainingSpeed = Accelerate(currentVehicleSpeed, maintainingSpeed, setCCSpeed)
        
    return(setCCSpeed, currentVehicleSpeed, maintainingSpeed)

    
















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
