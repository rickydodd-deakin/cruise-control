import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Antecedent objects, to hold universes of discourse and membership functions
angle = ctrl.Antecedent(np.arange(-46, 47, 1), 'angle')
speed = ctrl.Antecedent(np.arange(0, 101, 1), 'speed')

# Consequent object, to hold universe of discourse and membership functions
change = ctrl.Consequent(np.arange(-50, 51, 1), 'change')

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
change['heavily increase'] = fuzz.smf(change.universe, 0, 50)
change['increase'] = fuzz.trimf(change.universe, [0, 20, 20])
change['constant'] = fuzz.trapmf(change.universe, [-15, -5, 5, 15])
change['decrease'] = fuzz.trimf(change.universe, [-20, -20, 0])
change['heavily decrease'] = fuzz.zmf(change.universe, -50, 0)

# Fuzzy rules
R1 = ctrl.Rule(angle['very downhill'],                 change['heavily decrease'])
R2 = ctrl.Rule(angle['very uphill'],                   change['heavily increase'])
R3 = ctrl.Rule(angle['flat'],                          change['constant'])
R4 = ctrl.Rule(angle['downhill'] & speed['very slow'], change['constant'])
R5 = ctrl.Rule(angle['downhill'] & speed['slow'],      change['decrease'])
R6 = ctrl.Rule(angle['downhill'] & speed['fast'],      change['decrease'])
R7 = ctrl.Rule(angle['uphill'] & speed['very slow'],   change['constant'])
R8 = ctrl.Rule(angle['uphill'] & speed['slow'],        change['decrease'])
R9 = ctrl.Rule(angle['uphill'] & speed['fast'],        change['decrease'])