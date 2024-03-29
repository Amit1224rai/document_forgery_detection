import streamlit as st

def main():
    st.title('File Upload Tutorial')

    menu=['Home','Dataset','DocumentFiles','About']
    choice=st.sidebar.selectbox('Menu',menu)

    if choice=='Home':
        st.subheader('home')
        image_file=st.file_uploader("Upload Images",type=["png","jpg","jpeg"])
        if image_file is not None:
            #st.write(type(image_file))
            #st.write(dir(image_file))
            file_details={'filename':image_file.name,'filetype':image_file.type,'filesize':image_file.size}
            st.write(file_details)
    elif choice=='Dataset':
        st.subheader('Dataset')
        image_file=st.file_uploader("Upload Images",type=["png","jpg","jpeg"])
    elif choice=='DocumentFiles':
        st.subheader('DocumentFiles')
        image_file=st.file_uploader("Upload Images",type=["png","Text","pdf"])
    else:
        st.subheader('About')
        image_file=st.file_uploader("Upload Images",type=["png","Doc","pdf"])

if __name__ == '__main__':
    main()

