import streamlit as st
import pandas as pd

df = pd.read_csv('data/titanic_train.csv', delimiter = ',')

st.image('data/14047.webp')
st.title("Подсчет количества погибших детей")

df.drop_duplicates()
df = df.reset_index(drop=True)

age = st.number_input("Enter age:", min_value=0, max_value=18, value=10, step=1)

if st.button("Подсчитать"):
    children_died = df[(df['Age'] <= age) & (df['Survived'] == 0)]
    result = children_died.groupby('Embarked').size().reset_index(name='Count')

    st.write(result)

st.dataframe(df)
