import urllib.request

response = urllib.request.urlopen('http://python.org/')
html = response.read()
print(response.getcode())
