import ctypes

#Alias the required low level functions and constants
strcpy = ctypes.cdll.msvcrt.strcpy
OpenClipboard = ctypes.windll.user32.OpenClipboard    
EmptyClipboard = ctypes.windll.user32.EmptyClipboard
GetClipboardData = ctypes.windll.user32.GetClipboardData
SetClipboardData = ctypes.windll.user32.SetClipboardData
CloseClipboard = ctypes.windll.user32.CloseClipboard
GlobalAlloc = ctypes.windll.kernel32.GlobalAlloc    
GlobalLock = ctypes.windll.kernel32.GlobalLock     
GlobalUnlock = ctypes.windll.kernel32.GlobalUnlock
GMEM_DDESHARE = 0x2000 
CF_TEXT = 1 # Signifies plaintext clipboard format

def read_clipboard():
    ''' Reads the contents of the clipboard as plain text. '''
    opened = OpenClipboard(None) #None means we're opening in the context of this proces
    if not opened:
        raise WindowsError("Failed to open clipboard.")
    
    contents = GetClipboardData(CF_TEXT) #
    if contents is None:
        CloseClipboard()
        raise WindowsError("Failed to read from clipboard.")

    contents = GlobalLock(contents) #Need to acquire a global lock as this is global memory (see windows documentation)
    data_as_str = ctypes.c_char_p(contents).value
    GlobalUnlock(contents) #And release the lock

    CloseClipboard()

    return data_as_str

def write_to_clipboard(text):
    ''' Writes the supplied text to the clipboard. '''
    opened = OpenClipboard(None) #None means we're opening in the context of this proces
    if not opened:
        raise WindowsError("Failed to open clipboard.")
    
    emptied = EmptyClipboard()
    if not emptied:
        CloseClipboard()
        raise WindowsError("Failed to empty clipboard before writing to it.")
    
    buf = GlobalAlloc(GMEM_DDESHARE, len(text) + 1) #Allocate buffer as long as text plus 1 for null terminator
    if buf is None:
        CloseClipboard()
        raise WindowsError("Failed to allocate buffer to pass to clipboard.")

    buf = GlobalLock(buf)
    strcpy(ctypes.c_char_p(buf), text)
    GlobalUnlock(buf)

    data_written = SetClipboardData(1, buf)
    if data_written is None:
        CloseClipboard()
        raise WindowsError("Failed to write to clipboard.")
             
    CloseClipboard()
