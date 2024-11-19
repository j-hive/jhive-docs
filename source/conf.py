# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import morphfits
import jhive_previz
from importlib import resources as impresources
from jhive_previz import docsutil

# from . import previz

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "J-HIVE"
copyright = "2024, The J-HIVE Collaboration"
author = "The J-HIVE Collaboration"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.napoleon",
    # "sphinx.ext.autodoc",
    # "sphinx.ext.autosummary",
    "autoapi.extension",
    "sphinx_design",
    "sphinx_autodoc_typehints",
    "myst_nb",
]

templates_path = ["_templates"]
exclude_patterns = []

# Autodoc extension parameters
autodoc_typehints = "signature"
autodoc_typehints_format = "short"

autoapi_dirs = [*morphfits.__path__]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"

html_theme_options = {
    "show_nav_level": 1,
    "announcement": "This Documentation is Under Development",
}

html_static_path = ["_static"]

# Scripts

# convert jhive previz parameter csvs to markdown tables
print("Converting jhive_previz parameter tables to markdown files.")
files_to_convert = ["dja_catalogue_fields_table.csv", "db_catalogue_fields_table.csv"]
path_to_files = "./previz/tables/"
docsutil.convert_tables_to_markdown(files_to_convert, path_to_files)
