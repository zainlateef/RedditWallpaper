import subprocess
import wget
import os

APPLESCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""

cwd = os.getcwd()
currentBackgroundImageName = 'currentBackground'


def set_desktop_background(url):
    filepath = download_file_from_url(url)
    subprocess.Popen(APPLESCRIPT % filepath, shell=True)


def download_file_from_url(url):
    extension = url[url.rfind('.'):]
    filepath = cwd + '/' + currentBackgroundImageName + extension
    if os.path.exists(filepath):
        os.remove(filepath)
    wget.download(url, filepath)
    return filepath


if __name__ == "__main__":
    set_desktop_background("https://via.placeholder.com/150.png")
