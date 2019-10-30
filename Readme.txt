This is our first video in Tkinter gui application development with python3 in the first video we are going to introduce tkinter and also we are going to create our firs window in tkinter and also tkinter is a powerful module for making  gui applications in python, tkinter is a build in module in python


What's Tkinter?

The Tkinter module (“Tk interface”) is the standard Python interface to the Tk GUI toolkit from Scriptics (formerly developed by Sun Labs).
Both Tk and Tkinter are available on most Unix platforms, as well as on Windows and Macintosh systems. Starting with the 8.0 release, Tk offers native look and feel on all platforms.
Tkinter consists of a number of modules. The Tk interface is provided by a binary extension module named _tkinter. This module contains the low-level interface to Tk, and should never be used directly by application programmers. It is usually a shared library (or DLL), but might in some cases be statically linked with the Python interpreter.
The public interface is provided through a number of Python modules. The most important interface module is the Tkinter module itself. To use Tkinter, all you need to do is to import the Tkinter module:
import Tkinter
Or, more often:
from Tkinter import *
The Tkinter module only exports widget classes and associated constants, so you can safely use the from-in form in most cases. If you prefer not to, but still want to save some typing, you can use import-as:
import Tkinter as Tk

https://www.youtube.com/watch?v=1jn3PH-fA4g&list=PL1FgJUcJJ03sm4WuVCPMbT0RIf2uMmoAj