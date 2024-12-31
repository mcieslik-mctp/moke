Release 
-------

  - update moke.core.__version__
  - update setup.py version
  - update CHANGELOG.rst
  - python -m build --sdist
  - Find SECRET_PYPI_TOKEN if none, get token from https://pypi.org/account/login/ (starts with pypi-)
  - twine upload dist/moke-xxx.tar.gz

Documentation
-------------

  - update doc/source/conf.py
  - regenerate docs/html
  - push docs/html to gh-pages
  - push moke to github

Build Dependencies
------------------

  - pip install setuptools
  - pip install build
  - pip install twine

TODO
----

  - add version support to the moke executable
