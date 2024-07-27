#! /usr/bin/env python
# -*- coding: utf-8 -*-

#from iain_tree_development import enable_in_tree_development
#enable_in_tree_development()
#from src.iasimplesetup     import simplesetup
#simplesetup('iasimplesetup')

from typing       import Iterable

from setuptools   import Extension, find_packages, setup
from Cython.Build import cythonize

def get_extension(pkgname:str)->Extension:
    return Extension(
            f"{pkgname}.*",
            sources  = [f"src/{pkgname}/*.pyx",],
            language = "c++",)

def simplesetup(pkgname:str)->None:
    extension:Extension = get_extension(pkgname)
    setup(
        ext_modules         =cythonize([extension,]),
        packages            =[pkgname,],
        package_dir         = {
            pkgname : f'src/{pkgname}',
        },
        package_data        = {
            '': ['*.so'],
            '': ['sql/*.sql'],
        },
        exclude_package_data= {
            '': ['*.cpp', '*.pyx', '*.py',]
        }
    )

simplesetup('ghelephant')
