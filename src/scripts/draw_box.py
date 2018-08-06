import os
import matplotlib.pyplot as plt
import cv2 as cv
from matplotlib.widgets import RectangleSelector
from generate_xml import write_xml

img = None
tl_list = []
br_list = []
object_list = []

fixed_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(fixed_path, "../../../resources")

image_folder = "/toClass"
save_dir = "/annotations"
obj = "bus"


def select(clk, rls):
    global tl_list
    global br_list
    global object_list
    tl_list.append((int(clk.xdata), int(clk.ydata)))
    br_list.append((int(rls.xdata), int(rls.ydata)))
    object_list.append(obj)


def on_key_press(event):
    global object_list
    global tl_list
    global br_list
    global img
    if event.key == "q":
        write_xml(path+image_folder, img, object_list, tl_list, br_list, path+save_dir)
        tl_list = []
        br_list = []
        object_list = []
        img = None
        plt.close()


def toggle_selector(event):
    toggle_selector.RS.set_active(True)


if __name__ == '__main__':
    print(fixed_path)
    print(path)
    print(path+image_folder)
    for n, image_file in enumerate(os.scandir(path+image_folder)):
        img = image_file
        fig, ax = plt.subplots(1)
        image = cv.imread(image_file.path)
        image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        ax.imshow(image)
        toggle_selector.RS = RectangleSelector(
            ax, select,
            drawtype='box', useblit=True,
            button=[1], minspanx=5, minspany=5,
            spancoords='pixels', interactive=True
        )
        bbox = plt.connect("key_press_event", toggle_selector)
        key = plt.connect("key_press_event", on_key_press)
        plt.show()










