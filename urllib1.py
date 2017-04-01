import urllib
file = urllib.open(´http://helloworldbook.com/data/message.txt´)
msg = file.read
print msg
