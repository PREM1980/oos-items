import random
from rect import RectXY


def get_rgb():
	r = lambda: random.randint(0, 255)
	return r(), r(), r()

def convert_list_to_rect_object(rect_list):
	return [RectXY(each) for each in rect_list]

	
a = [[60, 350, 200, 400],[250, 350, 350, 400],[385, 350, 460, 400]]

convert_list_to_rect_object(a)