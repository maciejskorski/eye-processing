"""Sphinx configuration."""

from cgitb import enable
import os
import sys
sys.path.insert(0, os.path.abspath('../source'))

# General information about the project.
project = "Eye Processing"
author = "Maciej Skorski"
copyright = "2022, Maciej Skorski"

# Sources
source_suffix = ['.md']

# Extensions
extensions = [
    #"sphinx.ext.autodoc",
    #"sphinx.ext.napoleon",
    #"sphinx_click",
    "myst_parser",
]
#autodoc_typehints = "description"
#html_theme = "furo"
