import os
import sys
import threading

from controller.controller import Controller
from model.model import Model
from external.video import Video
from ui.view.config_view import ConfigView


def main(argv):
    fps: int = 24

    res = (1280, 720)

    video_model = Video('C:/Users/User/Music/8_6_18 bus factor/Bus-Factor/resources/vid.avi')
    model = Model(video=video_model, fps=fps, res=res)

    view = ConfigView(video=video_model, fps=fps, res=res)

    Controller(model,view, res)

    model_thread = threading.Thread(target=model.start)
    model_thread.daemon = True
    model_thread.start()

    view.run()
    sys.exit(1)

    pass


if __name__ == "__main__":
    main(sys.argv)

