import urllib.request
import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import json

# convert to unicode text
def readURL(url):
	return str(urllib.request.urlopen(url).read())

# category is the element in categories
def getURL(category):
	return 'https://www.thumbtack.com/request-categories/suggest?query=' + urllib.parse.quote(category) + '&limit=0'

# extract all queries from the website with url specified
def extract_queries(url):
	htmltext = readURL(url)
	regex = '<datalist id="request_form_hero_datalist">(.*?)</datalist><div class="request-form-hero home">'
	pattern = re.compile(regex)
	allqueries = re.findall(pattern, htmltext)[0] # return a list
	# then extract individual queries in allqueries
	
	regex1 = '<option value="(.*?)">'
	pattern1 = re.compile(regex1)
	queries = re.findall(pattern1,allqueries)
	return queries 

# extract id information from the url specified
def getId(url):
	htmltext = readURL(url)
	regex = '\"id\":\"(.*?)\",\"name\"' # id info pattern
	pattern = re.compile(regex)
	id = re.findall(pattern,htmltext)
	return id[0]

# extract the form content in json format from the url specified with id information
def getFormInJson(id):	
	url = 'https://www.thumbtack.com/request-categories/' + id + '/form-content'
	htmltext = readURL(url)
	text = [htmltext]
	text.append({'url_for_update': url}) # "url_for_update" can be used for future update of the form content
	jtext = json.dumps(text)
	print (jtext)
	print (" ")


home_improvement = 'https://www.thumbtack.com/home-improvement#'
categories = extract_queries(home_improvement)
# print (len(categories)) # 289

# return a list of urls which will be used to extract id. Each url corresponds to one unique id. e.g. id = "id":"JCfO$Crcj:P3TA"
urls_for_extract_id = [getURL(e) for e in categories[0:289]] # till 200 is fine
#urls_for_extract_id = [getURL(e) for e in categories]

# return a list of id corresponds to the urls in the list. Each url corresponds to one unique id. e.g. id = "id":"JCfO$Crcj:P3TA"
ids = [getId(e) for e in urls_for_extract_id]

# print out the content form in json format with url for update for each id
for id in ids:
	getFormInJson(id)


