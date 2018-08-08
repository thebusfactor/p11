from model.ai import start_ai
from model.ai import classify
import cv2 as cv

start_ai()
frame = cv.imread("Bus3.jpg")

img_width = 800
img_height = 600
confidence_threshold = 0.15

bus_colour = (0, 191, 255)
not_bus_colour = (0, 0, 0)

scaled_img = cv.resize(frame, (img_width, img_height))

classification = classify(scaled_img)

print(classification[0].tl)

window_name = 'image'
cv.namedWindow(window_name, cv.WINDOW_NORMAL)

#check every detected object
for i in range(0, len(classification)):
    c = classification[i]
    #confidence level of detected object has to be above threshold
    if(c.conf > confidence_threshold):
        if(c.label == "bus"):
            cv.rectangle(scaled_img, (c.tl.get('x'), c.tl.get('y')), (c.br.get('x'), c.br.get('y')),bus_colour,2)
            cv.putText(scaled_img, c.label,
                       (c.tl.get('x'), c.tl.get('y') + 15), cv.FONT_HERSHEY_SIMPLEX, 0.7, bus_colour, 2)
        else:
            cv.rectangle(scaled_img, (c.tl.get('x'), c.tl.get('y')), (c.br.get('x'), c.br.get('y')),not_bus_colour,2)
            cv.putText(scaled_img, c.label,
                       (c.tl.get('x'), c.tl.get('y') + 15), cv.FONT_HERSHEY_SIMPLEX, 0.7, not_bus_colour, 2)

cv.imshow(window_name,scaled_img)
cv.resizeWindow(window_name, img_width, img_height)
cv.waitKey(0)
cv.destroyAllWindows()
