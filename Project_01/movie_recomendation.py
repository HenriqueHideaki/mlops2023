import pandas as pd
import regex as re
import numpy as np
import ipywidgets as widgets
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from IPython.display import display

# Função para carregar os dados
def load_data():
    movies = pd.read_csv("movies.csv")
    ratings = pd.read_csv("ratings.csv")
    return movies, ratings

# Função para limpar o título do filme
def clean_title(title):
    title = re.sub(r"[^\w\s]", "", title)
    return title

# Função para criar o vectorizer TF-IDF
def create_tfidf_vectorizer(titles):
    vectorizer = TfidfVectorizer(ngram_range=(1, 2))
    tfidf_matrix = vectorizer.fit_transform(titles)
    return vectorizer, tfidf_matrix

# Função para pesquisar filmes por título
def search_movie_by_title(title, vectorizer, tfidf_matrix, movies):
    title_cleaned = clean_title(title)
    query_vec = vectorizer.transform([title_cleaned])
    similarity_scores = cosine_similarity(query_vec, tfidf_matrix).flatten()
    top_indices = np.argsort(similarity_scores)[-5:][::-1]
    top_movies = movies.iloc[top_indices]
    return top_movies

# Função para obter recomendações de filmes
def get_movie_recommendations(movie_id, ratings, movies):
    similar_users = ratings[(ratings["movieId"] == movie_id) & (ratings["rating"] > 4)]["userId"].unique()
    similar_user_recs = ratings[(ratings["userId"].isin(similar_users)) & (ratings["rating"] > 4)]["movieId"]
    similar_user_recs = similar_user_recs.value_counts() / len(similar_users)
    similar_user_recs = similar_user_recs[similar_user_recs > .10]
    all_users = ratings[(ratings["movieId"].isin(similar_user_recs.index)) & (ratings["rating"] > 4)]
    all_user_recs = all_users["movieId"].value_counts() / len(all_users["userId"].unique())
    rec_percentages = pd.concat([similar_user_recs, all_user_recs], axis=1)
    rec_percentages.columns = ["similar", "all"]
    rec_percentages["score"] = rec_percentages["similar"] / rec_percentages["all"]
    rec_percentages = rec_percentages.sort_values("score", ascending=False)
    return rec_percentages.head(10).merge(movies, left_index=True, right_on="movieId")[["score", "title", "genres"]]

# Função para encontrar filmes similares
def find_similar_movies(movie_id, ratings, movies):
    similar_users = ratings[(ratings["movieId"] == movie_id) & (ratings["rating"] > 4)]["userId"].unique()
    similar_user_recs = ratings[(ratings["userId"].isin(similar_users)) & (ratings["rating"] > 4)]["movieId"]
    similar_user_recs = similar_user_recs.value_counts() / len(similar_users)
    similar_user_recs = similar_user_recs[similar_user_recs > .10]
    all_users = ratings[(ratings["movieId"].isin(similar_user_recs.index)) & (ratings["rating"] > 4)]
    all_user_recs = all_users["movieId"].value_counts() / len(all_users["userId"].unique())
    rec_percentages = pd.concat([similar_user_recs, all_user_recs], axis=1)
    rec_percentages.columns = ["similar", "all"]
    rec_percentages["score"] = rec_percentages["similar"] / rec_percentages["all"]
    rec_percentages = rec_percentages.sort_values("score", ascending=False)
    return rec_percentages.head(10).merge(movies, left_index=True, right_on="movieId")[["score", "title", "genres"]]

# Função para criar a interface interativa
def interactive_movie_search(movies, ratings):
    movie_input = widgets.Text(
        value='',
        description='Movie Title:',
        disabled=False
    )

    movie_list = widgets.Output()

    def on_type(data):
        with movie_list:
            movie_list.clear_output()
            title = data["new"]
            if len(title) > 5:
                vectorizer, tfidf_matrix = create_tfidf_vectorizer(movies["clean_title"])
                results = search_movie_by_title(title, vectorizer, tfidf_matrix, movies)
                if not results.empty:
                    movie_id = results.iloc[0]["movieId"]
                    display(find_similar_movies(movie_id, ratings, movies))

    movie_input.observe(on_type, names='value')

    display(movie_input, movie_list)

# Carregar os dados
movies, ratings = load_data()

# Chamada da função para exibir a interface
interactive_movie_search(movies, ratings)
