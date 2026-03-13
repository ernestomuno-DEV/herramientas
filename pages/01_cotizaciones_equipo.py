import streamlit as st
import pandas as pd
import io
import plotly.express as px


st.set_page_config(page_title="Data Analytics Portal", page_icon="📈", layout="wide")
st.title("📊 Portal de Inteligencia de Negocios")
st.markdown("### Automatización de Reportes: Cotizaciones")
st.write("---")

archivo = st.file_uploader("Sube el Excel extraído del CRM", type=['xlsx'])

if archivo:

    df = pd.read_excel(archivo)
    

    col1, col2 = st.columns(2)
    with col1:
        fecha_inicio_in = st.date_input("Inicio del análisis")
    with col2:
        fecha_fin_in = st.date_input("Fin del análisis")

    df['Plantel'] = df['Plantel'].str.upper().str.strip()
    df.loc[df['Plantel'] != 'EN LINEA', 'Plantel'] = 'TRADICIONAL'
    df['Fecha de creación'] = pd.to_datetime(df['Fecha de creación'], dayfirst=True, errors='coerce')
    

    f_inicio = pd.to_datetime(fecha_inicio_in)
    f_fin = pd.to_datetime(fecha_fin_in)
    df[['Propietario', 'Plantel']] = df[['Propietario', 'Plantel']].astype(str)
    
    cotizaciones_rango = df[df['Fecha de creación'].between(f_inicio, f_fin)]
    
    if not cotizaciones_rango.empty:
   
        analisis_semana = pd.crosstab(cotizaciones_rango['Propietario'], 
                                      cotizaciones_rango['Plantel'], 
                                      margins=True, margins_name='Total')
        analisis_semana = analisis_semana.sort_values(by='Total', ascending=False)
        

        st.subheader("Resumen de Actividad por Reclutador")
        st.dataframe(
            analisis_semana.style.bar(
                subset=['TRADICIONAL', 'EN LINEA'], 
                color=['#d65f5f', '#5fba7d'], 
                align='mid'
            )
        )
        
        st.write("---")
        

        st.subheader("Visualización de Participación por Plantel")
        

        grafica_data = analisis_semana.drop(['Total', 'All'], axis=1, errors='ignore')
        grafica_data = grafica_data.drop(['Total', 'All'], axis=0, errors='ignore')
        

        fig = px.bar(
            grafica_data.reset_index(), 
            x='Propietario', 
            y=['TRADICIONAL', 'EN LINEA'], 
            title="Distribución de Cotizaciones por Tipo de Plantel",
            labels={'value': 'Cotizaciones', 'variable': 'Tipo de Plantel'},
            color_discrete_map={'TRADICIONAL': '#003366', 'EN LINEA': '#00AEEF'},
            barmode='stack'
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.write("---")
        st.subheader("📥 Descargar Reporte")
        
        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
            analisis_semana.to_excel(writer, index=True)
            
        st.download_button(
            label="Descargar análisis como Excel",
            data=buffer.getvalue(),
            file_name=f"Reporte_Ventas_{fecha_inicio_in}_{fecha_fin_in}.xlsx",
            mime="application/vnd.ms-excel"
        )
    else:
        st.warning("⚠️ No se encontraron cotizaciones en el rango de fechas seleccionado.")

st.write("---")
st.caption("Desarrollado por Erneto | Python 3.11 | Streamlit, Pandas & Plotly")