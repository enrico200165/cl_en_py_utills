import win32clipboard

# set clipboard data

def read_clipboard():

    win32clipboard.OpenClipboard()
    win32clipboard.CloseClipboard()
    # get clipboard data
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return data
