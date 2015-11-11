import urllib.request
import re
from bs4 import BeautifulSoup


def readURL(url):
	return str(urllib.request.urlopen(url).read())
	

garden_urls = "http://faq.gardenweb.com/faq/" #garden FAQ page
home_urls = "http://ths.gardenweb.com/faq/" #home FAQ page
htmlfile_g = urllib.request.urlopen(garden_urls)
htmltext_g = str(htmlfile_g.read())
htmlfile_h = urllib.request.urlopen(home_urls)
htmltext_h = str(htmlfile_h.read())

# test 
# htmltext = '<a class="topic-link mts" href="http://faq.gardenweb.com/forums/butterfly-garden-faq">Butterfly Garden</a>'
#regex1 = '<a class=\"topic-link mts\" href=\"(.*?)\">(.*?)</a>' 
#pattern1 = re.compile(regex1)
#urlpair_g = re.findall(pattern1,htmltext_g)


regex2 = '<a class=\"topic-link mts\" href=\"(.*?)\">.*?</a>' # topic links
pattern2 = re.compile(regex2)
urllist_g = re.findall(pattern2,htmltext_g) # topic links in garden FAQ
urllist_h = re.findall(pattern2,htmltext_h) # topic links in home FAQ

questions = []
question_urls = []

# home FAQ, topic means category
for topic_url in urllist_h:
	htmlfile = urllib.request.urlopen(topic_url)
	htmltext = str(htmlfile.read())
	regex_question = '<span class=\'questionTitle\'>(.*?)</span>'
	pattern_question = re.compile(regex_question)
	quests = re.findall(pattern_question, htmltext)
	#print(quests)
	questions.extend(quests)

	regex_question_urls = '<a class=\"question-title header-5 text-unbold top colorLink\" href=\"(.*?)\" compid=\"title\">'
	pattern_question_urls = re.compile(regex_question_urls)
	quest_urls = re.findall(pattern_question_urls, htmltext)
	question_urls.extend(quest_urls) 
	#print(quest_urls)

# #print questions[0:3]
# #print question_urls[0:3]
# #print ('start extracting answers')	

answers = []
#for url in question_urls: # get urls of one topic
for url in question_urls: 
	html = str(urllib.request.urlopen(url).read())
	soup = BeautifulSoup(html,'html.parser')
	answerText = soup.select('div#questionDesc')[0].get_text() #soup.select() returns a list
	#print(answerText)
	answers.append(answerText)
#print answers[0:3]


#print(len(questions))
#print(len(answers))
for question, answer in zip(questions, answers):
	print('<doc>')
	print('  <field name="question">{0}</field>'.format(question))
	print('  <field name="answer">{0}</field>'.format(answer))
	print('</doc>')

# '''
# for category in urllist_h:
# 	print("gettinng {category}.".format(category))
# 	questions = 
# 	for question in qeustions:
# 		print("geting")
# '''
