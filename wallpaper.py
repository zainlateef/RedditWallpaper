import subprocess
import requests
import os
import ctypes
from platform import system

APPLESCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""

current_os = system()
cwd = os.getcwd()
currentBackgroundImageName = 'currentBackground'


def set_desktop_background(url):
    filepath = download_file_from_url(url)
    if os.name == 'posix':
        changeMacBackground(filepath)
    elif os.name == 'nt':
        changeWindowsBackground(filepath)
    else:
        sys.exit('Your os is not supported')


def changeMacBackground(filepath):
    subprocess.Popen(APPLESCRIPT % filepath, shell=True)
    subprocess.check_call("killall Dock", shell=True)

def changeWindowsBackground(filepath):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath , 0)

def download_file_from_url(url):
    extension = url[url.rfind('.'):]
    filepath = cwd + '/' + currentBackgroundImageName + extension
    deleteFileIfExists(filepath)
    response = requests.get(url, timeout=5)
    if response.ok:
        with open(filepath, 'wb') as f:
            f .write(response.content)
    return filepath

def deleteFileIfExists(filepath):
    if os.path.exists(filepath):
        os.remove(filepath)