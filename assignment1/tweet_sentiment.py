import sys
import json

sent_file = open(sys.argv[1])
scores = {} # initialize an empty dictionary
for line in sent_file:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means 	"tab character"
		scores[term] = int(score)  # Convert the score to an integer.
		
def getTweets(file):
	tweets = {}
	lines = 0
	tweets = 0
	for line in file:
		lines += 1
		jsonEncoding = json.loads(line)
		tweet = jsonEncoding.get(u'text')
		if tweet != None:
			tweets += 1
			#print lines, tweets, tweet.encode('utf-8'), score(tweet)
			print score(tweet)
		else:
			print 0

			
def score(tweet):
	tweetWordList = tweet.split(' ')
	score = 0
	for word in tweetWordList:
		word = word.lower()
		if scores.get(word) != None:
			score += scores[word]
	return score

def main():
	tweet_file = open(sys.argv[2],'rU')
	getTweets(tweet_file)

if __name__ == '__main__':
    main()
