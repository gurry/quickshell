Quickshell
==========

A Python module to manipulate files, directories and the clipboard from a Python shell (clipboard function is currently Windows-only).

###What all can I do with it?###

You can:
* List the contents of a directory, using Unix glob patterns if you like.
* Read/write files easily (without all that file object sorcery).
* Apply a transform -- any, arbitrary Python lambda -- to a file, without having to open it first and then save it.
* On Windows, apply a transform to any text on clipboard, which can be supremely handy while editing code (Ctrl+C, transform, Ctrl+V). 
* A few others like these.

###Anything else?###

You may find it useful to ...
* Set up quickshell so it's automatically loaded when a Python shell starts (see [PYTHONSTARTUP](http://docs.python.org/using/cmdline.html#environment-variables) environment variable.)
* Use a shell that autocompletes file paths, such as [DreamPie](http://dreampie.sourceforge.net/).
