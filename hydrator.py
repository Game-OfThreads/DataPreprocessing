import csv
import time
from twarc import Twarc
import numpy as np

#https://stackoverflow.com/questions/51162636/unicodeencodeerror-ucs-2-codec-cant-encode-characters-in-position-8-8-non-b
# I adapted this

def BMP(s):
    print("called \n")
    return "".join((i if ord(i) < 10000 else '\ufffd' for i in s))


tweet_array = []
i = 0
foundid = ""


with open(r'''C:\Users\shann\OneDrive\Documents\FLU DATA\flu_annotations\2011-12\TESTPYTHON.csv''', 'r') as f:
    tweet_array = list(csv.reader(f))

#hydrate the tweets
t = Twarc("RNlmCwGeBhosfRAnkUCswZdrQ", "FPN1re2DugM3j5PysnXaA2JwPlOsoFdlGJSuPkLDPyWNd90hkG" , "1103298875652300800-qDk6jxDGiP5aP2WHr4xhoAUwhIwob1", "RMLXZlarWN1NVab2IF38bmtbKNX34euugxwrYnDChmyui")
for tweet in t.hydrate(open(r'''C:\Users\shann\OneDrive\Documents\FLU DATA\flu_annotations\2011-12\TESTPYTHON.csv''')):
    time.sleep(0.5)
    tweet_array[i][0] = tweet['id']
    print(tweet_array[i][0], " \n")

    
    tweet_array[i][1] = BMP(tweet['full_text']) # text
    print(tweet_array[i][1], " \n")


    tweet_array[i][2] = tweet['user']['id']
    print(tweet_array[i][2], " \n")

    tweet_array[i][3] = BMP(tweet['user']['location']) # encode it
    print(tweet_array[i][3], " \n")


    tweet_array[i][4] = BMP(tweet['created_at'])
    print(tweet_array[i][4], " \n")


    # now do location [3], time[4] and classifier keep the same
    i= i + 1




# copy the array into the csv



#write to the csv
with open(r'''C:\Users\shann\OneDrive\Documents\FLU DATA\flu_annotations\2011-12\AICOPY.csv''', mode ='a', newline='', encoding = 'UTF-8') as f: 
    
    writer = csv.writer(f)
    writer.writerow(["tweetid","text","userid","location","time","classifier"])
    writer.writerows(tweet_array)
    print('written')

 
