import urllib
import re
from bs4 import BeautifulSoup


garden_urls = "http://faq.gardenweb.com/faq/" #garden FAQ page
home_urls = "http://ths.gardenweb.com/faq/" #home FAQ page
htmlfile_g = urllib.urlopen(garden_urls)
htmltext_g = htmlfile_g.read() 
htmlfile_h = urllib.urlopen(home_urls)
htmltext_h = htmlfile_h.read()

# test 
# htmltext = '<a class="topic-link mts" href="http://faq.gardenweb.com/forums/butterfly-garden-faq">Butterfly Garden</a>'
#regex1 = '<a class=\"topic-link mts\" href=\"(.*?)\">(.*?)</a>' 
#pattern1 = re.compile(regex1)
#urlpair_g = re.findall(pattern1,htmltext_g)


regex2 = '<a class=\"topic-link mts\" href=\"(.*?)\">.*?</a>' # topic links
pattern2 = re.compile(regex2)
urllist_g = re.findall(pattern2,htmltext_g) # topic links in garden FAQ
urllist_h = re.findall(pattern2,htmltext_h) # topic links in home FAQ

topic = []
topic_urls = []

# home FAQ, topic means category
for url in urllist_h:
	htmlfile = urllib.urlopen(url)
	htmltext = htmlfile.read()
	regex_topic = '<span class=\'questionTitle\'>(.*?)</span>'
	pattern_topic = re.compile(regex_topic)
	topic.append(re.findall(pattern_topic,htmltext))  

	regex_topic_urls = '<a class=\"question-title header-5 text-unbold top colorLink\" href=\"(.*?)\" compid=\"title\">'
	pattern_topic_urls = re.compile(regex_topic_urls)
	topic_urls.append(re.findall(pattern_topic_urls,htmltext)) 

print topic[0:3]
print topic_urls[0:3]
print ('start extracting answers')	

answersToQ = []
answersToTopic = []
for i in topic_urls:
	for url in i:
		html = urllib.urlopen(url).read()
		soup = BeautifulSoup(html,'lxml')
		answerText =soup.select('div#questionDesc')[0].get_text()
		answersToQ.append(answerText) #soup.select() returns a list
	answersToTopic.append(answersToTopic)
print answersToTopic[0:3]		


'''
for category in urllist_h:
	print("gettinng {category}.".format(category))
	questions = 
	for question in qeustions:
		print("geting")
'''