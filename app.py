#!/usr/bin/env python
# coding: utf-8

# In[2]:


#get_ipython().system('pip install -q streamlit')


# In[3]:


import streamlit as st
import pickle


# In[4]:


st.write("""
# Division App
This app divides the number 'a' by number 'b' and gives output
""")


# In[5]:


#Get Input

st.header('User Input Parameters')


# In[6]:


def user_input_features():
    input_number1 = st.number_input("Input_number1",min_value=0,max_value=1000)
    input_number2 = st.number_input("Input_number2",min_value=0,max_value=1000)
    return (input_number1,input_number2)

num1,num2 = user_input_features()


# In[7]:


st.subheader('User Input numbers')
st.write(num1)
st.write(num2)


# In[8]:


st.subheader('The Division is:')
st.write(num1/num2)