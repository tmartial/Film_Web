from flask import Flask
from flask import request, make_response, render_template,redirect
# from BDD import *
import json

with open('dict.json') as json_file:
    FILMS = json.load(json_file)
print(FILMS)

app = Flask(__name__)

@app.route("/")
def welcome():
    app.logger.debug('serving root URL /')
    return render_template('Welcome.html')

@app.route('/movies')
def movies():
    name_list=[]
    for i in range(len(FILMS)):
        name_list.append(FILMS[i]["name"])
    app.logger.debug('serving root URL /')


    return render_template('movies.html',names=name_list)

@app.route('/movies/<name>')
def movies_profile(name):
    for k in range(len(FILMS)):
        if (FILMS[k]["name"]==name):
            this_film=FILMS[k]
            wiki=FILMS[k]["url"]
            cover=FILMS[k]["cover_url"]
    return render_template('movies_profile.html',film=this_film,wiki=wiki,cover=cover )

# Find the different types of movies
@app.route('/type')

def types_page():
    type_list=[]
    for i in range(len(FILMS)):
        type_list.append(FILMS[i]["Type"])
    type_list = {}.fromkeys(type_list).keys()
    return render_template('type.html', types=type_list)

# Get movies of a certain type
@app.route('/type/<typename>')
def type_movie(typename):
    a_type=[] # a list of movies of this type
    for i in range(len(FILMS)):
        if typename==FILMS[i]["Type"]:
            a_type.append(FILMS[i])
    if request.method=='GET':
        return render_template('type_movies.html', movies=a_type, type=typename)

# Find the different actors
@app.route('/actor')
def actors_page():
    actor_list=[]
    for i in range(len(FILMS)):
        for name in FILMS[i]["starring"]:
            actor_list.append(name)
    actor_list = {}.fromkeys(actor_list).keys()
    actor_list = sorted(actor_list)
    return render_template('actor.html', actors=actor_list)

# Get movies of a certain actor
@app.route('/actor/<actorname>')
def actor_movie(actorname):
    an_actor=[] # a list of movies of this actor
    for i in range(len(FILMS)):
        for name in FILMS[i]["starring"]:
            if actorname==name :
                an_actor.append(FILMS[i])
    if request.method=='GET':
        return render_template('actor_movies.html', movies=an_actor, actor=actorname)



# Find the years of publication of movies
@app.route('/year')
def years_page():
    '''
    before_1980=list(range(1980))
    between1980_2000=list(range(1980,2000))
    between2000_2010=list(range(2000,2010))
    between2010_2020=list(range(2010,2020))
    after_2020=list(range(2020,5000))
    '''
    return render_template('year.html', before1980=list(range(1980)), between1980_2000=list(range(1980,2000)),
        between2000_2010=list(range(2000,2010)), between2010_2020=list(range(2010,2020)), after_2020=list(range(2020,5000)))

# Get movies of certain years
@app.route('/year/<years>')
def year_movie(years):

    str=''
    years2=str.join(years)
    years3=years2.replace(' ','')
    years4=years3[1:-1]
    years5=years4.split(",")

    movies_years=[]

    for i in range(len(FILMS)):
        if FILMS[i]["year"] in years5:
            movies_years.append(FILMS[i])

    if int(years5[0]) < 1980:
        period = "before 1980"
    elif int(years5[0]) == 1980:
        period = "between 1980 and 2000"
    elif int(years5[0]) == 2000:
        period = "between 2000 and 2010"
    elif int(years5[0]) == 2010:
        period = "between 2010 and 2020"
    else:
        period = "after 2020"

    return render_template('year_movies.html', movies=movies_years, period=period,years=years5)

def year_movie2(years):
    movies_years=[]
    for i in range(len(FILMS)):
        for j in years :
            if int(FILMS[i]["year"]) == j:
                movies_years.append(FILMS[i])
    if years[0] < 1980:
        period = "before 1980"
    elif years[0] == 1980:
        period = "between 1980 and 2000"
    elif years[0] == 2000:
        period = "between 2000 and 2010"
    elif years[0] == 2010:
        period = "between 2010 and 2020"
    else:
        period = "after 2000"

    return years

print(year_movie2(list(range(1980))))
before_1980=range(1980)
years=before_1980
print(years[0]<2)

@app.route('/bibliography')
def bibliography():
    return render_template('bibliography.html')

@app.route('/add_movies', methods=['GET','POST'])
def add_movies_page():
    if request.method == 'POST':
        dict_length = len(FILMS)
        movie_name = request.form.get("name_movie")
        movie_type = request.form.get("type")
        movie_wiki = request.form.get("url_wikipedia_movie")
        movie_year = request.form.get("year_movie")
        actors = request.form.get("actor_movie")
        actor = actors.replace(' ','')
        movie_actor = actor.split(',')
        movie_length = request.form.get("length_movie")
        movie_cover = request.form.get("cover_movie")
        new_film = {'name': movie_name,
                                'id' : dict_length+1,
                                'Type': movie_type,
                                'url':movie_wiki,
                                'year': movie_year,
                                'starring': movie_actor,
                                'film_length' : movie_length,
                                'cover_url':movie_cover}
        # Writing a new dict object to a file as append and overwrite the whole file
        with open("dict.json", mode='w') as f:
            FILMS.append(new_film)
            json.dump(FILMS, f)
    return render_template('add_movies.html')
