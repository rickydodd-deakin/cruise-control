import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

'''
This is a manual generation of the fuzzification variables used to test the
different defuzzification methods available from SciKit Fuzzy.
Since the control API implements centroid, it was necessary to build this
to test different methods.
Based on
https://pythonhosted.org/scikit-fuzzy/auto_examples/plot_tipping_problem.html#example-plot-tipping-problem-py
Hannah Smith 216019732
'''


# Generate universe variables
closeness = np.arange(0, 101, 1)
speed = np.arange(0, 101, 1)
change = np.arange(-50, 51, 1)

# Generate fuzzy membership functions
close_vclose  = fuzz.trapmf(closeness, [0, 0, 25, 40])
close_close = fuzz.trimf(closeness, [10, 30, 50])
close_comfortable = fuzz.trimf(closeness, [30, 50, 70])
close_far = fuzz.trimf(closeness, [50, 70, 90])
close_vfar  = fuzz.trapmf(closeness, [60, 75, 100, 100])

speed_vslow = fuzz.trapmf(speed, [0, 0, 15, 50])
speed_slow = fuzz.trimf(speed, [20, 50, 80])
speed_fast = fuzz.trapmf(speed, [50, 85, 100, 100])

change_hincrease = fuzz.smf(change, 0, 50)
change_increase = fuzz.trimf(change, [0, 20, 20])
change_constant = fuzz.trapmf(change, [-15, -5, 5, 15])
change_decrease = fuzz.trimf(change, [-20, -20, 0])
change_hdecrease = fuzz.zmf(change, -50, 0)

# We need the activation of our fuzzy membership functions at these values.
#Change the values to test different inputs
VeryClose = fuzz.interp_membership(closeness, close_vclose, 20)
Close = fuzz.interp_membership(closeness, close_close, 20)
Comfortable = fuzz.interp_membership(closeness, close_comfortable, 20)
Far = fuzz.interp_membership(closeness, close_far, 20)
VeryFar = fuzz.interp_membership(closeness, close_vfar, 20)

VerySlow = fuzz.interp_membership(speed, speed_vslow, 80)
Slow = fuzz.interp_membership(speed, speed_slow, 80)
Fast = fuzz.interp_membership(speed, speed_fast, 80)

change_activation_hincrease = np.fmin(np.fmin(VeryFar, VerySlow), change_hincrease)
change_activation_increase = np.fmin(np.fmin(Far, np.fmin(VerySlow,np.fmin(Slow, np.fmin(Fast, VeryFar)))), change_increase)
change_activation_constant = np.fmin(Comfortable, change_constant)
change_activation_decrease = np.fmin(Close, change_decrease)
change_activation_hdecrease = np.fmin(VeryClose, change_hdecrease)

change0 = np.zeros_like(change)

# Aggregate all three output membership functions together
aggregated = np.fmax(change_activation_hdecrease, np.fmax(change_activation_decrease, np.fmax(change_activation_constant, np.fmax(change_activation_increase, change_activation_hincrease))))

# Calculate defuzzified result
changeResult = fuzz.defuzz(change, aggregated, 'mom')
change_activation = fuzz.interp_membership(change, aggregated, changeResult)  # for plot

# Visualize this
fig, ax0 = plt.subplots(figsize=(5, 3))

ax0.plot(change, change_activation_hdecrease, 'b', linewidth=1.5, linestyle='--', label='heavy decrease')
ax0.plot(change, change_activation_decrease, 'g', linewidth=1.5, linestyle='--', label='decrease')
ax0.plot(change, change_activation_constant, 'r', linewidth=1.5, linestyle='--', label='constant')
ax0.plot(change, change_activation_increase, 'c', linewidth=1.5, linestyle='--', label='increase')
ax0.plot(change, change_activation_hincrease, 'm', linewidth=1.5, linestyle='--', label='heavy increase')
ax0.fill_between(change, change0, aggregated, facecolor='Orange', alpha=0.5)
ax0.plot([changeResult, changeResult], [0, change_activation], 'k', linewidth=1.5, alpha=0.9)
ax0.set_title('Aggregated membership and result (mean of maximum)')
ax0.legend()

plt.plot()
plt.show()
