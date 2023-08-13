import urllib.request
import re
url = input('Enter - ')	#give URL of any website
html = urllib.request.urlopen(url).read()
links = re.findall(b'href="(http://.*?)"', html)
for link in links:
	print(link.decode())
import urllib.request
import re
url = input('Enter - ')	#give URL of any website
html = urllib.request.urlopen(url).read()
links = re.findall(b'href="(http://.*?)"', html)
for link in links:
	print(link.decode())
