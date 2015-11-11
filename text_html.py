import urllib
from bs4 import BeautifulSoup

url = "http://ths.gardenweb.com/discussions/2767118/what-should-i-know-about-installing-a-subpanel"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

elements = soup.select('div#questionDesc')

for element in elements:
	print element.get_text()

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

print len(elements)

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

# print(text)