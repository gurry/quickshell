Quickshell
==========

A Python module to manipulate files, directories and the clipboard from a Python shell.

###What all can I do with it?###

It lets you:
* List the contents of a directory (using Unix glob patterns if you like).
* Read/write files easily (without all that file object sorcery).
* Apply a transform -- any, arbitrary Python lambda -- to a file, without having to open it first or save it.
* Apply a transform to any text on clipboard, which can be supremely handy while editing code (Ctrl+C, transform, Ctrl+V). 
* Cast a few other spells.

###Anything else?###

To make it simple to use, you might want to...
* Set up quickshell so it's automatically loaded when a Python shell starts (see [PYTHONSTARTUP](http://docs.python.org/using/cmdline.html#environment-variables) environment variable.)
* Use a shell that autocompletes file paths, such as [DreamPie](http://dreampie.sourceforge.net/).
