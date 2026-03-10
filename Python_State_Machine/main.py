"""
Main robot control program.

Responsibilities:
-----------------
1. Initialize hardware
2. Read sensors
3. Run FSM
4. Handle interrupts
5. Send motor commands
"""


import time
import numpy as np

from fizzy_udp import Fizzy


from core.fsm import StateMachine
from core.interrupts import Interrupts

from states.neutral import Neutral
from states.wiggle import Wiggle
from states.vibrate import Vibrate
from states.inbalance import Inbalance
from states.manual import Manual
from states.zero_stand import Zero_stand
from states.forward import Forward 
from states.backward import Backward 

from fizzy_io.imu_angle import extract_euler
from fizzy_io.imu_acc import extract_acc
from fizzy_io.joystick import XboxThread


import config


def main():

    # Start joystick thread
    joystick = XboxThread()
    joystick.daemon = True
    joystick.start()

    # Hardware interface
    fizzy = Fizzy()

    # Create state sequence
    sequence = [
        
        Neutral(duration=2),

        Wiggle(config.T1, config.T2, config.A1, config.A2, duration=2),
        
        Zero_stand(config.K_P, duration=1),

        Wiggle(config.T1, config.T2, config.A1, config.A2, duration=1)

        # Vibrate(config.T1V, config.T2V, config.A1V, config.A2V, duration=3),

        # Zero_stand(config.K_P, duration=2),

        # Backward(config.K_P, config.time_backwards, config.time_forwards, config.cycle_duration_roll_forward, duration=5)
    ]
    ## not used:
    # Inbalance(config.K_P, duration=2),

    # FSM
    fsm = StateMachine(sequence)
    fsm.start()

    interrupts = Interrupts()

    last = time.time()

    # Main loop
    while True:

        now = time.time()
        dt = now - last
        last = now

        # Read IMU
        try:
            data = fizzy.get_data()
        except Exception as e:
            print("IMU read failed:", e) # Communication dropout try again and print error
            continue

        roll, pitch, yaw = extract_euler(data)

        acc_mag = extract_acc(data)

        sensors = {
            "roll": roll,
            "pitch": pitch,
            "yaw": yaw,
            "acc_mag": acc_mag
        }

        print(data[0])
        # Handle interrupts
        event = interrupts.check(joystick, sensors)

        # Exit program
        if event == "EXIT":
            fizzy.stop()
            print('Bye ...')
            break


        # IMU input correction
        elif event == "TAP":
            if fsm.auto_mode:
                fsm.push(Zero_stand(config.K_P, duration=1))
                fsm.push(Backward(config.K_P, config.time_backwards, config.time_forwards, config.cycle_duration_roll_forward, duration=5))

        # Manual override
        elif event == "MANUAL":
            if not isinstance(fsm.current, Manual):
                fsm.push(Manual())

        # Motor off
        elif event == "NEUTRAL":

            fsm.push(Neutral())

        # Resume autonomy
        elif event == "RESUME":

            while not fsm.auto_mode:
                fsm.pop()

        # Run FSM
        power = fsm.update(dt, sensors, joystick)

        # Saturate
        power = np.clip(power, -config.POWER_LIMIT, config.POWER_LIMIT)

        # Send command
        fizzy.set_motor(power)
   
        # Making sure that the cycle time is running with a minimum cycle time.
        endtime = time.time()
        cycle_duration = endtime-last
        if cycle_duration < config.MIN_CYCLE_TIME:
            time.sleep(config.MIN_CYCLE_TIME-(cycle_duration))

if __name__ == "__main__":
    main()
