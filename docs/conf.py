# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath('../src'))

import collectionish
import sphinx

# -- Project information -----------------------------------------------------

project = 'collectionish'
copyright = '2020, Lea Provenzano'
author = collectionish.__author__

# The full version, including alpha/beta/rc tags
release = collectionish.__version__


def monkeypatch(cls):
    """ decorator to monkey-patch methods """

    def decorator(f):
        method = f.__name__
        old_method = getattr(cls, method)
        setattr(cls, method, lambda self, *args, **kwargs: f(old_method, self, *args, **kwargs))

    return decorator


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # Need the autodoc and autosummary packages to generate our docs.
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    # The Napoleon extension allows for nicer argument formatting.
    'sphinx.ext.napoleon',
    'sphinx.ext.autosectionlabel',
    'sphinx_autodoc_typehints',
    'm2r2',
]


set_type_checking_flag = True

source_suffix = ['.rst', '.md']


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_material'


napoleon_numpy_docstring = False

autosummary_generate = True


autoclass_content = "class"  # include both class docstring and __init__
autodoc_default_flags = [
    # Make sure that any autodoc declarations show the right members
    "members",
    "inherited-members",
    "show-inheritance",
]

master_doc = 'index'
# Prefix document path to section labels, otherwise autogenerated labels would look like 'heading'
# rather than 'path/to/file:heading'
autosectionlabel_prefix_document = True

# dont prepend module names to everything
add_module_names = False


html_sidebars = {"**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]}

# Material theme options (see theme.conf for more information)
html_theme_options = {
    # Set the name of the project to appear in the navigation.
    'nav_title': project,
    # Set you GA account ID to enable tracking
    # 'google_analytics_account': 'UA-XXXXX',
    # # Specify a base_url used to generate sitemap.xml. If not
    # # specified, then no sitemap will be built.
    # 'base_url': 'https://project.github.io/project',
    # Set the color and the accent color
    'color_primary': 'deep-orange',
    'color_accent': 'teal',
    # Set the repo location to get a badge with stats
    'repo_url': 'https://github.com/leaprovenzano/collectionish/',
    'repo_name': 'collectionish',
    # Visible levels of the global TOC; -1 means unlimited
    'globaltoc_depth': 2,
    # If False, expand all TOC entries
    # 'globaltoc_collapse': False,
    # If True, show hidden TOC entries
    # 'globaltoc_includehidden': True,
    'html_minify': True,
    'css_minify': True,
}
