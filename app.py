from flask import Flask
from flask import request, make_response, render_template, redirect, url_for
import json
from itertools import chain
import string

# After running BDD.py, we get the file dict.json in which the original list of movie dictionaries are stored and the modification of dictionaries can be stored.
# We read the dict.json file to get the list of movie dictionaries FILMS which we can operate.
with open('dict.json') as json_file:
    FILMS = json.load(json_file)



app = Flask(__name__)

@app.route("/")
def welcome():
    '''
    Function allowing to show the page Welcome.html

            Parameters:
                    None

            Returns:
                    Redirect to the search(request) function if there's a request of searching
                    Show the page of Welcome.html if there's no action of search
    '''
    app.logger.debug('serving root URL /')
    if request.args:
        return search(request)
    return render_template('Welcome.html')



@app.route("/<searched_ids>")
def searched_page(searched_ids):
    '''
    Function allowing to show the page of the searching result

            Parameters:
                    searched_ids(list) : list of the indices of movies found with the searching word

            Returns:
                    Show the page of no_search_result.html if there's no movie with information corresponding to the searching word
                    Show the page of searched_movies.html if there are any movies found with the searching word, in providing to all the parameters with information needed to show in this page :
                    names(list) : names of searched movies
                    movies(list) : list of searched movies(dictionaries)
                    covers(list) : links of cover of each searched movie
                    ids(list) : list of continuous int from 0 to the number of searched movies-1
    '''
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
        return render_template('searched_movies.html',names=name_list, movies=films, covers=cover, ids=ordered)



@app.route('/movies')
def movies():
    '''
    Function allowing to show the page with all the movies

            Parameters:
                    None

            Returns:
                    Show the page of movies.html in providing to all the parameters with information needed to show in this page :
                    names(list) : names of all the movies
                    movies(list) : list of all the movies(dictionaries)
                    covers(list) : links of cover of every movie
                    ids(list) : list of continuous int from 0 to the number of movies-1

    '''
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
    '''
    Function allowing to show the profile of a movie. If we add a score to the movie in this page which is a method "POST", we calculate the mean of all the scores of this movie and refresh this page.

            Parameters:
                    name(string) : the name of a movie

            Returns:
                    Show the page of movies_profile.html in providing to all the parameters with information needed to show in this page :
                    film(dict) : dictionary of a movie
                    wiki(string) : link to Wikipedia of this movie
                    cover(string) : link to get this movie's cover
                    mean_score(float) : the mean of all the scores of this movie

    '''
    if request.method == 'GET':
        for k in range(len(FILMS)):
            if (FILMS[k]["name"]==name):
                this_film=FILMS[k]
                wiki=FILMS[k]["url"]
                cover=FILMS[k]["cover_url"]
                mean_score=sum(FILMS[k]['score'])/len(FILMS[k]['score'])
                mean_score=round(mean_score,2)
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
        for i in range(dict_length):
            if FILMS[i]["name"]==name :
                mean_score=sum(FILMS[i]['score'])/len(FILMS[i]['score'])
                mean_score=round(mean_score,2)
    return render_template('movies_profile.html',film=this_film,wiki=wiki,cover=cover,mean_score=mean_score)



@app.route('/movies/<indice>', methods=['GET','POST'])
def delete_movie(indice):
    '''
    Function allowing to show the page of all the movies after deleting a certain movie.

            Parameters:
                    indice(int) : the position the movie to remove from the original list

            Returns:
                    Show the page of movies.html in providing to all the parameters with information needed to show in this page :
                    names(list) : names of all the movies
                    movies(list) : list of all the movies
                    covers(list) : links of cover of every movie
                    ids(list) : list of continuous int from 0 to the number of movies-1

    '''
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
    '''
    Function allowing to show the page of all the types of movies.

            Parameters:
                    None

            Returns:
                    Show the page of type.html in providing to all the parameters with information needed to show in this page :
                    types(list) : list of all the existant types of movies
    '''
    type_list=[]
    for i in range(len(FILMS)):
        type_list.append(FILMS[i]["Type"])
    type_list = sorted(type_list)
    type_list = {}.fromkeys(type_list).keys()
    return render_template('type.html', types=type_list)


# Get movies of a certain type
@app.route('/type/<typename>')
def type_movie(typename):
    '''
    Function allowing to show all the movies of a certain type.

            Parameters:
                    typename(string) : one type of movies you want to search

            Returns:
                    Show the page type_movies.html in providing to all the parameters with information needed to show in this page :
                    movies(list) : list of movies of this type
                    covers(list) : list of links(string) to the cover of searched movies
                    type(string) : get this type(string) you search
                    ordered(list) : list of continuous int from 0 to the number of searched movies-1
    '''
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
    '''
    Function allowing to show all the actors involved in all the movies.

            Parameters:
                    None

            Returns:
                    Show the page actor.html in providing to all the parameters with information needed to show in this page :
                    actors(list) : list of names(string) of all the actors
    '''
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
    '''
    Function allowing to show all the movies of a certain actor.

            Parameters:
                    actorname(string) : the name of an actor whose movies you want to search

            Returns:
                    Show the page actor_movies.html' in providing to all the parameters with information needed to show in this page :
                    movies(list) : list of movies of this actor
                    covers(list) : list of links(string) to the cover of searched movies
                    actor(string) : get this name(string) of actor whose movies you search
                    ordered(list) : list of continuous int from 0 to the number of searched movies-1
    '''
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
    Function allowing to show the page with different periods of release years of movies.

            Parameters:
                    None

            Returns:
                    Show the page year.html in providing to all the parameters with information needed to show in this page :
                    before1980(list) : list of continuous int from 0 to 1979
                    between1980_2000(list) : list of continuous int from 1980 to 1999
                    between2000_2010(list) : list of continuous int from 2000 to 2009
                    between2010_2020(list) : list of continuous int from 2010 to 2019
                    after2020(list) : list of continuous int from 2020 to 4999
                    These lists will be used as parameter "years" of the function year_movie() below to classify the movies according to different release periods. So you can search movies of a certain period.
    '''
    return render_template('year.html', before1980=list(range(1980)), between1980_2000=list(range(1980,2000)),
        between2000_2010=list(range(2000,2010)), between2010_2020=list(range(2010,2020)), after_2020=list(range(2020,5000)))


# Get movies of certain years
@app.route('/year/<years>')
def year_movie(years):
    '''
    Function allowing to show all the movies released in a certain period.

            Parameters:
                    years(list) : list of string with every element of the list of years like before1980, between1980_2000 above. Because the list will be turned to string when this function is called by url_for in year.html.

            Returns:
                    Show the page year_movies.html in providing to all the parameters with information needed to show in this page :
                    movies(list) : list of movies released in this period
                    period(string) : get the string to print the release period of movies which you search
                    years(list) : list of years when the searched movies were released
                    covers(list) : list of links(string) to the cover of searched movies
                    ordered(list) : list of continuous int from 0 to the number of searched movies-1
    '''

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



@app.route('/bibliography')
def bibliography():
    '''
	Function allowing to show the page bibliography.html

                Parameters :
                            None
		        Returns :
                        Show the page bibliography.html in providing to all the parameters with information needed to show in this page :
                        names(list) : list containing the names of all the movies.
                        movies(list): list containing the json file’s list.
                        covers(list) : list containing the covers of all the movies.
                        ids(list) : list containing the keys of all the movies.

    '''
    name_list=[]
    cover=[]
    id=[]
    for k in range(len(FILMS)):
        cover.append(FILMS[k]['cover_url'])
        id.append(k)
        name_list.append(FILMS[k]['name'])
    return render_template('bibliography.html',names=name_list, movies=FILMS, covers=cover, ids=id)


@app.route('/add_movies', methods=['GET','POST'])
def add_movies_page():
    '''
	Function allowing to add a movie to the site by filling in some mandatory information. The user needs to fill in the name of the movie, its release year, its length, its wikipedia url, its type, its cover, some of its actors and add a note to this movie.

	            Parameters :
                            None

	            Returns :
                        Show the page add_movies.html with all the cases to fill blank.
                        The new movie is added in the json file.
    '''

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
        movie_score=[]
        movie_score.append(float(request.form.get("note")))

        new_film = {'name': movie_name,
                                'id' : dict_length+1,
                                'Type': movie_type,
                                'url':movie_wiki,
                                'year': movie_year,
                                'starring': movie_actor,
                                'film_length' : movie_length,
                                'cover_url':movie_cover,
                                'score':movie_score}
        # Writing a new dict object to a file as append and overwrite the whole file
        with open("dict.json", mode='w') as f:
            FILMS.append(new_film)
            json.dump(FILMS, f)
    return render_template('add_movies.html')



@app.route('/scores')
def scores():
    '''
	Function allowing to show the page scores.html

	            Parameters :
                            None

	            Returns :
                        Show the page scores.html with a button referring to movies’ classification, in providing to all the parameters with information needed to show in this page :
                        zero_to_one(list): list containing the lower and higher score accepted to be selected in the list returning the scores in between zero and one.
                        one_to_two(list) : list containing the lower and higher score accepted to be selected in the list returning the scores in between 1 and two.
                        two_to_three(list) :list containing the lower and higher score accepted to be selected in the list returning the scores in between two and three.
                        three_to_four(list):list containing the lower and higher score accepted to be selected in the list returning the scores in between three and four.
                        four to five(list):list containing the lower and higher score accepted to be selected in the list returning the scores in between four and five.
    '''

    return render_template('scores.html', zero_to_one=[0,1], one_to_two=[1,2],
            two_to_three=[2,3], three_to_four=[3,4], four_to_five=[4,5])


@app.route('/scores/<scores>')
def scores_movies(scores):
    '''
    Function allowing to show a list of movies which have a  score's mean within a certain range.The range is set according to the button chosen by the user.

                Parameters :
                           scores(list): list of the lower and higher score accepted to be selected for each button.

                Returns :
                        Show the page no_scores_movies.html if the list is empty.
                        Show the page scores_movies.html with the list of selected movies within the wanted range if there is at least one movie in the list :
                        movies(list) : list containing all the films having a score within the wanted range.
                        covers(list) : list containing the covers of all the films within the wanted range.
                        ordered(list) : list of continuous int from 0 to the number of searched movies-1.
                        inf(float): value representing the lower score which is not included in the wanted values.
                        sup(float): value representing the highest score accepted which is included in the wanted values.
                        mean(list): list of the movies’ mean score which are the values used for classifying the movies in the different categories.
    '''

    movies_scores=[]
    covers=[]
    mean_scores=[]
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
            mean_score=round(mean_score,2)
            mean_scores.append(mean_score)
            order+=1
    ordered=range(order)

    if len(movies_scores) == 0 :
        return render_template('no_movies_score.html')
    else :
        return render_template('scores_movies.html', movies=movies_scores ,covers=covers,ordered=ordered,inf=inf,sup=sup,mean=mean_scores)



def search(request):
    '''
    Function allowing to search movies with informations corresponding to the searching word.
    This function permits us to search movies and get a list of indices of searched movies. It will be used for the function searched_page() which can show the searched movies in a page.
    Movies can be found by comparing the searching word with their informations. We can search movies according to the name, the type, the release year or the actors.

            Parameters:
                    request(an object of flask) : request can give us the string of the searching word

            Returns:
                    Use redirect function of flask to go to another function searched_page() in providing the parameter searched_ids.
    '''
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
