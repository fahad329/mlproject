from setuptools import find_packages,setup
from typing import List


HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
        This funtion will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

setup(
    name="ML Project",
    version="1.0.0",
    author="Fahad Farooq",
    author_email="kh_fahad_farooq@yahoo.com",
    pakages = find_packages(),
    install_requires = get_requirements('requirements.txt')  
    )
