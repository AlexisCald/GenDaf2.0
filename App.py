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
proveedores = ["A-1 CARMET", 
"ALAMBRES PROCESADOS INDUSTRIALES, S.A. DE C.V.", 
"ALL PINS LLC", 
"ARTURO CORDOVA PICHARDO", 
"BARBAROTTO INTERNATIONAL MACHINERY", 
"BIRLOS INTERNACIONALES, S.A. DE C.V.", 
"BRINELL, S.A.", 
"BULNES HERMANOS, S.A. DE C.V.", 
"CARLO SALVI USA INC", 
"CEVIZPRES", 
"CHASE PLASTICS SERVICES LLC", 
"CHI NING CO, LTD.", 
"CHIEN TSAI MACHINERY ENTERPRISE CO., LTD", 
"CHUN ZU MACHINERY IND. CO., LTD", 
"CIFRE, S.A. DE C.V.", 
"CINCO INDUSTRIES, INC.", 
"CLAVOS NACIONALES MEXICO, S.A. DE C.V.", 
"CMF MARELLI S.R.L.", 
"COLD HEADING TECHNOLOGIES S DE RL DE CV", 
"COLTEC INDUSTRIES INC./ HABER TOOL COMPANY INC.", 
"CONCRETE FASTENING", 
"CONTEMPORARY CARBIDE TECHNOLOGIES", 
"CREATIVE CARBIDE INC.", 
"DAFCO TOOL", 
"DAGAN INTERNATIONAL CO., LTD.", 
"DAHBIN ENTERPRISE CO., LTD", 
"DANIELSON TOOL & DIE CORP.", 
"DER SHIN TOOL INDUSTRY", 
"DF INTERNATIONAL LLC", 
"DIAMOND PRECISION PRODUCTS", 
"EASCO-SPARCATRON", 
"EDISON MACHINERY INDUSTRIAL CO., LTD", 
"EDK CO., LTD", 
"ESPAMEX METALICA INDUSTRIAL, S.A. DE C.V.", 
"EVER READY PIN & MANUFACTURING, INC.", 
"FARGIL DE MEXICO, S.A. DE C.V.", 
"FASTEN FOUR", 
"FH MACHINERY INC", 
"FLOCK TEX INCORPORATED", 
"FMC CORPORATION", 
"FORM G TECH", 
"FU CHIEF CO., LTD.", 
"FUTURE TOOL & GAGE, INC.", 
"GIOVANNI ANCESCHI, SRL", 
"GLUE MACHINERY CORPORATION", 
"GREENSLADE & COMPANY, INC.", 
"HABER TOOL COMPANY, INC.", 
"HARITON MACHINERY COMPANY, INC.", 
"HARITON MACHINERY MEXICO, S.A. DE C.V.", 
"HEADER CRAFT, INC.", 
"HEARTLAND TOOL SUPPLY", 
"HEROSLAM,  S.A.L.", 
"HERRAMIENTAS DIAZ, S.A.", 
"HOWELL PENNCRAFT, INC.", 
"INDUSTRY DEPOT", 
"IRETHAN ENTERPRISE CO.", 
"J.M. DIE COMPANY, INC.", 
"JACKSON EXPORT, INC.", 
"JAUME ALTIMIS MANZANARES", 
"JCC INCORPORATED", 
"JERHEN INDUSTRIES, INC.", 
"JP METAL GROUP", 
"KELLER CUTTING TOOL, CO.", 
"KENNAMETAL VICTORIA LTD", 
"KIM UNION INDUSTRIAL CO., LTD", 
"L & L EQUIPMENT, LLC", 
"LAMINADORA MEXICANA DE METALES, S.A. DE C.V.", 
"LANDSTAR IN WAY, INC", 
"LEHMAN FAST-TECH", 
"LONG MING (HONG KONG) INDUSTRIES CO.", 
"LOOMIS INTERNATIONAL", 
"MAJOR INTERNATIONAL, INC.", 
"MALCO SAW, CO.", 
"MARTINDALE ELECTRIC", 
"McMASTER-CARR SUPPLY Co.", 
"METALURGIA TRES B, S.A.", 
"MJR INTERNATIONAL, INC.", 
"MUNCHMEYER CALDERON SA DE CV", 
"NAKASIMADA USA; MACHINERY, PARTS AND SERVICE", 
"NATIONAL HEADER DIE", 
"NATIONAL MACHINERY LLC", 
"NORM TOOLING", 
"NORTH ATTLEBORO TAPS, INC.", 
"O.L.M. S.A.S. DI BIFFI E & C.", 
"PCBYTES, S.A. DE C.V.", 
"PCC SPECIALTY PRODUCTS, INC.", 
"PEINES TANGENCIALES, S.A. DE C.V.", 
"PITTSBURGH CARBIDE DIE COMPANY", 
"PLAN-E-TECH, INC.", 
"Proveedor por eliminar", 
"QUALITY REBUILDING CORPORATION", 
"R.I. CARBIDE TOOL", 
"REED MACHINERY INC.", 
"REG ELLEN MACHINE TOOL CORP.", 
"ROBERTO CUENCA HERNANDEZ", 
"ROCKFORM CARBIDE MANUFACTURING, INC.", 
"ROCKFORM TOOLING & MACHINERY", 
"RODIX INC", 
"ROL-FLO ENGINEERING, INC.", 
"RTM PRODUCTS, INC", 
"SALA PUNZONI", 
"SANSHING FASTECH CORP.", 
"SCORTA S.R.L.", 
"SEOUL TRADE COMPANY", 
"SINOGRAPHIC INTERNATIONAL LIMITED", 
"SPROUT TOOLING CO., LTD.", 
"STAR METAL PRODUCTS", 
"TEUDELOFF GMBH & CO., KG", 
"THURSTON MANUFACTURING COMPANY.", 
"TOMAS PARDO DOMINGUEZ", 
"TOOLING INTERNATIONAL LIMITED", 
"TORNILLOS Y TUERCAS ESTRELLA, S.A.", 
"U.S.A. CARBIDE TOOLING INC.", 
"UNIVERSAL PUNCH CORP.", 
"VALLEY HEADER DIE, INC.", 
"VEDIA INDUSTRIAL, S.A. DE C.V.", 
"VERMONT GAGE DISTRIBUTOR", 
"VISTA METALS INC.", 
"V-TIP MASTER TASK", 
"WALDEN GAGE DISTRIBUTION & CALIBRATION SERVICES INC", 
"WARREN INDUSTRIES", 
"WATERBURY HEADERS CORP.", 
"WORLD TECH, CO.", 
"WRENTHAM TOOL GROUP", 
"XALOY", 
"XINGZHOU CARBIDE CO., LTD", 
"YI TI MOLD ENTERPRISE CO., LTD", 
"ZHUZHOU UKO PRECISION CARBIDE CO., LTD"]

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
