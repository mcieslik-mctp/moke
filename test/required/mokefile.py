#!/usr/bin/env python3
from moke import * #@UnusedWildImport

@task
def sayhello(name=required):
    """
     - name(``str``)
    """
    log("executing hello task")
    stdout.write("hello %s\n" % name)

if __name__ == "__main__":
    task()
