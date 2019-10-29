import tweepy
from config import generate_api
from follow_followers import follow_back
import time
from price_parser import Price

# 4 main search terms to cover possible donatation routes
searchTerms = ["for every retweet donate", "for every RT donate", "for every favorite donate", "for every like donate"]

# Charity and general donations differ. We are not going to support the following things:
#      Political Campaigns

# exclude the leave out list joined by spaces
leaveOutList = ["Sanders", "Warren", "Biden", "Yang", "Trump", "Rebuplican", "Democrat"]

# max number of results per search
searchDepth = 10
# prevent reexamining tweets
newestIds = [0,0,0,0]

# total money raised
total = 0.0

def get_current_total(api):
  return float(api.me().description.split('$')[1])
  
def build_query(i):
  # (search term)- (unwanted words) - (retweets)
  output = searchTerms[i]
  for item in leaveOutList:
    output += " -" + item
  output += " -filter:retweets"
  return output

def check_validity(i, tweet):
  text = tweet.full_text.lower()
  if i < 2:
    x = text.find("for every retweet")
    if x != -1:
      return [True, x]
    x = text.find("for every rt")
    if x != -1:
      return [True, x]
    x = text.find("for every reply")
    if x != -1:
      return [True, x]
    x = text.find("for each retweet")
    if x != -1:
      return [True, x]
  else:
    x = text.find("for every favorite")
    if x != -1:
      return [True, x]
    x = text.find("for every like")
    if x != -1:
      return [True, x]
    x = text.find("for each like")
    if x != -1:
      return [True, x]
  return [False, 0]

def perform_action(i, tweet):
  if i < 2:
    try:
      tweet.retweet()
      return True
    except tweepy.TweepError as e:
      return False
  else:
    try:
      tweet.favorite()
      return True
    except tweepy.TweepError as e:
      return False

def parse_for_ammount(tweet, index):
  price_dict = {}
  for item in tweet.full_text.split(' '):
    if item.find("¢") != -1 or item.find("$") != -1:
      price = Price.fromstring(item)
      if price.currency == None: # case for ¢
        i = tweet.full_text.find(item)
        price_dict[i] = price.amount_float / 100.0
      else: #case for $
        i = tweet.full_text.find(item)
        price_dict[i] = price.amount_float
  needed_key = min(price_dict.keys(), key=lambda x:abs(x-index))
  return price_dict[needed_key]

def update_profile(api):
  global total
  total = round(total, 2)
  api.update_profile(description="This is my little charity bot. Lets see how much money a one simple project can raise for others!\nTotal Raised: $" + str(total))


# make queries for tweets 
def make_queries(api):
  for i in range(0,4) :
    for tweet in api.search(q=build_query(i), count= searchDepth, max_id=str(newestIds[i]), result_type='recent', tweet_mode='extended', lang="en"):
      # update the latest tweet for the search
      if tweet.id > newestIds[i]:
        newestIds[i] = tweet.id
      # check text
      flags = check_validity(i, tweet)
      if flags[0]:
        if perform_action(i, tweet):
          global total
          total += parse_for_ammount(tweet, flags[1])
          update_profile(api)

def main():
  api = generate_api()
  global total
  total = get_current_total(api)
  while True:
    make_queries(api)
    follow_back(api)
    time.sleep(3600)


if __name__ == "__main__":
    main()