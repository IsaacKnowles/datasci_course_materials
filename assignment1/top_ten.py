import collections
import sys
import json

hashTags = []

def getTweets(file):
	global placesDefined
	tweets = {}
	lines = 0
	tweets = 0
	for line in file:
		lines += 1
		jsonEncoding = json.loads(line)
		if jsonEncoding.keys() != [u'delete']:
			tagsInPost = len(jsonEncoding[u'entities'][u'hashtags'])
			i = 0
			while i < tagsInPost:
				tag = jsonEncoding[u'entities'][u'hashtags'][i][u'text']
				hashTags.append(tag)
				i+=1
				
	
def main():
	tweet_file = open(sys.argv[1],'rU')
	getTweets(tweet_file)
	top10 = collections.Counter(hashTags).most_common(10)
	i = 0
	for i in range(10):
		print  top10[i][0].encode('utf-8'), float(top10[i][1])
	
if __name__ == '__main__':
    main()
	
