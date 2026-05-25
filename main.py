from fastapi import FastAPI
from database import movies, reviews

app = FastAPI()


# HOME API
@app.get("/")
def home():

    return {
        "message": "Movie Review Database API Running"
    }


# ADD MOVIE
@app.post("/add-movie")
def add_movie(movie: dict):

    movies.insert_one(movie)

    return {
        "message": "Movie Added Successfully"
    }


# GET ALL MOVIES
@app.get("/movies")
def get_movies():

    data = list(
        movies.find({}, {"_id": 0})
    )

    return data


# ADD REVIEW
@app.post("/add-review")
def add_review(review: dict):

    reviews.insert_one(review)

    return {
        "message": "Review Added Successfully"
    }


# GET REVIEWS
@app.get("/reviews")
def get_reviews():

    data = list(
        reviews.find({}, {"_id": 0})
    )

    return data


# SEARCH MOVIE BY GENRE
@app.get("/search/{genre}")
def search_movie(genre: str):

    data = list(
        movies.find(
            {"genre": genre},
            {"_id": 0}
        )
    )

    return data


# UPDATE MOVIE
@app.put("/update-movie/{title}")
def update_movie(title: str):

    movies.update_one(
        {"title": title},
        {
            "$set": {
                "language": "Tamil"
            }
        }
    )

    return {
        "message": "Movie Updated Successfully"
    }


# DELETE MOVIE
@app.delete("/delete-movie/{title}")
def delete_movie(title: str):

    movies.delete_one({
        "title": title
    })

    return {
        "message": "Movie Deleted Successfully"
    }