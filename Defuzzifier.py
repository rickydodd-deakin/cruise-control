import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

import Fuzzifier

'''
Based on the tipping example in the SciKit Fuzzy docs. Available at:
https://pythonhosted.org/scikit-fuzzy/auto_examples/plot_tipping_problem.html
https://pythonhosted.org/scikit-fuzzy/auto_examples/plot_tipping_problem_newapi.html#example-plot-tipping-problem-newapi-py

Hannah Smith 216019732
'''

#Getting Rules
R1 = Fuzzifier.R1
R2 = Fuzzifier.R2
R3 = Fuzzifier.R3
R4 = Fuzzifier.R4
R5 = Fuzzifier.R5
R6 = Fuzzifier.R6
R7 = Fuzzifier.R7
R8 = Fuzzifier.R8
R9 = Fuzzifier.R9

#Controller for defuzzifying using the fuzzy logic rules
cruise_ctrl = ctrl.ControlSystem([R1, R2, R3, R4, R5, R6, R7, R8, R9])


def Defuzzify(realClosenessValue, realSpeedValue):
    '''
    This method is used to provide the cruise control system with
    defuzzified outputs based on real inputs.
    Inputs:
    realClosenessValue: The closeness to the vehicle in front in metres
    realSpeedValue: The speed the vehicle is traveling in km/h

    Returns the change in km per hour as an int or null if the input was invalid
    '''
    #Validates inputs
    if isinstance(realClosenessValue, int) and isinstance(realSpeedValue, int):
                                                         
        #Create simulation for outputting values
        cruise_sim = ctrl.ControlSystemSimulation(cruise_ctrl)

        cruise_sim.input['closeness'] = realClosenessValue
        cruise_sim.input['speed'] = realSpeedValue

        cruise_sim.compute()

        return cruise_sim.output['change']
    else:
        #return null if input is invalid
        return null
