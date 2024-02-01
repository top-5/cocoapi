from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension
# from setuptools import setup, Extension
import numpy as np

# To compile and install locally run "python setup.py build_ext --inplace"
# To install library to Python site-packages run "python setup.py build_ext install"

ext_modules = [
    Extension(
        'pycocotools._mask',
        sources=['../common/maskApi.c', 'pycocotools/_mask.pyx'],
        include_dirs = [np.get_include(), '../common'],
        extra_compile_args=[] # originally was ['-Wno-cpp', '-Wno-unused-function', '-std=c99'],
    )
]

setup(name='pycocotools',
      packages=['pycocotools'],
      package_dir = {'pycocotools': 'pycocotools'},
      setup_requires=[
        'setuptools>=18.0',
        'cython>=3.0.8'
      ],
      install_requires=[
        'setuptools>=18.0',
        'cython>=3.0.8',
        'matplotlib>=3.8.2'
      ],
      version='2.0.7',
      ext_modules=
          cythonize(ext_modules)
      )
