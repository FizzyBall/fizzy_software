from fizzy_udp import Fizzy

import time
from typing import Any
import numpy as np
import matplotlib.pyplot as plt
from collections import deque
import csv
from pynput import keyboard


def extract_euler_from_packet(packet):
    """
    Given a data packet with the specified format, extract Euler angles.
    Input packet: [timestamp, motor_speed, battery_voltage, qx, qy, qz, qw, mag_cal_level]
    Returns: (roll, pitch, yaw) in radians
    """
    # Extract quaternion components
    qx = packet[3]
    qy = packet[4]
    qz = packet[5]
    qw = packet[6]

    # Rearrange to [w, x, y, z]
    q = [qw, qx, qy, qz]

    # Convert to Euler angles
    w, x, y, z = q

    t0 = +2.0 * (w * x + y * z)
    t1 = +1.0 - 2.0 * (x * x + y * y)
    roll = np.arctan2(t0, t1)

    t2 = +2.0 * (w * y - z * x)
    t2 = np.clip(t2, -1.0, 1.0)
    pitch = np.arcsin(t2)

    t3 = +2.0 * (w * z + x * y)
    t4 = +1.0 - 2.0 * (y * y + z * z)
    yaw = np.arctan2(t3, t4)

    return roll, pitch, yaw


# Set up plots
plt.ion()  # Turn on interactive mode
fig, axs = plt.subplots(3, 1, figsize=(8, 6))
data_plotting = 50

# Lists to store all data for each signal
x_data_all = [[] for _ in range(3)]
y_data_all = [[] for _ in range(3)]

# Deques to store the last 100 data points for plotting for each signal
x_data_plot = [deque(maxlen=data_plotting) for _ in range(3)]
y_data_plot = [deque(maxlen=data_plotting) for _ in range(3)]


# # Functions to simulate sensor data for each signal
# def get_sensor_data(signal_id):
#     return random.randint(0, 10)  # Replace with actual sensor reading


save_data = False                  # Flag to indicate if data should be saved
desired_minimal_cycle_time = 0.01  # this value is used to limit really fast cylcle times 
bais_negative = 0
bais_positive = 0

# # Get starting time
# s.sendto(struct.pack('Bf', 1, 0), ('192.168.4.1', 4711)) # idel motor
# try:
#     rec_list = list(struct.unpack(16*'f'+'q', s.recv(200)))
# except:
#     print("dropout")


# Initialize fizzy
fizzy = Fizzy()

data = fizzy.get_data()

print(data)

start_time_on_PCB = data[0]/1_000_000 # in seconds

# Main loop
try:
    while True:
        start = time.time()

        # Import angles, temperature, battery voltage and time
        data = fizzy.get_data()
        roll, pitch, yaw = extract_euler_from_packet(data)
        print(np.degrees([roll, pitch, yaw]))  # Convert to degrees
        
        
        yaw_measurement = data[0]       # in degrees
        pitch_measurment = data[1]      # in degrees
        roll_measurement = data[2]      # in degrees
        
        time_on_PCB = data[0]/1_000_000 # in seconds
        


        
     


        # for signal_id in range(3):
        #     # y = acc[signal_id] # for accelerationsc
        #     y = rec_list[signal_id] # for angles
        #     x = time_on_PCB
            
        #     x_data_all[signal_id].append(x)
        #     y_data_all[signal_id].append(y)

        #     x_data_plot[signal_id].append(x)
        #     y_data_plot[signal_id].append(y)

        #     axs[signal_id].clear()  # Clear previous plot
        #     axs[signal_id].plot(x_data_plot[signal_id], y_data_plot[signal_id])

        #     axs[signal_id].set_xlabel('X Axis')
        #     axs[signal_id].set_ylabel(f'Y Axis {signal_id}')
        #     axs[signal_id].set_title(f'Signal {signal_id}')

        
        
        # plt.tight_layout()

        plt.pause(0.01)  # Adjust the pause time as needed
        # time.sleep(0.1)  # Simulate sensor data interval

        

        endtime = time.time()
        cycle_time = endtime-start
        # print('time in python',start-initial_time)
    
        if endtime-start < desired_minimal_cycle_time:
            # print('processing time', endtime-start)
            # print("sleep")
            time.sleep(desired_minimal_cycle_time-(endtime-start))



        # Check for keyboard input 'c'
except KeyboardInterrupt:
    print("Measurement interrupted by user.")




# # Save data if condition is met
# if save_data:
#     filename = "sensor_data_angles.csv"
#     with open(filename, 'w', newline='') as csvfile:
#         csvwriter = csv.writer(csvfile)
#         csvwriter.writerow(['Time', 'Signal 0', 'Signal 1', 'Signal 2'])
#         for i in range(len(x_data_all[0])):
#             row = (x_data_all[0][i], y_data_all[0][i], y_data_all[1][i], y_data_all[2][i]) 
#             csvwriter.writerow(row)
#     print(f"Data saved to {filename}")

# # plt.show()