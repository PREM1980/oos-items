# import sys
# sys.path.append('../rect_tutorial')
# print sys.path

import numpy as np
import cv2
import random

font                   = cv2.FONT_HERSHEY_SIMPLEX
# bottomLeftCornerOfText = (10,500)
fontScale              = .5
fontColor              = (255,255,255)
lineType               = 1

class CreatePano(object):
    def __init__(self, pano_x_position='', pano_y_position=''):
        self.pano_x_position = pano_x_position
        self.pano_y_position = pano_y_position
        self.img = self._blank_image()
        self._create_sections()
        self._create_shelves_and_labels()
        self._write_image()

    def _blank_image(self):
        return np.zeros((self.pano_x_position, self.pano_y_position, 3), np.uint8)

    def _create_sections(self):
        cv2.rectangle(self.img, (0, 0), (25, 550), (0, 69, 255), -1)
        section_x2 = self.pano_x_position
        x1, x2 = section_x2-25, section_x2
        print 'section x1 = {0}, x2 ={1}'.format(x1, x2)
        cv2.rectangle(self.img, (x1, 0), (x2, self.pano_y_position), (0, 69, 255), -1)


    def _create_shelves_and_labels(self):
        x1, x2 = 25, 525
        y1, y2 = 450, 550
        incr = 25
        label_text_incr = 1
        miss_product_ctr = 1
        r = lambda: random.randint(0, 255)
        rgb = r(), r(), r()
        final_labels = []
        final_products = []
        for each in range(1):
            for each in range(1):
                print 'shelves x1={0},x2={1},y1={2},y2={3}'.format(x1,x2,y1,y2)
                cv2.rectangle(self.img, (x1, y1), (x2, y2), (255, 0, 255), 3)
                random_miss_prod =  random.randint(1,5)
                for each in range(incr,x1+500,100): # Labels
                    # print ' x1={0},x2={1},y1={2},y2={3}'.format(each, each+100, y1 + 10 ,y2- 10)
                    final_labels.append('x1={x1},y1={y1},x1={x1},x2={x2}'.format
                        (x1=each, x2=each+100, y1=y1 + 10,y2=y2- 10))
                    cv2.rectangle(self.img, (each + 10, y1+10), (each + 100,y2-10), (rgb), -1)                    
                    # cv2.rectangle(self.img, (each, y1), (each + 100,y2), (rgb), -1)                    
                    r = lambda: random.randint(0, 255)
                    rgb = r(), r(), r()
                    cv2.putText(self.img,'L' + str(label_text_incr), 
                                (each+20,y2-20), 
                                font, 
                                fontScale,
                                rgb,
                                lineType)                    
                    if miss_product_ctr != random_miss_prod:
                        cv2.rectangle(self.img, (each + 10, y1-300), (each + 100,y2-120), (rgb), -1)
                        # print ' px1={0},px2={1},py1={2},py2={3}'.format(each+10, y1-300, each+100, y2-120)
                        final_products.append('px1={px1},py1={px2},px2={px1},py2={py2}'.format
                            (px1=each+10, py1=y1-300, px2=each+100, py2=y2-120))
                        cv2.putText(self.img,'P' + str(label_text_incr), 
                                    (each+20,y2-130), 
                                    font, 
                                    fontScale,
                                    fontColor,
                                    lineType)
                    label_text_incr += 1
                    miss_product_ctr += 1
                miss_product_ctr = 1
                y1 = y1 + 500
                y2 = y2 + 500
            incr = incr + 525
            # break
            x1 = x1 + 525
            x2 = x2 + 525
            y1, y2 = 450, 500
            # print x1

        print 'labels'
        for each in final_labels:
            print each
        print 'products'
        for each in final_products:
            print each
    def _write_image(self):
        cv2.imwrite('test/condition-1.jpg', self.img)

if __name__ == "__main__":
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    # print sys.path
    from rect import RectXY
    shelves = RectXY([25, 125,460,540],is_wh=False)
    labels = [
            RectXY([125,225,460,540], is_wh=False),
            RectXY([225,325,460,540], is_wh=False),
            RectXY([325,425,460,540], is_wh=False),
            RectXY([425,525,460,540], is_wh=False)
            ]
    products = [
            RectXY([35 ,150,125,430], is_wh=False),
            RectXY([235,150,325,430], is_wh=False),
            RectXY([335,150,425,430], is_wh=False),
            RectXY([435,150,525,430], is_wh=False)
            ]
    cp = CreatePano(pano_x_position=550,pano_y_position=550)