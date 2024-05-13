import streamlit as st

y="ans"
# this returns a variable that can be stored

x=st.text_input('why?')
# this outputs the variable
st.write(x,y)
# /button
is_clicked=st.button("hey click me")
# italic using markdown head over to
if(is_clicked):
    st.write("##hey i am new")
# /button

st.title("A bird Classifier")
col1,col2=st.columns(2)
h=col1.number_input("hi",min_value=10,max_value=2000)
y=col1.number_input("bye",min_value=10,max_value=2000)
x=col2.number_input("hy",min_value=10,max_value=2000)
c=col2.number_input("ko",min_value=10,max_value=2000)
st.write("hey bro")
col1,col2,col3=st.columns(3)
col1.metric(label="hoal",value=x)
col2.metric(label="goal",value=y)
col3.metric(label="lol",value=h)