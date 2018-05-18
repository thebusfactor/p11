import sys

from controller.output import *
#from ui.sample import Gui


def main(argv):
    output_specific_number_of_images(1, 1, 200, 200, 400, 400)
    #output_video()
    pass


if __name__ == "__main__":
    main(sys.argv)