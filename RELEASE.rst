Release 
-------

  - update moke.core.__version__
  - update setup.py version
  - update CHANGELOG.rst
  - python3 setup.py sdist
  - get password from https://pypi.org/account/login/
  - twine upload dist/moke-xxx.tar.gz

Documentation
-------------

  - update doc/source/conf.py
  - regenerate docs/html
  - push docs/html to gh-pages
  - push moke to github
    
TODO
----

  - add version support to the moke executable
