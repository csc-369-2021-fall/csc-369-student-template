#!/usr/bin/env python
import sys
import os

import joblib

from pathlib import Path
home = str(Path.home())

from IPython.display import display, Markdown, Latex

student_repo="csc-369-student"
student_repo_path=f"{home}/{student_repo}"
github_organization="csc-369-2021-fall"

def get_student_repo():
    if os.path.isdir(student_repo_path):
        print("Updating %s"%student_repo_path)
        cmd = "cd %s && git pull"%student_repo_path 
        r = os.system(cmd)
        if r != 0:
            print("Command failed:",cmd)
        else:
            print("Success")
    else:
        cmd = f"cd .. && git clone https://github.com/{github_organization}/csc-369-student.git"
        r = os.system(cmd)
        if r != 0:
            print("Command failed:",cmd)
        else:
            print("Success")

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

def get_name(identifier):
    #if subdir != "assignments":
    name = "".join([c[0].upper()+c[1:] for c in identifier.split("-")])
    #else:
    #    name = identifier.split("-")[0]
    #    name = name[0].upper()+name[1:]
    return name

def print_autograder_info(exercise_number):
    identifier = get_identifier()
    name = get_name(identifier)
    answers = joblib.load(f"{student_repo_path}/tests/answers_{name}.joblib")
    for key in answers.keys():
        if int(key.split("_")[-1]) == exercise_number:
            display(Markdown(f"## Information for {key}"))
            display(answers[key])
