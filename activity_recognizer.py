# this program recognizes activities
import numpy as np
import pandas as pd
import os
from sklearn import svm
from DIPPID import SensorUDP
from time import sleep

from sklearn.model_selection import GridSearchCV


# use UPD (via WiFi) for communication
PORT = 5700
sensor = SensorUDP(PORT)

csv_path = './data'

# 10 values per Second
sampling_rate = 10

# get all csv files, platform-independent
csv_files = [file for file in os.listdir(csv_path) if file.endswith('.csv')]

data = []

new_d = pd.DataFrame(columns=["label", "spectrum"])
all_data = pd.DataFrame(columns=["label", "spectrum"])
for file in csv_files:
    path = os.path.join(csv_path, file)
    single_dataframe = pd.read_csv(path, delimiter=" ")
    fft_data = np.abs(np.fft.fft(single_dataframe['accelerometer_avg'].to_numpy()))
    label = single_dataframe['label'][1]
    data_help = [label, fft_data]
    data.append(data_help)

df = pd.DataFrame(data, columns=['label', 'spectrum'])
df.loc[df["label"] == "standing", "label"] = 1
df.loc[df["label"] == "walking", "label"] = 2
df.loc[df["label"] == "punching", "label"] = 3
df['label'] = df['label'].astype('int64')


classifier = svm.SVC(kernel='linear')

X_train = df['spectrum']
Y_train = df['label']

x = np.array(list(map(np.float_, X_train)))

classifier.fit(x, Y_train)

'''
button_pressed = False
recorded_data = []

label = 0


def get_current_activity():
    return label


while True:
    if sensor.get_value('button_1') == 1:
        recorded_data = []
        button_pressed = True
        print("Collecting activity data...")

    if sensor.has_capability('accelerometer') and button_pressed:
        accelerometer_x = sensor.get_value('accelerometer')['x']
        accelerometer_y = sensor.get_value('accelerometer')['y']
        accelerometer_z = sensor.get_value('accelerometer')['z']

        accelerometer_average = (accelerometer_x + accelerometer_y + accelerometer_y) / 3
        recorded_data.append(accelerometer_average)
        if len(recorded_data) == 51:
            activity_spectrum = np.abs(np.fft.fft(recorded_data))
            label = classifier.predict([activity_spectrum])[0]
            print(f"label: {label}")
            # recorded_data.pop(0)
            button_pressed = False
            print("Activity predicted...")

    sleep(0.01)
'''