"""
fetch a file from an HTTP (web) server over sockets via http.client; the filename
parameter may have a full directory path, and may name a CGI script with ? query
parameters on the end to invoke a remote program; fetched file data or remote
program output could be saved to a local file to mimic FTP, or parsed with str.find
or html.parser module; also: http.client request(method, url, body=None, hdrs={});
"""

import sys, http.client
showlines = 6
try:
	servername, filename = sys.argv[1:]
except:
	servername, filename = 'flerat.com', '/index.html'
	#servername, filename = 'learning-python.com', '/index.html'

print(servername, filename)
server = http.client.HTTPConnection(servername)
server.putrequest('GET', filename)
server.putheader('Accept', 'text/html')
server.endheaders()

reply = server.getresponse()

if reply.status != 200:
	print('Error sending request', reply.status, reply.reason)
else:
	data = reply.readlines()
	reply.close()
	for line in data[:showlines]:
		print(line)
