# this program visualizes activities with pyglet
import os
import pyglet
from pyglet import window

from continuous_activity_recognizer import ActivityRecognizer

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

activity_text_label = pyglet.text.Label(text=f"Start/Connect your DIPPID device", x=10, y=380, color=(0, 0, 0, 255),
                                        font_size=16, batch=batch, group=foreground)


# initialize the activity recognizer
recognizer = ActivityRecognizer()


def check_prediction(dt):
    # gets prediction from DIPPID sensor data
    predicted_label = recognizer.get_prediction()

    # change picture accordingly to predicted data
    if predicted_label == 1:
        activity.image = standing_img
        activity_text_label.text = "currently standing!"
    elif predicted_label == 2:
        activity.image = walking_img
        activity_text_label.text = "currently walking!"
    elif predicted_label == 3:
        activity.image = punching_img
        activity_text_label.text = "currently punching!"
    else:
        return

@window.event
def on_draw():
    window.clear()
    batch.draw()

pyglet.clock.schedule_interval(check_prediction, 0.01) # 0.01 for faster recognition
pyglet.app.run()

