# this program gathers sensor data
import time
import csv
from DIPPID import SensorUDP

PORT = 5700
sensor = SensorUDP(PORT)
activity = '' # standing, waving, jumping, ...
is_tracking = False
ROW_HEADER = ['label', 'accelerometer_x', 'accelerometer_y', 'accelerometer_z', 'accelerometer_avg']
MAX_COLLECTING_TIME = 5 # every motion will get recorderd for 5 seconds
RECORD_FREQUENCY = 0.1 # seconds data will be transmitted, TODO probably lower number
recording_time = 0 # how long recording is going on
recorded_data = [] # all data in array
num_standing = 0
num_walking = 0
num_punching = 0

print('How to gather data:')
print('Press Button 1 to gather activity one')
print('Press Button 2 to gather activity two')
print('Press Button 3 to gather activity three')
print('Then: do motion for xy seconds')


while (True):
    # print('capabilities: ', sensor.get_capabilities())

    if(sensor.has_capability('button_1') and sensor.has_capability('button_2') and
       sensor.has_capability('button_3')):
        button_one = sensor.get_value('button_1')
        button_two = sensor.get_value('button_2')
        button_three = sensor.get_value('button_3')

        if button_one == 1 and not is_tracking:
            # start tracking activity 1
            label = 'standing' # TODO automation which motion is recorded
            is_tracking = True
            num_standing += 1
            print("Starting to track standing-activity")
        if button_two == 1 and not is_tracking:
            # start tracking activity 1
            label = 'walking'
            is_tracking = True
            print("Starting to track walking-activity")
        if button_three == 1 and not is_tracking:
            # start tracking activity 1
            label = 'punching'
            is_tracking = True
            print("Starting to track punching-activity")
        
        if is_tracking and recording_time < MAX_COLLECTING_TIME:
            
            # add or edit gyroscope, gravity (don't know what we need)
            accelerometer_x = sensor.get_value('accelerometer')['x']
            accelerometer_y = sensor.get_value('accelerometer')['y']
            accelerometer_z = sensor.get_value('accelerometer')['z']

            accelerometer_average = (accelerometer_x + accelerometer_y + accelerometer_y)/3

            recorded_data.append([label, accelerometer_x, accelerometer_y, accelerometer_z, accelerometer_average])
            print(f"Time: {recording_time} | {accelerometer_x} | {accelerometer_y} | {accelerometer_z} | {accelerometer_average}")
            recording_time += 0.1
        
        if is_tracking and recording_time >= MAX_COLLECTING_TIME:
            # stop recording
            is_tracking = False

            # make csv data | alternative with pandas df.to_csv
            file_name = './data/' + label + '01.csv' # TODO some more automation/information
            with open(file_name, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=' ',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(ROW_HEADER)
                writer.writerows(recorded_data)
            print("csv-file created, you can record another motion now")
            is_tracking = False
            recording_time = 0
            recorded_data = []

    time.sleep(RECORD_FREQUENCY)

    