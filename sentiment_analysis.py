import pickle
import streamlit as st

with open("model_pickle2","rb") as f:
    mp=pickle.load(f)
def u_in():
  text = st.text_input("Enter your review: ")
  a = []
  a.append(text)
  return a

st.title("ML Project")
st.subheader("This is sentiment analysis model made by Shreyas Mandaokar")
df = u_in()
pred = mp.predict(df) 
if pred == 0:
  st.write("Negative Sentiment")
else:
  st.write("Positive Sentiment")
