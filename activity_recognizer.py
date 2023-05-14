# this program recognizes activities
import numpy as np
import pandas as pd
import os
from sklearn import svm
from DIPPID import SensorUDP
from time import sleep

from sklearn.model_selection import GridSearchCV

class ActivityRecognizer:

    def __init__(self):
        self.PORT = 5700
        self.sensor = SensorUDP(self.PORT)
        self.CSV_PATH = './data'
        self.data = []
        self.classifier = self._train()
        self.recorded_data = []
        self.button_pressed = False
        self.predicted_label = ''

    def _train(self):
         # get all csv files, platform-independent
        csv_files = [file for file in os.listdir(self.CSV_PATH) if file.endswith('.csv')]
        for file in csv_files:
            path = os.path.join(self.CSV_PATH, file)
            single_dataframe = pd.read_csv(path, delimiter=" ")
            fft_data = np.abs(np.fft.fft(single_dataframe['accelerometer_avg'].to_numpy()))
            label = single_dataframe['label'][1]
            data_help = [label, fft_data]
            self.data.append(data_help)

        df = pd.DataFrame(self.data, columns=['label', 'spectrum'])
        df.loc[df["label"] == "standing", "label"] = 1
        df.loc[df["label"] == "walking", "label"] = 2
        df.loc[df["label"] == "punching", "label"] = 3
        df['label'] = df['label'].astype('int64')

        classifier = svm.SVC(kernel='linear')

        X_train = df['spectrum']
        Y_train = df['label']

        x = np.array(list(map(np.float_, X_train)))

        return classifier.fit(x, Y_train)
    
    def get_prediction(self):
        if self.sensor.get_value('button_1') == 1:
        #recorded_data = []
            self.button_pressed = True
            print("Collecting activity data...")

        if self.sensor.has_capability('accelerometer') and self.button_pressed:
            accelerometer_x = self.sensor.get_value('accelerometer')['x']
            accelerometer_y = self.sensor.get_value('accelerometer')['y']
            accelerometer_z = self.sensor.get_value('accelerometer')['z']

            accelerometer_average = (accelerometer_x + accelerometer_y + accelerometer_z) / 3
            self.recorded_data.append(accelerometer_average)
            if len(self.recorded_data) == 51:
                activity_spectrum = np.abs(np.fft.fft(self.recorded_data))
                label = self.classifier.predict([activity_spectrum])[0]
                print(f"label: {label}")
                #change_image(label)
                # recorded_data.pop(0)
                self.predicted_label = label
                self.button_pressed = False
                self.recorded_data = []
                print("Activity predicted...")
                return label        
        return 0

    def get_record_button_pressed(self):
        return self.button_pressed