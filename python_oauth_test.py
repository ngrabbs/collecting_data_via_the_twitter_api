#!/usr/bin/env python

import oauth2
import json

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
KEY = ''
SECRET = ''
screen_names = ['', '', '', '', '']

def oauth_req(url, key, secret, http_method="GET", post_body="", http_headers=None):
    consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
    return content

count = 0
cursor = '-1'

for screen_name in screen_names:
    followers_list = oauth_req( 'https://api.twitter.com/1.1/followers/list.json?cursor=' + str(cursor) + '&screen_name=' + screen_name + '&count=200&skip_status=true&include_user_entities=false' , KEY , SECRET )
    a = json.loads(followers_list)
    ## need to check for error here
    f = open(screen_name + '_' + str(cursor), 'w')
    f.write(followers_list)
    f.close()

    print a["next_cursor"]
    cursor = a["next_cursor"]
