from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    Reads the requirements.txt file and returns a list of dependencies.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Remove newline characters
        requirements = [req.replace("\n", "") for req in requirements]

        # Remove '-e .' if it exists so it doesn't try to install it as a package from PyPI
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
    return requirements

setup(
    name='nlp-triage-project',
    version='0.0.1',
    author='Nishit',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)