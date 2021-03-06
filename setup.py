from distutils.core import setup
from Cython.Build import cythonize
import numpy as np

setup(
    ext_modules = cythonize(["mst.pyx", "genie.pyx"], include_path=[np.get_include()])
)
