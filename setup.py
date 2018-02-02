from setuptools import find_packages, setup

setup(name='gnuplot',
      version='0.1',
      author='cympfh',
      author_email='cympfh@gmail.com',
      install_requires=[],
      packages=find_packages(exclude=["tests.*", "tests", "README.md"]),
      )
