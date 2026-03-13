import streamlit as st

# 1. Configuración de la pestaña (Neutro y profesional)
st.set_page_config(
    page_title="Portal de reportes",
    page_icon="📈",
    layout="wide"
)

# 2. Título principal
st.title("📊 Portal de reportes")
st.markdown("### Automatización de Reportes")
st.write("---")

# 3. Distribución de la Portada
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("👋 ¡Bienvenido!")
    st.write("""
    Esta plataforma centraliza las herramientas de procesamiento de datos para la optimización de procesos operativos. 
    El objetivo es transformar archivos de registros brutos en información estratégica de manera inmediata.
    """)
    
    st.info("""
    **🛡️ Nota de Privacidad:**
    Este sistema procesa la información localmente en la sesión. Los datos cargados no se almacenan 
    en servidores externos, garantizando la confidencialidad de la información operativa.
    """)

with col2:
    # Espacio para un resumen rápido de capacidades
    st.metric(label="Módulos Disponibles", value="2", delta="Escalable")
    st.write("**Capacidades del Sistema:**")
    st.checkbox("Procesamiento de Archivos Excel", value=True, disabled=True)
    st.checkbox("Normalización de Datos Automática", value=True, disabled=True)
    st.checkbox("Generación de Reportes Dinámicos", value=True, disabled=True)

st.write("---")

# 4. Instrucciones de Uso (Genéricas)
st.subheader("📖 Guía de Usuario")
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("#### 1. Selección")
    st.write("Elige el módulo de análisis correspondiente en la barra lateral izquierda.")

with c2:
    st.markdown("#### 2. Carga")
    st.write("Sube el archivo extraído del sistema de gestión (CRM) en formato `.xlsx`.")

with c3:
    st.markdown("#### 3. Exportación")
    st.write("Visualiza los KPIs y descarga el resumen ejecutivo procesado en un nuevo archivo.")

# 5. Pie de página minimalista
st.write("---")
st.caption("Desarrollado por Ernesto | Python 3.11 | Streamlit & Pandas Core")