# MIT License
# Copyright (c) 2018 ENGR301-302-2018 / Project-11

import os
import sys
import threading

from controller.controller import Controller
from model.ai import *
from model.model import Model
from ui.debug_ui import DebugGUI
from external.cam import Cam


def main(argv):
    fps: int = 24
    res = (1280, 720)

    fixed_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(fixed_path, "../../resources/vid.avi")

    # cam = Cam(path)
    cam = Cam(None)
    model = Model(cam, fps, res)
    view = DebugGUI()

    Controller(model, view)

    model.start()

    # start_ai()

    # model_thread = threading.Thread(target=model.start)
    # model_thread.daemon = True
    # model_thread.start()
    # sys.exit(1)


if __name__ == "__main__":
    main(sys.argv)

