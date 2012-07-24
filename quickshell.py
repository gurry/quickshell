''' Provides functions to manipulate Windows files, directories and text on the clipboard. '''
''' Designed to be used from a within python repl. Hence all functions have very short names. ''' 

import os
import os.path
import glob
from shutil import copy2 as _copy
from clipboard import read_clipboard as _read_clipboard
from clipboard import write_to_clipboard as _write_to_clipboard

def ls(file_pattern="*"):
    ''' Lists items in the current directory matching the given file pattern akin to the Unix 'ls' command. '''
    ''' Returns all items if called without arguments. '''
    if file_pattern is not None:
        return glob.glob(file_pattern)
    else:
        return []

def lsl(file_pattern="*"):
    ''' For each item in the curent directory matching a given file pattern (like the Unix 'ls' command) returns a tuple of item name and its type (type is 'd' for directory or 'f' for file). '''
    ''' All items in the current directory are listed if called without arguments. '''
    if file_pattern is not None:
        return [(file, "f" if isf(file) else "d") for file in glob.glob(file_pattern)]
    else:
        return []


def isd(path):
    ''' Determines if the object at the given path is a directory. '''
    if path is not None:
        return os.path.isdir(path)
    else:
        return False

def isf(path):
    ''' Determines if the object at the given path is a file. '''
    if path is not None:
        return os.path.isfile(path)
    else:
        return False
    
def cd(path = None):
    ''' Changes current directory to the specified path. '''
    ''' If called without argument, simply returns the currenty directory path. '''
    if path is not None:
        os.chdir(path)
    else:
        return os.getcwd().replace("\\", '/')


def rf(filename):
    ''' Reads and returns all lines from a file. '''
    if filename is not None:
        try:
            f = open(filename, 'r')
            lines = f.readlines()
        except IOError as error:
            raise IOError(error.strerror)
        except:
            raise IOError("Reading file failed for unknown reason.")
        finally:
            f.close()
						
        return lines
    else:
        return []
		

def wf(filename, lines, append_newlines = True):
    ''' Writes a file with the given lines. '''
    ''' If a file with the same name already exists, overwrites it.'''
    if filename is not None and lines is not None:
        if os.path.isfile(filename): #If the file already exists, confirm overwrite with user.
            response = raw_input("Overwrite {0}? (y/n)".format(filename))
            if not (response == 'y' or response == 'Y'):
                return
            
        try:
            f = open(filename, 'w')
            f.writelines(lines)
        except IOError as error:
            raise IOError(error.strerror)
        except:
            raise IOError("Writing file failed for unknown reason.")
        finally:
            f.close()

def wfn(filename, lines):
    ''' Writes a file with the given lines appending newline characters after each line. '''
    ''' If a file with the same name already exists, overwrites it.'''    
    try:
        wf(filename, [line + '\n' for line in lines])        
    except IOError as error:
        raise IOError(error.strerror)
    except:
        raise IOError("Writing file failed for unknown reason.")
            

            
def cf(src_filename, dest_filename):
    ''' Copies the contents of source file to the given destination file. '''
    ''' Overwrites destination file if it already exists. '''
    if src_filename is not None and dest_filename is not None:
        try:
            _copy(src_filename, dest_filename)
        except IOError as error:
            raise IOError(error.strerror)    
		
def tfa(filename, transform_function):
    ''' Transforms the specified file by passing its lines through a transform function. '''
    ''' The transform function should take a list of strings and return the result as a list of strings. '''
    if filename is not None and transform_function is not None:
        wfn(filename, transform_function(rf(filename)))

def tf(filename, transform_func):
	''' Transforms a file by applying the given transform function to each its line. '''
	''' The transform function should take a string and return a string after transformation. '''
	if filename is not None and transform_func is not None:
            tfa(filename, lambda lines: [transform_func(line) for line in lines])


       
def df(file_pattern, should_prompt = True):
    ''' Deletes the file(s) specified by the given glob pattern. '''
    ''' If you don't want to be prompted before each file pass 1 or True as second the parameter. '''
    if file_pattern is not None:
        for filename in glob.glob(file_pattern):
            go_ahead = True
            if (should_prompt):
                response = raw_input("Delete {0}? (y/n)".format(filename))
                if not(response == 'y' or response == 'Y'):
                    go_ahead = False

            if go_ahead:
                try:
                    os.remove(filename)
                except WindowsError as error:
                    raise IOError(error.strerror)
             
def rc():
    ''' Reads the text on Windows clipboard and returns it as a list of lines. '''
    try:
        clipboard_text = _read_clipboard()
    except Exception:
        raise WindowsError("Failed to read clipboard.")

    if clipboard_text is not None:
        return clipboard_text.splitlines()
    else:
        return []

def wc(lines):
    ''' Writes the given lines on the Windows clipboard after concatenating them together.'''
    if lines is not None:
        try:
            _write_to_clipboard(''.join(lines))
        except Exception:
            raise WindowsError("Failed to write to the clipboard.")
    
def wcn(lines):
    ''' Writes the given lines on the Windows clipboard separating them with a newline character.'''
    if lines is not None:
        try:
            _write_to_clipboard('\n'.join(lines))
        except Exception:
            raise WindowsError("Failed to write to the clipboard.")

def tca(transform_function):
    ''' Transforms the text on the clipboard by passing it through a transform function. '''
    ''' The transform function should take a list of strings and return the result as a list of strings. '''
    if transform_function is not None:
        wcn(transform_function(rc()))

def tc(filename, transform_func):
	''' Transforms the text on the clipboard by applying the given transform function to each its line. '''
	''' The transform function should take a string and return a string after transformation. '''
	if transform_func is not None:
            tca(lambda lines: [transform_func(line) for line in lines])

   
def pp(filename):
    ''' Reads the given file and pretty prints it. '''
    if filename is not None:
        lines = rf(filename)
        for line in lines:
            print(line.rstrip())
