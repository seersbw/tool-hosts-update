import urllib

url = "https://raw.githubusercontent.com/racaljk/hosts/master/hosts"
content = urllib.urlopen(url).read()


print content
