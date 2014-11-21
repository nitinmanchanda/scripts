import csv, sys, os, re

myMap = {}
with open('category_urls.conf','rb') as data:
	test = open('test.conf', 'w')
	writeFile = open('unique_category_urls.conf', 'w')
	writeFileDuplicateInstances = open('duplicate_category_urls.conf', 'w')
	resultSet = open('result.conf', 'w')
	for line in data:
		temp = line.strip().split(':')
		if temp[0] not in myMap:
			myMap[temp[0]] = temp[1]
			writeFile.write('rewrite ^' + temp[0] + '(/?)$ ' + temp[1] + ' last;\n')
			test.write('http://www.limeroad.com' + temp[0] + '\n')
			resultSet.write('rewrite ^' + temp[0] + '(/?)$ ' + '/new-url' + ' last;\n')
			resultSet.write('rewrite ^' + '/new-url' + '(/?)$ ' + temp[1] + ' last;\n')
		else:
			writeFileDuplicateInstances.write('rewrite ^' + temp[0] + '(/?)$ ' + temp[1] + ' last;\n')
	data.close()
	writeFile.close()
	writeFileDuplicateInstances.close()
	resultSet.close()
	test.close()