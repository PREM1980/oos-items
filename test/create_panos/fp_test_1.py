import numpy as np
import cv2
import random
from utils.utils import get_rgb, convert_list_to_rect_object

font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10,500)
fontScale              = .5
fontColor              = (255,255,255)
lineType               = 1

def get_test_data():
    print 'prepare test_1 data'
    products_rect = [
            [50, 200, 150, 330],
            [151, 200, 250, 330],
            [251, 200, 350, 330],
            [351, 200, 450, 330],
            # [451, 200, 520, 330],
            ]

    labels_rect = [
            [50, 350, 150, 400],
            [151, 350, 250, 400],
            [251, 350, 350, 400],
            [351, 350, 450, 400]
            ]

    img = np.zeros((500, 500, 3), np.uint8)

    # bounding box
    cv2.rectangle(img, (50, 50), (450, 450), (get_rgb()), 0)

    # products
    for each in products_rect:
        cv2.rectangle(img, (each[0],  each[1]), (each[2], each[3]), (get_rgb()), -1)

    # labels
    for each in labels_rect:
        cv2.rectangle(img, (each[0],  each[1]), (each[2], each[3]), (get_rgb()), -1)


    # write to output file
    cv2.imwrite('./panos/fp_test_1.jpg', img)

    return convert_list_to_rect_object(products_rect), convert_list_to_rect_object(labels_rect), \
        convert_list_to_rect_object([[50, 50, 450, 450]]), products_rect, labels_rect

# test_2()