🎬 Movie Recommendation System

A Streamlit Web App using TF-IDF + Cosine Similarity

This project is a movie recommendation system that suggests similar movies based on title and genres. It uses the MovieLens dataset, TF-IDF vectorization, and cosine similarity to generate recommendations.

The web app is built with Streamlit, making it interactive and easy to use.

🚀 Features

Search for movies using partial or full titles

Get top-N similar movie recommendations

Memory-safe implementation

Uses TF-IDF for text vectorization

Streamlit web app with sidebar controls

📁 Project Structure
movie-recommender-project/
│
├── app_streamlit.py          # Main Streamlit application
├── requirements.txt          # Dependencies
│
├── data/
│   └── .gitkeep              # Placeholder (data not stored in GitHub)
│
└── src/
    ├── recommender.py
    └── data_loader.py

📥 Dataset Download (Required)

This project uses the MovieLens Dataset, which cannot be uploaded to GitHub.

Download it here:
🔗 https://grouplens.org/datasets/movielens/

After downloading:

Copy movies.csv into the data/ folder:

movie-recommender-project/data/movies.csv


Note: Only movies.csv is required for this project.

🛠 Installation
1. Clone the repository
git clone https://github.com/YOUR-USERNAME/movie-recommender-project.git
cd movie-recommender-project

2. Install dependencies
pip install -r requirements.txt

▶️ Run the Web App
streamlit run app_streamlit.py


Your browser will open automatically at:

http://localhost:8501

🧠 How It Works
1. Content Creation

Each movie description is created by combining:

title + genres

2. TF-IDF Vectorization

Movies are converted into numerical vectors based on text importance.

3. Dynamic Cosine Similarity

Instead of computing similarity between all movies (which is huge), the app computes similarity only for the selected movie, making it memory-efficient.

✨ Possible Future Enhancements

Add movie posters (TMDb API)

Add fuzzy search (fix spelling errors)

Deploy to Streamlit Cloud

Add ratings-based collaborative filtering

👤 Author

Irine Vincent
Data Science Enthusiast
