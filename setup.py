"""Setup module for NI Veristand."""
from os.path import dirname
from os.path import join
from setuptools import find_packages
from setuptools import setup


pypi_name = 'niveristand'


def get_version(name):
    """Calculate a version number."""
    import os
    version = None
    script_dir = os.path.dirname(os.path.realpath(__file__))
    script_dir = os.path.join(script_dir, name)
    if not os.path.exists(os.path.join(script_dir, 'VERSION')):
        version = '2.0.0'
    else:
        with open(os.path.join(script_dir, 'VERSION'), 'r') as version_file:
            version = version_file.read().rstrip()
    return version


def read_contents(file_to_read):
    """Read a file in this folder."""
    with open(join(dirname(__file__), file_to_read), 'r') as f:
        return f.read()


setup(
    name=pypi_name,
    version=get_version(pypi_name),
    description='NI VeriStand Python API',
    long_description=read_contents('README.rst'),
    author='National Instruments',
    maintainer="Marcelo Izaguirre",
    maintainer_email="marcelo.izaguirre@ni.com",
    url="https://github.com/ni/niveristand-python",
    keywords=['niveristand', 'veristand'],
    license='MIT',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=['pythonnet', 'PyYAML'],
    tests_require=['pytest', 'numpy'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Testing"
    ],
    package_data={pypi_name: ['VERSION']},
)
