from flask import Flask,render_template
from flask import redirect

app=Flask(__name__)

#from flask import make_response
#@app.route('/')
#def index():
#    response = make_response('<h1>This document carries a cookie!</h1>')
#    response.set_cookie('answer', '42')
#    return response


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

#@app.route('/')
#def hello_world():
#    return 'Hello World!'


#@app.route('/')
#def index():
#    return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello'


@app.route('/about')
def about():
    return 'The about page'


@app.route('/projects/')
def projects():
    return 'The project page'


class Human():
    def somemethod(self):
        return 'what the fucking world!'

@app.route('/vars')
def users():
    mydict = {"key": "To Be or Not To Be"}
    mylist = ['it', 'is', 'a', 'problem']
    myintvar = int(1)
    myobj = Human()

    return render_template('vars.html', mydict=mydict, mylist=mylist, myintvar=myintvar, myobj=myobj)

@app.route('/flow')
def flow():
    user = 'tangyefei'
    return render_template('flow.html', user=user)


@app.route('/loop')
def loop():
    comments = ["To Be","Or","Not To Be"]
    return render_template('loop.html',comments=comments)


@app.route('/macro')
def macro():
    comments = ["To Be", "Or", "Not To Be"]
    return render_template('macro.html', comments=comments)

@app.route('/extends')
def extends():
    return render_template('child.html')






if __name__ =='__main__':
    app.run(debug=True)
    

