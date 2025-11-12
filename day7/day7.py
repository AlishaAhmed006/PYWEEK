import streamlit as st
st.title("This is the title")
st.header("the header")
st.subheader("the subheader")
st.text("My name is Alisha Ahmed")

st.write("i hope this works")
st.write("checking if this will still work")

st.markdown("hehehhehe")
st.code("blah blah blah but like code")
st.latex("E=mx+c")

name=st.text_input("Enter your name:")
age=st.number_input("enter age",0,100)
gender=st.radio("select gender",["male","female"])
hobbies=st.multiselect("select hobbies",["reading","gaming","travelling","coding","sports"])
rating=st.slider("rate the quiz:",0,5)
date=st.date_input("enter date:")
color=st.color_picker("pick a color:")

if st.button("submit"):
    st.write(f" name{name}\n age={age}\n hobbies={hobbies}\n favourite color={color}\n you rated this quiz={rating}")
    st.success("form submitted!")