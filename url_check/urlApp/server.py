from flask import Flask, request, Response, jsonify, render_template
from flask.ext.cors import CORS
import svm_result as uc
app = Flask(__name__)
import urllib2
import httplib
CORS(app)


@app.route('/')
def load():
    return render_template('bt.html')

@app.route('/api/', methods=['POST', 'GET'])
def api_response():
    if request.method == 'POST':
        url = str(request.data)
        #url = addHttpIfNeeded(url)
        print url
        try:
            urllib2.urlopen(url)
            result = str(uc.checkUrl(url))
        except:
            return 'fail'
    	return result

if __name__ == '__main__':
	app.debug = True
	app.run()
