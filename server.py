from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from threading import Thread
import SocketServer
import json
import cgi
from urlparse import urlparse, parse_qs
import subprocess
import os
import re
class ThreadedHTTPServer(HTTPServer):
    def process_request(self, request, client_address):
        thread = Thread(target=self.__new_request, args=(self.RequestHandlerClass, request, client_address, self))
        thread.start()
    def __new_request(self, handlerClass, request, address, server):
        handlerClass(request, address, server)
        self.shutdown_request(request)


class Server(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
    def do_HEAD(self):
        self._set_headers()
        
    # GET sends back a Hello world message
    def do_GET(self):
		self._set_headers()
		query_components = parse_qs(urlparse(self.path).query)
		print(query_components)
		dbTableId = query_components["dbTableId"]
		hiveDbNm = query_components["hiveDbNm"]
		hiveTableNm = query_components["hiveTableNm"]
		dbTableId=dbTableId[0]
		hiveDbNm=hiveDbNm[0]
		hiveTableNm=hiveTableNm[0]
		print dbTableId,hiveDbNm,hiveTableNm
		cmd = "mongo --eval \"a=db.getSiblingDB(\'"+hiveDbNm+"\')."+hiveTableNm+".find({},{_id:0}).toArray(); printjson(a)  \" | sed -n  \"5,\$p\" | sed 's/[\t\f]//g' "
#		os.system("mongo --eval \"a=db.getSiblingDB('"+hiveDbNm+"')."+hiveTableNm+".find().toArray();\" | sed -n -n \"3,\$p\"")
		#out = subprocess.Popen(['mongo', '--eval', "a=db.getSiblingDB('"+hiveDbNm+"')."+hiveTableNm+".find().toArray();"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
		output=subprocess.check_output(cmd,shell=True)
		pattern=re.compile(r'\s+')
		output=re.sub(pattern,'',output)
		
		#self.wfile.write(json.dumps({'hello': 'world', 'received': 1}))
		print output
		self.wfile.write(output)
    # POST echoes the message adding a JSON field
    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
        
        # refuse to receive non-json content
        if ctype != 'application/json':
            self.send_response(400)
            self.end_headers()
            return
            
        # read the message and convert it into a python dictionary
        #length = int(self.headers.getheader('content-length'))
        #message = json.loads(self.rfile.read(length))
        length = int(self.headers.get('content-length'))
        message_string = self.rfile.read(length).decode('utf-8')
        message = json.loads(message_string) if message_string else None
        
        
        # add a property to the object, just to mess with data
        message['received'] = 'ok'
        
        # send the message back
        self._set_headers()
        self.wfile.write(json.dumps(message))
        
def run(server_class=HTTPServer, handler_class=Server, port=8008):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    
    print 'Starting httpd on port %d...' % port
    httpd.serve_forever()
    
if __name__ == "__main__":
    from sys import argv
    
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
