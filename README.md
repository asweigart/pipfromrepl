Pip From REPL
======

Run pip to install packages from the Python interactive shell aka REPL.

The benefit of pipfromrepl is that the user doesn't need to know how to navigate the command-line or have their PATH environment variables set up. If multiple versions of Python are installed, pipfromrepl uses the pip module associated with the currently running interactive shell. The goal of pipfromrepl is to reduce the number of steps that students and beginners need to take to get Python packages installed on their computer.

Pipfromrepl is meant to assist students and instructors. It's probably a good idea to not rely on it in production environments.

Installation
------------

To install pipfromrepl from the REPL, copy and paste the following into the REPL:

    import subprocess, sys; subprocess.run([sys.executable, '-m', 'pip', 'install', 'pipfromrepl'])

Pipfromrepl works on Python 2.7 and Python 3.4+ (the versions of Python that come with the pip module.)

To install with pip from the command-line, run:

    pip install pipfromrepl


Quickstart Guide
----------------

Here's how to import and use pipfromrepl:

    >>> import pipfromrepl

    >>> pipfromrepl.list()
    Package     Version Editable project location
    ----------- ------- -------------------------
    pip         22.3.1
    pipfromrepl 0.1.0   C:\github\pipfromrepl
    setuptools  65.5.1
    wheel       0.37.1
    
    >>> pipfromrepl.install('pymsgbox')
    Collecting pymsgbox
      Using cached PyMsgBox-1.0.9-py3-none-any.whl
    Installing collected packages: pymsgbox
    Successfully installed pymsgbox-1.0.9
    
    >>> pipfromrepl.list()
    Package     Version Editable project location
    ----------- ------- -------------------------
    pip         22.3.1
    pipfromrepl 0.1.0   C:\github\pipfromrepl
    PyMsgBox    1.0.9
    setuptools  65.5.1
    wheel       0.37.1
    
    >>> pipfromrepl.uninstall('pymsgbox')
    Found existing installation: PyMsgBox 1.0.9
    Uninstalling PyMsgBox-1.0.9:
      Would remove:
        c:\users\al\.virtualenvs\pipfromrepl-fxbqt5ki\lib\site-packages\pymsgbox-1.0.9.dist-info\*
        c:\users\al\.virtualenvs\pipfromrepl-fxbqt5ki\lib\site-packages\pymsgbox\*
    Proceed (Y/n)?   Successfully uninstalled PyMsgBox-1.0.9

The `uninstall()` function has a `confirm` keyword argument you can set to `True` to force the user to manually enter Y to proceed.

The `user_install()` function passes the `'--user'` argument to pip.

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

You can use this `pip()` function to specify a version to upgrade/downgrade to:

    >>> import pipfromrepl

    >>> pipfromrepl.pip('install --upgrade pymsgbox==1.0.8')
    Collecting pymsgbox==1.0.8
      Downloading PyMsgBox-1.0.8.tar.gz (18 kB)
      Installing build dependencies ... done
      Getting requirements to build wheel ... done
      Preparing metadata (pyproject.toml) ... done
    Building wheels for collected packages: pymsgbox
      Building wheel for pymsgbox (pyproject.toml) ... done
      Created wheel for pymsgbox: filename=PyMsgBox-1.0.8-py3-none-any.whl size=7414 sha256=2090f340a5abbf1b82a4aa76ba443df1ef487d7a164fa8e98668e9db028c36a1
      Stored in directory: c:\users\al\appdata\local\pip\cache\wheels\2e\2b\67\6cc96eb8f0a10fd69d9fac43814dfaf3e697da293af7d5a29f
    Successfully built pymsgbox
    Installing collected packages: pymsgbox
    Successfully installed pymsgbox-1.0.8
