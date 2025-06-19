# Epalexia
📘 Experiencia Dislexia.

Este proyecto ofrece una simulación interactiva diseñada para mostrar cómo perciben el mundo las personas con dislexia, fomentando la empatía a través de la tecnología.

Para conocer en detalle el funcionamiento del proyecto, consulta el archivo Guía Básica para Comprender y Modificar el Código, donde se explican todos los componentes y se describe cómo se enlazan los distintos archivos y módulos del sistema. Además, se muestra como puedes modificar el contenido para personalizarlo.


📦 Navegador portátil incluido
Este proyecto utiliza una versión portable de Chromium (ungoogled-chromium) incluida directamente en la estructura de carpetas. Esto permite ejecutar el navegador sin necesidad de instalación previa en el sistema del usuario y garantiza la compatibilidad con el ejecutable generado mediante PyInstaller.

¿Por qué un navegador portable?
Evita depender del navegador instalado en el ordenador.

Asegura compatibilidad total con Selenium y ChromeDriver.

Permite que el proyecto sea completamente autónomo y portable (por ejemplo, desde un pendrive).

📁 Estructura relevante:
Copiar
Editar
proyecto/
├── AF_EJECUTABLE.exe
├── chromedriver.exe
└── ungoogled-chromium-portable/
    └── chrome.exe
⚠️ Nota
La versión de chrome.exe incluida debe coincidir exactamente con la versión de chromedriver.exe usada. En este caso:
Chromium 137.0.7151.120 + ChromeDriver 137.0.7151.120.
