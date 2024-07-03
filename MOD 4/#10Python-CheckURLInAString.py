#10Python-CheckURLInAString.py 

import re
def Find(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)
    return [x[0] for x in url]

string = 'My Profile: \
https://www.geeksforgeeks.org/batch/fork-python/track/python-module-4/article/MTQ5MQ%3D%3D'
print("Urls: ",Find(string))
print("\r")