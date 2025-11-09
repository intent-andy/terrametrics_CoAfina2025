import streamlit as st

# Título de la página del Indice de Equilibrio Territorial (IET)
st.markdown('<h1 style="text-align: center;">Índice de Equilibrio Territorial (IET)</h1>', unsafe_allow_html=True)

# Divisor
st.divider()

# Descripción del IET
st.markdown("""
<p style="text-align: justify;">El Índice de Equilibrio Territorial (IET) es una herramienta diseñada para evaluar la salud ecológica y la funcionalidad ambiental de un territorio. Utiliza exclusivamente índices derivados de imágenes satelitales Sentinel-2, enfocándose en aspectos clave como la vegetación y la humedad.</p>
<p style="text-align: justify;">Nuestra propuesta se basa en la combinación de tres índices fundamentales: NDVI (Índice de Vegetación Normalizado), NDMI (Índice de Humedad de Vegetación) y NDBI (Índice de Construcción). Estos índices permiten una evaluación integral del estado ambiental del territorio, proporcionando información valiosa para la toma de decisiones en planificación territorial y gestión ambiental.</p>
""", unsafe_allow_html=True)

# Divisor
st.divider()

# Ecuación del IET
st.markdown('<h2 style="text-align: center;">Cálculo del IET</h2>', unsafe_allow_html=True)
st.markdown('<p style="text-align: justify;">El resultado de nuestra propuesta se expresa mediante la siguiente ecuación:</p>', unsafe_allow_html=True)
st.latex(r"""
IET = \frac{NDVI \cdot NDMI}{NDBI + 1}
"""
)
st.markdown('<p style="text-align: justify;">Donde:</p', unsafe_allow_html=True)
st.latex(r"""
NDBI = \frac{SWIR - NIR}{SWIR + NIR}
""")
st.markdown('<p style="text-align: justify;">Esta diferencia entre los valores de SWIR (Short Wave Infrared) y NIR (Near Infrared) refleja la presencia de áreas construidas en el territorio, lo que permite identificar zonas urbanas.</p>', unsafe_allow_html=True)

# Divisor
st.divider()

# Interpretación del IET
st.markdown('<h3 style="text-align: center;">Interpretación del IET</h3>', unsafe_allow_html=True)
st.markdown("""
<p style="text-align: justify;">El valor del IET proporciona una indicación clara del equilibrio territorial:</p>
- <p style="text-align: justify;">Valores altos de IET indican un territorio con buena cobertura vegetal y humedad, y baja presencia de áreas construidas, lo que sugiere un equilibrio ecológico favorable.</p>
- <p style="text-align: justify;">Valores bajos de IET señalan un territorio con escasa vegetación y humedad, y una alta proporción de áreas construidas, lo que puede indicar un desequilibrio ecológico.</p>
""", unsafe_allow_html=True)