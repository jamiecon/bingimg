#! /usr/bin/python
"""This module downloads the Bing home page image, converts it to PNG, and
   saves it in the current directory.
"""
import os
import urllib
import json
from PIL import Image

BING_DATA_URL = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-GB"

output = urllib.urlopen(BING_DATA_URL).read()
jsonobj = json.loads(output)
imgurl = jsonobj["images"][0]["url"]
urllib.urlretrieve("https://www.bing.com/" + imgurl, "bing-daily.jpg")
img_object = Image.open("bing-daily.jpg")
img_object.save("bing-daily.png", "PNG")
os.remove("bing-daily.jpg")
