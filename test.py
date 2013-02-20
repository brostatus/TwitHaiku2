import urllib
import simplejson
import re
from wordnik import *
def Syl(target):
	target=target.rstrip()
	target.replace(" ","")
	apiUrl = 'http://api.wordnik.com/v4'
	apiKey = 'eb013ff58c8d56e51a7080f66c90fb696661180a938cd679a'
	client = swagger.ApiClient(apiKey, apiUrl)
	wordApi = WordApi.WordApi(client)
	example = wordApi.getHyphenation(target) 

	if example is None:
		count = 0
		vowels = "aeiuoAEIOU"
		for letter in target:
			if letter in vowels:
				count += 10
		return count
	else:
		return len(example)



f1 = open('1.txt', 'w')
f2 = open('2.txt', 'w')
f3 = open('3.txt', 'w')
f4 = open('4.txt', 'w')
f5 = open('5.txt', 'w')
flist = open("words.txt", 'r')
for line in flist:
	x=Syl(line)
	print x
	z=line
	z=z.rstrip()
	if x<6 and len(z)>1 and (z!= "i" or z!= "I"):
		if x==1:
			f1.write(line)
		if x==2:
			f2.write(line)
		if x==3:
			f3.write(line)
		if x==4:
			f4.write(line)
		if x==5:
			f5.write(line)
		


word="boy"

num=Syl(word)
print "done!!!!"
