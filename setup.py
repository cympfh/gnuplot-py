from setuptools import find_packages, setup

setup(name='gnuplot',
      version='0.2.0b',
      author='cympfh',
      author_email='cympfh@gmail.com',
      install_requires=[],
      packages=find_packages(exclude=["examples/*", "examples", "README.md"]),
      )
