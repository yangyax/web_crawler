import urllib.request
import re
from bs4 import BeautifulSoup


def readURL(url):
	return urllib.request.urlopen(url).read().decode("utf-8")
	

garden_url = "http://faq.gardenweb.com/faq/" #garden FAQ page
home_url = "http://ths.gardenweb.com/faq/" #home FAQ page
garden_html = readURL(garden_url)
home_html = readURL(home_url)

regex2 = '<a class="topic-link mts" href="(.*?)">' # topic links
pattern2 = re.compile(regex2)
urllist_g = re.findall(pattern2, garden_html) # topic links in garden FAQ
urllist_h = re.findall(pattern2, home_html) # topic links in home FAQ

questions = []
question_urls = []

# home FAQ, topic means category
for topic_url in urllist_h:
	htmltext = readURL(topic_url)
	regex_question = "<span class='questionTitle'>(.*?)</span>"
	pattern_question = re.compile(regex_question)
	quests = re.findall(pattern_question, htmltext)
	questions.extend(quests)

	regex_question_urls = '<a class="question-title header-5 text-unbold top colorLink" href="(.*?)" compid="title">'
	pattern_question_urls = re.compile(regex_question_urls)
	quest_urls = re.findall(pattern_question_urls, htmltext)
	question_urls.extend(quest_urls) 


answers = []
#for url in question_urls: # get urls of one topic
for url in question_urls: 
	html = readURL(url)
	soup = BeautifulSoup(html,'html.parser')
	answerText = soup.select('div#questionDesc')[0].get_text() #soup.select() returns a list
	answers.append(answerText)


# print(len(questions))
# print(len(answers))
# print(len(question_urls))
for question, answer in zip(questions, answers):
	print('<doc>')
	print('  <field name="question">{0}</field>'.format(question))
	print('  <field name="answer">{0}</field>'.format(answer))
	print('</doc>')
