import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Antecedent objects, to hold universes of discourse and membership functions
angle = ctrl.Antecedent(np.arange(-46, 47, 1), 'angle')
speed = ctrl.Antecedent(np.arange(0, 101, 1), 'speed')

# Consequent object, to hold universe of discourse and membership functions
change = ctrl.Consequent(np.arange(-100, 101, 1), 'change')

# Fuzzy membership functions for "angle"
angle['very downhill'] = fuzz.trimf(angle.universe, [-46, -46, -23])
angle['downhill']      = fuzz.trimf(angle.universe, [-46, -23, 0])
angle['flat']          = fuzz.trimf(angle.universe, [-23, 0, 23])
angle['uphill']        = fuzz.trimf(angle.universe, [0, 23, 46])
angle['very uphill']   = fuzz.trimf(angle.universe, [23, 46, 46])

# Fuzzy membership functions for "speed"
speed['very slow'] = fuzz.trapmf(speed.universe, [0, 0, 15, 50])
speed['slow'] = fuzz.trimf(speed.universe, [20, 50, 80])
speed['fast'] = fuzz.trapmf(speed.universe, [50, 85, 100, 100])

# Fuzzy membership functions for "change"
change['increase'] = fuzz.smf(change.universe, 0, 100)
change['constant'] = fuzz.trapmf(change.universe, [-50, -10, 10, 50])
change['decrease'] = fuzz.zmf(change.universe, -100, 0)
