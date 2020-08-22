from functions import *
import streamlit as st




dep_type = st.selectbox('Select Decription Method', ['None', 'Atbash', 'Caeser', 'A2Z'])
if dep_type == 'Atbash':
    txt = st.text_input('Choose the text you want to encrypt/decrypt (Both return the same answer in Atbash)')
    answer = Atbash(txt)
    if st.button('Submit'):
        st.success(answer)
    else:
        pass

if dep_type == 'Caeser':

    method = st.selectbox('Choose whether you want to encrypt or decrypt a message:', ['None', 'Encrypt', 'Decrypt'])
    if method == 'Encrypt':
        txt = st.text_input('Choose the text you want to encrypt')
    if method == 'Decrypt':
        txt = st.text_input('Choose the text you want to decrypt')
    if method == 'Encrypt' or method == 'Decrypt':
        answer = Caeser(txt, method)
        if st.button('Submit'):
            st.success(answer)


if dep_type == 'A2Z':
    method = st.selectbox('Choose whether you want to encrypt or decrypt a message:', ['None', 'Encrypt', 'Decrypt'])
    if method == 'Encrypt':
        txt = st.text_input('Choose the text you want to encrypt')
    elif method == 'Decrypt':
        txt = st.text_input('Choose the text you want to decrypt (Space Each Number for eg: 10 5 4, not 1054), Use ? in between two words, if you want to. ? should also be spaced out like 1 ? 2')
    if method == 'Encrypt' or method == 'Decrypt':
        answer = A2Z(txt, method)
        if st.button('Submit'):
            st.success(answer)
