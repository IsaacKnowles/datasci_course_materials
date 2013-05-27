import sys
import json

terms = {}
totalTermOccurrences = 0

def getTweetsThenCount(file):
	tweets = {}
	lines = 0
	tweets = 0
	for line in file:
		lines += 1
		jsonEncoding = json.loads(line)
		#print jsonEncoding.get(u'lang')
		tweet = jsonEncoding.get(u'text')
		if tweet != None:
			tweets += 1
			#print lines, tweets, tweet.encode('utf-8'), score(tweet)
			#print 'line number is',lines
			count_terms(tweet)
			
def count_terms(tweet):
	tweetWordList = tweet.split(' ')
	global totalTermOccurrences
	for word in tweetWordList:
		word=word.replace('\n','')
		word=word.replace('\t','')
		totalTermOccurrences += 1
		if terms.get(word) != None:
			terms[word] += 1
		else: terms[word] = 1.0


def main():
	tweet_file = open(sys.argv[1],'rU')
	getTweetsThenCount(tweet_file)
	global totalTermOccurrences
	#print totalTermOccurrences
	for key in terms:
		try:
			print key.encode('utf-8'),round(terms[key]/totalTermOccurrences,4)
		except UnicodeDecodeError:
			print key,round(terms[key]/totalTermOccurrences,4)

if __name__ == '__main__':
    main()
