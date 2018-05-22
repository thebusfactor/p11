import sys

from ui.view.gui import GUI


def main(argv):
    GUI().run()
    sys.exit(1)
    pass


if __name__ == "__main__":
    main(sys.argv)

