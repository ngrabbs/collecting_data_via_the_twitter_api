# collecting_data_via_the_twitter_api
Collecting data via the Twitter API

https://www.upwork.com/jobs/_~01a14c5dfcea84a91a/

Details

I want to find the overlap between the followers of a given twitter account and 20 other twitter accounts (some of them with millions of followers). 

In order to complete this task, you will need to:
1. Write a python script collecting the followers of all the Twitter accounts I will list.
2. Store the data in a MySQL database.
3. Run quires to find the overlap in the followers of the different accounts.  
warbird:Collecting data via the Twitter API ngrabbs$ 

Notes:
pull down a follower list:
https://dev.twitter.com/rest/reference/get/followers/list

how to setup oauth tokens:
https://dev.twitter.com/oauth/overview/application-owner-access-tokens

authorizing requests:
https://dev.twitter.com/oauth/overview/authorizing-requests

oauth overview:
https://dev.twitter.com/oauth/overview

TODO:

put in a handler for no more records:
{"users":[],"next_cursor":0,"next_cursor_str":"0","previous_cursor":0,"previous_cursor_str":"0"}

put in an error handler for this:
{
    "errors": [
        {
            "code": 88,
            "message": "Rate limit exceeded"
        }
    ]
}

put in an error handler for this:
{"request":"\/1.1\/followers\/list.json","error":"Not authorized."}


next thing we need to build a dict/array that houses all the users we want to search
and for testing do something simple like
pull 200 from each

then we need to pump them into a database
and start to run outputs against them

i think it should have a report that says:
all these users are in all followers
then walk down through the next highest amount

it probably wont have a highest amount deal
just a 20 connections
