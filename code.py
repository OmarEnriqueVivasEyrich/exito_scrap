import streamlit as st
from browserless import Browserless

# Configura la clave API de Browserless
browserless = Browserless(api_key="tu_clave_api_aqui")

# Función para interactuar con el navegador
def interact_with_browser():
    try:
        # Lanza el navegador con Browserless
        browser = browserless.launch(headless=True)
        page = browser.new_page()

        # Navegar a la página
        page.goto("https://www.exito.com/tecnologia/computadores")

        # Realizar acciones
        page.click('[data-fs-dropdown-button="true"]')
        page.click('//button[@data-fs-dropdown-item="true" and .//span[text()="Más vendidos"]]')

        st.success("¡Interacción con la página realizada correctamente!")
        browser.close()
    except Exception as e:
        st.error(f"Se produjo un error: {e}")

# Interfaz de usuario en Streamlit
st.title("Automatización de Interacción con Browserless")

if st.button("Ejecutar"):
    interact_with_browser()
