import streamlit as st
import ee
import folium
import geemap.foliumap as geemap_folium
from streamlit_folium import st_folium
from google.oauth2 import service_account # Importante para la autenticación


# Define el scope/ámbito necesario para Earth Engine
EE_SCOPES = [
    'https://www.googleapis.com/auth/cloud-platform',
    'https://www.googleapis.com/auth/earthengine' 
]

# --- 0. Configuración de la Página ---
st.set_page_config(page_title="Índice IET en GEE", layout="wide")
st.title("🛰️ Visualizador GEE: Índice IET Córdoba (2023)")

# --- 1. Autenticación Segura (Usando Streamlit Secrets) ---
# Este bloque es el que cambia para el despliegue.
try:
    # Obtener las credenciales desde los Secrets de Streamlit
    # st.secrets["google_credentials"] hace referencia a la sección [google_credentials] en tu TOML
    creds_dict = st.secrets["google_credentials"]
    
    # Crear un objeto de credenciales de Google
    credentials = service_account.Credentials.from_service_account_info(
        creds_dict,
        scopes=EE_SCOPES # <-- Esto resuelve el 'invalid_scope'
    )
    
    # Inicializar Earth Engine con esas credenciales
    ee.Initialize(credentials=credentials)
    
    # Opcional: un mensaje de éxito que solo tú verás mientras depuras
    # st.success("¡Autenticación con Google Earth Engine exitosa!")

except Exception as e:
    st.error(f"Error al autenticar o inicializar GEE: {e}")
    st.error("Por favor, verifica: \n"
             "1. Que el 'Secret' [google_credentials] esté bien configurado en Streamlit Cloud. \n"
             "2. Que la cuenta de servicio esté registrada en GEE (earthengine.google.com/signup).")
    st.stop() # Detiene la ejecución si la autenticación falla

# --- 2. Tu Código GEE (Traducido a Python) ---
# Esta parte es idéntica a tu lógica original
try:
    cordoba = ee.FeatureCollection("FAO/GAUL/2015/level2") \
        .filter(ee.Filter.eq('ADM2_NAME', 'Córdoba'))

    s2 = ee.ImageCollection("COPERNICUS/S2_SR") \
        .filterBounds(cordoba) \
        .filterDate('2023-01-01', '2023-12-31') \
        .select(['B4', 'B8', 'B11']) \
        .median() # Usamos median() para tener una sola imagen

    ndvi = s2.normalizedDifference(['B8', 'B4']).rename('NDVI')
    ndmi = s2.normalizedDifference(['B8', 'B11']).rename('NDMI')

    chirps = ee.ImageCollection("UCSB-CHG/CHIRPS/DAILY") \
        .filterBounds(cordoba) \
        .filterDate('2023-01-01', '2023-12-31') \
        .sum() \
        .rename('Precipitation')

    urban = ee.Image("ESA/WorldCover/v100/2020") \
        .select('Map') \
        .eq(50) \
        .rename('Urban')

    iet = ndvi \
        .multiply(ndmi) \
        .multiply(chirps) \
        .divide(urban.add(1)) \
        .rename('IET')

    # Recortamos la imagen final a la geometría de Córdoba
    iet_clipped = iet.clip(cordoba)

    # --- 3. Parámetros de Visualización ---
    vis_params = {
        'min': 0,
        'max': 1,
        'palette': ['red', 'yellow', 'green']
    }

    # --- 4. Centrado del Mapa (Obtener info del servidor) ---
    # Usamos .getInfo() para traer las coordenadas al script
    region_info = cordoba.geometry().bounds().getInfo()
    coords = region_info['coordinates'][0]
    # Calcular el centroide de la caja delimitadora (bounds)
    center_lon = (coords[0][0] + coords[2][0]) / 2
    center_lat = (coords[0][1] + coords[1][1]) / 2
    map_center = [center_lat, center_lon]
    zoom_start = 7

except Exception as e:
    st.error(f"Error durante el procesamiento GEE: {e}")
    st.stop()


# --- 5. Creación y Visualización del Mapa Folium ---
st.markdown("Mapa interactivo del Índice IET:")

# Crear un mapa base de Folium (usamos un fondo más limpio)
m = folium.Map(location=map_center, zoom_start=zoom_start, tiles="CartoDB positron")

# Añadir tu capa GEE al mapa Folium usando geemap
geemap_folium.add_ee_layer(
    m,                # El mapa folium
    iet_clipped,      # Tu imagen de GEE
    vis_params,       # Parámetros de visualización
    'Índice IET'      # Nombre de la capa
)

# También añadimos el contorno de Córdoba para contexto
m.add_child(folium.GeoJson(
    data=cordoba.geometry().getInfo(),
    style_function=lambda x: {'fillColor': 'none', 'color': 'blue', 'weight': 2},
    name="Límite Córdoba"
))

# Añadir un control de capas al mapa
folium.LayerControl().add_to(m)

# --- 6. Renderizar el mapa en Streamlit ---
# Usamos st_folium para mostrar el mapa 'm'
st_folium(m, width=1000, height=600, returned_objects=[])