import urllib.request

try :
    url = urllib.request.urlopen('https://www.python.org/')
    content = url.read()
    url.close
except urllib.error.HTTPError :
    print("Requested web page is not found!!!")
    exit()

f = open('python.html', 'wb')
f.write(content)
f.close()

'''By Ankush Chavan'''