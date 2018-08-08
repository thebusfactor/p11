from model.ai import start_ai
from model.ai import classify
import cv2 as cv

start_ai()
frame = cv.imread("Bus1.jpg")
classify(frame)