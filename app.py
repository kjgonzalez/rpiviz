'''
STAT|DESCRIP
TODO functionality tests
TODO add other info pages
TODO think of other bits of info to add
TODO find way to make waitress properly output data instead of needing to do it self

Miscellaneous notes:
* don't ever link a full path, the user's browser won't understand
* you can't link to something outside of the project, either
* individual functions are run each time page is requested
'''
from flask import Flask, render_template
from datetime import datetime
import json
import socket
#import logging
# logger = logging.getLogger('waitress')
#logger.setLevel(logging.INFO)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/'

with open('static/config.json') as f:
    dat = json.load(f)

def printaccess():
    print('GET index [{}]'.format(str(datetime.now())))

@app.route("/")
@app.route("/index")
def show_index():
    ''' "Homepage", accessed via <ipaddress>:<port> '''
    printaccess()
    if (type(dat['info']) == str):
        # allow for both single and multiple information lines
        dat['info'] = [dat['info']]
    return render_template('index.html',
                           analysis_title=dat['title'],
                           info=dat['info'],
                           data=dat['datpath'],
                           img=dat['imgpath']
                           )

@app.route('/status')
def status():
    printaccess()
    d = dict()
    d['hwname'] = dat['hwname']
    d['purpose'] = dat['purpose']
    d['starttime'] = dat['starttime']
    return str(d)

if __name__ =="__main__":
    from waitress import serve
    local_ip = socket.gethostbyname(socket.gethostname())
    port = 1010
    print('running, starting at {}'.format(str(datetime.now())))
    print('address: {}:{}'.format(local_ip,port))
    dat['starttime']=str(datetime.now())
    serve(app,port=port)

# eof
