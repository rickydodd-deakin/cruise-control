import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

'''
Based on the tipping example in the SciKit Fuzzy docs. Available at:
https://pythonhosted.org/scikit-fuzzy/auto_examples/plot_tipping_problem.html
https://pythonhosted.org/scikit-fuzzy/auto_examples/plot_tipping_problem_newapi.html#example-plot-tipping-problem-newapi-py

Ricky Dodd 220010849
'''

# Antecedent objects, to hold universes of discourse and membership functions
closeness = ctrl.Antecedent(np.arange(0, 101, 1), 'closeness')
speed = ctrl.Antecedent(np.arange(0, 101, 1), 'speed')

# Consequent object, to hold universe of discourse and membership functions
change = ctrl.Consequent(np.arange(-50, 51, 1), 'change')

# Fuzzy membership functions for "closeness"
closeness['very close']  = fuzz.trapmf(closeness.universe, [0, 0, 25, 40])
closeness['close']       = fuzz.trimf(closeness.universe, [10, 30, 50])
closeness['comfortable'] = fuzz.trimf(closeness.universe, [30, 50, 70])
closeness['far']         = fuzz.trimf(closeness.universe, [50, 70, 90])
closeness['very far']    = fuzz.trapmf(closeness.universe, [60, 75, 100, 100])

# Fuzzy membership functions for "speed"
speed['very slow'] = fuzz.trapmf(speed.universe, [0, 0, 15, 50])
speed['slow'] = fuzz.trimf(speed.universe, [20, 50, 80])
speed['fast'] = fuzz.trapmf(speed.universe, [50, 85, 100, 100])

# Fuzzy membership functions for "change"
change['heavily increase'] = fuzz.smf(change.universe, 0, 50)
change['increase'] = fuzz.trimf(change.universe, [0, 20, 20])
change['constant'] = fuzz.trapmf(change.universe, [-15, -5, 5, 15])
change['decrease'] = fuzz.trimf(change.universe, [-20, -20, 0])
change['heavily decrease'] = fuzz.zmf(change.universe, -50, 0)

# Fuzzy rules
R1 = ctrl.Rule(closeness['very close'], change['heavily decrease'])
R2 = ctrl.Rule(closeness['close'], change['decrease'])
R3 = ctrl.Rule(closeness['comfortable'], change['constant'])
R4 = ctrl.Rule(closeness['far'] & speed['very slow'], change['increase'])
R5 = ctrl.Rule(closeness['far'] & speed['slow'], change['constant'])
R6 = ctrl.Rule(closeness['far'] & speed['fast'], change['constant'])
R7 = ctrl.Rule(closeness['very far'] & speed['very slow'], change['heavily increase'])
R8 = ctrl.Rule(closeness['very far'] & speed['slow'], change['constant'])
R9 = ctrl.Rule(closeness['very far'] & speed['fast'], change['constant'])
