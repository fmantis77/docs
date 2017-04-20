# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
import requests, json
from requests_oauthlib import OAuth1
from urllib.parse import parse_qs

REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

CONSUMER_KEY = "VZnpUJWJ2FEv4U4j2esikbA88"
CONSUMER_SECRET = "kyjU0DAmlBfcn1ZL2T7lDxz4Zh7D5N4ebmMDzzWbReiLUKCuIU"

OAUTH_TOKEN = "792357464784134144-poxgzaNt6CGFimzeCWOLjDnDB0W1tJn"
OAUTH_TOKEN_SECRET = "I7g8yHXI8Eiaf0Nyc7B2Os3VglCg0GaJKUE2AJHATSqhY"


def setup_oauth():
    """Authorize your app via identifier."""
    # Request token
    oauth = OAuth1(CONSUMER_KEY, client_secret=CONSUMER_SECRET)
    r = requests.post(url=REQUEST_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)

    resource_owner_key = credentials.get('oauth_token')[0]
    resource_owner_secret = credentials.get('oauth_token_secret')[0]

    # Authorize
    authorize_url = AUTHORIZE_URL + resource_owner_key
    print ('Please go here and authorize: ' + authorize_url)

    verifier = raw_input('Please input the verifier: ')
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=resource_owner_key,
                   resource_owner_secret=resource_owner_secret,
                   verifier=verifier)

    # Finally, Obtain the Access Token
    r = requests.post(url=ACCESS_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)
    token = credentials.get('oauth_token')[0]
    secret = credentials.get('oauth_token_secret')[0]

    return token, secret


def get_oauth():
    oauth = OAuth1(CONSUMER_KEY,
                client_secret=CONSUMER_SECRET,
                resource_owner_key=OAUTH_TOKEN,
                resource_owner_secret=OAUTH_TOKEN_SECRET)
    return oauth

if __name__ == "__main__":
    if not OAUTH_TOKEN:
        token, secret = setup_oauth()
        print ("OAUTH_TOKEN: " + token)
        print ("OAUTH_TOKEN_SECRET: " + secret)
    else:
        oauth = get_oauth()
        #r = requests.get(url="https://api.twitter.com/1.1/search/tweets.json?q=python", auth=oauth)
        data=json.loads(requests.get(url="https://api.twitter.com/1.1/search/tweets.json?q=python", auth=oauth).text)
        #for tweet in data['search_metadata']:
        for tweet in data['statuses']:
               print(tweet['text'])
               #for tweet2 in tweet:
               #      print(tweet2)

