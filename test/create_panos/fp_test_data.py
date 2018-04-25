import sys
import os
# add to path variable
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
for path in sys.path:
	print path
from utils.utils import get_rgb
from fp_test_1 import test_1_data
from fp_test_2 import test_2_data
from fp_test_3 import test_3_data
from fp_test_4 import test_4_data
from fp_test_5 import test_5_data



test_1_data()
test_2_data()
test_3_data()
test_4_data()
test_5_data()