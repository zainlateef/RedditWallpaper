import praw
r = praw.Reddit(
    client_id='dl7NsHAAfRgzOA',
    client_secret='XyxGqNFc3Lt-fDF-MkP93ECa9IQ',
    user_agent='nature_is_lit_wallpaper_app')

for submission in r.subreddit('natureisfuckinglit').hot(limit=30):
    print(submission.title)