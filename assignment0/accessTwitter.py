import urllib
import json
url = "http://search.twitter.com/search.json?q=warcraft&page="
response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")
pyResponse = json.load(response)
#print 'pyResponse if of type',type(pyResponse)
print pyResponse.keys()
#print pyResponse["results"]
print type(pyResponse["results"])
print
results = pyResponse["results"]
print len(results)
#print results[0]
#print results[0].keys()
for pages in range(1,11):
	response = urllib.urlopen(url+str(pages))
	pyResponse = json.load(response)
	results = pyResponse["results"]
	for i in range(len(results)):
		print i, results[i]["text"].encode('utf-8')
		#print resultsText
		


