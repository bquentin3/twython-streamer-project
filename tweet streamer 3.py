# info on setting up the tokens in "auth" are from the Raspberry Pi
# Getting Started with the Twitter API" resource
from time import sleep
from sense_hat import SenseHat
from twython import TwythonStreamer
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

sense = SenseHat()
r = [255, 0, 0]
w = [255, 255, 255]
e = [0, 0, 0]
# santa hat image, upside down because that's the orientation on my workspace
image = [
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    r, r, r, r, r, r, r, r,
    e, r, r, r, r, r, r, e,
    e, e, r, r, r, r, e, e,
    e, e, e, r, r, r, e, e,
    e, e, e, e, r, r, w, e,
    e, e, e, e, e, e, e, e
    ]



class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            username = data['user']['screen_name']
            tweet = str(data['text'].encode('utf-8'))
            if '#christmas' or '#Christmas' in tweet:
                sense.set_pixels(image)
                sleep(2)
                sense.clear()
        
            print("@%s: %s" % (username, tweet))

stream = MyStreamer(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
stream.statuses.filter(track='#christmas, #Christmas')


