from urllib.request import urlopen

page_text = urlopen("http://mezuro.org/humans.txt")
print(page_text.read(), "utf8")
