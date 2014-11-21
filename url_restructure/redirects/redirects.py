import csv, sys, os, re

redirectMap = {}
with open('301_302_clean.conf','rb') as data:
	redirect = open('redirect_map.out', 'w')
	redirectDuplicate = open('redirect_map_duplicate.out', 'w')
	for line in data:
		temp = line.strip().split(':')
		if temp[0] not in redirectMap:
			redirectMap[temp[0]] = temp[1]
			redirect.write('rewrite ^' + temp[0] + '(/?)$ ' + temp[1] + ';\n')
		else:
			redirectDuplicate.write('rewrite ^' + temp[0] + '(/?)$ ' + temp[1] + ';\n')
	data.close()
	redirect.close()
	redirectDuplicate.close()

print len(redirectMap)

categoryMap = {}
with open('category_urls.conf','rb') as data:
	for line in data:
		temp = line.strip().split(':')
		if temp[0] not in categoryMap:
			categoryMap[temp[0]] = temp[1]
	data.close()

print len(categoryMap)

newMap = {}
notFound = {}
for oldUrl, newUrl in redirectMap.iteritems():
	if newUrl in categoryMap:
		newMap[oldUrl] = newUrl
	else:
		notFound[oldUrl] = newUrl

doubleRedirectCases = 0
for oldUrl, newUrl in notFound.iteritems():
	if newUrl in redirectMap:
		doubleRedirectCases = doubleRedirectCases + 1
		newMap[oldUrl] = newUrl
	else:
		print oldUrl

print len(newMap)
print len(notFound)
print doubleRedirectCases

newConfig = open('new_config.conf', 'w')
for a, b in newMap.iteritems():
	newConfig.write('rewrite ^' + a + '(/?)$ ' + b + ';\n')
newConfig.close()

print notFound