"""Sphinx configuration."""
project = "Eye Processing"
author = "Maciej Skorski"
copyright = "2022, Maciej Skorski"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
