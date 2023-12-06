import pandas as pd
import streamlit as st
from numpy import pi, e, linspace, cos

st.title("Fourier Series")

t = linspace(0, 10, 1000)

# a
st.latex("y(t) = 2\sum_{k=1}^{\infty} \\frac{(-1)^k}{k} e^{jk\pi t}")

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

y_a = 0
sum_a = st.slider("Sum A", 1, 100, 30)

for k in range(1, sum_a + 1):
    y_a = y_a + 1j * (-1) ** k / k * e ** (1j * k * pi * t)

df_a = pd.DataFrame(y_a.real, index=t, columns=["y"])

st.line_chart(df_a, x=None, y="y")

# d
st.latex(r"y(t) = 1 + 2 \sum_{k=1}^{\infty} \left[\frac{1}{2} (1+(-1)^k)\right] e^{j k \pi t}") 

y_d = 0
sum_d = st.slider("Sum D", 1, 100, 30)

for k in range(1, sum_d +1):
    y_d = y_d + (1/2 * (1+(-1)**k)* e ** (1j * k * pi * t))

y_d = y_d*2
y_d = 1 + y_d

df_d = pd.DataFrame(y_d.real, index=t, columns=["y"])

st.line_chart(df_d, x=None, y="y")

# e 
st.latex(r"1 + 2 \sum_{k=1}^{\infty} \frac{1}{j k} \left[cos(2k\pi/3) * cos(k\pi/3) \right] e^{j k t \pi/3}")

y_e = 0
sum_e = st.slider("Sum E", 1, 100, 30)

for k in range(1, sum_e + 1):
    y_e = y_e + (1 / (1j * k) * (cos(2 * k * pi / 3) - cos(k * pi / 3))) * e ** (1j * k * pi * t)

y_e = y_e * 2
y_e = 1 + y_e

df_e = pd.DataFrame(y_e.real, index=t, columns=["y"])

st.line_chart(df_e, x=None, y="y")

#f
st.latex(r"4/3 + 2 \sum_{k=1}^{\infty} \left(\frac{1}{1 j 2 pi} * \left[2  - e^{-jk4\pi/3} - e^{-jk2\pi/3} \right] \right) e^{j k 2\pi/3}")

y_f = 0
sum_f = st.slider("Sum F", 1, 100, 30)

for k in range(1, sum_f + 1):
    y_f = y_f + (1 / (1j * k * 2 * pi) * (2 - e ** (-1j * k * 4 * pi / 3) - e ** (-1j * k * 2 * pi / 3))) * e ** (1j * k * 2 * pi * t / 3)

y_f = y_f * 2
y_f = 4 / 3 + y_f

df_f = pd.DataFrame(y_f.real, index=t, columns=["y"])

st.line_chart(df_f, x=None, y="y")