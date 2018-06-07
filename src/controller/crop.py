import cv2
import numpy as np


def crop_image(x1, y1, x2, y2, x4, y4, x3, y3, image_name):

    image = cv2.imread(image_name, -1)
    img_height, img_width, channels = image.shape

    x1 = x1*img_width
    y1 = y1*img_height

    x2 = x2*img_width
    y2 = y2*img_height

    x3 = x3*img_width
    y3 = y3*img_height

    x4 = x4*img_width
    y4 = y4*img_height

    mask = np.zeros(image.shape, dtype=np.uint8)

    roi_corners = np.array([[(x1,y1), (x2,y2), (x3,y3), (x4,y4)]], dtype=np.int32)
    channel_count = image.shape[2]
    ignore_mask_color = (255,)*channel_count
    cv2.fillPoly(mask, roi_corners, ignore_mask_color)

    masked_image = cv2.bitwise_and(image, mask)

    #generate cropping coordinates
    min_x = int(min(x1, x2, x3, x4))
    min_y = int(min(y1, y2, y3, y4))
    max_x = int(max(x1, x2, x3, x4))
    max_y = int(max(y1, y2, y3, y4))

    #crop the image
    crop_img = masked_image[min_y:min_y+(max_y-min_y), min_x:min_x+(max_x-min_x)]

    # save the result
    cv2.imwrite('yeet.png', crop_img)