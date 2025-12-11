import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


# ============================
# STEP 1 — LOAD MOVIES
# ============================
@st.cache_data(show_spinner=False)
def load_movies(path="data/movies.csv"):
    movies = pd.read_csv(path)

    # Keep only necessary columns
    movies = movies[['movieId', 'title', 'genres']].dropna(subset=['title']).reset_index(drop=True)

    # Replace missing genres
    movies['genres'] = movies['genres'].fillna("")

    return movies


# ============================
# STEP 2 — TF-IDF CONTENT VECTOR
# ============================
@st.cache_resource(show_spinner=False)
def build_tfidf_matrix(movies):
    # Combine title + genres
    movies['content'] = movies['title'] + " " + movies['genres']

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(movies['content'])

    return vectorizer, tfidf_matrix


# ============================
# STEP 3 — DYNAMIC RECOMMENDER
# (uses your code)
# ============================
def get_recommendations_dynamic(title, movies, tfidf_matrix, top_n=10):
    indices = pd.Series(movies.index, index=movies['title'].str.lower())
    title_lower = title.strip().lower()

    # Exact match
    if title_lower not in indices:
        # Try partial match
        matches = movies[movies['title'].str.lower().str.contains(title_lower)]
        if matches.empty:
            return pd.DataFrame()
        idx = matches.index[0]
    else:
        idx = indices[title_lower]

    # Compute similarity ONLY for this movie
    cosine_similarities = linear_kernel(tfidf_matrix[idx:idx+1], tfidf_matrix).flatten()

    # Sort similarity scores
    sim_scores = list(enumerate(cosine_similarities))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1 : top_n + 1]  # Skip itself

    movie_indices = [i for i, _ in sim_scores]
    results = movies.iloc[movie_indices].copy()
    results["score"] = [score for _, score in sim_scores]

    return results[['title', 'genres', 'score']]


# ============================
# STEP 4 — STREAMLIT APP UI
# ============================
def main():
    st.set_page_config(page_title="Movie Recommender", layout="wide")

    st.title("🎬 Movie Recommender System")
    st.write("This app recommends movies based on **TF-IDF + Cosine Similarity** using MovieLens dataset.")

    # Load movies
    movies = load_movies()

    # Build TF-IDF
    vectorizer, tfidf_matrix = build_tfidf_matrix(movies)

    # Sidebar options
    st.sidebar.header("Find Similar Movies")
    movie_name = st.sidebar.text_input("Enter movie name")
    top_n = st.sidebar.slider("Number of recommendations", 5, 20, 10)

    if st.sidebar.button("Recommend"):
        if movie_name.strip() == "":
            st.warning("Please enter a movie name.")
        else:
            results = get_recommendations_dynamic(movie_name, movies, tfidf_matrix, top_n)

            if results.empty:
                st.error("Movie not found. Try a different title.")
            else:
                st.success(f"Top {top_n} recommendations for: **{movie_name}**")

                # Display results
                for idx, row in results.iterrows():
                    st.write(f"### 🎥 {row['title']}")
                    st.write(f"Genres: {row['genres']}")
                    st.write(f"Similarity Score: `{row['score']:.4f}`")
                    st.markdown("---")


if __name__ == "__main__":
    main()
