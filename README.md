Quickshell
==========

Quickshell is a Python module that lets you quickly manipulate files, directories text copied to the clipboard. Meant to be the python equivalent of shell commands like `sed`. Currently supports Windows only.

The following are a few things you can do with it:
* List the contents of a directory (using Unix-like glob patterns if you like).
* Read/write files easily without having to worry about file objects.
* Apply a transform -- any, arbitrary Python lambda -- to a file, without having to explicitly open it or save it.
* Apply a transform to any text on clipboard, which can be supremely handy while editing code (Ctrl+C, transform, Ctrl+V). 
* Cast a few other spells.

To install, run `pip install git+https://github.com/gurry/quickshell.git`
