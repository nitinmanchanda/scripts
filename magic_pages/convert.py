import csv
import sys

with open('data.csv','rb') as data:
	datain = csv.reader(data, delimiter=',')
	result = open('output.txt', 'w+')

	for row in datain:
		primaryKeyword = row[0].capitalize()
		metaTitle = '%s - Buy %s Online at Best Prices in India - LimeRoad.com' % (primaryKeyword, primaryKeyword)
		metaDescription = '%s - Buy Latest %s Online at Best Prices in India. Best Online Shopping Experience for Women - LimeRoad.com' % (primaryKeyword, primaryKeyword)
		metaKeywords = row[1].strip()
		content = row[2].strip()
		shortDescription = row[3].strip()
		websiteUrl = row[4].strip()
		magicPageUrl = '/m/' + row[0].strip().lower().replace(' ', '-')

		insertQuery = "INSERT INTO custompages (solrSearchQuery, status, url, title, shortDescription, metaTitle, keywords, metaDescription, content, creator_id, created, modifier_id, modified) VALUES (\"%s\", 0, \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", 0, NOW(), 0, NOW());\n" % (websiteUrl, magicPageUrl, primaryKeyword, shortDescription, metaTitle, metaKeywords, metaDescription, content)
		
		# print insertQuery
		# sys.exit(0)

		result.write(insertQuery)

	data.close()
	result.close()
