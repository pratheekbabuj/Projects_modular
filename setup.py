from setuptools import find_packages, setup 
from typing import List



edot= "-e ."


def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ")for req in requirements]

        if edot in requirements:
            requirements.remove(edot)


    return requirements    

setup(
    name='regressorproject',
    version='0.0.1',
    author='pratheek',
    author_mail='pratheekbau@gmail.com',
    install_req = get_requirements("requirements.txt"),
    packages=find_packages()

)