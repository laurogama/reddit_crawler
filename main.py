import time

import praw

user_agent = "Reddit api tests 1.0 by /u/pandassauro "


def filter_submissions(sub_reddit=None, filter_words=None):
    if not filter_words:
        filter_words = []
    r = praw.Reddit(user_agent=user_agent)
    # r.login(disable_warning=True)
    already_done = []
    delta = 0
    while True:
        subreddit = r.get_subreddit(sub_reddit)
        for submission in subreddit.get_hot(limit=10):
            # print("Checking submission: {} ".format(submission.id))
            op_text = submission.title
            # print(op_text)
            op_text = op_text.lower()
            has_filter_content = any(
                string in op_text for string in filter_words)
            if submission.id not in already_done and has_filter_content:
                print("found a hit: {} ".format(submission.short_link))
                already_done.append(submission.id)
        print(
            "sleeping after founding {} hits".format(len(already_done) - delta))
        delta = len(already_done)
        time.sleep(60)

if __name__ == '__main__':
    filter_words = ['greece', 'debt', 'nyc', 'canadian']
    filter_submissions(sub_reddit="news", filter_words=filter_words)
