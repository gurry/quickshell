Quickshell
==========

Quickshell is a Python module that lets you quickly and effortlessly manipulate files, directories and the clipboard from within a Python shell.

###What all can I do with it?###

You can:
* List the contents of a directory (using Unix glob patterns if you like).
* Read/write files easily (without all that file object sorcery).
* Apply a transform -- any, arbitrary Python lambda -- to a file, without having to open it first or save it.
* Apply a transform to any text on clipboard, which can be supremely handy while editing code (Ctrl+C, transform, Ctrl+V). 
* Cast a few other spells.

###Anything else?###

You might like to ...
* Set Quickshell up so it loads automatically when your Python shell starts (see [PYTHONSTARTUP](http://docs.python.org/using/cmdline.html#environment-variables) environment variable.)
* Use a shell that autocompletes file paths, such as [DreamPie](http://dreampie.sourceforge.net/).
