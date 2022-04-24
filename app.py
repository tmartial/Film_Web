from flask import Flask
from flask import request, make_response, render_template,redirect,url_for
from BDD import *
import json
from itertools import chain
import string


with open('dict.json') as json_file:
    FILMS = json.load(json_file)
print(FILMS)

print(type(FILMS[0]["id"]))

app = Flask(__name__)

@app.route("/")
def welcome():
    app.logger.debug('serving root URL /')
    if request.args:
        return search(request)
    return render_template('Welcome.html')

@app.route("/<searched_ids>")
def searched_page(searched_ids):
    str=''
    ids=str.join(searched_ids)
    ids2=ids.replace(' ','')
    ids3=ids2[1:-1]
    ids4=ids3.split(",")

    if ids4[0]=='':
        return render_template('no_search_result.html')

    else :
        name_list=[]
        cover=[]
        films=[]
        order=0
        for k in ids4:
            cover.append(FILMS[int(k)]['cover_url'])
            name_list.append(FILMS[int(k)]['name'])
            films.append(FILMS[int(k)])
            order+=1
        ordered=range(order)
        return render_template('searched_movies.html',names=name_list, movies=films, covers=cover, ids=ordered, ids4=ids4)

@app.route("/<search_word>")
def searched_none(search_word):
    return render_template('no_search_result.html',searching_word=search_word)


@app.route('/movies')
def movies():
    # use this command after rerunning the BDD.py to get all the 5 movies when test delete
    '''
    with open('dict.json') as json_file:
        FILMS = json.load(json_file)
    '''
    name_list=[]
    cover=[]
    id=[]
    for k in range(len(FILMS)):
        cover.append(FILMS[k]['cover_url'])
        id.append(k)
        name_list.append(FILMS[k]['name'])
    return render_template('movies.html',names=name_list, movies=FILMS, covers=cover, ids=id)



@app.route('/movies/<name>', methods=['GET','POST'])
def movies_profile(name):
    if request.method == 'GET':
        for k in range(len(FILMS)):
            if (FILMS[k]["name"]==name):
                this_film=FILMS[k]
                wiki=FILMS[k]["url"]
                cover=FILMS[k]["cover_url"]
                mean_score=sum(FILMS[k]['score'])/len(FILMS[k]['score'])
                print(sum(FILMS[k]['score']))
                print(len(FILMS[k]['score']))
                print(mean_score)
        return render_template('movies_profile.html',film=this_film,wiki=wiki,cover=cover,mean_score=mean_score)

    if request.method == 'POST':
        dict_length = len(FILMS)
        for i in range(dict_length):
            if FILMS[i]["name"]==name :
                this_film=FILMS[i]
                wiki=FILMS[i]["url"]
                cover=FILMS[i]["cover_url"]
                #mean_score=sum(FILMS[i]['score'])/len(FILMS[i]['score'])
                id = i

        movie_score = request.form.get("note")
        with open("dict.json", mode='w') as f:
            FILMS[id]['score'].append(float(movie_score))
            json.dump(FILMS, f)

        mean_score=sum(FILMS[i]['score'])/len(FILMS[i]['score'])
    return render_template('movies_profile.html',film=this_film,wiki=wiki,cover=cover,mean_score=mean_score)

@app.route('/movies/<indice>', methods=['GET','POST'])
def delete_movie(indice):
    if request.method == 'POST':
        with open("dict.json", mode='w') as f:
            FILMS.pop(int(indice))
            json.dump(FILMS, f)

        name_list=[]
        cover=[]
        id=[]
        for k in range(len(FILMS)):
            cover.append(FILMS[k]['cover_url'])
            id.append(k)
            name_list.append(FILMS[k]['name'])
        return render_template('movies.html',names=name_list, movies=FILMS, covers=cover, ids=id)


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
    indices=[]
    covers=[]
    order=0
    for i in range(len(FILMS)):
        if typename==FILMS[i]["Type"]:
            a_type.append(FILMS[i])
            covers.append(FILMS[i]["cover_url"])
            order+=1
    ordered=range(order)
    if request.method=='GET':
        return render_template('type_movies.html', movies=a_type, covers=covers,type=typename, ordered=ordered)

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
    covers=[]
    order=0
    for i in range(len(FILMS)):
        for name in FILMS[i]["starring"]:
            if actorname==name :
                an_actor.append(FILMS[i])
                covers.append(FILMS[i]["cover_url"])
                order+=1
    ordered=range(order)
    if request.method=='GET':
        return render_template('actor_movies.html', movies=an_actor, covers=covers,actor=actorname,ordered=ordered)



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
    covers=[]
    order=0

    for i in range(len(FILMS)):
        if FILMS[i]["year"] in years5:
            movies_years.append(FILMS[i])
            covers.append(FILMS[i]["cover_url"])
            order+=1
    ordered=range(order)

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

    return render_template('year_movies.html', movies=movies_years, period=period,years=years5,covers=covers,ordered=ordered)
'''
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
'''

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

@app.route('/scores')
def scores():
        return render_template('scores.html', zero_to_one=[0,1], one_to_two=[1,2],
            two_to_three=[2,3], three_to_four=[3,4], four_to_five=[4,5])

# Get movies of certain years
@app.route('/scores/<scores>')
def scores_movies(scores):

    movies_scores=[]
    covers=[]
    order=0
    print(scores)
    print(scores[0])
    print(scores[4])
    print("lalala", FILMS[1]['score'])
    inf=float(scores[1])
    sup=float(scores[4])

    for i in range(len(FILMS)):
        mean_score=sum(FILMS[i]['score'])/len(FILMS[i]['score'])
        if mean_score <= sup and mean_score > inf : #à remplacer par la moyenne
            movies_scores.append(FILMS[i])
            covers.append(FILMS[i]["cover_url"])
            order+=1
    ordered=range(order)

    return render_template('scores_movies.html', movies=movies_scores ,covers=covers,ordered=ordered,inf=inf,sup=sup)

#Je ferais la méthode demain
'''@app.route('/movies/<name>', methods=['GET','POST'])
def add_note(name):
    if request.method == 'POST':
        dict_length = len(FILMS)
        for i in range(dict_length):
            if FILMS[i]["name"]==name :
                id = i
        movie_score = request.form.get("note")
        #movie_type = request.form.get("type")
        #movie_wiki = request.form.get("url_wikipedia_movie")
        #movie_year = request.form.get("year_movie")
        #actors = request.form.get("actor_movie")
        #actor = actors.replace(' ','')
        #movie_actor = actor.split(',')
        #movie_length = request.form.get("length_movie")
        #movie_cover = request.form.get("cover_movie")
        #new_film = {'name': movie_name,
                                #'id' : dict_length+1,
                                #'Type': movie_type,
                                #'url':movie_wiki,
                                #'year': movie_year,
                                #'starring': movie_actor,
                                #'film_length' : movie_length,
                                #'cover_url':movie_cover}

        # Writing a new dict object to a file as append and overwrite the whole file
        with open("dict.json", mode='w') as f:
            FILMS[id]['score'].append(movie_score)
            json.dump(FILMS, f)
    return render_template('movies_profile.html') '''

def search(request):
    app.logger.debug(request.args)
    #abort(make_response('Not implemented yet ;)', 501))
    searchword = request.args.get('pattern', '') # ici key est 'pattern'
    name_list=[]
    year_list=[]
    actor_list=[]
    type_list=[]
    for k in range(len(FILMS)):
        year_list.append(FILMS[k]['year'])
        actor_list.append(FILMS[k]['starring'])
        name_list.append(FILMS[k]['name'])
        type_list.append(FILMS[k]['Type'])
    actors_list = list(chain(actor_list))

    searched_movies=[]
    for i in range(len(FILMS)):
        if searchword in name_list[i] or searchword in name_list[i].lower() or searchword in name_list[i].upper():
            searched_movies.append(i)
        if searchword==type_list[i] or searchword==type_list[i].lower() or searchword==type_list[i].upper():
            searched_movies.append(i)
        if searchword==year_list[i]:
            searched_movies.append(i)
        for j in actor_list[i]:
            if searchword in j or searchword in j.lower() or searchword in j.upper():
                searched_movies.append(i)

    return redirect(url_for('searched_page', searched_ids= searched_movies))
