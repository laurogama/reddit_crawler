import time

import praw

user_agent = ("Karma breakdown 1.0 by /u/_Daimon_ ")
r = praw.Reddit(user_agent=user_agent)
# r.login(disable_warning=True)
filterWords = ['greece', 'debt', 'nyc', 'canadian']
already_done = []
delta = 0
while True:
    subreddit = r.get_subreddit('news')
    for submission in subreddit.get_hot(limit=10):
        # print("Checking submission: {} ".format(submission.id))
        op_text = submission.title
        # print(op_text)
        op_text = op_text.lower()
        has_filter_content = any(string in op_text for string in filterWords)
        if submission.id not in already_done and has_filter_content:
            print("found a hit: {} ".format(submission.short_link))
            already_done.append(submission.id)
    print("sleeping after founding {} hits".format(len(already_done) - delta))
    delta = len(already_done)
    time.sleep(60)
