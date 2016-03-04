import urllib
import os
url = "https://raw.githubusercontent.com/racaljk/hosts/master/hosts"
content = urllib.urlopen(url).read()
filePath ='C:\Windows\System32\drivers\etc\hosts'
hostsFile = open(filePath,'w')
hostsFile.write(content)
hostsFile.close()
print 'You have successfully updated your hosts file'
print 'Press any key to exit'
os.system('pause')
