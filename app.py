import streamlit as st
import pandas as pd

data= {
"id":range(1,11),
"name" : [f"Item_{i}" for i in range(1,11)],
"value" : [i*10 for i in range(1,11)]
}

df=pd.DataFrame(data)

st.title("Hello World !")
st.subheader("Jai Sadgurudeva")
st.dataframe(df)
