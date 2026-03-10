import csv
import matplotlib.pyplot as plt
# from matplotlib.widgets import ZoomPan

# Read data from the CSV file
filename = "sensor_data_drop_1m_test1.csv"  # Replace with the name of your CSV file
time = []
signal1 = []
signal2 = []
signal3 = []

with open(filename, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)  # Skip header row if present
    for row in csv_reader:
        time.append(float(row[0]))
        signal1.append(float(row[1]))
        signal2.append(float(row[2]))
        signal3.append(float(row[3]))


# # Plot the data
# fig, ax = plt.subplots()
# ax.plot(time, signal1, label='Signal 1')
# ax.plot(time, signal2, label='Signal 2')
# ax.plot(time, signal3, label='Signal 3')

# # Add labels and title
# ax.set_xlabel('Time')
# ax.set_ylabel('Signal Value')
# ax.set_title('Signals Over Time')

# # Add legend
# ax.legend()

# # Create a zoom/pan widget
# zoom_pan = ZoomPan()
# figZoom = zoom_pan.zoom_factory(ax, base_scale=1.1)

# plt.show()



# Plot the data
plt.plot(time, signal1, label='Signal 1')
plt.plot(time, signal2, label='Signal 2')
plt.plot(time, signal3, label='Signal 3')

# Add labels and title
plt.xlabel('Time')
plt.ylabel('Signal Value')
plt.title('Signals Over Time')

# Add legend
plt.legend()

# Show plot
plt.show()