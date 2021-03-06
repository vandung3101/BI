from sklearn.preprocessing import KBinsDiscretizer
from sklearn.preprocessing import OrdinalEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import export_graphviz
import streamlit as st
import pandas as pd
import numpy as np

st.image('image.jpg', use_column_width=True)
st.title('ML Web App')
with st.beta_expander('README'):
    st.markdown('''
    #### Dataset (.csv):
    - Algorithm work best with dataset contains **binary features** (others run well but the prediction will bad) 
    - Record with ***NaN*** values would be removed by the algorithm
    - Dataset should following structure (see demo dataset /data.csv):
    - feature_0      feature_1     ....     feature_n             Target
    - ----------       -----------     ....     -----------      -------
    - ----------       -----------     ....     -----------      -------
    - ----------       -----------     ....     -----------      -------
    #### All datatype will be converted to numeric for sklearn library, click Show head data below
    ''')
st.sidebar.header('Panel')
st.sidebar.write('(Please read the README first)')
dataset = st.sidebar.file_uploader(
    label="Upload your .csv file", type=['csv'])
if dataset is not None:
    df = pd.read_csv(dataset)
    with st.beta_expander('Show head of raw data'):
        st.write(df.head())
algorithm = st.sidebar.selectbox('Please select algorithm', [
                                 'Classifier', 'Regressor'])
max_depth = st.sidebar.slider(
    'Max depth of the tree', min_value=1, max_value=10, value=3)
button = st.sidebar.button('Gender')


def buldTree(algorithm, data):
    encoder = OrdinalEncoder()
    data = encoder.fit_transform(data)
    if algorithm == 'Classifier':
        discrete = KBinsDiscretizer(encode='ordinal', strategy='kmeans')
        data[:, -
             1] = discrete.fit_transform(data[:, -1].reshape(-1, 1)).ravel()
        with st.beta_expander('Show head of data processed'):
            data[1:50]
        feature = data[:, :-1]
        target = data[:, -1]
        model = DecisionTreeClassifier(criterion='entropy')
        model.fit(feature, target)
    else:
        with st.beta_expander('Show head of data processed'):
            data[1:50]
        feature = data[:, :-1]
        target = data[:, -1]
        model = DecisionTreeRegressor(criterion='friedman_mse')
        model.fit(feature, target)
    return model


if button and df is not None:
    feature_names = ['feature_' + str(i) for i in range(df.shape[1] - 1)]
    df.columns = feature_names + ['target']
    data = df.dropna(axis=0)

    tree = buldTree(algorithm, data)

    st.header('Visualize the tree')
    st.write('Sometime you have to scroll down to see the tree')
    visual_tree = export_graphviz(
        tree, max_depth=max_depth, feature_names=feature_names, filled=True)
    st.graphviz_chart(visual_tree)
