import urllib.request
import urllib.parse
import urllib.error
import twurl
import json
import ssl
# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py
TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def create_json(acct):
    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': 100})
    # if you want to see info about more friends, just change the count
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    js = json.loads(data)
    with open('web.json', 'w') as file:
        json.dump(js, file, ensure_ascii=False, indent=4)
    return js
