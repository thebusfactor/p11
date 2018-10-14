# MIT License
# Copyright (c) 2018 ENGR301-302-2018 / Project-11

from json import load
from cv2 import imread
from model.ai import Ai

# set up the ai classification
ai = Ai()

# load the data from a json file
with open("imagedata.json", "r") as read_file:
    data = load(read_file)

    test_data_size = len(data.get("images"))
    correct_test_data = 0

    for test_case in data.get("images"):
        # assign variables
        image_id = test_case.get("id")
        count = test_case.get("count")
        # Load image
        img = imread(test_case.get("path"))
        print(image_id)
        test_val = (ai.classify(img))

        if count == len(test_val):
            correct_test_data += 1

    accuracy = correct_test_data/test_data_size
    print(float("{0:.5f}".format(accuracy)))

    assert(accuracy >= 0.9)
