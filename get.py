#!/usr/bin/env python
import sys
import os

import utils

utils.get_student_repo()

identifier = utils.get_identifier()
print("Identifier:",identifier)

subdir = utils.get_subdir(identifier)

name = utils.get_name(identifier)

if subdir is not None:
    if os.path.isfile("%s.ipynb"%name):
        print("File already exists. Rename it and run this program again if you want a fresh copy.")
        exit(1)

    print("Copying %s*"%name)
    cmd = "cp -Rp %s%s/%s* ."%(utils.student_repo_path,subdir,name)
    r = os.system(cmd)
    if r != 0:
        print("Command failed:",cmd)
        exit(1)

    print('You now have your chapter/assignment/lab')

