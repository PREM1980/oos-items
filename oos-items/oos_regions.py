import sys
import os
import pkgutil
# add to path variable
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from test.create_panos import fp_test_1

test_data = [fp_test_1.get_test_data()]

for each in test_data:
	
