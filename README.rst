``moke`` is not like ``make``
#############################

Moke transforms a Python module into a command line script. Every function can
become a sub-command, with options inferred from the argument list and the
optional doc string.

A command line application that greets exactly two persons. (put the following
into a file called ``mokefile.py``::

  from moke import task, log

  @task
  def greet(who, shout=False, times=1):
      """
      Sends greetings from moke.

       - who(str2) two persons to greet
       - shout(switch) triggers CAPS

      """
      greetings = ("Hello %s and %s!" % (who[0], who[1])) * times
      if shout:
          greetings = greetings.upper()
      log("greeted: %s and %s" % (who[0], who[1]), INFO)

  if __name__ == "__main__":
      task()

Execute the mokefile by calling ``moke``::

  moke greet --shout -times 2 Mary Kate

this returns::

  2011-09-30 14:12:52,815 moke (version 1.0.0)
  2011-09-30 14:12:52,815 cwd: "/home/.../moke/test/scripts"
  2011-09-30 14:12:52,815 mokefile: "/home/.../moke/test/scripts/mokefile.py"
  2011-09-30 14:12:52,815 task: greet
  2011-09-30 14:12:52,815 params: ('who', ['Mary', 'Kate']) ('shout', True) ('times', 2)
  HELLO MARY AND KATE!
  HELLO MARY AND KATE!

If you forgot what your ``mokefile.py`` does, just ask for help::

  moke --help

  usage: mokefile.py [-h] [-ls LS] [-ll {info,warn,error}] [-lf {tab}]
    {greet} ...

  positional arguments:
    {greet}
      greet               Sends greetings from moke.

  optional arguments:
    -h, --help            show this help message and exit
    -ls LS                (file_a) [default: <stderr>] logging stream
    -ll {info,warn,error}
                          (str) [default: info] logging level
    -lf {tab}             (str) [default: tab] logging format

Sub-command specific help is also generated::

  moke greet --help

  usage: mokefile.py greet [-h] [--shout] [-times TIMES] who who

  positional arguments:
    who           (str) two persons to greet

  optional arguments:
    -h, --help    show this help message and exit
    --shout       (switch) triggers CAPS
    -times TIMES  (int) [default: 1]

Now it's time to start your own Mokefile::

  moke new [filename]

Which creates a skeleton file for you::
	
  $ moke new Mokefile
  moke: *** Created /...path.../Mokefile
  moke: *** Running 'moke Mokefile --help'

Have fun!
