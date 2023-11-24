![demo](https://github.com/SayedShaun/Movie-Recommendation-System/assets/126845316/d50e38e6-827b-447e-a950-21977980608e)

Live Demo: https://recommendation-movie.streamlit.app
# Movie Recommendation System

A content-based movie recommendation system leveraging IMDb data. Discover movies tailored to your preferences based on their content and attributes.

## Overview

This project employs content-based filtering to deliver personalized movie recommendations. It relies on a dataset of 25,000 IMDb movies, analyzing movie content and attributes to suggest films that match your interests and tastes. Enhance your movie-watching experience with tailored suggestions.

## Key Files

- `25k IMDb movie Dataset.csv`: The IMDb dataset providing detailed movie information.
- `app.py`: The primary application script for generating content-based movie recommendations.
- `config.toml`: Configuration settings for the application.
- `movie-recommendation.ipynb`: Jupyter Notebook with code for the content-based recommendation system.
- `tmdb_poster_movie.csv`: Additional data with movie posters.
- `pickle_movie.pkl`: Pickled DataFrame containing movie data.
- `similarity_matrix.pkl`: Pickled file containing the similarity matrix used for content-based recommendations.

## Getting Started

- Clone this repository and install the necessary dependencies.
- Run the application to receive personalized movie suggestions.
- Select a movie, and the system will recommend related films based on content and attributes.

## Features

- Recommends movies based on the content and attributes of selected films.
- Utilizes content-based filtering and similarity calculations.
- Provides movie posters and titles for recommended movies.
