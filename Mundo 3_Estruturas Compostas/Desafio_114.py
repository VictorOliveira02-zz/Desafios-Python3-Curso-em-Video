import urllib.request

try:
    website = urllib.request.urlopen('http://pudim.com.br/')
except:
    print('\033[41mWebsite is inaccessibel\033[m')
else:
    print('\033[42mWebsite is accessibel\033[m')
    print(website.read())
