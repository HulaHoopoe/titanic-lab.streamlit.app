import streamlit as st
import pandas as pd

df = pd.read_csv('data/titanic_train.csv', delimiter = ',')

st.image('data/14047.webp')
st.title("Подсчет количества погибших детей")
st.dataframe(df)

# import csv
# import json


# with open('/titanic_train.csv') as f:
#   reader = csv.reader(f)

#   headers = next(reader)
#   embarks = {}

#   for row in reader:
#     id = row[0]
#     survived = row[1]
#     age = row[5]
#     embarked = row[11]
#     if not age or not embarked:
#       continue

#     if int(float(age)) > 18 or int(float(age)) == 0 or survived == '1':
#       continue

#     # print(f'{id} | {age} | {embarked}')

#     # if embarked not in embarks:
#     #   embarks[embarked] = [age]
#     # else:
#     #   embarks[embarked] += [age]

#     if embarked not in embarks:
#       embarks.update({embarked: 1})
#     else:
#       embarks.update({embarked: embarks[embarked] + 1})

# result = {
#     "embarked": []
# }

# for key in embarks:
#   res = {"name" : key, "survived_children": embarks[key]}
#   result["embarked"].append(res)

# with open('data.json', 'w') as file:
#   json.dump(result, file, indent=4)

# json.dumps(result)
