from flask import Flask
from flask import request, make_response, render_template,redirect

app = Flask(__name__)

@app.route("/")
def welcome():
    app.logger.debug('serving root URL /')
    return render_template('Welcome.html')

@app.route('/movies')
def movies():
    app.logger.debug('serving root URL /')
    return render_template('movies.html')
