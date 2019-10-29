import tweepy
from config import generate_api
import time

def follow_back(api):
  for follower in tweepy.Cursor(api.followers).items():
    # if am I not following that follower, try to follow them
    if not follower.following:
      follower.follow()

def main():
  api = generate_api()
  while True:
    # run once every hour
    follow_back(api)
    time.sleep(3600)

if __name__ == "__main__":
    main()