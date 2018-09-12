# MIT License
# Copyright (c) 2018 ENGR301-302-2018 / Project-11

import json
import os


# constructs a json file of test images

def build_json_file(filepath):
    """
        grabs all images within a file path under sub dirs
        zero, one, & two to put into json source file for
        test classification

        Parameters
        ----------
         filepath: String
            the path to dir that contains sub dirs zero, one, & two
    """

    # create the dict object to populate
    data = {'images': []}
    index = 0

    for subdir, dirs, files in os.walk(filepath):
        for file in files:
            wholepath = os.path.join(subdir, file)
            path_prefix = "../../../resources/testImages/"

            count = -1

            # Make a new relative path for the image
            if "Zero" in wholepath:
                count = 0
                newpath = path_prefix + "Zero/" + file
                print(newpath)
            elif "One" in wholepath:
                count = 1
                newpath = path_prefix + "One/" + file
                print(newpath)
            elif "Two" in wholepath:
                count = 2
                newpath = path_prefix + "Two/" + file
                print(newpath)

            data['images'].append({
                'id': index,
                'path': newpath,
                'count': count
            })
            index += 1

    # saves the to json file
    with open('imagedata.json', 'w') as outfile:
        json.dump(data, outfile, sort_keys=True, indent=4)


# build the json file with absolute pathing, since its just a utility script
build_json_file("../../../resources/TestImages")
