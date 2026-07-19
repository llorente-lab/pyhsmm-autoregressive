# eg. see https://backend.pdm-project.org/hooks/#call-setup-function-to-build-extensions
import os
from Cython.Build import cythonize
import numpy
from setuptools.extension import Extension

extensions = [
    Extension(
        'autoregressive.messages',
        [os.path.join('autoregressive','messages.pyx')],
        extra_compile_args=['-O2', '-std=c++11', '-DEIGEN_NO_MALLOC', '-DNDEBUG','-w','-DHMM_TEMPS_ON_HEAP']
    )
]

ext_modules = cythonize(extensions)

def pdm_build_update_setup_kwargs(context, setup_kwargs):
    setup_kwargs.update(
        ext_modules=ext_modules,
        include_dirs=[numpy.get_include(), 'deps'],
    
    )
