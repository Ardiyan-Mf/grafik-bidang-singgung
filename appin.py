import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# --- Fungsi: Hitung turunan parsial ---
def compute_partial_derivatives(expr_str):
    x, y = sp.symbols('x y')
    expr = sp.sympify(expr_str)
    fx = sp.diff(expr, x)
    fy = sp.diff(expr, y)
    return fx, fy

# --- Fungsi: Hitung bidang singgung ---
def evaluate_tangent_plane(expr_str, x0, y0):
    x, y = sp.symbols('x y')
    expr = sp.sympify(expr_str)
    fx = sp.diff(expr, x)
    fy = sp.diff(expr, y)
    z0 = expr.subs({x: x0, y: y0})
    fx0 = fx.subs({x: x0, y: y0})
    fy0 = fy.subs({x: x0, y: y0})

    def plane(X, Y):
        return float(z0) + float(fx0)*(X - x0) + float(fy0)*(Y - y0)
    
    return plane

# --- Fungsi: Plot permukaan dan bidang singgung ---
def plot_surface_with_tangent(expr_str, x0, y0):
    x, y = sp.symbols('x y')
    expr = sp.sympify(expr_str)
    f_lambdified = sp.lambdify((x, y), expr, 'numpy')

    X_vals = np.linspace(x0 - 2, x0 + 2, 50)
    Y_vals = np.linspace(y0 - 2, y0 + 2, 50)
    X, Y = np.meshgrid(X_vals, Y_vals)
    Z = f_lambdified(X, Y)

    tangent_plane = evaluate_tangent_plane(expr_str, x0, y0)
    Z_plane = tangent_plane(X, Y)

    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7)
    ax.plot_surface(X, Y, Z_plane, color='red', alpha=0.5)
    ax.set_title('Permukaan Fungsi dan Bidang Singgung')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    return fig

# --- Streamlit UI ---
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

