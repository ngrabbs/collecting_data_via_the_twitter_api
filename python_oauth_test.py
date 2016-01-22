#!/usr/bin/env python

import oauth2
import json
import time

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
KEY = ''
SECRET = ''
#screen_names = ['ngrabbs', 'sparky_klystron', '4771cu5', 'AbayomiAAsana', 'dc0de']
screen_names = ['YourAnonNews']

def oauth_req(url, key, secret, http_method="GET", post_body="", http_headers=None):
    consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
    return content

count = 0
cursor = '-1'

## when you get to the end the cursor goes to 0
##next_cursor":0

## if you catch a ratelimit you gotta sleep for a bit
#ngrabbs@jobsbox:~/collecting_data_via_the_twitter_api$ cat YourAnonNews_5| python -mjson.tool|more
#{
#   "errors": [
#       {
#           "code": 88,
#           "message": "Rate limit exceeded"
#       }
#   ]
#}

#while (count < 8200):                     
#    f = open('YourAnonNews_' + str(count), 'w')
#    followers_list = oauth_req( 'https://api.twitter.com/1.1/followers/list.json?cursor=' + str(cursor) + '&screen_name=' + screen_name + '&count=200&skip_status=true&include_user_entities=false' , KEY , SECRET )
#    f.write(followers_list)
#    f.close()
#    a = json.loads(followers_list)
#    print a["next_cursor"]
#    cursor = a["next_cursor"]
#    print count
#    count = count + 1
#    #print followers_list
for screen_name in screen_names:
    while(cursor != 0):
        error_count = 0
        print "bout to bust down on a screen name: [" + screen_name + "]\n"
        followers_list = oauth_req( 'https://api.twitter.com/1.1/followers/list.json?cursor=' + str(cursor) + '&screen_name=' + screen_name + '&count=200&skip_status=true&include_user_entities=false' , KEY , SECRET )
        print "got a list back for [" + screen_name + "]\n"
        a = json.loads(followers_list)
        ## need to check for error here
        print "check for errors..."
        if 'errors' in a:
            print "should have errors\n"
            print a
            if a["errors"][0]["code"] == 88:
                print "We got the error we need to sleep"
                print a
                time.sleep(900)
            else:
                print "We got errors but I dont know what about\n"
                print a
        else:
            print "looks like we dont gotta sleep yet\n"
        print "check for Not authorized error\n"
        if 'error' in a:
            if a["error"] == "Not authorized.":
                print "No Access skip out of the loop\n"
                print a
                error_count = 1
            else:
                print "we got an 'error' but I dont know what about"
                print a
                error_count = 1
            next
        else:
            print "looks like we're authorized\n"

        print "lets write the file for: [" + screen_name + "]\n"
        f = open(screen_name + '_' + str(cursor), 'w')
        f.write(followers_list)
        f.close()
        print "close file\n"

        if(error_count == 0):
            if(a["next_cursor"] == "0"):
                print "got 0 next cursor hitting next"
                next
            else:
                print "next cursor: [" + str(a["next_cursor"]) + "]\n"
                cursor = a["next_cursor"]
