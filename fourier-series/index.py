import pandas as pd
import streamlit as st
from numpy import pi, e, linspace

st.title("Fourier Series")

t = linspace(0, 10, 1000)
y = 0

st.latex("y(t) = \sum_{k=1}^{\infty} \\frac{(-1)^k}{k} e^{jk\pi t}")

with st.expander(label="Demonstration"):
    st.markdown("Calculating the integral of $te^{at}$")
    st.latex(
        r"""
        \begin{align*}
        \int f g' dt &= f g - \int f' g dt \\
        
        \\

        f &= t ; g' = e^{at}\\
        f' &= 1 ; g = \frac{1}{a} e^{at} \\
        
        \\

        \int t e^{at} dt &= t \frac{1}{a} e^{at} - \int 1 \frac{1}{a} e^{at} dt \\ 
        &= \frac{1}{a} t e^{at} - \frac{1}{a} \int e^{at} dt \\
        &= \frac{1}{a} t e^{at} - \frac{1}{a^2} e^{at} + C \\ 
        &= \frac{(at - 1) e^{at}}{a^2}  + C \\
        \end{align*}

        """
    )
    # \xRightarrow{a=-jk\pi}

    st.latex(
        r"""
        \begin{align*}
        a_k &= \frac{1}{T} \int_{0}^{T} x(t) e^{-jk\frac{2\pi}{T}t} dt \\
        a_k &= \frac{1}{2} \int_{0}^{2} {t[u(t+1)-u(t-1)]} e^{-jk\pi t} dt \\
        a_k &= \frac{1}{2} \int_{-1}^{1} t e^{-jk\pi t} dt \\
        
        \\

        \int t e^{-jk\pi t} dt &=  \frac{(-jk\pi t - 1) e^{-jk\pi t}}{(-jk\pi)^2} \\
        &= \frac{(-jk\pi t - 1) e^{-jk\pi t}}{j^2k^2\pi^2} \\
        &= \frac{(-jk\pi t - 1) e^{-jk\pi t}}{(-1)2k^2\pi^2} \\
        &= \frac{(jk\pi t + 1) e^{-jk\pi t}}{k^2\pi^2} \\
        
        \\

        a_k &= \frac{1}{2} \left[\frac{(jk\pi t + 1) e^{-jk\pi t}}{k^2\pi^2}\right]\biggr\vert_{-1}^{1} \\
        a_k &= \frac{1}{2} \left[\frac{(jk\pi + 1) e^{-jk\pi}}{k^2 \pi^2} - \frac{(-jk\pi + 1) e^{jk\pi}}{k^2\pi^2}\right] \\
        a_k &= \frac{1}{2} \left[\frac{(jk\pi + 1) e^{-jk\pi}}{k^2 \pi^2} + \frac{(jk\pi - 1) e^{jk\pi}}{k^2\pi^2}\right] \\
        a_k &= \frac{1}{2} \left[\frac{jk\pi e^{-jk\pi}}{k^2 \pi^2} + \frac{e^{-jk\pi}}{k^2 \pi^2} + \frac{jk\pi e^{jk\pi}}{k^2\pi^2} - \frac{e^{jk\pi}}{k^2\pi^2}\right] \\
        a_k &= \frac{1}{2} \left[\frac{j e^{-jk\pi}}{k \pi} + \frac{e^{-jk\pi}}{k^2 \pi^2} + \frac{j e^{jk\pi}}{k \pi} - \frac{e^{jk\pi}}{k^2\pi^2}\right] \\
        a_k &= \frac{1}{2} \left[\frac{j e^{-jk\pi} + j e^{jk\pi}}{k \pi} + \frac{e^{-jk\pi} - e^{jk\pi}}{k^2\pi^2}\right] \\
        a_k &= \frac{1}{2} \left[\frac{j (e^{-jk\pi} + e^{jk\pi})}{k \pi} + \frac{e^{-jk\pi} - e^{jk\pi}}{k^2\pi^2}\right] \\
        
        \\

        \begin{cases}
        e^{j\theta} = \cos\theta + j\sin\theta \\
        e^{-j\theta} = \cos\theta - j\sin\theta \\
        \end{cases}

        &\quad\therefore\quad

        \begin{cases}
        e^{j\theta} + e^{-j\theta} = 2\cos\theta \\
        e^{j\theta} - e^{-j\theta} = 2j\sin\theta \\
        \end{cases}

        \\

        a_k &= \frac{1}{2} \left[\frac{j (2\cos(jk\pi))}{k \pi} + \frac{2j\sin(jk\pi)}{k^2\pi^2}\right] \\
        
        \\
        \cos(k\pi) &=
        \begin{cases}
        1 & \text{if } k \text{ is even} \\
        -1 & \text{if } k \text{ is odd} \\
        \end{cases}
        = (-1)^k \\
        
        \\

        \sin(k\pi) &=
        \begin{cases}
        0 & \text{if } k \text{ is even} \\
        0 & \text{if } k \text{ is odd} \\
        \end{cases}
        = 0 \\
        
        \\

        a_k &= \frac{1}{2} \left[\frac{j (2(-1)^k)}{k \pi} + \frac{2j(0)}{k^2\pi^2}\right] \\
        a_k &= \frac{1}{2} \left[\frac{j (2(-1)^k)}{k \pi}\right] \\
        a_k &= \frac{j (-1)^{k}}{k \pi} \\
        
        \\

        y(t) &= \frac{1}{T} \sum_{k=-\infty}^{\infty} a_k e^{jk\frac{2\pi}{T}t} \\
        &= \frac{1}{2} \sum_{k=-\infty}^{\infty} \frac{j (-1)^{k}}{k \pi} e^{jk\frac{2\pi}{2}t} \\
        &= \frac{1}{2} \sum_{k=-\infty}^{\infty} \frac{j (-1)^{k}}{k \pi} e^{jk\pi t} \\
        \end{align*}
        """
    )


sum = st.slider("Sum", 1, 100, 1)

for k in range(1, sum + 1):
    y = y + 1j * (-1) ** k / k * e ** (1j * k * pi * t)

df = pd.DataFrame(y.real, index=t, columns=["y"])

st.line_chart(df, x=None, y="y")
