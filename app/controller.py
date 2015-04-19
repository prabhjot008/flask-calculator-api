from app import app
from flask import render_template


@app.route('/')


def index_route():
    return render_template('welcome_b.html')


@app.route('/add/<int:a>/and/<int:b>')


def adder(a,b):
    c=a+b
    return render_template('calc_history.html',result=c)


@app.route('/subtract/<int:a>/and/<int:b>')

def subtractor(a,b):
    d=a-b
    return render_template('calc_history.html',result=d)

@app.route('/multiply/<int:a>/and/<int:b>')

def multiplier(a,b):
    f=a*b
    return render_template('calc_history.html',result=f)

@app.route('/divide/<int:a>/and/<int:b>')

def divider(a,b):
    if b==0:
        return('Divide by zero is not valid')
    g=a/b
    return render_template('calc_history.html',result=g)

