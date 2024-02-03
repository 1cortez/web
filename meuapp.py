import streamlit as st 

st.set_page_config(page_title="Meu primeiro site com streamlit")

st.subheader("Minhas Redes Sociais:")
st.write("Me Siga no GitHub, [clique aqui](https://github.com/1cortez)")
st.write("Me Siga no YouTube, [clique aqui](https://www.youtube.com/@leeafs6_)")
from streamlit_player import st_player

# Embed a youtube video
st_player("https://www.youtube.com/watch?v=KML9ScIznags")

st.toast('Your edited image was saved!', icon='😍')

