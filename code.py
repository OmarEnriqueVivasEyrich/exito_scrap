import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuración de la página de Streamlit
st.set_page_config(page_title="Automatización con Selenium", layout="centered")

# Función para interactuar con el navegador y hacer clic en los botones
def interact_with_browser():
    # Configuración de Chrome en modo headless
    options = Options()
    options.add_argument('--headless')  # Modo sin interfaz gráfica
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    
    try:
        # Configura y descarga automáticamente el controlador ChromeDriver
        service = Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service, options=options)

        # Navega a la página
        browser.get('https://www.exito.com/tecnologia/computadores')

        # Hacemos clic en el botón "Ordenar por"
        time.sleep(5)
        boton_ordenar = browser.find_element(By.CSS_SELECTOR, '[data-fs-dropdown-button="true"]')
        boton_ordenar.click()

        # Hacemos clic en el botón "Más vendidos"
        time.sleep(2)
        boton_mas_vendidos = browser.find_element(By.XPATH, '//button[@data-fs-dropdown-item="true" and .//span[text()="Más vendidos"]]')
        boton_mas_vendidos.click()

        time.sleep(2)
        st.success("¡Se hizo clic en 'Más vendidos' correctamente!")
    
    except Exception as e:
        st.error(f"Se produjo un error: {e}")

    finally:
        # Cerramos el navegador
        browser.quit()

# Interfaz de usuario en Streamlit
st.title("Automatización de Interacción con Selenium")

if st.button("Ejecutar"):
    st.info("Ejecutando el script con Selenium...")
    interact_with_browser()
