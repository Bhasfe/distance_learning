# Sentiment analysis on the tweets about distance learning with TextBlob

## Introduction

The Covid19 Pandemic brought about distance learning in the 2020 academic term. Although some people could adapt easily, some of them found it inefficient. Nowadays, the re-opening of schools is being discussed. Most experts suggest that at least one semester should be online again. As a student who passed the last semester with distance learning, I could find a lot of time to spend on learning natural language processing. Finally, I decided to explore what people think about distance learning. We are going to explore the tweets related to distance learning to understand people's opinions (a.k.a opinion mining) and to discover facts. I have used the lexicon-based approach to determine the tweets' polarities. I have also build a machine learning model to predict the positivity and the negativity of the tweets.

I have collected **202.645** tweets related to distance learning by using Twitter API.

*You can find the related story on [Medium](http://medium.com/@barishasdemir)*

## Content
  **1. Data Gathering**  <br><br>
    - Twitter API <br>
    - Retrieve tweets with tweepy <br><br>
  **2. Preprocessing and Cleaning** <br><br>
    - Drop duplicates <br> 
    - Data type conversions <br>
    - Drop uninformative columns <br>
    - Get rid of stop words, hashtags, punctuation, and one or two-letter words <br>
    - Tokenize the words <br>
    - Apply lemmatization <br>
    - Term frequency-inverse document frequency vectorization <br><br>
  **3. Exploratory Data Analysis** <br><br>
    - Visualize the data <br>
    - Compare word counts <br>
    - Investigate the creation times distribution <br>
    - Investigate the locations of tweets <br>
    - Look at the popular tweets and the most frequent words <br>
    - Make a word cloud <br><br>
  **4. Sentiment Analysis**  <br><br>
  **5. Machine Learning** <br><br>
  **6. Summary**

## Some findings

![Label Counts](/images/label_counts.png)

![Scores](/images/subjectivity_vs_polarity.png)

![Word cloud](/images/wordcloud_general.png)
