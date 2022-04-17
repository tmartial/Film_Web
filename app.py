from flask import Flask
from flask import request, make_response, render_template,redirect
from BDD import *


app = Flask(__name__)

@app.route("/")
def welcome():
    app.logger.debug('serving root URL /')
    return render_template('Welcome.html')

@app.route('/movies')
def movies():
    app.logger.debug('serving root URL /')
    return render_template('movies.html')



@app.route('/type')

def types_page():
    app.logger.debug('serving users URL /types/')
    # The request contains an arguments in the query string

    type_list=[]
    for i in range(len(FILMS)):
        type_list.append(FILMS[i+1]["Type"])
    type_list = {}.fromkeys(type_list).keys()
    return render_template('type.html', types=type_list)


@app.route('/type/<typename>')
def type_movie(typename):
    #app.logger.debug('serving users URL /users/')
    a_type=[]
    for i in range(len(FILMS)):
        if typename==FILMS[i+1]["Type"]:
            a_type.append(FILMS[i+1])
    if request.method=='GET':
        return render_template('type_movies.html', movies=a_type, type=typename)
