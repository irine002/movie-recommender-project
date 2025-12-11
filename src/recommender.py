import pandas as pd

# Load dataset
movies = pd.read_csv(r"C:\Users\irine\Downloads\archive (3)\movies.csv")

# Clean and preprocess
movies['genres'] = movies['genres'].fillna("")

# Convert genres into sets for easy comparison
movies['genres_set'] = movies['genres'].apply(lambda g: set(g.split("|")))

print(movies.head())

# --- Function to get movie genres ---
def get_movie_genres(movie_name):
    result = movies[movies['title'].str.lower() == movie_name.lower()]
    if result.empty:
        return None
    return result.iloc[0]['genres_set']

# --- Function to recommend movies ---
def recommend_movies(movie_name, top_n=10):
    movie_genres = get_movie_genres(movie_name)

    if movie_genres is None:
        print("Movie not found!")
        return []

    # Compute similarity based on genre overlap
    movies['similarity'] = movies['genres_set'].apply(
        lambda g: len(movie_genres.intersection(g))
    )

    # Sort by similarity
    recommendations = movies.sort_values(by="similarity", ascending=False)

    # Remove the same movie
    recommendations = recommendations[recommendations['title'].str.lower() != movie_name.lower()]


    # Return top results
    return recommendations[['title', 'genres', 'similarity']].head(top_n)


# -------- MAIN PROGRAM --------
user_movie = input("Enter a movie name: ")

genres = get_movie_genres(user_movie)

if genres is None:
    print("Movie not found in dataset.")
else:
    print("\nGenres of movie:", " | ".join(genres))

    print("\nTop recommended movies:")
    recs = recommend_movies(user_movie, top_n=10)
    print(recs)

