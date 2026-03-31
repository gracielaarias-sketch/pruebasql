import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="Test Conexión FAMMA", page_icon="🔌")

st.title("🔌 Test de Conexión SQL: FAMMA")
st.write("Esta aplicación intenta conectarse a la base de datos `wii_bi` usando la IP pública configurada en los secretos para verificar si el puerto 1433 está accesible desde internet.")

st.divider()

if st.button("Iniciar Prueba de Conexión", type="primary"):
    with st.spinner("Intentando conectar con el servidor SQL de FAMMA... (Puede demorar si el firewall bloquea)"):
        start_time = time.time()
        try:
            # Intentamos establecer la conexión usando los secretos
            conn = st.connection("wii_bi", type="sql")
            
            # Ejecutamos una consulta súper básica y liviana
            df_prueba = conn.query("SELECT TOP 5 CellId, Code, Name FROM CELL")
            
            end_time = time.time()
            st.success(f"¡CONEXIÓN EXITOSA! 🎉 (Tiempo: {end_time - start_time:.2f} segundos)")
            
            st.write("**Datos de prueba obtenidos (Las primeras 5 máquinas):**")
            st.dataframe(df_prueba)
            
        except Exception as e:
            end_time = time.time()
            st.error(f"❌ FALLÓ LA CONEXIÓN (Tiempo: {end_time - start_time:.2f} segundos)")
            st.write("**Detalle técnico del error:**")
            st.code(str(e))
            
            st.info("""
            **Diagnóstico:**
            Si el error dice `Timeout`, `Login timeout expired`, o `TCP Provider: Error`, significa que el router de FAMMA está bloqueando el acceso al puerto 1433 desde afuera. 
            Debes contactar a IT para aplicar la 'Opción 1' o 'Opción 2' de nuestra charla.
            """)
