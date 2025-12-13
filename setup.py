from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        print(requirements)         # just to check what we are reading from requirements.txt
        requirements = [req.replace("\n","") for req in requirements]       # remove the \n from each line
        print(requirements)         # just to check what is the chanes

        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements

setup(
    name="Ml Project" ,
    version="0.0.1",
    author="Bibek Gupta",
    author_email="biplabupta50@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)