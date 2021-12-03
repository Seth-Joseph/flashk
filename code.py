from flask import Flask,jsonify,request
import csv

all_movies = []

with open('movies.csv',encoding='utf8')as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

liked_movies = []
disliked_movies = []
notwatched_movies = []

#creating constructor
app = Flask(__name__)

@app.route('/get-movie')
def getTheMovies():
    return jsonify({
        'data':all_movies[0],
        'status':'success'
    })
@app.route('/like-movie',methods = ['POST'])
def likedMovies():
    movie = all_movies[0]
    all_m = all_movies[1:]
    liked_movies.append(movie)

    return jsonify({
        'status':'success'
    }),201

@app.route('/dislike-movie',methods = ['POST'])
def disLikedMovies():
    movie = all_movies[0]
    all_m = all_movies[1:]
    disliked_movies.append(movie)
    return jsonify({
        'status':'success'
    }),201

@app.route('/notwatched-movie',methods = ['POST'])
def notWatchedMovies():
    movie = all_movies[0]
    all_m = all_movies[1:]
    notwatched_movies.append(movie)

    return jsonify({
        'status':'success'
    }),201

#running
if __name__ == '__main__':
    app.run()