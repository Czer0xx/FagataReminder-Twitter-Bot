import tweepy
import threading

day = 1

Secret_API_KEY = ''
API_KEY = ''
Bearer_Key = ''
Acces_token = ''
Acces_secret_token = ''



client = tweepy.Client(bearer_token=Bearer_Key, access_token_secret=Acces_secret_token, access_token=Acces_token, consumer_key=API_KEY, consumer_secret=Secret_API_KEY)

def Post():
    global day
    threading.Timer(86400, Post).start()
    client.create_tweet(text=f'Dzień {day}\n\nFAGATA WYKORZYSTAŁA STUU DLA ZASIĘGÓW!!\n\n#Fagata')
    day += 1

Post()
