Changelog
=========

Version 1.2.5
-------------
  
  - better formatting of subtask docstrings

Version 1.2.4
-------------
  
  - better logging defaults and support for stderr/stdout in ini

Version 1.2.3
-------------
  
  - remove broken/partial support for cargs
  - perserve formatting for docstrings
  - allow main task in mokefile with other tasks, 
    cannot be called but useful for documentation 
    and custom global named args

Version 1.2.2
-------------
  
  - more fixes for python 3

Version 1.2.1
-------------
  
  - fix for python 3.6

Version 1.2.0
-------------
  
  - transition to python 3.6


Version 1.1.11
-------------
  
  - pass-forward config args support


Version 1.1.10
-------------
  
  - minor bug fixes
   

Version 1.1.9
-------------
  
  - simplify logging defaults


Version 1.1.8
-------------
  
  - fixes in logging defaults


Version 1.1.7
-------------
  
  - fixes in logging defaults

Version 1.1.6
-------------

  - clean-up, documentation fixes, and github import
  - fixed devel.sh script  


Version 1.1.5
-------------

  - improved ``log_run`` verbosity 


Version 1.1.4
-------------
  
  - support global description ``task(DOC STRING)`` in ``__main__`` 

Version 1.1.3
-------------
  
  - moke now supports a ``required`` argument parameter


Version 1.1.2
-------------
  
  - moke now automatically logs the name of the filename(s) of stdin, stdout, and stderr redictection i.e.
    e.g. ``moke sayhello < inp > out`` will (by default) save the full path of ``inp`` and ``out`` in 
    ``moke.log``

Version 1.1.0
-------------

  - bug fixes / refactoring in moke executable
  - moke depends on python2 in path
  - moke command now works only with mokefile.py / mokefile.ini
  - refactored moke new to accept basename for basename.py / basename.ini
  - coupled mokefiles with configurations files
  - added script to setup dev environment
  - added ``path`` as a supported default
  - added functional test 
  
Version 1.0.5
-------------

  - bug fixes for logger configuration
  - bug fixes in moke executable

Version 1.0.4
-------------

  - added support to bootstrap with config file
  - fixed moke binary to handle script, config, and args

Version 1.0.3
-------------
  
  - added support for config file with global options
  - fixed moke binary to properly create new mokefile 

Version 1.0.2
-------------

  - fixed 'moke' script option parsing


Version 1.0.1
-------------

  - support for 'moke new'
  - added error when mokefile contains no functions
  

Version 1.0.0
-------------

  - Initial commit
