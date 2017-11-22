Quickshell
==========

Quickshell is a Python module that lets you quickly transform contents of files any text copied to the clipboard from a Python shell.

A few of the things you can do with it are:
* List the contents of a directory (using Unix glob patterns if you like).
* Read/write files easily (without having to worry about file objects).
* Apply a transform -- any, arbitrary Python lambda -- to a file, without having to open it first or save it.
* Apply a transform to any text on clipboard, which can be supremely handy while editing code (Ctrl+C, transform, Ctrl+V). 
* Cast a few other spells.

To install, run `pip install git+https://github.com/gurry/quickshell.git`
