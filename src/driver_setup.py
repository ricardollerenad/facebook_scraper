## Este archivo se encarga de la configuración del driver de Selenium:

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # Utiliza el Service para manejar el driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver
