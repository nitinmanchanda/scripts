import csv, sys, os, re

categoryMap = {}
redirectMap = {}
finalMap = {}

with open('input.csv','rb') as data:

	result = open('result.out', 'w')
	
	for line in data:

		row = line.strip().split(',')
		currentUrl = row[0].replace('http://www.limeroad.com', '')
		redirectUrl = row[1].replace('http://www.limeroad.com', '')
		wrongRedirects = row[2]
		categoryId = row[3]
		isDuplicate = row[4].lower()
		newUrl = row[5].lower().replace('http://www.limeroad.com', '')

		if isDuplicate == "yes":
			continue

		if redirectUrl != '' and redirectUrl not in redirectMap:
			redirectMap[currentUrl] = redirectUrl

		if categoryId != '' and currentUrl not in categoryMap:
			categoryMap[currentUrl] = newUrl
			if currentUrl != newUrl:
				result.write('rewrite ^' + currentUrl + '(/?)$ ' + newUrl + ' permanent;\n')
			result.write('rewrite ^' + newUrl + '(/?)$ /products/category/' + categoryId + ' last;\n')

	for currentUrl, redirectUrl in redirectMap.iteritems():

		if redirectUrl in categoryMap:
			result.write('rewrite ^' + currentUrl + '(/?)$ ' + categoryMap[redirectUrl] + ' permanent;\n')
		else:
			print "Error: For " + currentUrl + ", given redirect URL " + redirectUrl + " is invalid it seems!"

	data.close()
	result.close()
