Pip From REPL
======

Run pip to install packages from the Python interactive shell aka REPL.

If you are leading a programming workshop and want to avoid headaches of running pip from students' machines (with all their possible )

The benefit of pipfromrepl is that the user doesn't need to know how to navigate the command-line or have their PATH environment variables set up. If multiple versions of Python are installed, pipfromrepl uses the pip module associated with the currently running interactive shell. The goal of pipfromrepl is to reduce the number of steps that students and beginners need to take to get Python packages installed on their computer.

Pipfromrepl is meant to assist students and instructors. It's probably a good idea to not rely on it in production environments.

Installation
------------

To install pipfromrepl from the REPL, copy and paste the following into the REPL:

    import subprocess, sys; subprocess.run([sys.executable, '-m', 'pip', 'install', 'pipfromrepl'])

Pipfromrepl works on Python 2.7 and Python 3.4+. Linux users may need to install pip separately by running `sudo apt-get install python3-pip` from a Terminal.


Quickstart Guide
----------------

After installing pipfromrepl, run `import pipfromrepl`:

    >>> import pipfromrepl

Call `pipfromrepl.install()` to install a package from PyPI:

    >>> pipfromrepl.install('pymsgbox')
    Collecting pymsgbox
      Using cached PyMsgBox-1.0.9-py3-none-any.whl
    Installing collected packages: pymsgbox
    Successfully installed pymsgbox-1.0.9

Call `pipfromrepl.list()` to list the installed packages:

    >>> pipfromrepl.list()
    Package     Version Editable project location
    ----------- ------- -------------------------
    pip         22.3.1
    pipfromrepl 0.1.0   C:\github\pipfromrepl
    PyMsgBox    1.0.9
    setuptools  65.5.1
    wheel       0.37.1

Call `pipfromrepl.uninstall()` to uninstall a package:

    >>> pipfromrepl.uninstall('pymsgbox')
    Found existing installation: PyMsgBox 1.0.9
    Uninstalling PyMsgBox-1.0.9:
      Would remove:
        c:\users\al\.virtualenvs\pipfromrepl-fxbqt5ki\lib\site-packages\pymsgbox-1.0.9.dist-info\*
        c:\users\al\.virtualenvs\pipfromrepl-fxbqt5ki\lib\site-packages\pymsgbox\*
    Proceed (Y/n)?   Successfully uninstalled PyMsgBox-1.0.9


Additional Details
----------------

The `uninstall()` function has a `confirm` keyword argument you can set to `True` to force the user to manually enter Y to proceed.

The `user_install()` function passes the `'--user'` argument to pip.

You can install a specific version just like pip: `pipfromrepl.install('pymsgbox==1.0.9')`

You can pass pip commands to pip directly with the `pip()` functions:

    >>> import pipfromrepl

    >>> pipfromrepl.pip('install pymsgbox')
    Collecting pymsgbox
      Using cached PyMsgBox-1.0.9-py3-none-any.whl
    Installing collected packages: pymsgbox
    Successfully installed pymsgbox-1.0.9

    >>> pipfromrepl.pip('list')
    Package          Version    Editable project location
    ---------------- ---------- -------------------------
    certifi          2022.9.24
    distlib          0.3.6
    filelock         3.8.0
    pip              22.3.1
    pipenv           2022.11.11
    pipfromrepl      0.1.0      C:\github\pipfromrepl
    platformdirs     2.5.4
    PyMsgBox         1.0.9
    setuptools       65.5.1
    virtualenv       20.16.7
    virtualenv-clone 0.5.7
    wheel            0.37.1

    >>> pipfromrepl.pip('uninstall pymsgbox')
    Found existing installation: PyMsgBox 1.0.9
    Uninstalling PyMsgBox-1.0.9:
      Would remove:
        c:\users\al\.virtualenvs\pipfromrepl-fxbqt5ki\lib\site-packages\pymsgbox-1.0.9.dist-info\*
        c:\users\al\.virtualenvs\pipfromrepl-fxbqt5ki\lib\site-packages\pymsgbox\*
    Proceed (Y/n)? y
      Successfully uninstalled PyMsgBox-1.0.9
