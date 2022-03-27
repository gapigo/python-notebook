import os
from pathlib import Path

# rootdir = Path(__file__)
rootdir = os.path.dirname(__file__)
testdir = os.path.join(rootdir, 'tests\\2022\\march')
print(testdir)

for file in os.listdir(testdir):
    d = os.path.join(testdir, file)
    print(file)
    # if os.path.isdir(d):
    #     print(d)