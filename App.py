import streamlit as st
import random
import string
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from datetime import datetime

# --- Configurar la conexión con Google Sheets ---
SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
CREDENTIALS_FILE = "credenciales.json"  # Reemplaza con tu archivo JSON de credenciales
SPREADSHEET_NAME = "Claves Generadas"   # Reemplaza con el nombre de tu Google Sheets

# Autenticación con Google Sheets
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, SCOPE)
client = gspread.authorize(credentials)
sheet = client.open(SPREADSHEET_NAME).sheet1

# --- Función para generar clave única ---
def generar_clave():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

# --- Interfaz de usuario con Streamlit ---
st.title("Generador de Claves para Proveedores")

# Lista de proveedores
proveedores = [
    "A-1  CARMET", "ALAMBRES PROCESADOS INDUSTRIALES, S.A. DE C.V.", "ALL PINS LLC",
    "ARTURO CORDOVA PICHARDO", "BARBAROTTO INTERNATIONAL MACHINERY",
    "BIRLOS INTERNACIONALES, S.A. DE C.V.", "BRINELL, S.A.", "BULNES HERMANOS, S.A. DE C.V.",
    "CARLO SALVI USA INC", "CEVIZPRES", "CHASE PLASTICS SERVICES LLC",
    # (Agregar el resto de proveedores de la lista)
]

# Selección de proveedores (máximo 10)
seleccionados = st.multiselect("Selecciona hasta 10 proveedores:", proveedores, max_selections=10)

# Botón para generar la clave
if st.button("Generar Clave") and seleccionados:
    clave = generar_clave()
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Guardar en Google Sheets
    data = [fecha, clave] + seleccionados + [""] * (10 - len(seleccionados))  # Rellenar espacios vacíos
    sheet.append_row(data)

    # Mostrar la clave generada
    st.success(f"Clave generada: `{clave}`")
    st.code(clave, language="plaintext")

    # Botón para copiar
    st.button("Copiar Clave", on_click=lambda: st.write(f"Clave copiada: {clave}"))

else:
    st.warning("Selecciona al menos un proveedor.")
