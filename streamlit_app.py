import streamlit as st
import pandas as pd

df = pd.read_csv('data/titanic_train.csv', delimiter=',')

st.image('data/14047.webp')
st.title("Подсчет количества погибших детей по каждому пункту посадки")

df.drop_duplicates()
df = df.reset_index(drop=True)

age_input = st.number_input("Введите возраст (0-18):", min_value=0, max_value=18, value=10, step=1)

if st.button("Подсчитать") or st.session_state.get('age_entered', False):
    age = int(age_input)
    children_died = df[(df['Age'] <= age) & (df['Survived'] == 0)]
    result = children_died.groupby('Embarked').size().reset_index(name='Count')

    st.write(result)

# st.dataframe(df)

if st.session_state.get('age_entered', False):
    st.session_state['age_entered'] = False
else:
    st.session_state['age_entered'] = True
