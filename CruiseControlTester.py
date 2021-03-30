import time
import Cruise_Control

def cruiseControlTest(testLength):
    '''
    This method runs a test of the cruise control code for a certain length
    of time specified by the user.
    Inputs:
    testLength    The time in seconds you want to run the test for
    '''
    startTime = time.time()

    #Initialise variables
    Cruise_Control.driving = True
    maintainingSpeed = False
    setCCSpeed = 60
    currentVehicleSpeed = 40
    frontVehicleDistance = 55

    print("Beginning test of {0} seconds".format(testLength))
    while (Cruise_Control.driving):
        setCCSpeed, currentVehicleSpeed, maintainingSpeed = Cruise_Control.Driving(setCCSpeed, currentVehicleSpeed, frontVehicleDistance, maintainingSpeed)
        print("Set speed is {0}, current vehicle speed is {1}kph, front vehicle is {2}m away".format(setCCSpeed, currentVehicleSpeed, frontVehicleDistance))
        if (time.time() > startTime + testLength):
            Cruise_Control.driving = False

#This starts a test of 10 seconds
cruiseControlTest(30)
