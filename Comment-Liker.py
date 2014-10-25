import requests
import json
import time
import urllib2
import facebook
def main():
    Token = raw_input("\nGo to https://developers.facebook.com/tools/explorer ,\nclick on get access token,\ncheck on all the permissions in basic and extended permissions \nand paste the access token here\n")
    post_id = raw_input("\nEnter the post id:\n")
    post = "https://graph.facebook.com/" + post_id + "/comments?access_token=" + Token;
    response = requests.get(post).text
    jsondata = json.loads(response)
    for comment in jsondata['data']:
        if str(comment['from']['id'])!="539395822858113":
            requests.get("https://graph.facebook.com/"+str(comment['id'])+"/likes?access_token="+Token+"&POST")
if __name__ == "__main__":
    main()
