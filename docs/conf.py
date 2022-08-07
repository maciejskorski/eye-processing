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
master_doc = 'index'

# Extensions
extensions = [
    #"sphinx.ext.autodoc",
    #"sphinx.ext.napoleon",
    #"sphinx_click",
    #"myst_parser",
    "myst_nb",
    "sphinxcontrib.bibtex",
]
bibtex_bibfiles = ['citations.bib']

html_theme = "sphinx_book_theme"
html_theme_options = {
    "repository_url": "https://github.com/maciejskorski/eye-processing/",
    "repository_branch": "dev",
    "path_to_docs": "docs",
}

nb_execution_mode = "off"