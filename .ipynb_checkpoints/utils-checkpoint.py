#!/usr/bin/env python
import sys
import os

def get_student_repo(student_repo_path):
    if os.path.isdir(student_repo_path):
        print("Updating %s"%student_repo_path)
        cmd = "cd %s && git pull"%student_repo_path 
        r = os.system(cmd)
        if r != 0:
            print("Command failed:",cmd)
    else:
        cmd = "cd .. && git clone https://github.com/csc-369-2021-fall/csc-369-student.git"
        r = os.system(cmd)
        if r != 0:
            print("Command failed:",cmd)

def get_identifier():
    path = os.getcwd()

    identifier = "-".join(path.split("/")[-1].split("-")[:2])
    return identifier

def get_subdir(identifier):
    subdir = None
    if "lab-" in identifier:
        print("Auto-detected that this is a lab")
        subdir="labs"
    elif "chapter-" in identifier:
        print("Auto-detected that this is a chapter")
        subdir="chapters"
    elif "tutorial-" in identifier:
        print("Auto-detected that this is a tutorial")
        subdir="tutorials"
    else:
        print("Auto-detected that this is an assignment")
        subdir="assignments"

def get_name(subdir,identifier):
    if subdir != "assignments":
        name = "".join([c[0].upper()+c[1:] for c in identifier.split("-")])
    else:
        name = identifier.split("-")[0]
        name = name[0].upper()+name[1:]