import streamlit as st
from functions import compute_partial_derivatives, plot_surface_with_tangent

st.set_page_config(page_title="Partial Derivative App", layout="wide")

st.title("🔢 Visualisasi Turunan Parsial dan Bidang Singgung")

expr_str = st.text_input("Masukkan fungsi f(x, y):", "x**2 + y**2")
x0 = st.number_input("Nilai x₀:", value=1.0)
y0 = st.number_input("Nilai y₀:", value=1.0)

if st.button("Hitung dan Tampilkan Grafik"):
    fx, fy = compute_partial_derivatives(expr_str)
    st.write("∂f/∂x =", fx)
    st.write("∂f/∂y =", fy)

    fig = plot_surface_with_tangent(expr_str, x0, y0)
    st.pyplot(fig)
