Example
=======

Stand-alone command line apps
-----------------------------

If for some reason you do not want call ``moke`` to execute your mokefile it
is possible to rename it and call it directly.::

  chmod +x mokefile.py
  mv mokefile.py myapp.py
  ./myapp.py <task>

This requires shebang line::

  #!/usr/bin/env python3

If your ``mokefile.py`` contains only a single task call the function ``main``
and you will be able to omit ``<task>`` from the call::

  ./myapp.py

The tiny ``grop.py`` example included in the test-suite is a tiny replacement
for ``grep``.

.. literalinclude:: ../../test/scripts/grop.py


Example usage (in the ``test`` directory)::

  cat data/grop.inp | scripts/grop.py ".*\(\d{2}\).*"'

