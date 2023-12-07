import pandas as pd
import streamlit as st
import plotly.express as px
from numpy import pi, e, linspace, cos

st.title("Fourier Series")

t = linspace(-5, 5, 1000)

st.subheader("a)")
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

fig_a = px.line(df_a, x=None, y="y")
fig_a.update_layout(
    title="Fourier Series",
    xaxis_title="t",
    yaxis_title="y(t)",
    legend_title="",
    font=dict(family="Courier New, monospace", size=18, color="RebeccaPurple"),
)
st.plotly_chart(fig_a)

st.subheader("d)")
st.latex(
    r"y(t) = -\frac{1}{2} + \sum_{k=1}^{\infty} \left[\frac{1}{2} - (-1)^k\right] e^{j k \pi t}"
)

with st.expander(label="Demonstration"):
    st.latex(
        r"""
        \begin{align*}  
        T = 2 ; &\quad \omega_0 = \frac{2\pi}{T} = \frac{2\pi}{2} = \pi \\
        
        \\
        
        a_0 &= \frac{1}{T} \int_{0}^{T} x(t) dt \\
        &= \frac{1}{2} \int_{0}^{2} \delta(t) - 2 \delta(t-1) dt \\
        &= \frac{1}{2} \left[\int_{0}^{2} \delta(t) dt - 2 \int_{0}^{2} \delta(t-1) dt\right] \\
        &= \frac{1}{2} \left[1 - 2 \right] \\
        &= \frac{1}{2} \cdot (-1) \\
        &= -\frac{1}{2} \\
        
        \\

        a_k &= \frac{1}{T} \int_{0}^{T} x(t) e^{-jk\omega_0 t} dt \\
        &= \frac{1}{2} \int_{0}^{2} \left[\delta(t) - 2 \delta(t-1) \right] e^{-jk\pi t} dt \\
        &= \frac{1}{2} \left[\int_{0}^{2} \delta(t) e^{-jk\pi t} dt - 2 \int_{0}^{2} \delta(t-1) e^{-jk\pi t} dt\right] \\
        &= \frac{1}{2} \left[\int_{0}^{2} \delta(t) e^{-jk\pi \cdot 0} dt - 2 \int_{0}^{2} \delta(t-1) e^{-jk\pi \cdot (1)} dt\right] \\
        &= \frac{1}{2} \left[e^{0} \int_{0}^{2} \delta(t) dt - 2 e^{-jk\pi} \int_{0}^{2} \delta(t-1) dt\right] \\ 
        &= \frac{1}{2} \left[1 - 2 e^{-jk\pi} \right] \\
        &= \frac{1}{2} \left[1 - 2 \cdot (-1)^k \right] \\
        &= \frac{1}{2} - (-1)^k \\
        
        \\

        y(t) &= a_0 + \frac{1}{T} \sum_{k=-\infty}^{\infty} a_k e^{jk\omega_0 t} \\
        &= -\frac{1}{2} + \frac{1}{2} \sum_{k=-\infty}^{\infty} \left[\frac{1}{2} - (-1)^k\right] e^{jk\pi t} \\
        \end{align*}
        """
    )

y_d = 0
sum_d = st.slider("Sum D", 1, 100, 30)

for k in range(1, sum_d + 1):
    y_d = y_d + (1 / 2 - (-1) ** k) * e ** (1j * k * pi * t)

y_d = -1 / 2 + y_d / 2

df_d = pd.DataFrame(y_d.real, index=t, columns=["y"])

st.line_chart(df_d, x=None, y="y")

st.subheader("e)")
st.latex(
    r"1 + 2 \sum_{k=1}^{\infty} \frac{1}{j k} \left[cos(2k\pi/3) * cos(k\pi/3) \right] e^{j k t \pi/3}"
)

with st.expander(label="Demonstration"):
    st.latex(
        r"""
        \begin{align*}
        T = 6 ; &\quad \omega_0 = \frac{2\pi}{T} = \frac{2\pi}{6} = \frac{\pi}{3} \\
        
        \\

        a_0 &= \frac{1}{T} \int_{0}^{T} x(t) dt \\
        &= \frac{1}{6} \left[ \int_{-2}^{-1} dt - \int_{1}^{2} dt \right]\\
        &= \frac{1}{6} \left[ t \biggr\vert_{-2}^{-1} - t \biggr\vert_{1}^{2}\right] \\
        &= \frac{1}{6} \left[ (-1) - (-2) - \left(2 - 1 \right) \right] \\
        &= \frac{1}{6} \left[ 1 - 1 \right] \\
        &= 0 \\
        
        \\

        a_k &= \frac{1}{T} \int_{0}^{T} x(t) e^{-jk\omega_0 t} dt \\
        
        &= \frac{1}{6} \left[\int_{-2}^{-1} e^{-jk\pi t/3} dt - \int_{1}^{2} e^{-jk\pi t/3} dt \right]\\
        &= \frac{1}{6} \left[ \frac{e^{-jk\pi t/3}}{-jk\pi/3} \biggr\vert_{-2}^{-1} - \frac{e^{-jk\pi t/3}}{-jk\pi/3} \biggr\vert_{1}^{2}\right]\\
        &= \frac{1}{6} \frac{1}{-jk\pi/3} \left[ e^{-jk\pi/3t} \biggr\vert_{-2}^{-1} - e^{-jk\pi/3t} \biggr\vert_{1}^{2}\right]\\
        &= \frac{1}{6} \frac{1}{-jk\pi/3} \left[ \left(e^{-jk\pi/3(-1)} - e^{-jk\pi/3(-2)}\right) - \left(e^{-jk\pi/3(2)} - e^{-jk\pi/3(1)}\right)\right]\\
        &= \frac{1}{6} \frac{1}{-jk\pi/3} \left[ \left(e^{jk\pi/3} - e^{2jk\pi/3}\right) - \left(e^{-2jk\pi/3} - e^{-jk\pi/3}\right)\right]\\
        &= \frac{1}{6} \frac{1}{-jk\pi/3} \left[ e^{jk\pi/3} - e^{2jk\pi/3} - e^{-2jk\pi/3} + e^{-jk\pi/3}\right]\\
        &= \frac{1}{6} \frac{1}{-jk\pi/3} \left[ \left(e^{jk\pi/3} + e^{-jk\pi/3}\right) - \left(e^{2jk\pi/3} + e^{-2jk\pi/3}\right)\right]\\
        
        \\ 

        \text{Obs.:} &\begin{cases}
        e^{j\theta} = \cos\theta + j\sin\theta \\
        e^{-j\theta} = \cos\theta - j\sin\theta \\
        \end{cases}

        \quad \therefore \quad

        e^{-j\theta} + e^{j\theta} = 2\cos\theta \\

        \\

        a_k &= \frac{1}{6} \frac{1}{-jk\pi/3} \left[ 2\cos(k\pi/3) - 2\cos(2k\pi/3)\right]\\
        &= \frac{1}{6} \frac{1}{jk\pi/3} \left[ 2\cos(2k\pi/3) - 2\cos(k\pi/3)\right]\\
        &= \frac{1}{3} \frac{1}{jk\pi/3} \left[ \cos(2k\pi/3) - \cos(k\pi/3)\right]\\
        &= \frac{1}{jk\pi} \left[ \cos(2k\pi/3) - \cos(k\pi/3)\right]\\

        \end{align*}
        """
    )

y_e = 0
sum_e = st.slider("Sum E", 1, 100, 30)

for k in range(1, sum_e + 1):
    y_e = y_e + (cos(2 * k * pi / 3) - cos(k * pi / 3)) / (1j * k * pi) * e ** (
        1j * k * pi * t / 3
    )

y_e = y_e * 2
y_e = 1 + y_e

df_e = pd.DataFrame(y_e.real, index=t, columns=["y"])

st.line_chart(df_e, x=None, y="y")

st.subheader("f)")
st.latex(
    r"4/3 + 2 \sum_{k=1}^{\infty} \left(\frac{1}{1 j 2 pi} * \left[2  - e^{-jk4\pi/3} - e^{-jk2\pi/3} \right] \right) e^{j k 2\pi/3}"
)

y_f = 0
sum_f = st.slider("Sum F", 1, 100, 30)

for k in range(1, sum_f + 1):
    y_f = y_f + (
        1
        / (1j * k * 2 * pi)
        * (2 - e ** (-1j * k * 4 * pi / 3) - e ** (-1j * k * 2 * pi / 3))
    ) * e ** (1j * k * 2 * pi * t / 3)

y_f = y_f * 2
y_f = 4 / 3 + y_f

df_f = pd.DataFrame(y_f.real, index=t, columns=["y"])

st.line_chart(df_f, x=None, y="y")
