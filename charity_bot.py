import tweepy
from config import generate_api

# 4 main search terms to cover possible donatation routes
searchTerms = ["for every retweet donate", "for every RT donate", "for every favorite donate", "for every like donate"]

# Charity and general donations differ. We are not going to support the following things:
#      Political Campaigns

leaveOutList = ["Sanders", "Warren", "Biden", "Yang", "Trump", "Rebuplican", "Democrat"]
# exclude the leave out list joined by spaces

# method to parse tweet text to make sure it looks right to take action

# method to determine the action to take based off of the searchTerm

# Method to parse tweet text to find the ammount and 

# craft searchs for retweet
for term in searchTerms :
    for tweet in api.search(q=term, lang="en", rpp=3, page=1):
        # print(tweet.text)
        print(tweet.id)
        # check text
        # make action
        # add to the running total

# update total ammount in bio



def main():
  api = generate_api()
  print(api)
  while True:
    # run once every hour
    follow_followers(api)
    time.sleep(3600)

if __name__ == "__main__":
    main()