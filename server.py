from BaseHTTPServer import BaseHTTPRequestHandler
from threading import Thread
import cgi,datetime
from keyer import keypress

class PostHandler(BaseHTTPRequestHandler):
    
    def do_POST(self):
        # Parse the form data posted
        form = cgi.FieldStorage(
            fp=self.rfile, 
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })

        # Begin the response
        self.send_response(200)
        self.end_headers()
        self.wfile.write('Client: %s\n' % str(self.client_address))
        self.wfile.write('User-agent: %s\n' % str(self.headers['user-agent']))
        self.wfile.write('Path: %s\n' % self.path)
        self.wfile.write('Form data:\n')
        
		# Echo back information about what was posted in the form
        for field in form.keys():
            #print form[field].value
             keypress(form[field].value)
        return
		
if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('0.0.0.0', 8090), PostHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()

