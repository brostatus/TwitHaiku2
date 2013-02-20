import urllib
import simplejson
import re
from collections import Counter
words = open('/Users/CodyFulcher/Desktop/Haiku/guns/words.txt', 'w')
tweets = open('/Users/CodyFulcher/Desktop/Haiku/guns/tweets.txt', 'w')
def searchTweets(query):
 search = urllib.urlopen("http://search.twitter.com/search.json?q="+query)
 dict = simplejson.loads(search.read())
 for result in dict["results"]: # result is a list of dictionaries
 	t=result["text"].encode("utf8")
 	t=t.replace("(" or ")" or "[" or "]" or "\'" or "\"" or "." or "," , " ")
 	t= t.replace(" ","\n")
 	tweets.write(t)

def priorityWords():
	wordcount = re.findall('\w+', open('/Users/CodyFulcher/Desktop/Haiku/guns/tweets.txt').read().lower())
	common=Counter(wordcount).most_common(500)
	for element in common:
		words.write(str(element[0]))
		words.write("\n")
# we will search tweets about "fc liverpool" football team
searchTweets("guns&rpp=50")
priorityWords()