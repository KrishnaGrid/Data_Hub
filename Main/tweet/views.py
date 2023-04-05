from django.shortcuts import render
import json
from django.http import JsonResponse
import pandas as pd
import snscrape.modules.twitter as sntwitter
from datetime import datetime

def tweets_view(request):
    search_query = request.GET.get("query")
    max_tweets = request.GET.get("number")

    if search_query and max_tweets is not None:
        tweets_list = []
        max_tweets = int(max_tweets)
        for i, tweet in enumerate(sntwitter.TwitterSearchScraper(search_query,top = True).get_items()):
            if i >= max_tweets:
                break
            tweets_list.append([tweet.username, tweet.content, tweet.likeCount, tweet.date])
        tweets_df = pd.DataFrame(tweets_list, columns=['Username', 'Tweet', 'Likes', 'Date', ])

        tweets_df['Date'] = pd.to_datetime(tweets_df['Date'], format='%Y-%m-%d %H:%M:%S')
        tweets_df['Date'] = tweets_df['Date'].apply(lambda x: datetime.strftime(x, '%b %d, %Y %I:%M %p'))


        tweets_json = tweets_df.to_json(orient='records')
        tweets = json.loads(tweets_json)
        return render(request, 'tweets_view.html', {'tweets': tweets})
    else:
        return render(request,'tweets_view.html')
