"""Pip From REPL
By Al Sweigart al@inventwithpython.com

Run pip to install packages from the Python interactive shell aka REPL."""

__version__ = '0.1.3'

import sys, subprocess


def user_install(module_name):
    subprocess.run([sys.executable, '-m', 'pip', 'install', '--user', module_name])


def install(module_name):
    subprocess.run([sys.executable, '-m', 'pip', 'install', module_name])


def uninstall(module_name, confirm=False):
    if confirm:
        subprocess.run(['echo', 'y', '|', sys.executable, '-m', 'pip', 'uninstall', module_name])
    else:
        echoProcess = subprocess.Popen(['echo', 'y'], stdout=subprocess.PIPE)
        pipProcess = subprocess.Popen([sys.executable, '-m', 'pip', 'uninstall', module_name], stdin=echoProcess.stdout)
        pipProcess.communicate()


def list():
    subprocess.run([sys.executable, '-m', 'pip', 'list'])


def pip(*args):
    if len(args) == 1:
        args = tuple(args[0].split())
    subprocess.run([sys.executable, '-m', 'pip', *args])


"""
REMOVED FOR NOW:
def pipenv(*args):
    if len(args) == 1:
        args = tuple(args[0].split())
    subprocess.run([sys.executable, '-m', 'pipenv', *args])
"""

