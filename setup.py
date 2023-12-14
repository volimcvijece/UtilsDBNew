#from setuptools import setup
from setuptools import setup, find_packages

setup(
    name='UtilsDB',
    version='0.0.4',
    description='Utility functions for SQL Server connections and queries',
    url='git@github.com:volimcvijece/UtilsDBNew.git',
    author='Tonko Caric',
    author_email='caric.tonko@gmail.com',
    license='unlicensed',
    #packages=find_packages(),
    packages=find_packages(where="src"),
    package_dir={'': 'src'},
    #install_requires=['pandas', 'pyodbc', 'numpy'], #no nr - any version. specify - "numpy>=1.13.3"
    install_requires=['pandas', 'pymssql', 'numpy'], #no nr - any version. specify - "numpy>=1.13.3"
    zip_safe=False
)