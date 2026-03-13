import streamlit as st
import pandas as pd

st.title("📊 Reporte Automatizado de Cotizaciones")

archivo = st.file_uploader("Sube el Excel de la Agenda", type=['xlsx'])

if archivo:
    df = pd.read_excel(archivo)
    
   
    col1, col2 = st.columns(2) 
    with col1:
        fecha_inicio = st.date_input("Inicio")
    with col2:
        fecha_fin = st.date_input("Fin")
    

    df['Plantel'] = df['Plantel'].str.upper().str.strip()
    df.loc[df['Plantel'] != 'EN LINEA', 'Plantel'] = 'TRADICIONAL'
    
   
    df['Fecha de creación'] = pd.to_datetime(df['Fecha de creación'], dayfirst=True, errors='coerce')
    

    f_inicio = pd.to_datetime(fecha_inicio)
    f_fin = pd.to_datetime(fecha_fin)
    

    cotizaciones_rango = df[df['Fecha de creación'].between(f_inicio, f_fin)]
    

    analisis_semana = pd.crosstab(cotizaciones_rango['Propietario'], 
                                  cotizaciones_rango['Plantel'], 
                                  margins=True, 
                                  margins_name='Total')
    

    if 'Total' in analisis_semana.columns:
       analisis_semana = analisis_semana.sort_values(by='Total', ascending=False)
    else:
       st.warning("⚠️ No se encontraron cotizaciones en el rango de fechas seleccionado.")
    
    analisis_semana = analisis_semana.astype(str)

    st.subheader("Resumen por Reclutador")
    st.dataframe(analisis_semana.style.background_gradient(cmap='Greens'))
    
    
    st.subheader("Visualización de Productividad")
    grafica_data = analisis_semana.drop('Total', axis=0, errors='ignore')
    st.bar_chart(grafica_data[['TRADICIONAL', 'EN LINEA']])

    st.subheader("📥 Descargar Reporte")


    import io
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
     analisis_semana.to_excel(writer, index=True)

    st.download_button(
    label="Descargar análisis como Excel",
    data=buffer.getvalue(),
    file_name=f"Reporte_Ventas_{fecha_inicio}.xlsx",
    mime="application/vnd.ms-excel"
)