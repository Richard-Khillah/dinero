from optparse import OptionParser
from app import app

parser = OptionParser()
parser.add_option("-p", "--port", dest="user_port", help="port to run server on", metavar="PORT")
parser.add_option("-u", "--host", dest="user_host", help="host to run on ", metavar="HOST")

(options, args) = parser.parse_args()

user_port = 5000
user_host = '127.0.0.1'

if options.user_port != None:
    user_port = int(options.user_port)
if options.user_host != None:
    user_host = options.user_host

app.run(debug=True, port=user_port, host=user_host)
