import streamlit as st
import pandas as pd
import joblib

st.set_page_config(layout="wide")

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

movies_ds = pd.read_pickle("Saved Pickle File/pickle_movie")
similer_matrix = joblib.load("Saved Pickle File/similer_matrix.pkl")

def get_poster(movie_poster):
    return movies_ds[movies_ds["id"]==movie_poster]["poster"].values[0]

def recommend(movie):
    index = movies_ds[movies_ds['title'] == movie].index[0]
    distances = sorted(list(enumerate(similer_matrix[index])),reverse=True,key = lambda x: x[1])

    recommend_movie_name = []
    recommend_movie_poster = []

    for i in distances[1:6]:
        movie_id = movies_ds.iloc[i[0]]["id"]
        movie_name = movies_ds.iloc[i[0]]["title"]
        
        recommend_movie_name.append(movie_name)
        recommend_movie_poster.append(get_poster(movie_id))
    return recommend_movie_name, recommend_movie_poster


st.title("Movie Recommendation")
selected_movie = st.selectbox("Search the Movie", movies_ds["title"].values)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    num_columns = 5
    cols = st.columns(num_columns)
    
    for i in range(min(num_columns, len(recommended_movie_names))):
        with cols[i]:
            st.text(recommended_movie_names[i])
            st.image(recommended_movie_posters[i])



