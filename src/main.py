import sys
import threading

from controller.controller import Controller
from model.model import Model
from external.video import Video
from ui.view.config_view import ConfigView


def main(argv):
    fps: int = 24

    video_model = Video('C:/Users/Kristen/AppData/Local/Programs/Python/Bus-Factor/resources/vid.avi')
    video_view = Video('C:/Users/Kristen/AppData/Local/Programs/Python/Bus-Factor/resources/vid.avi')
    model = Model(video=video_model, fps=fps)

    view = ConfigView(video=video_view, fps=fps)

    Controller(model,view)

    model_thread = threading.Thread(target=model.start)
    model_thread.daemon = True
    model_thread.start()

    view.run()
    sys.exit(1)

    pass


if __name__ == "__main__":
    main(sys.argv)

