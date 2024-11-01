import pandas as pd
import pytest as pt
# from streamlit_app import get_died_children_count

def get_died_children_count(dataFrame, age):    
        age = int(age)
        children_died = dataFrame[(dataFrame['Age'] <= age) & (dataFrame['Survived'] == 0)]
        return children_died.groupby('Embarked').size().reset_index(name='Count')

def test1():
    test = {'Age': [15, 10, 10], 'Survived': [0, 1, 0], 'Embarked': ['C', 'Q', 'S']}
    expected = {'Embarked': ['C', 'S'], 'Count': [1, 1]}

    test_df = pd.DataFrame(test)
    expected_df = pd.DataFrame(expected)
    assert str(get_died_children_count(test_df, 18)) == str(expected_df)

def test2():
    test = {'Age': [20, 10, 10], 'Survived': [0, 1, 0], 'Embarked': ['C', 'Q', 'S']}
    expected = {'Embarked': ['S'], 'Count': [1]}

    test_df = pd.DataFrame(test)
    expected_df = pd.DataFrame(expected)
    assert str(get_died_children_count(test_df, 15)) == str(expected_df)

def test3():
    test = {'Age': [20, 20, 40], 'Survived': [0, 1, 0], 'Embarked': ['C', 'Q', 'S']}
    expected = {'Embarked': [], 'Count': []}

    test_df = pd.DataFrame(test)
    expected_df = pd.DataFrame(expected)
    assert str(get_died_children_count(test_df, 18)) == str(expected_df)
