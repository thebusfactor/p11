#MIT License
#Copyright (c) 2018 ENGR301-302-2018 / Project-11

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

    fixed_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(fixed_path, "../resources/vid.avi")

    video = Video(path)
    model = Model(video=video, fps=fps, res=res)

    view = ConfigView(video=video, fps=fps, res=res)

    Controller(model,view, res)

    model_thread = threading.Thread(target=model.start)
    model_thread.daemon = True
    model_thread.start()

    view.run()
    sys.exit(1)

    pass


if __name__ == "__main__":
    main(sys.argv)

