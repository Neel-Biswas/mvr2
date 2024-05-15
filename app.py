import streamlit as st
import pickle
import pandas as pd
import requests

page_bg_img = """
 <style>
# [data-testid="stAppViewContainer"]{
# background-image: url("https://cdn.pixabay.com/photo/2020/04/20/18/10/cinema-5069314_1280.jpg");
# background-size: cover;
# }
  #myVideo {
		  position: fixed;
		  right: 0;
		  bottom: 0;
		  min-width: 100%; 
		  min-height: 100%;
		  background-size: cover;
		}

		.content {
		  position: fixed;
		  bottom: 0;
		  background: rgba(0, 0, 0, 0.5);
		  color: #f1f1f1;
		  width: 100%;
		  padding: 20px;
		}

</style>
<video autoplay muted loop id="myVideo">
<source src="https://videos.pexels.com/video-files/3141208/3141208-uhd_3840_2160_25fps.mp4")>
Your browser does not support HTML5 video.
</video>
"""

st.markdown(page_bg_img,unsafe_allow_html=True)
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=44b6bb9cfca6bbbe40f3d84f5caa77c4'.format(movie_id))
    data = response.json()
    print(data)
    return  "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:10]

    recommended_movies = []
    recommended_movies_posters = []
    recommended_movies_overview = []
    # fetch poster from api
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_overview.append(movies.iloc[i[0]].tags)

        #fetch poster from api
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters,recommended_movies_overview

movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
st.title('Movie recommender System')
selected_movie = st.selectbox("Enter the Title of the Movie",movies['title'].values)
if st.button("Recommend"):
    names,posters,overview = recommend(selected_movie)
    # col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)
    col1, col2, col3 = st.columns(3)
    col1.image(posters[0])
    col1.text(names[0])
    col1.caption(overview[0])

    col2.image(posters[1])
    col2.text(names[1])
    col2.caption(overview[1])

    col3.image(posters[2])
    col3.text(names[2])
    col3.caption(overview[2])

    # Second row
    col4, col5, col6 = st.columns(3)
    col4.image(posters[3])
    col4.text(names[3])
    col4.caption(overview[3])

    col5.image(posters[4])
    col5.text(names[4])
    col5.caption(overview[4])

    col6.image(posters[5])
    col6.text(names[5])
    col6.caption(overview[5])

    # Third row
    col7, col8, col9 = st.columns(3)
    col7.image(posters[6])
    col7.text(names[6])
    col7.caption(overview[6])

    col8.image(posters[7])
    col8.text(names[7])
    col8.caption(overview[7])

    col9.image(posters[8])
    col9.text(names[8])
    col9.caption(overview[8])

    # for i in recommendations:
    #     st.write(i)
