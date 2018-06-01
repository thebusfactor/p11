import cv2


class Video:

    def __init__(self, path: str):
        self.path = path
        self.video = open_video(path)

    def get_frame(self):
        ret, frame = self.video.read()
        print(ret)
        return frame


def open_video(path: str):
    video = cv2.VideoCapture(path)
    return video
