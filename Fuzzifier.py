import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Antecedent objects, to hold universes of discourse and membership functions
closeness = ctrl.Antecedent(np.arange(0, 101, 1), 'closeness')
speed = ctrl.Antecedent(np.arange(0, 101, 1), 'speed')

# Consequent object, to hold universe of discourse and membership functions
change = ctrl.Consequent(np.arange(-50, 51, 1), 'change')

# Fuzzy membership functions for "closeness"
closeness['very close']  = fuzz.trimf(closeness.universe, [-46, -46, -23])
closeness['close']       = fuzz.trimf(closeness.universe, [-46, -23, 0])
closeness['comfortable'] = fuzz.trimf(closeness.universe, [-23, 0, 23])
closeness['far']         = fuzz.trimf(closeness.universe, [0, 23, 46])
closeness['very far']    = fuzz.trimf(closeness.universe, [23, 46, 46])

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
