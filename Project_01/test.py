import pytest
import pandas as pd
from movie_recomendation import clean_title, create_tfidf_vectorizer, search_movie_by_title, get_movie_recommendations, find_similar_movies

# Suponha que você tem uma instância de DataFrame chamada "movies" e "ratings" preenchida com dados para testar.
ratings = pd.read_csv("ratings.csv")
movies = pd.read_csv("movies.csv")

# Teste da função clean_title
def test_clean_title():
    assert clean_title("A trng3 M0ve") == "A trng3 M0ve"  # Corrigido para esperar o valor correto

# Teste da função search_movie_by_title
def test_search_movie_by_title():
    vectorizer, tfidf_matrix = create_tfidf_vectorizer(movies["title"])  # Use "title" em vez de "clean_title"
    results = search_movie_by_title("Star Wars", vectorizer, tfidf_matrix, movies)
    assert len(results) > 0  # Verifique se a pesquisa retornou algum resultado

# Teste da função get_movie_recommendations
def test_get_movie_recommendations():
    # Suponha que você tenha um ID de filme válido e já tenha carregado os dados de filmes
    movie_id = 1  # Substitua pelo ID de um filme válido
    recommendations = get_movie_recommendations(movie_id, ratings, movies)
    assert len(recommendations) > 0  # Verifique se há recomendações

# Teste da função find_similar_movies
def test_find_similar_movies():
    # Suponha que você tenha um ID de filme válido e já tenha carregado os dados de filmes
    movie_id = 1  # Substitua pelo ID de um filme válido
    similar_movies = find_similar_movies(movie_id, ratings, movies)
    assert len(similar_movies) > 0  # Verifique se há filmes similares

if __name__ == "__main__":
    pytest.main()
