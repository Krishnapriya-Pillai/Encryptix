# Encryptix
Recommendation system: Create a simple recommendation system that suggests items to sers based on their preferences. You can use techniques like collaborative filtering or content-based filtering to recommend movies, books, or products to users.

Based on the datset,it is a content based recommendation system that:
1. uses user ratings to find similar movies
2. finds th enearest neighbor using cosine similarity
3. recommends movies based on a movie title entered by user

ratings.csv - contains the ratings by the users
movies.csv - contains the metadata of the movies
Using the above, the data is converted into a matrix of movies (rows), users (columns) and ratings (values)

The system uses the NearestNeighbors with cosine similarity to find the top k+1 similar movies, finds the movies similar to the one with the movie_id based on the user rating vectors and returns a list of movieIds of similar movies

The recommended movie titles are found by searching for all movie titles that contain the user input, suggest all possible matches, picks the first match and finds the similar movies.


