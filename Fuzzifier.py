import numpy as np
import simpful as sf
import skfuzzy as fuzz

x_angle = np.arange(-46, 47, 1)
x_speed = np.arange(-100, 101, 1)

# Giving the persistent fuzzy system an easier to handle name
FuzzySystem = sf.FuzzySystem()

#  Fuzzy sets
## Fuzzy sets associated with linguistic variable "angle"
set_vd = sf.FuzzySet(function=sf.Triangular_MF(a=-46, b=-46, c=-23), term="very downhill")
set_sd = sf.FuzzySet(function=sf.Triangular_MF(a=-46, b=-23, c=0),   term="somewhat downhill")
set_f  = sf.FuzzySet(function=sf.Triangular_MF(a=-23, b=0, c=23),    term="flat")
set_su = sf.FuzzySet(function=sf.Triangular_MF(a=0, b=23, c=46),     term="somewhat uphill")
set_vu = sf.FuzzySet(function=sf.Triangular_MF(a=23, b=46, c=46),    term="very uphill")

## Fuzzy sets associated with the linguistic variable "speed"
set_in  = sf.FuzzySet(function=fuzz.smf(x_speed, 0, 100), term="increase")
set_con = sf.FuzzySet(function=sf.Trapezoidal_MF())

#  Linguistic variables
## Linguistic variable "Angle"
FuzzySystem.add_linguistic_variable("Angle", sf.LinguisticVariable([set_vd, set_sd, set_f, set_su, set_vu],
                                                                concept="Angle depth", universe_of_discourse=[-46,46]))

