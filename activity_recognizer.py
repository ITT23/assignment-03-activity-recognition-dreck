# this program recognizes activities
import numpy as np
import pandas as pd
import os
from sklearn import svm
from DIPPID import SensorUDP


# holds DIPPID sensor datas and the classifier
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

    # trains the svm classifier
    def _train(self):
         # get all csv files, platform-independent | hint from chatGPT
        csv_files = [file for file in os.listdir(self.CSV_PATH) if file.endswith('.csv')]

        # csv files are stored in a dataframe
        # the accelerometer_avg data of every recorded motion is processed with fft for better differentiation of motions
        # spectrum data gets saved as a array in a new dataframe with its corresponding label
        # classifier learns spectrum and not single accelerometer data
        for file in csv_files:
            path = os.path.join(self.CSV_PATH, file)
            single_dataframe = pd.read_csv(path, delimiter=" ")
            fft_data = np.abs(np.fft.fft(single_dataframe['accelerometer_avg'].to_numpy()))
            label = single_dataframe['label'][1]
            data_help = [label, fft_data]
            self.data.append(data_help)

        # textlabels are now numbers
        df = pd.DataFrame(self.data, columns=['label', 'spectrum'])
        df.loc[df["label"] == "standing", "label"] = 1
        df.loc[df["label"] == "walking", "label"] = 2
        df.loc[df["label"] == "punching", "label"] = 3
        df['label'] = df['label'].astype('int64')

        classifier = svm.SVC(kernel='linear')

        X_train = df['spectrum'] # spectrum data for training
        Y_train = df['label'] # label data for training

        # X_train has to be a 1D-Array
        # Google search of problem brought me here: https://www.freecodecamp.org/news/how-to-fix-typeerror-only-size-1-arrays-can-be-converted-to-python-scalars/
        x = np.array(list(map(np.float_, X_train)))

        return classifier.fit(x, Y_train)
    
    # predits the current data
    def get_prediction(self):
        if self.sensor.get_value('button_1') == 1:
            self.button_pressed = True
            print("Collecting activity data...")

        if self.sensor.has_capability('accelerometer') and self.button_pressed:
            accelerometer_x = self.sensor.get_value('accelerometer')['x']
            accelerometer_y = self.sensor.get_value('accelerometer')['y']
            accelerometer_z = self.sensor.get_value('accelerometer')['z']

            # average data for fft
            accelerometer_average = (accelerometer_x + accelerometer_y + accelerometer_z) / 3 
            self.recorded_data.append(accelerometer_average)

            # training data is 50 samples long -> at 51 the first recorded sample is thrown out
            if len(self.recorded_data) == 51:
                self.recorded_data.pop(0)
                activity_spectrum = np.abs(np.fft.fft(self.recorded_data)) # fft
                label = self.classifier.predict([activity_spectrum])[0] # prediction
                print(f"label: {label}")

                # reset for new data
                self.predicted_label = label
                self.button_pressed = False
                self.recorded_data = []
                print("Activity predicted...")
                return label        
        return 0

    def get_record_button_pressed(self):
        return self.button_pressed