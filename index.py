import streamlit as st
#from main import start
import code as d
import os
import shutil

# streamlit assets 

url = st.text_input("YT Url: ")
down_path = d.file_path()
total, used, free = shutil.disk_usage(down_path)
st.write('Download path: {}'.format(down_path))
st.write("Total: %d GiB" % (total // (2**30)))
st.write("Used: %d GiB" % (used // (2**30)))
st.write("Free: %d GiB" % (free // (2**30)))

st.write("Files: ")
st.write(os.listdir(down_path))
# ------ CODE ------

if st.button("Download"):
    '''
    if 'DESKTOP_SESSION' not in os.environ: #and os.environ('HOSTNAME')=='streamlit':
        
        with open(title, 'rb') as f:
            bytes = f.read()
            b64 = base64.b64encode(bytes).decode()
            href = f'<a href="data:file/zip;base64,{b64}" download=\'{title}\'>\
                Here is your link \
            </a>'
            st.markdown(href, unsafe_allow_html=True)

        os.remove(title)
        st.error('Can not download online')
    else:'''
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
