import os
from dotenv import load_dotenv
load_dotenv() ## aloading all the environment variable
groq_api_key=os.getenv("GROQ_API_KEY")


import streamlit as st
st.title("ChatBot Model With Groq")
input_text=st.text_input("What question you have in mind?")




from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

model=ChatGroq(model="Mixtral-8x7b-32768",groq_api_key=groq_api_key)
model.invoke([HumanMessage(content=input_text)])
response=model.invoke([HumanMessage(content=input_text)])


#if input_text:
#    st.write(response.content)

if input_text:
    st.text_area(label='Here is my response' ,value=response.content)



