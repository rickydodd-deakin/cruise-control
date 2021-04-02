#created by Patrick Wright ID: 217530505

#IMPORTS
import time
import Fuzzifier
import Defuzzifier


#CONSTANTS
THROTTLE_RATE = 2 #creates speed change of 2km/h per tick
CAR_DRAG = 1 #the car will lose 1km/h per tick if throttle disengaged


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
    #get car back up to Cruise Control speed and return to maintaining speed
    while(currentVehicleSpeed < setCCSpeed):
       currentVehicleSpeed += THROTTLE_RATE
       time.sleep(1)
    maintainingSpeed = True
    return currentVehicleSpeed, maintainingSpeed

    
    
#reduce speed by car drag every second until setCCSpeed is reached, then return to maintaining speed
def Decelerate(currentVehicleSpeed, maintainingSpeed, setCCSpeed):
    while(currentVehicleSpeed > setCCSpeed):
        currentVehicleSpeed -= CAR_DRAG
        time.sleep(2)
    maintainingSpeed = True
    return currentVehicleSpeed, maintainingSpeed



def Driving(setCCSpeed, currentVehicleSpeed, frontVehicleDistance, maintainingSpeed):
    #this stores an int which is the change of speed we need to make
    safeSpeedCheck = Defuzzifier.Defuzzify(frontVehicleDistance, currentVehicleSpeed)
    setCCSpeed = currentVehicleSpeed + safeSpeedCheck
    #if we are too close, slow down
    if(safeSpeedCheck < 0):
        print('Decelerating')
        currentVehicleSpeed, maintainingSpeed = Decelerate(currentVehicleSpeed, maintainingSpeed, setCCSpeed)
    #if we are safe distance for our current speed, maintain it
    elif(safeSpeedCheck == 0):
        print('Maintaining Speed')
        currentVehicleSpeed, maintainingSpeed = MaintainSpeed(currentVehicleSpeed, maintainingSpeed, setCCSpeed)
    #if we are too far away but below CCspeed, accelerate
    elif(safeSpeedCheck > 0): 
        print('Accelerating')
        currentVehicleSpeed, maintainingSpeed = Accelerate(currentVehicleSpeed, maintainingSpeed, setCCSpeed)
        
    return(setCCSpeed, currentVehicleSpeed, maintainingSpeed)

    

