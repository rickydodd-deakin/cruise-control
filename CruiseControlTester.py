import time
import CruiseControl

def cruiseControlTest(testLength):
    '''
    This method runs a test of the cruise control code for a certain length
    of time specified by the user.
    Inputs:
    testLength    The time in seconds you want to run the test for
    '''
    startTime = time.time()

    #Initialise variables
    CruiseControl.driving = True
    maintainingSpeed = False
    setCCSpeed = 60
    currentVehicleSpeed = 40
    frontVehicleDistance = 55

    print("Beginning test of {0} seconds".format(testLength))
    while (CruiseControl.driving):
        setCCSpeed, currentVehicleSpeed, maintainingSpeed = CruiseControl.Driving(setCCSpeed, currentVehicleSpeed, frontVehicleDistance, maintainingSpeed)
        print("Set speed is {0}, current vehicle speed is {1}kph, front vehicle is {2}m away".format(setCCSpeed, currentVehicleSpeed, frontVehicleDistance))
        if (time.time() > startTime + testLength):
            CruiseControl.driving = False




#This starts a test of 30 seconds
cruiseControlTest(30)
#cruiseControlTest2(30)
#cruiseControlTest3(30)
