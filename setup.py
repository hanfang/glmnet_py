import os, sys
from setuptools import setup, find_packages
# from numpy.distutils.core import setup, Extension

cmd = 'gfortran ./glmnet_py/GLMnet.f -fPIC -fdefault-real-8 -shared -o ./glmnet_py/GLMnet.so'
os.system(cmd)

setup(name='glmnet_py',
      version = '0.1.0b1',
      description = 'Python version of glmnet, originally from Stanford University, modified by Han Fang',
      long_description=open('README.md').read(),
      url="https://github.com/hanfang/glmnet_py",
      author = 'Han Fang',
      author_email = 'hanfang.cshl@gmail.com',
      license = 'GPL-2',
      packages=['glmnet_py'],
      install_requires=['joblib>=0.10.3'],
      package_data={'glmnet_py': ['*.so', 'glmnet_py/*.so']},
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Mathematics',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Operating System :: Unix',
        ],
      keywords='glm glmnet ridge lasso elasticnet',
      )

