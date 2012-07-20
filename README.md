Quickshell
==========

A Python module to manipulate files, directories and the clipboard from a Python shell. Clipboard function is Windows-only, but everything else is cross-platform.

###What all can I do with it?###

The most useful things are:

* List the contents of a directory. Use Unix glob patterns.
* Read/write files easily (without all that file object sorcery).
* Apply a transform -- any Python lambda -- to a file, without having to open it first and then save it.
* On Windows, apply a transform to text on clipboard, something supremely handy while editing code (Ctrl+C, transform, Ctrl+V). 


Because Quickshell is designed to be used from a shell, all functions names are as short as possible. Also, speaking of shells, it'll really help if you use one that that supports file path completion, like [DreamPie](http://dreampie.sourceforge.net/).