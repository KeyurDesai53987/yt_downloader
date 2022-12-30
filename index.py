import streamlit as st
#from main import start
import code as d

# streamlit assets 

url = st.text_input("YT Url: ")
down_path = d.file_path()
st.write('Download path: ', down_path)
# ------ CODE ------

if st.button("Download"):
    val = d.check_link(url)
    #down_path = d.file_path()

    if val == 'plist':
        res = d.playlist_down(url)
    elif val == 'single':
        res = d.downloading(url)
    else:
        res = 'no'

    if res == 'no':
        st.error(res)
    else:
        st.success(res)