import praw

def isImageUrl(url):
    return url.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff'))

r = praw.Reddit(
    client_id='dl7NsHAAfRgzOA',
    client_secret='XyxGqNFc3Lt-fDF-MkP93ECa9IQ',
    user_agent='nature_is_lit_wallpaper_app')



def getRedditUrls():
    urls = []
    for sub in r.subreddit('natureisfuckinglit').hot(limit=30):
        if(getattr(sub,"over_18",True)==False and getattr(sub,"post_hint","")=='image'and isImageUrl(getattr(sub,"url",""))):
            urls.append(sub.url)
# post_hint: image