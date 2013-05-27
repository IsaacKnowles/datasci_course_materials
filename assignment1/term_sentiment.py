import sys
import json

sent_file = open(sys.argv[1])
scoresOrig = {} # initialize an empty dictionary
scores = {} # scores for new words
for line in sent_file:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means 	"tab character"
		scoresOrig[term] = float(score) # Convert the score to an integer.
		#Note that the dictionary now contains a "mutable" boolean, and a times seen
		#Dictionary now contains indicator of whether the word was in the original 	list
def getTweets(file):
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
			score(tweet)

			
def score(tweet):
	tweetWordList = tweet.split(' ')
	tweet_score = 0 #for tweet score
	for word in tweetWordList:
		if scoresOrig.get(word) != None:
			tweet_score += scoresOrig[word]
			
	for word in tweetWordList:
		# word=word.replace('?','')
		# word=word.replace('!','')
		# word=word.replace('.','')
		# word=word.replace(';','')
		# word=word.replace('%','')
		# word=word.replace('(','')
		# word=word.replace(')','')
		# word=word.replace('&','')
		# word=word.replace('\"','')
		# word=word.replace(',','')
		# word=word.replace('\'','')
		word=word.replace('\n','')
		word=word.replace('\t','')
		if len(word) <= 2 or scoresOrig.get(word) != None: continue
		word = word.lower()
		if scores.get(word) == None:
			scores[word] = 0
		scores[word] += tweet_score #Adjust the avg sentiment
			
			

def main():
	tweet_file = open(sys.argv[2],'rU')
	getTweets(tweet_file)
	#print 'got back'
	for word in scores:
		#if scores[word][0] < 0 and scores[word][1] == True:
		try: 
			#print word.encode('utf-8'),round(scores[word][0],3)
			print word.encode('utf-8'),scores[word]
		except UnicodeDecodeError:
			#print word,round(scores[word][0],3)
			print word,scores[word]
	



if __name__ == '__main__':
    main()
