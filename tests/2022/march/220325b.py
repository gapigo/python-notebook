# testing how to get name of the python file
# https://stackoverflow.com/questions/4152963/get-name-of-current-script-in-python

import os
print(__file__)  # get full path
print(os.path.basename(__file__))  # get only the file name