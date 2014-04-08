from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home/')
def landing():
    return render_template('landing.html')
 
@app.route('/search')
def search():
	#term = request.args.get('')
	return render_template('search.html')

@app.route('/view/')
def view():
    type = request.args.get('type')
    color = request.args.get('color') or None
    return render_template('view.html', case_img_url = GetCaseImage(type, color))

# In template, use <img src={{url_for('static', filename = case_img_url)}} />

def GetCaseImage(type, color = None):
    path = "images/"
    
    type = type.lower()
    if color != None:
        color = color.lower()
    
    #Type
    if type == "uphone":
        path = path + "uPhone/"
    elif type == "mandroid":
        path = path + "manDroid/"
    elif type == "blueberry":
        path = path + "blueberry/"

    if color == 1:
        path = path + "one.gif"
    elif color == 2:
        path = paht + "two.jpg"
    elif color == 3:
        path = path + "three.jpg"
    else:
        path = path + "one.gif"

    return path

if __name__ == "__main__":
    app.run(debug=True)
