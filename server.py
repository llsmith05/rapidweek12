from flask import Flask, request, render_template
from lib import bssep as bsep
from lib import termsSearched as ts

app = Flask(__name__)

@app.route('/')
@app.route("/home/")
def landing():
    x = bsep.bssep
    return render_template('landing.html', bsep=x)
    
@app.route('/search')
def search():
	term = request.args.get('')
	return render_template('searchpage.html', bsep=bsep.bssep, term=term)
	
@app.route('/request', methods=['POST'])
def req():
	term = request.form['text'] + ' is what you typed'
	print(term)
	return render_template('request.html', term=term)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
