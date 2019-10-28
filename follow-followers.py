import tweepy
import logging
from config import generate_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def follow_followers(api):
  for follower in tweepy.Cursor(api.followers).items():
    # if am I not following that follower, try to follow them
    if not follower.following:
      follower.follow()

def main():
  api = generate_api()
  print(api)
  while True:
    # run once every hour
    follow_followers(api)
    time.sleep(3600)

if __name__ == "__main__":
    main()