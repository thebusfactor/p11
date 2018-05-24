import sys
import time
from ui.view import tray
from ui.view.gui import GUI


def main(argv):
    ##time.sleep(2)
    ##tray.start()
    GUI().run()
    pass


if __name__ == "__main__":
    main(sys.argv)

