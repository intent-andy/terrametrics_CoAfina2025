# Terrametrics — Índices territoriales y videos animados (CoAfina 2025)

Proyecto desarrollado para el reto "Índices del futuro: Tierra y Mar Argentino" (CoAfina 2025). Entrega de un toolkit reproducible que mezcla análisis territorial (satélite + series temporales), visualización web con Streamlit y generación de videos anuales animados.

## Resumen rápido
- Analiza cobertura de suelo, vegetación secundaria y pérdida de vegetación (1985–2024).
- Visualiza mapas derivados de Sentinel‑2 + CHIRPS + WorldCover (índice IET / IVT).
- Genera gráficos temporales y videos animados por año con contenido didáctico.

Estructura principal (raíz del repo)
- app.py — Launcher / navegación de la aplicación Streamlit.
- mapas.py — Código para obtener índices desde Google Earth Engine y mostrar mapa interactivo.
- graficos.py — Panel de gráficos a partir de CSV consolidados.
- iet.py, ipmi.py, inicio.py, vid-int.py, about.py — páginas de la app.
- references.py — página Streamlit que muestra la lista de referencias y bibliografía.
- time-series_data/ — CSV consolidados:
  - coverage_completo_1985_2024.csv
  - secondary_vegetation_completo_1985_2024.csv
  - vegetation_loss_completo_1985_2024.csv
- video_generation/ — notebooks y recursos para generar videos por año (carátulas, imágenes, libretos, output).
- videos/ — carpeta destino para mp4 por año (usada por vid-int.py).
- requirements.txt — dependencias mínimas.
- .gitignore — excluye secrets y claves.
- LICENSE.txt — CC BY‑NC‑SA 4.0.

## Instalación (local)
1. Clonar el repositorio:
   git clone <https://github.com/intent-andy/terrametrics_CoAfina2025.git>
   cd terrametrics_CoAfina2025
2. Crear entorno virtual e instalar dependencias:
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt

## Ejecución
- Interfaz principal (Streamlit):
  streamlit run app.py
- Páginas relevantes:
  - Mapas: requiere autenticación de Google Earth Engine. En local, ejecutar `earthengine authenticate` o configurar secrets en Streamlit Cloud (`EE_SERVICE_ACCOUNT` / `EE_PRIVATE_KEY`).
  - Referencias: página "Referencias" incorporada en la app (archivo references.py) muestra la bibliografía usada.
  - Videos interactivos: vid-int.py reproduce mp4 desde la carpeta videos/{año}.mp4
- Generación de videos: abrir `video_generation/Generador de videos.ipynb` y seguir las celdas; los MP4 se guardan en `video_generation/Videos/output` o en `videos/` según configuración.

## Datos
- Los CSV en time-series_data ya contienen las series consolidadas (1985–2024). Son usados por graficos.py y por los notebooks en video_generation/Analisis/.
- No subir credenciales ni claves: .gitignore incluye exclusiones para .streamlit y claves EE.

## Video
Puede ver la presentación de este proyecto en este [link](https://www.youtube.com/watch?v=Zejh2q0paII)

Notas técnicas / advertencias
- Google Earth Engine: si se ejecuta en Streamlit Cloud, configura secrets con la cuenta de servicio y la clave (JSON o PEM). mapas.py contiene helpers para escribir la clave temporalmente y inicializar EE.
- geemap + streamlit_folium + earthengine-api son necesarios para la capa de mapas.
- Revisa paths relativos si mueves archivos o cambias la estructura.

Contribución
- Issues y PRs son bienvenidos. Mantener la estructura de datos al añadir nuevas series o años.
- Respeta la licencia CC BY‑NC‑SA al reutilizar o adaptar contenido.

Licencia

This project is developed for the CoAfina 2025 hackathon.

Shield: [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

Contacto
- Repositorio: https://github.com/intent-andy/terrametrics_CoAfina2025

## Referencias

- Agencia Espacial Europea (ESA). (s.f.). Centro de Acceso Abierto de Copernicus (Copernicus Open Access Hub). Programa Copernicus. Recuperado de https://dataspace.copernicus.eu/
- Esri. (s.f.). NDBI (Normalized Difference Built‑Up Index)—ArcGIS Pro Documentation. ArcGIS Pro. Recuperado de https://pro.arcgis.com/es/pro-app/3.3/arcpy/spatial-analyst/ndbi.htm
- MapBiomas Argentina. (s.f.). Cobertura y uso del suelo — Plataforma MapBiomas Argentina. Recuperado de https://plataforma.argentina.mapbiomas.org/coverage/coverage_lclu
- Naciones Unidas. (s.f.). Objetivo 11: Ciudades y comunidades sostenibles. Objetivos de Desarrollo Sostenible de las Naciones Unidas. Recuperado de https://www.un.org/sustainabledevelopment/es/cities/
- Naciones Unidas. (s.f.). Objetivo 13: Acción por el clima. Objetivos de Desarrollo Sostenible de las Naciones Unidas. Recuperado de https://www.un.org/sustainabledevelopment/es/climate-change-2/
- Naciones Unidas. (s.f.). Objetivo 15: Vida de ecosistemas terrestres. Objetivos de Desarrollo Sostenible de las Naciones Unidas. Recuperado de https://www.un.org/sustainabledevelopment/es/biodiversity/
- Naciones Unidas. (s.f.). Objetivo 16: Paz, justicia e instituciones sólidas. Objetivos de Desarrollo Sostenible de las Naciones Unidas. Recuperado de https://www.un.org/sustainabledevelopment/es/peace-justice/
- Sentinel Hub. (s.f.). EVI (Enhanced Vegetation Index). Sentinel Hub Custom Scripts. Recuperado de https://custom-scripts.sentinel-hub.com/sentinel-2/evi/
- Sentinel Hub. (s.f.). NDMI (Normalized Difference Moisture Index). Sentinel Hub Custom Scripts. Recuperado de https://custom-scripts.sentinel-hub.com/sentinel-2/ndmi/
- Sentinel Hub. (s.f.). NDVI (Normalized Difference Vegetation Index). Sentinel Hub Custom Scripts. Recuperado de https://custom-scripts.sentinel-hub.com/sentinel-2/ndvi/
- Sentinel Hub. (s.f.). SAVI (Soil Adjusted Vegetation Index). Sentinel Hub Custom Scripts. Recuperado de https://custom-scripts.sentinel-hub.com/sentinel-2/savi/
- Sentinel Hub. (s.f.). SWIR RGB (Short‑Wave Infrared RGB). Sentinel Hub Custom Scripts. Recuperado de https://custom-scripts.sentinel-hub.com/sentinel-2/swir-rgb/
