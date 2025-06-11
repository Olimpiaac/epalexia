import serial
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Configurar navegador
CHROMEDRIVER_PATH = "chromedriver.exe"
options = Options()
options.add_argument("--start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-infobars")
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

# URLs
URL_NORMAL = "file:///C:/Users/Olimpia/Desktop/Prototipo_master/HTML_INICIOEXPERIENCIA.html"

# Lista de páginas para simular dislexia
URLS_DISLEXIA = [
    "file:///C:/Users/Olimpia/Desktop/Prototipo_master/HTML_DESAFIO1.html",
    "file:///C:/Users/Olimpia/Desktop/Prototipo_master/HTML_DESAFIOO2.html",
    "file:///C:/Users/Olimpia/Desktop/Prototipo_master/HTML_DESAFIO3.html",
    "file:///C:/Users/Olimpia/Desktop/Prototipo_master/HTML_DESAFIO4.html",
    "file:///C:/Users/Olimpia/Desktop/Prototipo_master/HTML_DESAFIO5.html",
    "file:///C:/Users/Olimpia/Desktop/Prototipo_master/HTML_DESAFIO6.html",
]

# Cargar la página inicial
driver.get(URL_NORMAL)

# Conectar al Arduino
arduino = serial.Serial('COM3', 9600)
time.sleep(2)

estado_actual = None

while True:
    dato_crudo = arduino.readline()
    dato = dato_crudo.decode(errors="ignore").strip().upper()

    print(f"Raw: {dato_crudo} → Dato recibido: '{dato}'")

    if dato not in ["LDR_ON", "LDR_OFF"]:
        continue

    if dato != estado_actual:
        estado_actual = dato

        if dato == "LDR_OFF":
            url_random = random.choice(URLS_DISLEXIA)
            print(f"Cambiando a una experiencia disléxica aleatoria: {url_random}")
            driver.get(url_random)

        elif dato == "LDR_ON":
            print("Volviendo a la experiencia normal.")
            driver.get(URL_NORMAL)
