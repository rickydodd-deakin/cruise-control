import numpy as np
import skfuzzy as fuzz

# Generate universe variables
x_angle = np.arange(-46, 47, 1)
x_speed = np.arange(0, 101, 1)
x_change = np.arange(-100, 101, 1) # Universe for the consequent

# Generate fuzzy membership functions
## Angle (antecedent)
angle_vd = fuzz.trimf(x_angle, [-46, -46, -23])
angle_sd = fuzz.trimf(x_angle, [-46, -23, 0])
angle_f  = fuzz.trimf(x_angle, [-23, 0, 23])
angle_su = fuzz.trimf(x_angle, [0, 23, 46])
angle_vu = fuzz.trimf(x_angle, [23, 46, 46])

## Speed (antecedent)
speed_slo = fuzz.trapmf(x_speed, [0, 0, 15, 50])
speed_med = fuzz.trimf(x_speed, [20, 50, 80])
speed_fas = fuzz.trapmf(x_speed, [50, 85, 100, 100])

## Change (consequent)
change_inc = fuzz.smf(x_change, 0, 100)
change_con = fuzz.trapmf(x_change, [-50, -10, 10, 50])
change_dec = fuzz.zmf(x_change, -100, 0)
