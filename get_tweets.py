# -*- coding: utf-8 -*-
"""
Created by Bhasfe
"""

import tweepy
import pandas as pd
import numpy as np
import os

# Create a hashtags list
hashtags = ["#distancelearning", \
            "#onlineschool",     \
            "#onlineteaching",   \
            "#virtuallearning",  \
            "#onlineducation",   \
            "#distanceeducation",\
            "#OnlineClasses",    \
            "#DigitalLearning",  \
            "#elearning",        \
            "#onlinelearning"]

# Create a search list
search_list = ["distance learning",  \
               "online teaching",    \
               "online education,",  \
               "online course",      \
               "online semester",    \
               "distance course",    \
               "distance education", \
               "online class",       \
               "e-learning",         \
               "e learning"]


# Get the necessary API information from a text file
with open('../twitter_api.txt') as file:
    consumer_key, consumer_key_secret, access_token, access_token_secret = [line.strip('\n').split('=')[1] for line in file.readlines()]

# Setup tweepy with Twitter credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Define a function to get tweets
def get_tweets(search, isHashtag):
    
    # Create a pandas DataFrame
    df_temp = pd.DataFrame(columns=["Content", "Location", "Username", "Retweet-Count", "Favorites", "Created at"])
    
    # Get the tweets
    tweets = tweepy.Cursor(api.search, q= search+" -filter:retweets", lang="en",since="2020-08-06", tweet_mode='extended').items(15000)
    
    # Iterate over tweets
    for tweet in tweets:
        content = tweet.full_text
        username = tweet.user.screen_name
        location = tweet.user.location
        created_at = tweet.created_at
        retweetcount = tweet.retweet_count
        favorites = tweet.favorite_count
        
        # Create a list consists of the features
        retrieved = [content, location, username, retweetcount, favorites, created_at]
        
        # Append list to the DataFrame
        df_temp.loc[len(df_temp)] = retrieved
        
    # Generate unique filename
    path = os.getcwd()
    
    # Generate a filename for hashtags or specific word
    if isHashtag:
        filename = path + '/output/' + search[1:] + '_hashtag.csv'
    else:
        filename = path + '/output/' + search.replace(" ", "") + '_wordsearch.csv'
    # Save the csv file
    df_temp.to_csv(filename)


# Call get_tweets function for each hashtag and search word

for hashtag in hashtags:
    get_tweets(hashtag, isHashtag=True)

for search in search_list:
    get_tweets(search, isHashtag=False)
