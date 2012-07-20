quickshell
==========

A Python module to manipulate files, directories and the clipboard from a Python REPL. Clipboard function is Windows-only. Everything else is cross-platform.

Since Quickshell is designed to be used from a REPL, all functions names are as short as possible.

###What all can I do with it?###

The most useful things are:

* List the contents of a directory. Use Unix glob patterns.
* Read/write files easily (without all that file object sorcery).
* Apply a transform -- any arbitrary Python lambda -- to a file (without having to open it first and then save it).
* Apply a transform to text on clipboard, something supremely handy while editing code.

It'll really help if you use a REPL like [DreamPie](http://dreampie.sourceforge.net/) that supports file path completion.