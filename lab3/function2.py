# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#Exercise 1
def ab55(movie):
    return movie["imdb"] > 5.5

movie = {
    "name": "We Two", 
    "imdb": 7.2,
    "category": "Romance"
}
print(ab55(movie))  
#in ex 1 we take only one film to find out 


#Exercise 2
def abo5_5(movies):
    return [movie for movie in movies if ab55(movie)]

print(abo5_5(movies))

#Exercise 3
def mcategory(movies, category):
    return [movie for movie in movies if movie["category"] == category]
print(mcategory(movies, "Romance"))


#Exercise 4
def aveimbd(movies):
    if not movies:
        return 0
    total_score = sum(movie["imdb"] for movie in movies)
    return total_score / len(movies)
print(aveimbd(movies))


#Exercise 5
def avecategory(movies, category):
    category_movies = mcategory(movies, category)
    return aveimbd(category_movies)
print(avecategory(movies, "Thriller"))