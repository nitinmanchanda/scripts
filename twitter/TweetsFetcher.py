import requests, bs4, sys

profileUrl = sys.argv[1]

try:
	response = requests.get(profileUrl)
except Exception, e:
	print "First command line argument should be a valid twitter profile link! \nFor instance: 'https://twitter.com/narendramodi'\n"
	sys.exit(0)

soup = bs4.BeautifulSoup(response.text)

links = soup.select('p.ProfileTweet-text')

print "All tweets for the profile URL '" + profileUrl + "' are as follows: \n"
counter = 1
for p in links:
	print "Tweet #" + str(counter) + " : " + p.get_text()
	counter += 1