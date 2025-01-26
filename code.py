import streamlit as st
from playwright.sync_api import sync_playwright

# Configuración de la página de Streamlit
st.set_page_config(page_title="Automatización con Playwright", layout="centered")

# Función para interactuar con el navegador
def interact_with_browser():
    try:
        with sync_playwright() as p:
            # Usamos Chromium en modo headless
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            # Navegamos a la página
            page.goto('https://www.exito.com/tecnologia/computadores')

            # Hacemos clic en el botón "Ordenar por"
            page.wait_for_selector('[data-fs-dropdown-button="true"]')
            page.click('[data-fs-dropdown-button="true"]')

            # Hacemos clic en el botón "Más vendidos"
            page.wait_for_selector('//button[@data-fs-dropdown-item="true" and .//span[text()="Más vendidos"]]')
            page.click('//button[@data-fs-dropdown-item="true" and .//span[text()="Más vendidos"]]')

            st.success("¡Se hizo clic en 'Más vendidos' correctamente!")
            browser.close()

    except Exception as e:
        st.error(f"Se produjo un error: {e}")

# Interfaz de usuario en Streamlit
st.title("Automatización de Interacción con Playwright")

if st.button("Ejecutar"):
    st.info("Ejecutando el script con Playwright...")
    interact_with_browser()
