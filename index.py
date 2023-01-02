import streamlit as st
#from main import start
import code as d
import shutil
import os
import base64


def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'wb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href

def down_url(url):
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

# streamlit assets 
number = None
option = None
url = None
url = st.text_input("YT Url: ")
down_path = d.file_path()
try:
    total, used, free = shutil.disk_usage(down_path)
    files = os.listdir(down_path)
    st.write('Download path: {}'.format(down_path))
    st.write("Total: %d GiB" % (total // (2**30)))
    st.write("Used: %d GiB" % (used // (2**30)))
    st.write("Free: %d GiB" % (free // (2**30)))
    st.write("Files: ")
    #st.write(files)
    print(files)
except:
    st.write('Can\'t find download path')
    st.write('Download Something')

try:
    option = st.selectbox(
        'What would you like to download?',
        files)
    st.write('You selected:', option)
except:
    st.write("Files not present in directory")

# ------ CODE ------

if st.button("Download"):
    if option==None:
        st.error('select something')
        if url!=None:
            down_url(url)
        else:
            st.write('Enter valid url')
    else:
        p = down_path + '{}'.format('\\') + option
        st.write(p)
        st.markdown(get_binary_file_downloader_html(p, 'Video'), unsafe_allow_html=True)
        st.write('{} is downloaded'.format(option))
        
def dummy():
    if val == 'Invalid Link!!!':
        p = down_path + '{}'.format('\\') + files[number]
        st.write(p)
        st.markdown(get_binary_file_downloader_html(p, 'Video'), unsafe_allow_html=True)
        st.write('{} is downloaded'.format(files[number]))
