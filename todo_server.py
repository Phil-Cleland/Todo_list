
from flask import *
 
app = Flask(__name__)

items=[]
 
@app.route('/')
def index():
    return render_template('form.html', items=items)

@app.route('/add_todo')
def add_todo():
    item = request.args.get("item")
    print(item)
    items.append(item)
    return redirect("http://localhost:5000/", code=302)

@app.route('/get_todos')
def get_todos():
    resp = Response(json.dumps(items))
    resp.headers['Content-Type'] = 'application/json'
    return resp

@app.route('/foo/<name>')
def foo(name):
    return render_template('index.html', to=name)
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    

