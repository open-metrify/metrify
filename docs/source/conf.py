# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
project = "metrify"
copyright = "2024, Pedro Binotto, Eric Fernandes Evaristo"
author = "Pedro Binotto, Eric Fernandes Evaristo"
version = "0.1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinxcontrib.autohttp.flask",
]

templates_path = ["_templates"]
exclude_patterns = []

language = "pt_BR"

autodoc_typehints_format = "short"
python_use_unqualified_type_names = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]
