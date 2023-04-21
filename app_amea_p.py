import streamlit as st
from bokeh.plotting import figure, show
from bokeh.sampledata.penguins import data
from bokeh.transform import factor_cmap, factor_mark
import pandas as pd
from sklearn.manifold import TSNE
from sklearn import preprocessing
import matplotlib.pyplot as plt

#Magia de ML TODO: ver si esta bien
from sklearn.naive_bayes import GaussianNB
import seaborn as sns
import joblib
import random

SPECIES = sorted(data.species.unique())
MARKERS = ['hex', 'circle_x', 'triangle']

p = figure(title = "Tamaño del Pingüino", background_fill_color="#fafafa")
p.xaxis.axis_label = 'Tamaño de la aleta(mm)'
p.yaxis.axis_label = 'Masa del cuerpo(g)'

p.scatter("flipper_length_mm", "body_mass_g", source=data,
          legend_group="species", fill_alpha=0.4, size=12,
          marker=factor_mark('species', MARKERS, SPECIES),
          color=factor_cmap('species', 'Category10_3', SPECIES))

p.legend.location = "top_left"
p.legend.title = "Species"
dataset_url = "https://allisonhorst.github.io/palmerpenguins/"
st.title('Visualizaciones del dataset [palmerpenguins](%s)' % dataset_url)
bokeh_url = "https://docs.bokeh.org/en/latest/docs/examples/basic/data/transform_markers.html"
st.markdown('Ejemplo de [Bokeh](%s)' % bokeh_url)
st.bokeh_chart(p, use_container_width=True)


st.markdown("""---""")
tsne_url = 'https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html'
st.markdown("Reduccion de dimensiones con [TSNE](%s) y visualización" % tsne_url)




#Reduccion de dimensiones v1
df = pd.read_csv('penguins_size.csv')
features = ['species','culmen_length_mm','culmen_depth_mm','flipper_length_mm', 'body_mass_g']
species =list(set(df['species']))
df['species'].replace(species,range(len(species)),inplace=True)
data = df[features].dropna()
X_n = preprocessing.normalize(data.values)

r = data['species'] == 0
g = data['species'] == 1
b = data['species'] == 2

tsne = TSNE(
    n_components=2,
    init="random",
    random_state=30,
    perplexity=100,
    n_iter=300,
)
Y = tsne.fit_transform(X_n)

fig, ax = plt.subplots()

ax.scatter(Y[r,0],Y[r,1],c = 'r',label=species[0])
ax.scatter(Y[g,0],Y[g,1],c = 'g',label=species[1])
ax.scatter(Y[b,0],Y[b,1],c = 'b',label=species[2])
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)


st.pyplot(fig)

#Intento de generar el modelo mas simple de ML
df = pd.read_csv("penguins_size.csv") #TODO no deberia leerse dos veces...
df = df.dropna()

y = df["species"]
X = df.iloc[:,[2,3,4,5]]

clf = GaussianNB()
clf.fit(X, y)

import joblib

joblib.dump(clf, "clf.pkl")
sns.pairplot(df, hue="species", size=3,diag_kind="hist")

#inputs TODO: Input para llamar al clf.pkl que te traiga las caracteristicas del piinguino
# y que te diga que penguin es
st.number_input('Pick a number', 0,10)
st.text_input('Email address')
st.date_input('Travelling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')

#Load the model pickle
model_path = "clf.pkl"
# Unpickle classifier
clf = joblib.load(model_path)
# Get values through input bars
culmen_length_mm = random.uniform(5.5, 75.5)
culmen_depth_mm = random.uniform(5.5, 75.5)
flipper_length_mm = random.uniform(5.5, 75.5)
body_mass_g =random.uniform(2900, 4500)
# Put inputs to dataframe
X = pd.DataFrame([[culmen_length_mm, culmen_depth_mm,flipper_length_mm,body_mass_g]], columns = ["culmen_length_mm", "culmen_depth_mm","flipper_length_mm","body_mass_g"])
# Get prediction
prediction = clf.predict(X)[0]
penguins = [
    {
        "culmen lenght": culmen_length_mm,
        "culmen depth": culmen_depth_mm,
        "flipper lenght": flipper_length_mm,
        "body mass": body_mass_g,
        "What penguin am I?": prediction
        }
    ]

st.markdown(culmen_length_mm)
st.markdown(culmen_depth_mm)
st.markdown(flipper_length_mm)
st.markdown(body_mass_g)
st.markdown(prediction)