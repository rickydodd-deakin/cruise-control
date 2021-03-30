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

#Controller for testing
cruise_ctrl = ctrl.ControlSystem([R1, R2, R3, R4, R5, R6, R7, R8, R9])

#Simulation for testing
cruise_sim = ctrl.ControlSystemSimulation(cruise_ctrl)

#Change the inputs here to generate different outputs
#Test 1 - Vehicle in front is a safe distance
cruise_sim.input['closeness'] = 55
cruise_sim.input['speed'] = 60

cruise_sim.compute()

#printing and creating an image of the simulation
print('Test 1 output:', cruise_sim.output['change'], 'safe distance condition')
Fuzzifier.change.view(sim=cruise_sim)

#Test 2 - Vehicle in front is slightly too close
cruise_sim.input['closeness'] = 45
cruise_sim.input['speed'] = 60

cruise_sim.compute()

print('Test 2 output:', cruise_sim.output['change'], 'close condition')
Fuzzifier.change.view(sim=cruise_sim)

#Test 3 - Vehicle in front is much too close
cruise_sim.input['closeness'] = 15
cruise_sim.input['speed'] = 60

cruise_sim.compute()

#printing and creating an image of the simulation
print('Test 3 output:', cruise_sim.output['change'], 'very close condition')
Fuzzifier.change.view(sim=cruise_sim)

#Test 4 - Vehicle in front is far, speed is high
cruise_sim.input['closeness'] = 90
cruise_sim.input['speed'] = 80

cruise_sim.compute()

#printing and creating an image of the simulation
print('Test 4 output:', cruise_sim.output['change'], 'very far, speed is fast condition')
Fuzzifier.change.view(sim=cruise_sim)

#Test 5 - Vehicle in front is far, speed is slow
cruise_sim.input['closeness'] = 90
cruise_sim.input['speed'] = 50

cruise_sim.compute()

#printing and creating an image of the simulation
print('Test 5 output:', cruise_sim.output['change'], 'very far, speed is slow condition')
Fuzzifier.change.view(sim=cruise_sim)

#Test 6 - Vehicle in front is far, speed is very slow
cruise_sim.input['closeness'] = 90
cruise_sim.input['speed'] = 30

cruise_sim.compute()

#printing and creating an image of the simulation
print('Test 6 output:', cruise_sim.output['change'], 'very far, speed is very slow condition')
Fuzzifier.change.view(sim=cruise_sim)

#Test 7 - Extreme inputs - front vehicle is very close and speed is very slow
cruise_sim.input['closeness'] = 0
cruise_sim.input['speed'] = 10

cruise_sim.compute()

#printing and creating an image of the simulation
print('Test 7 output:', cruise_sim.output['change'], 'very close, very slow condition')
Fuzzifier.change.view(sim=cruise_sim)

#Test 8 - Vehicle in front is very close, speed is very fast
cruise_sim.input['closeness'] = 0
cruise_sim.input['speed'] = 100

cruise_sim.compute()

#printing and creating an image of the simulation
print('Test 8 output:', cruise_sim.output['change'], 'very far, speed is very slow condition')
Fuzzifier.change.view(sim=cruise_sim)
