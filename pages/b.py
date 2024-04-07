import streamlit as st

st.write('Hello world!')
st.header('B')

if st.button('Click me'):
    st.write('You clicked the button!')
else:
    st.write('You did not click the button.')