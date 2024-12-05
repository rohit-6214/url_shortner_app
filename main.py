# pip install pyshorteners

import pyshorteners

url = input("enter your url: ")

def url_shortner(url):
    try:
        shortner = pyshorteners.Shortener()
        shortnered_url = shortner.tinyurl.short(url)
        return  shortnered_url
    except:
        return "an error occured"
    
shortered_url = url_shortner(url)

print("your short url: ",shortered_url)

