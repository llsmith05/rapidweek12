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
    color = int(color)
    
    #Type
    if type == "uphone":
        path = path + "uPhone/"
    elif type == "mandroid":
        path = path + "manDroid/"
    elif type == "blueberry":
        path = path + "blueberry/"

    if color == 1:
        path = path + "01.JPG"
    elif color == 2:
        path = path + "02.JPG"
    elif color == 3:
        path = path + "03.JPG"
    elif color == 4:
        path = path + "04.JPG"
    elif color == 5:
        path = path + "05.JPG"
    else:
        path = path + "01.JPG"

    print(path)

    return path

if __name__ == "__main__":
    app.run(debug=True)
