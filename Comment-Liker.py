import requests
import json
import time

Token = raw_input("\nGo to https://developers.facebook.com/tools/explorer ,\nclick on get access token,\ncheck on all the permissions in basic and extended permissions \nand paste the access token here\n")
post_id = raw_input("\nEnter the post id:\n")
self_id = json.loads(requests.get("https://graph.facebook.com/me?access_token=" + Token).text)['id']

def like():
    post = "https://graph.facebook.com/" + post_id + "/comments?access_token=" + Token;
    response = requests.get(post).text
    jsondata = json.loads(response)
    for comment in jsondata['data']:
        if str(comment['from']['id']) != str(self_id):
            requests.get("https://graph.facebook.com/" + str(comment['id']) + "/likes?access_token=" + Token + "&POST")
            
if __name__ == "__main__":
    like()
