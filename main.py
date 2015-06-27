__author__ = 'laurogama'

import praw.Reddit as reddit

reddit_object = reddit(user_agent='get_reddit_dataset')
user_name = "pandassauro"
user = reddit.get_redditor(user_name)
thing_limit = 10
gen = user.get_submitted(limit=thing_limit)
