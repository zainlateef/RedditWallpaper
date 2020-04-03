import time
from wallpaper import set_desktop_background
from reddit import getRedditUrls

if __name__ == "__main__":
    while True:
        urls = getRedditUrls()
        for url in urls:
            set_desktop_background(url)
            time.sleep(5)
# argument for oldMac
# subreddit of choice
# parameters for subreddit, top 20 or whatever
# time interval for changing in hours
# option to disinclude images of certain dimensions