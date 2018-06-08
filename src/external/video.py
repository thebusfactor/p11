import cv2


class Video:

    def __init__(self, path):
        self.path = path
        self.video = open_video(path)

    def get_frame(self):
        ret, frame = self.video.read()
        return frame

    def reset_video(self):
        self.video = cv2.VideoCapture(self.path)


def open_video(path):
    video = cv2.VideoCapture(path)
    return video
