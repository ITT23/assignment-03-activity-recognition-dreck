# this program visualizes activities with pyglet
import os

import numpy as np
# import activity_recognizer
# from activity_recognizer import get_current_activity
import pyglet
from pyglet import window

from activity_recognizer import sensor, classifier

# Pyglet initialization
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

window = window.Window(WINDOW_WIDTH, WINDOW_HEIGHT)

batch = pyglet.graphics.Batch()
background = pyglet.graphics.Group(0)
foreground = pyglet.graphics.Group(1)

# chatgpt
white = pyglet.image.SolidColorImagePattern((255, 255, 255, 255))
white = white.create_image(window.width, window.height)
white_bg = pyglet.sprite.Sprite(white, batch=batch, group=background)


print("hello")
# images:
# https://www.svgrepo.com/svg/19155/running-stick-figure
path_walking = os.path.join(".", "images", "walking.png")
# https://www.svgrepo.com/svg/173423/man-standing-black-silhouette
path_standing = os.path.join(".", "images", "standing.png")
# https://www.svgrepo.com/svg/323070/punching-bag
path_punching = os.path.join(".", "images", "punching.png")
# https://www.svgrepo.com/svg/404026/question-mark
path_question = os.path.join(".", "images", "questionmark.png")


walking_img = pyglet.image.load(path_walking)
standing_img = pyglet.image.load(path_standing)
punching_img = pyglet.image.load(path_punching)
question_img = pyglet.image.load(path_question)


activity = pyglet.sprite.Sprite(question_img, x=60, y=50, batch=batch, group=foreground)

activity_text_label = pyglet.text.Label(text=f"Start to track your activities.", x=10, y=380, color=(0, 0, 0, 255),
                                        font_size=16, batch=batch, group=foreground)

activity_text_label_explanation = pyglet.text.Label(text=f"Press button_1 to make a new detection.", x=10, y=360,
                                                    color=(0, 0, 0, 255), font_size= 10, batch=batch, group=foreground)


@window.event
def on_draw():
    window.clear()
    batch.draw()


button_pressed = False
recorded_data = []


def change_image(label):
    if label == 1:
        activity.image = standing_img
        activity_text_label.text = "standing detected!"
    if label == 2:
        activity.image = walking_img
        activity_text_label.text = "walking detected!"
    if label == 3:
        activity.image = punching_img
        activity_text_label.text = "punching detected!"
    else:
        return

def get_label(dt):
    global button_pressed
    global recorded_data

    if sensor.get_value('button_1') == 1:
        recorded_data = []
        button_pressed = True
        print("Collecting activity data...")

    if sensor.has_capability('accelerometer') and button_pressed:
        accelerometer_x = sensor.get_value('accelerometer')['x']
        accelerometer_y = sensor.get_value('accelerometer')['y']
        accelerometer_z = sensor.get_value('accelerometer')['z']

        accelerometer_average = (accelerometer_x + accelerometer_y + accelerometer_z) / 3
        recorded_data.append(accelerometer_average)
        if len(recorded_data) == 51:
            activity_spectrum = np.abs(np.fft.fft(recorded_data))
            label = classifier.predict([activity_spectrum])[0]
            print(f"label: {label}")
            change_image(label)
            # recorded_data.pop(0)
            button_pressed = False
            print("Activity predicted...")


pyglet.clock.schedule_interval(get_label, 0.01)

pyglet.app.run()

