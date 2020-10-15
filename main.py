import praw
from urllib.request import urlretrieve
from slugify import slugify
from pprint import pprint

reddit = praw.Reddit(client_id='####',
                client_secret='####',
                user_agent='SirAelic Content Downloader',
                username='####',
                password='####')

media = []

for post in reddit.subreddit("MadeMeSmile").top("week", limit=40):
    print("Appending media {}".format(post.url))
    fileName = slugify(post.title)[:75]
    if "i.redd.it" in post.url:
        # Append images to the download array normally. 
        media.append((post.url, fileName + post.url[-4:]))
    else:
        #Pull the direct video link from the post object.
        url = post.media['reddit_video']['fallback_url']
        url = url.split("?")[0]
        media.append((url, fileName + '.mp4'))

if media:
    for part in media:
        print('Downloading {}'.format(part[0]))
        try:
            urlretrieve(part[0], part[1])
        except Exception:
            print("An error happened, trying again")
            urlretrieve(part[0], part[1])
