import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

ratings_df = pd.read_csv("ratings.csv")
movies_df = pd.read_csv("movies.csv")

def build_rating_matrix(df):
    movie_user_matrix = df.pivot_table(index='movieId', columns='userId', values='rating').fillna(0)
    sparse_matrix = csr_matrix(movie_user_matrix.values)
    return movie_user_matrix, sparse_matrix

movie_user_df, movie_user_sparse = build_rating_matrix(ratings_df)

def get_similar_movies(movie_id, movie_user_df, sparse_matrix, k=10, metric='cosine'):
    try:
        index = list(movie_user_df.index).index(movie_id)
    except ValueError:
        print(f"Movie ID {movie_id} not found in rating matrix.")
        return []

    model = NearestNeighbors(n_neighbors=k+1, metric=metric, algorithm='brute')
    model.fit(sparse_matrix)

    distances, indices = model.kneighbors([sparse_matrix[index].toarray().flatten()])
    similar_indices = indices.flatten()[1:]  # exclude the input movie itself

    similar_movie_ids = [movie_user_df.index[i] for i in similar_indices]
    return similar_movie_ids

def recommend_by_title(input_title, movies_df, ratings_df, movie_user_df, sparse_matrix, top_k=10):
    matches = movies_df[movies_df['title'].str.lower().str.contains(input_title.lower(), na=False)]

    if matches.empty:
        print(f"No movie found with title containing: '{input_title}'")
        return

    print("\nDid you mean:")
    for idx, row in matches.iterrows():
        print(f" - {row['title']} (ID: {row['movieId']})")

    selected_movie = matches.iloc[0]
    movie_id = selected_movie['movieId']
    movie_title = selected_movie['title']

    similar_ids = get_similar_movies(movie_id, movie_user_df, sparse_matrix, k=top_k)

    valid_ids = [mid for mid in similar_ids if mid in movies_df['movieId'].values]
    recommended_titles = movies_df[movies_df['movieId'].isin(valid_ids)]['title'].values

    print(f"\nSince you like '{movie_title}', you might also enjoy:")
    for title in recommended_titles:
        print(f" - {title}")

if __name__ == "__main__":
    user_input = input("Enter a movie you like: ")
    recommend_by_title(user_input, movies_df, ratings_df, movie_user_df, movie_user_sparse, top_k=10)
