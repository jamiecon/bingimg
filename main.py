#! /usr/bin/python
import urllib, json, os
from subprocess import call

output = urllib.urlopen("https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-GB").read()
jsonobj = json.loads(output)
imgurl = jsonobj["images"][0]["url"]
urllib.urlretrieve("https://www.bing.com/" + imgurl, "bing-daily.jpg")
call(["convert", "bing-daily.jpg", "bing-daily.png"])
os.remove("bing-daily.jpg")