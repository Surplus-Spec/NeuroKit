#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# neurokit2 documentation build configuration file, created by
# sphinx-quickstart on Fri Jun  9 13:47:02 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another
# directory, add these directories to sys.path here. If the directory is
# relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
#
import os
import re
import sys
import mock
import recommonmark

from recommonmark.transform import AutoStructify



sys.path.insert(0, os.path.abspath('../'))


# -- Mock modules ---------------------------------------------
MOCK_MODULES = ['scipy', 'scipy.signal', 'scipy.ndimage', 'scipy.stats', 'scipy.misc', 'scipy.interpolate', 'scipy.sparse', 'scipy.linalg',
                'scipy.spatial', 'scipy.special', 'scipy.integrate', 'scipy.cluster', 'scipy.optimize',
                'sklearn', 'sklearn.neighbors', 'sklearn.mixture', 'sklearn.datasets', 'sklearn.metrics', 'sklearn.metrics.pairwise', 'sklearn.decomposition',
                'mne', 'bioread', 'cvxopt', 'pywt']

for mod_name in MOCK_MODULES:
    sys.modules[mod_name] = mock.Mock()




# -- General configuration ---------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx_rtd_theme',
    'nbsphinx',
    'sphinx_nbexamples',
    'matplotlib.sphinxext.plot_directive',
    'sphinx_copybutton',
    'recommonmark'
]

# matplotlib plot directive
plot_include_source = True
plot_formats = [("png", 90)]
plot_html_show_formats = True
plot_html_show_source_link = False
plot_pre_code = """import numpy as np
import pandas as pd"""

# on_rtd is whether we are on readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

# sphinx-nbexamples
process_examples = not os.path.exists(os.path.join(os.path.dirname(__file__), 'examples'))
not_document_data = 'sphinx_nbexamples.gallery_config'

# Style autodoc
napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_use_param = False
napoleon_use_ivar = False
napoleon_use_rtype = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ['.rst', '.md']


# The master toctree document.
master_doc = 'index'

# General information about the project.
def find_author():
    result = re.search(r'{}\s*=\s*[\'"]([^\'"]*)[\'"]'.format("__author__"), open('../neurokit2/__init__.py').read())
    return str(result.group(1))


project = u'NeuroKit'
copyright = u"2020, Dominique Makowski"
author = find_author()


# The version info for the project you're documenting, acts as replacement
# for |version| and |release|, also used in various other places throughout
# the built documents.
#
# The short X.Y version.
def find_version():
    result = re.search(r'{}\s*=\s*[\'"]([^\'"]*)[\'"]'.format("__version__"), open('../neurokit2/__init__.py').read())
    return result.group(1)


version = find_version()
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**.ipynb_checkpoints']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'monokai'  # 'default', 'monokai'
# nbsphinx_codecell_lexer = 'default'  # Doesn't do anything :/

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# -- Options for HTML THEME: sphinx_rtd_theme -------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for a list of builtin themes.
html_theme = 'sphinx_rtd_theme'
html_favicon = "img/icon.ico"
html_logo = "img/neurokit.png"
html_static_path = ['_static']  # Folder that contain custom static files (e.g., CSS files)

# Theme options are theme-specific and customize the look and feel of a theme further.
# For a list of options available for each theme, see https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html
html_theme_options = {
    'collapse_navigation': False  # Expandables entries
}



# -- Options for HTMLHelp output ---------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'neurokit2doc'


# Bootstrap theme
# html_theme = 'bootstrap'
# html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
# html_theme_options = {
#     'source_link_position': "footer",
#     'bootswatch_theme': "readable",
#     'navbar_sidebarrel': False,
#     'nosidebar': True,
#     'navbar_pagenav': False,
#     'bootstrap_version': "3",
#     'navbar_links': [
#                      ("Installation", "installation"),
#                      ("What's new", "news"),
#                      ("Functions", "functions"),
#                      ("Contributing", "contributing"),
#                      ("Authors", "credits")
#                      ],
#
#     }


# -- Options for LaTeX output ------------------------------------------
pdf_title = u'NeuroKit2'
author_field = u'Official Documentation'

latex_elements = {
    'sphinxsetup': r"""
        VerbatimColor={RGB}{38,50,56},
        verbatimwithframe=false,
        """
    # Background color of chunks
    # '

    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass
# [howto, manual, or own class]).
latex_documents = [
        (master_doc,
         'neurokit2.tex',
         pdf_title,
         author_field,
         'manual'),
]


# -- Options for manual page output ------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
        (master_doc,
         'neurokit2',
         pdf_title,
         [author_field],
         1)
]


# -- Options for Texinfo output ----------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc,
     'neurokit2',
     pdf_title,
     author_field,
     'neurokit2',
     'The Python Toolbox for Neurophysiological Signal Processing.',
     'Miscellaneous'),
]


# Other
add_module_names = False  # so functions aren’t prepended with the name of the package/module
add_function_parentheses = True  # to ensure that parentheses are added to the end of all function names


# -- Setup for recommonmark ---------------------------------------------
def setup(app):
    app.add_config_value('recommonmark_config', {
            # 'url_resolver': lambda url: github_doc_root + url,
            'auto_toc_tree_section': 'Contents',
            }, True)
    app.add_transform(AutoStructify)
