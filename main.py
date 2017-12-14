#! /usr/bin/python
"""This module downloads the Bing home page image, converts it to PNG, and
   saves it in the current directory.
"""
import os
import urllib
import json
from subprocess import call

bing_data_url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-GB"

output = urllib.urlopen(bing_data_url).read()
jsonobj = json.loads(output)
imgurl = jsonobj["images"][0]["url"]
urllib.urlretrieve("https://www.bing.com/" + imgurl, "bing-daily.jpg")
call(["convert", "bing-daily.jpg", "bing-daily.png"])
os.remove("bing-daily.jpg")
