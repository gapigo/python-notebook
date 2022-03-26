# https://stackoverflow.com/questions/2860153/how-do-i-get-the-parent-directory-in-python
# related with 220325b.py
print('220325b test in __init__.py')
import os
from pathlib import Path
path = Path("/here/your/path/file.txt")
print(path.parent.absolute())

print(__name__)
print(__file__)  # get full path
print(os.path.basename(__file__))  # get only the file name

path = Path(__file__)
print(os.path.basename(path.parent.absolute()))
