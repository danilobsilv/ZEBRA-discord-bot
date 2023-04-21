from setuptools import setup
from setuptools import find_packages

setup(
      name = "ZEBRA discord bot",
    
      version = "1.0.0",
    
      author = "Danilo Bruno da Silva",

      author_email = "danilobsilv@gmail.com",
    
      description = "Discord bot for Brazilian football championship info and updates",

      install_requires = ["discord.py 2.2.2"],

      packages = find_packages(),

      classifiers = [
            "Programming Language :: Python :: 3.9.13",
            "License :: MIT license",
            "Operating System :: Windows 11"
      ]
)