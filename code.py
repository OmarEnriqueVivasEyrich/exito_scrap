import streamlit as st
import requests
from bs4 import BeautifulSoup

# Función para hacer scraping de la página
def scrape_website():
    url = 'https://www.exito.com/tecnologia/computadores'
    
    try:
        # Realizamos una solicitud GET a la página
        response = requests.get(url)
        response.raise_for_status()  # Verifica si la solicitud fue exitosa

        # Creamos el objeto BeautifulSoup para analizar el HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encontramos el título de la página como ejemplo de extracción
        title = soup.title.text

        # Mostramos el título en Streamlit
        st.write(f"El título de la página es: {title}")

        # Ejemplo de extracción de información: Botón "Ordenar por"
        ordenar_button = soup.find('button', {'data-fs-dropdown-button': 'true'})
        if ordenar_button:
            st.write("Se encontró el botón 'Ordenar por'.")
        else:
            st.write("No se encontró el botón 'Ordenar por'.")

    except requests.exceptions.RequestException as e:
        st.error(f"Se ha producido un error: {e}")

# Interfaz en Streamlit
st.title("Web Scraping con BeautifulSoup")

# Botón para ejecutar el scraping
if st.button("Ejecutar Web Scraping"):
    scrape_website()
