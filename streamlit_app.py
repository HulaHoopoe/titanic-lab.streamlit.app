import streamlit as st
import pandas as pd

df = pd.read_csv('data/titanic_train.csv', delimiter=',')

st.image('data/14047.webp')
st.title("Подсчет количества погибших детей по каждому пункту посадки")

df.drop_duplicates()
df = df.reset_index(drop=True)

age_input = st.number_input("Введите возраст (0-18):", min_value=0, max_value=18, value=10, step=1)

def get_died_children_count(dataFrame, age):    
        age = int(age)
        children_died = dataFrame[(dataFrame['Age'] <= age) & (dataFrame['Survived'] == 0)]
        return children_died.groupby('Embarked').size().reset_index(name='Count').sort('Embarked')

if st.button("Подсчитать"):
    result = get_died_children_count(df, age_input)

    st.write(result)

    print(result)

