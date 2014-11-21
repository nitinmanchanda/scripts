import csv, sys, os, re

myMap = {}
with open('conf-824.in','rb') as data:
	for line in data:
		temp = line.strip().split(':')
		if temp[0] not in myMap:
			myMap[temp[0]] = temp[1]
	data.close()

catList = []
with open('db-519.in','rb') as data:
	for line in data:
		catId = line.strip()
		if catId not in catList:
			catList.append(catId)
	data.close()

validCategories = open('validCategories.out', 'w')
validCategories.write('# valid categories\n')
oldCategories = open('oldCategories.out', 'w')
oldCategories.write('# old categories - soft 404 to home page\n')
for url, catId in myMap.iteritems():
	if catId in catList:
		validCategories.write('rewrite ^' + url + '(/?)$ /products/category/' + catId + ' last;\n')
	else:
		oldCategories.write('rewrite ^' + url + '(/?)$ / last;\n')

validCategories.close()
oldCategories.close()