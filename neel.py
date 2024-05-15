import streamlit as st

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
st.title("Its summer")



