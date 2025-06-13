import streamlit as st
import pandas as pd
from io import BytesIO
import base64

# CONFIGURACIÓN GENERAL
st.set_page_config(page_title="Buscador Maestro de Equipos", page_icon="🧭", layout="wide")

# FUNCIÓN PARA AGREGAR EL FONDO
def set_background(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: black;
    }}
    h1, h2, h3, h4, h5, h6, p, div {{
        color: black !important;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# APLICAMOS EL FONDO
set_background("fondo.jpg")

# LOGO SUPERIOR
st.image("logo.jpg", width=150)

# TÍTULO Y LEMA INSTITUCIONAL
st.markdown("<h1 style='text-align: center;'>🧭 Buscador Maestro de Equipos</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Al servicio de la excelencia operativa y la gestión responsable de activos</h3>", unsafe_allow_html=True)

# Cargar el archivo Excel
archivo_excel = 'Información de equipos.xlsx'
hoja1 = pd.read_excel(archivo_excel, sheet_name='HOJA_1')
hoja2 = pd.read_excel(archivo_excel, sheet_name='HOJA_2')

st.write("Introduce el nombre del equipo para obtener su información detallada de ambas hojas:")

# Entrada del usuario
equipo = st.text_input("🔎 Ingrese el nombre del equipo (Hostname o Leaf):")

if equipo:
    resultado_hoja1 = hoja1[hoja1['Hostname'].astype(str).str.contains(equipo, case=False, na=False)]
    resultado_hoja2 = hoja2[hoja2['Leaf'].astype(str).str.contains(equipo, case=False, na=False)]

    if resultado_hoja1.empty and resultado_hoja2.empty:
        st.error("⚠ No se encontraron datos en ninguna de las hojas.")
    else:
        if not resultado_hoja1.empty:
            st.subheader("📄 Datos Generales del Equipo (Hoja 1):")
            st.dataframe(resultado_hoja1)

        if not resultado_hoja2.empty:
            st.subheader("📊 Interfaces del Equipo (Hoja 2):")
            st.dataframe(resultado_hoja2)

        if not resultado_hoja1.empty and not resultado_hoja2.empty:
            st.subheader("🔗 Reporte combinado listo para descargar:")

            datos_generales = resultado_hoja1.iloc[0].to_dict()
            resultado_combinado = resultado_hoja2.copy()
            for campo in datos_generales:
                resultado_combinado[campo] = datos_generales[campo]

            st.dataframe(resultado_combinado)

            output = BytesIO()
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                resultado_combinado.to_excel(writer, index=False, sheet_name='Reporte Combinado')

            st.download_button(
                 label="📥 Descargar Reporte en Excel",
                 data=output.getvalue(),
                 file_name=f"Reporte_{equipo}.xlsx",
                 mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                type="primary"
)

