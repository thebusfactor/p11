import os
import signal
import sys
import threading



from model.model import Model
from model.video import Video
from ui.view.video_view import CameraView


def main(argv):
    # output_specific_number_of_images(1, 0, 200, 200, 400, 400)
    # output_video()
    fps: int = 30

    video_model = Video('./src/model/vid.avi')
    video_view = Video('./src/model/vid.avi')
    model = Model(video=video_model, fps=fps)

    model_thread = threading.Thread(target=model.start)
    model_thread.daemon = True
    model_thread.start()

    # GUI().run()
    # GUI().stop()
    CameraView(video=video_view, fps=fps).run()
    sys.exit(1)
    pass


if __name__ == "__main__":
    main(sys.argv)

