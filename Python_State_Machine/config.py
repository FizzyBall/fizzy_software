"""
Global configuration parameters.
Change values here instead of inside code.
"""

# Loop timing
MIN_CYCLE_TIME = 0.001

# Motor limits
POWER_LIMIT = 0.95

# Control gains
K_P = 0.6


## Ossilating movement parameters ##

# Wiggle parameters
T1 = 0.4            # Period for the first and third segments, in seconds, limit: both period on 0.03 with 0.4 amplitude
T2 = 0.8            # Period for the second segment, in seconds

A2 = 0.9            # Amplitude of second segment   choose value between 0 and 0.5, Limit 0.8 with period 0.1
A1 = -0.5*A2        # Amplitude of first segment, (needs to be in relation with the second one)

# Vibration parameters
T1V = 0.2
T2V = 0.2

A2V = 0.7
A1V = -0.5 * A2V

# forward and backward motion
time_backwards = 2
time_forwards = 3
cycle_duration_roll_forward = 5 # total ammount of time in this cycle