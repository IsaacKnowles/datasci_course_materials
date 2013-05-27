import collections
import sys
import json

sent_file = open(sys.argv[1])
scores = {} # initialize an empty dictionary
validTimeZones = ['Alaska','Arizona','Central Time (US & Canada)','Eastern Time (US & Canada)','Hawaii','Indiana (East)', 'Mountain Time (US & Canada)','Pacific Time (US & Canada)']
hashTags = []
statecounts = {}
timezones = []
locations = []
stateHappiness = {}
places = []
states={}
placesDefined = 0
for line in sent_file:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means 	"tab character"
		scores[term] = int(score)  # Convert the score to an integer.
		
def getTweets(file):
	global placesDefined
	tweets = {}
	lines = 0
	tweets = 0
	for line in file:
		lines += 1
		jsonEncoding = json.loads(line)
		if jsonEncoding.keys() != [u'delete']:
			tweet = jsonEncoding.get(u'text')
			if  jsonEncoding.get(u'place') != None:
				if jsonEncoding[u'place'][u'country'] == 'United States':
					places.append(jsonEncoding[u'place'][u'full_name'])
					for keys in states:
						if statecounts.get(keys) == None: statecounts[keys] = 0
						if jsonEncoding[u'place'][u'full_name'].find(keys) >= 0 or  jsonEncoding[u'place'][u'full_name'].find(states[keys]) >= 0 :
							placesDefined+=1
							statecounts[keys] += 1
							if stateHappiness.get(keys) == None:
								stateHappiness[keys] = score(tweet)
							else:
								stateHappiness[keys] = stateHappiness[keys]/(statecounts[keys]-1) + (1/statecounts[keys]*score(tweet))
		
def statesList():
	global states
	states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

			
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
	statesList()
	global placesDefined
	getTweets(tweet_file)
	#timezones.sort()
	#locations.sort()
	#print timezones
	#print locations
	# print places
	# print statecounts
	# print placesDefined
	# print stateHappiness
	happiness = -100
	for keys in stateHappiness:
		if stateHappiness > happiness:
			state = keys
			happiness = stateHappiness[keys]
	print state
	
	
if __name__ == '__main__':
    main()
	
