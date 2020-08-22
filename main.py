from functions import *
import streamlit as st




dep_type = st.selectbox('Select Decription Method', ['None', 'Atbash', 'Caeser Cipher', 'A2Z', 'Atbash + A2Z', 'Atbash + Caeser Cipher'])
if dep_type == 'Atbash':
    txt = st.text_input('Choose the text you want to encrypt/decrypt (Both return the same answer in Atbash)')
    answer = Atbash(txt)
    if st.button('Submit'):
        st.success(answer)
    else:
        pass

if dep_type == 'Caeser Cipher':

    method = st.selectbox('Choose whether you want to encrypt or decrypt a message:', ['None', 'Encrypt', 'Decrypt'])
    if method == 'Encrypt':
        txt = st.text_input('Choose the text you want to encrypt')
    if method == 'Decrypt':
        txt = st.text_input('Choose the text you want to decrypt')
    if method == 'Encrypt' or method == 'Decrypt':
        answer = Caeser(txt, method)
        if st.button('Submit'):
            st.success(answer)


if dep_type == 'Atbash + Caeser Cipher':
    method = st.selectbox('Choose whether you want to encrypt or decrypt a message:', ['None', 'Encrypt', 'Decrypt'])
    if method == 'Encrypt':
        txt = st.text_input('Choose the text you want to encrypt')
        returnvalue = Atbash(txt)
        answer = Caeser(returnvalue, method)
        if st.button('Submit'):
            st.success(answer)
    elif method == 'Decrypt':
        txt = st.text_input('Choose the text you want to decrypt')
        returnvalue = Caeser(txt, method, True)
        answer = Atbash(returnvalue)
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

if dep_type == 'Atbash + A2Z':
    method = st.selectbox('Choose whether you want to encrypt or decrypt a message:', ['None', 'Encrypt', 'Decrypt'])
    if method == 'Encrypt':
        txt = st.text_input('Choose the text you want to encrypt')
        returnvalue = Atbash(txt)
        answer = A2Z(returnvalue, method)
        if st.button('Submit'):
            st.success(answer)
    elif method == 'Decrypt':
        txt = st.text_input('Choose the text you want to decrypt (Space Each Number for eg: 10 5 4, not 1054), Use ? in between two words, if you want to. ? should also be spaced out like 1 ? 2')
        returnvalue = A2Z(txt, method)
        answer = Atbash(returnvalue)
        if st.button('Submit'):
            st.success(answer)
