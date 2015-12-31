import os

hostname = "google.com"
response = os.popen('ping -c 1 ' + hostname).read()

f = response.find('time=', 0)
e = response.find(' ', f)

print response[f + 5:e]