import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

# Load the penguins dataset
penguins_df = sns.load_dataset('penguins')

# Set page title and layout
st.set_page_config(page_title='App pingüinesca', layout='wide')

# Define sidebar options
species_options = sorted(penguins_df.species.unique())
island_options = sorted(penguins_df.island.unique())

# Define sidebar widgets
st.sidebar.title('App Pingüistastica')
species = st.sidebar.selectbox('¿Qué especie?', species_options)
island = st.sidebar.selectbox('¿Qué isla?', island_options)

# Add a logo to the sidebar
logo = Image.open("logo.png")
st.sidebar.image(logo, width=100)
# Add a legend to the sidebar
st.sidebar.write("<div style='text-align: center; font-size: small;'>App creada por los fabulosos cientificos de datos de la AMEA.</div>", unsafe_allow_html=True)
st.sidebar.write("<br><div style='text-align: center; font-size: small;'>Desarrollado por</div><div style='text-align: center; font-size: small;'><a href='https://www.linkedin.com/in/ekaropolus/'>Edgar Valdés</a></div>", unsafe_allow_html=True)

# Filter the data based on user selection
filtered_df = penguins_df[(penguins_df.species == species) & (penguins_df.island == island)]

# Tell the story of penguins
st.write('## La historia de los pingüinos')
# Define two columns
col1, col2 = st.columns(2)

# Add text to the left column
col1.write('Los pingüinos son aves especiales que viven en las partes más frías del mundo, como la Antártida y las islas circundantes. Son famosos por sus plumas negras y blancas, su caminar balanceante y sus increíbles habilidades para nadar y bucear. Hay muchos tipos diferentes de pingüinos, que varían en tamaño desde el pequeño pingüino azul hasta el alto pingüino emperador, que puede crecer hasta cuatro pies de altura!')

# Add an image to the right column
col2.image('pinguinos.jpg', use_column_width=True)
st.write('Los pingüinos tienen que ser duros para sobrevivir en sus hogares helados. Tienen una capa gruesa de grasa llamada grasa para mantenerlos calientes, y sus cuerpos están diseñados para ayudarlos a nadar y bucear fácilmente. Les encanta comer krill y otros peces pequeños, y pasan mucho tiempo en el agua buscando comida.')

st.write('Los pingüinos son animales muy importantes porque nos ayudan a entender lo que está sucediendo en el océano. Los científicos utilizan a los pingüinos para estudiar la salud del océano y aprender cómo los cambios en el ambiente pueden afectar a los animales que viven allí. Al estudiar y proteger a los pingüinos, podemos ayudar a mantener los océanos saludables para todas las criaturas.')

st.write('La gente de todo el mundo ama a los pingüinos porque son animales lindos, divertidos y muy curiosos. Han aparecido en películas, libros y programas de televisión, y siempre nos hacen sonreír. Al aprender más sobre los pingüinos, podemos ayudar a proteger a estos increíbles animales y asegurarnos de que siempre estén aquí para que los disfrutemos!')
# Show instructions for children
st.write('## Instrucciones para niños')
st.write('1. Usa los menús desplegables del lado izquierdo de la página para elegir una especie e isla de pingüinos para aprender sobre ellos.')
st.write('2. Observa la tabla de datos para ver información sobre los pingüinos que seleccionaste.')
st.write('3. Mira el gráfico de dispersión para ver cómo se relacionan la masa corporal y la longitud de las aletas para los pingüinos que seleccionaste.')
st.write('4. ¡Diviértete aprendiendo sobre pingüinos!')

# Show the filtered data
st.write(f"## {species} pingüinos que viven en {island}")
st.write(filtered_df)

# Show a scatter plot of penguin body mass and flipper length
st.write('### Gráfico de dispersión de Masa Corporal y Longitud de Aleta')
st.write('Este gráfico de dispersión muestra cómo el peso corporal y la longitud de la aleta están relacionados para los pingüinos que seleccionaste. Cada punto en el gráfico representa un pingüino individual, y los puntos están coloreados según si son machos o hembras. La línea que atraviesa el gráfico muestra la relación general entre el peso corporal y la longitud de la aleta. Si un punto está por encima de la línea, significa que ese pingüino es más grande de lo que se esperaría por su longitud de aleta, y si está por debajo de la línea, significa que es más pequeño de lo que se esperaría. ¡Es divertido mirar los puntos y ver cómo se distribuyen en el gráfico!')
fig, ax = plt.subplots()
sns.scatterplot(x='body_mass_g', y='flipper_length_mm', hue='sex', data=filtered_df)
st.pyplot(fig)
