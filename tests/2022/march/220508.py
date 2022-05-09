# Running windows shell commands with python
# https://stackoverflow.com/questions/14894993/running-windows-shell-commands-with-python

import os
from subprocess import check_output
#check_output("dir C:", shell=True)
#check_output("ls", shell=True)
os.system('ls')
