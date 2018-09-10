import json
import cv2
import unittest
from model.ai import Ai

# set up the ai classification
ai = Ai()

# load the data from a json file
with open("imagedata.json", "r") as read_file:
    data = json.load(read_file)

    test_data_size = len(data.get("images"))
    correct_test_data = 0

    for test_case in data.get("images"):
        # assign variables
        image_id = test_case.get("id")
        count = test_case.get("count")
        # Load image
        img = cv2.imread(test_case.get("path"))
        print("---")
        print(id)
        test_val = (ai.classify(img))
        print(len(test_val))
        print("---")

        if count == len(test_val):
            correct_test_data += 1

    accuracy = correct_test_data/test_data_size
    print(float("{0:.2f}".format(accuracy)))

    assert(correct_test_data == test_data_size)
