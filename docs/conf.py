"""Sphinx configuration."""
project = "PeteE GPT"
author = "Pete Erickson"
copyright = "2023, Pete Erickson"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
