# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt
from io import BytesIO
from aux import graficar_duval

st.write('# Triángulo de Duval')

col1, col2, col3 = st.columns(3)
with col1:
    x = st.number_input('ACETILENO (C2H2, ppm)', 0, 1000, value=150, step=1)
with col2:
    y = st.number_input('ETILENO (C2H4, ppm)', 0, 1000, value=200, step=1)
with col3:
    z = st.number_input('METANO (CH4, ppm)', 0, 1000, value=300, step=1)

x_ = x * 100 / (x + y + z)
y_ = y * 100 / (x + y + z)
z_ = z * 100 / (x + y + z)

concentraciones_rel = pd.DataFrame(data={'Acetileno (C2H2)': [x_],
                                         'Etileno (C2H4)': [y_],
                                         'Metano (CH4)': [z_]})
concentraciones_rel.index = ['Concentraciones relativas (%)']


fig, ax = graficar_duval(concentraciones_rel)
buf = BytesIO()
fig.savefig(buf, format="png", dpi=150)

with st.container():
    st.write(concentraciones_rel.transpose())
    st.image(buf)