from setuptools import setup, Extension
import pybind11


module = Extension(
    'filter',
    sources=['filter.cpp'],
    include_dirs=[pybind11.get_include()],
    language='c++',
    extra_compile_args=['-std=c++11'],
)

setup(
    name='filter',
    version='1.0',
    description='C++ filter module for Whiteboard Polling',
    ext_modules=[module],
)