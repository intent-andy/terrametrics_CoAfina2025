# Proyecto de Análisis Territorial y Videos Animados (1985-2024)

Este proyecto analiza cambios territoriales históricos, genera reportes, visualizaciones y videos animados por año, usando datos de cobertura vegetal, vegetación secundaria y pérdida de vegetación.

## Estructura de carpetas y función

- Dates/
  - Secondary_vegetation/: CSV anuales de vegetación secundaria (1985-2024). Notebook `Concatenador_secondary_vegetation.ipynb` para unirlos y generar `secondary_vegetation_completo_1985_2024.csv`.
  - Coverage/: CSV anuales de cobertura territorial. Notebook `Concatenador_coverage.ipynb` para unirlos y generar `coverage_completo_1985_2024.csv`.
  - Vegetation_loss/: CSV anuales de pérdida de vegetación. Notebook `Concatenador_veg_loss.ipynb` para unirlos y generar `vegetation_loss_completo_1985_2024.csv`.

- Analisis/
  - `Análisis de datos.ipynb`: calcula tendencias, puntos de inflexión, genera reportes y gráficos a partir de los CSV consolidados.
  - CSV consolidados: combinan todos los años de cada dataset.
  - Archivos `.png` y `.txt`: visualizaciones y reporte territorial final.
  - `analisis_territorial.json` y `datos_analisis_estructurado.csv`: datos estructurados para análisis adicional.

- Videos/
  - Caratulas/: imágenes de fondo para cada año.
  - imagenes/: imágenes del personaje (boca abierta/cerrada) por año.
  - Libretos/: texto de cada año y videos `.mp4` generados automáticamente combinando audio TTS con animación de imágenes.

## Librerías requeridas

| Librería | Uso | Documentación |
|---|---:|---|
| pandas | Manejo y unión de archivos CSV, procesamiento de datos | https://pandas.pydata.org/ |
| glob | Buscar archivos con patrones en carpetas | https://docs.python.org/3/library/glob.html |
| os | Manejo de rutas y directorios | https://docs.python.org/3/library/os.html |
| re | Expresiones regulares para extraer años de nombres de archivos | https://docs.python.org/3/library/re.html |
| matplotlib | Generación de gráficos y visualizaciones | https://matplotlib.org/stable/index.html |
| numpy | Cálculos numéricos y manipulación de arrays | https://numpy.org/doc/stable/ |
| gTTS | Generación de audio TTS (texto a voz) | https://gtts.readthedocs.io/ |
| cv2 (OpenCV) | Procesamiento de imágenes y creación de videos | https://docs.opencv.org/ |
| wave | Lectura y manipulación de archivos WAV | https://docs.python.org/3/library/wave.html |
| audioop | Cálculo de energía RMS del audio | https://docs.python.org/3/library/audioop.html |
| imageio_ffmpeg | Llamadas a ffmpeg para combinar video y audio | https://imageio.readthedocs.io/en/stable/ |
| subprocess | Ejecutar comandos de sistema (ffmpeg) | https://docs.python.org/3/library/subprocess.html |

## Flujo del proyecto

1. Ejecutar los notebooks en `Dates/` para generar los CSV completos de cada categoría (Coverage, Secondary Vegetation, Vegetation Loss).  
2. Ejecutar `Analisis/Análisis de datos.ipynb` para generar reportes, métricas y gráficos.  
3. Generar videos anuales con los archivos en `Videos/`.

## Notas

- Todos los CSV consolidados incluyen años de 1985 a 2024.  
- Los gráficos se exportan únicamente en formato `.png`.  
- Mantener la estructura de carpetas es crucial para el correcto funcionamiento de notebooks y scripts.