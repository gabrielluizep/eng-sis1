import pandas as pd
import streamlit as st
from numpy import pi, e, linspace

st.title("Fourier Series")

t = linspace(0, 10, 1000)
y = 0


st.latex("y(t) = \sum_{k=1}^{\infty} \\frac{(-1)^k}{k} e^{jk\pi t}")

sum = st.slider("Sum", 1, 100, 1)

for k in range(1, sum + 1):
    y = y + 1j * (-1) ** k / k * e ** (1j * k * pi * t)

df = pd.DataFrame(y.real, index=t, columns=["y"])

st.line_chart(df, x=None, y="y")
