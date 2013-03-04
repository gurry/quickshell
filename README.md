Quickshell
==========

Quickshell is a Python module that lets you quickly and efforlessly manipulate files, directories and the clipboard from a Python shell.

A few of the things you can do with it are:
* List the contents of a directory (using Unix glob patterns if you like).
* Read/write files easily (without all that file object sorcery).
* Apply a transform -- any, arbitrary Python lambda -- to a file, without having to open it first or save it.
* Apply a transform to any text on clipboard, which can be supremely handy while editing code (Ctrl+C, transform, Ctrl+V). 
* Cast a few other spells.

####Installation####
* Clone this repository and add `quickshell.py` to your [PYTHONSTARTUP](http://docs.python.org/2/using/cmdline.html#envvar-PYTHONSTARTUP).
* (Optionally) install and use a shell that autocompletes file paths, such as [DreamPie](http://dreampie.sourceforge.net/).
