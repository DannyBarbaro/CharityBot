import tweepy

# Authenticate to Twitter and give access token
auth = tweepy.OAuthHandler("", "")
auth.set_access_token("", "")

# getting a safe rate limitted api point
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

try:
    api.verify_credentials()
    print("Authentication Succeeded")
except:
    print("Authentication Failed")

# 4 main search terms to cover possible donatation routes
searchTerms = ["for every retweet donate", "for every RT donate", "for every favorite donate", "for every like donate"]

# Charity and general donations differ. We are not going to support the following things:
#      Political Campaigns

leaveOutList = ["Sanders", "Warren", "Biden", "Yang", "Trump"]
# exclude the leave out list joined by spaces

# method to parse tweet text to make sure it looks right to take action

# method to determine the action to take based off of the searchTerm

# Method to parse tweet text to find the ammount and 

# craft searchs for retweet
for term in searchTerms :
    for tweet in api.search(q=term, lang="en", rpp=10):
        print(tweet)
        # check text
        # make action
        # add to the running total

# update total ammount in bio
