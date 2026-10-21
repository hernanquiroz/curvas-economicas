import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# ───────────────────────────────────────────────────────────────
# Configuración de la página
# ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Curva Desplazable",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ───────────────────────────────────────────────────────────────
# Título y descripción
# ──────────────────────────────────────────────────────────────
st.title("📈 Curva Roja Desplazable")
st.markdown("""
Desplaza manualmente la **curva roja punteada** $g(x)=x^3$ usando los sliders,
mientras la **curva azul** $f(x)=x^3+4$ permanece **fija**.
""")

# ───────────────────────────────────────────────────────────────
# Sidebar con sliders
# ───────────────────────────────────────────────────────────────
st.sidebar.header("⚙️ Controles de desplazamiento")

dx = st.sidebar.slider(
    "Desplazamiento horizontal (Δx)",
    min_value=-5.0,
    max_value=5.0,
    value=0.0,
    step=0.1,
    format="%.1f"
)

dy = st.sidebar.slider(
    "Desplazamiento vertical (Δy)",
    min_value=-5.0,
    max_value=5.0,
    value=0.0,
    step=0.1,
    format="%.1f"
)

st.sidebar.markdown("---")
st.sidebar.markdown(f"""
**Desplazamiento actual:**
- Δx = **{dx:+.1f}**
- Δy = **{dy:+.1f}**
""")

st.sidebar.markdown("---")
st.sidebar.markdown("""
**Ecuaciones:**
- 🔵 Azul (fija): $f(x) = x^3 + 4$
- 🔴 Roja (móvil): $g(x) = (x - \\Delta x)^3 + \\Delta y$
""")

# ───────────────────────────────────────────────────────────────
# Datos de las funciones
# ──────────────────────────────────────────────────────────────
x = np.linspace(-3, 2.5, 500)

f_azul = x**3 + 4
f_roja = (x - dx)**3 + dy   # desplazada

# ───────────────────────────────────────────────────────────────
# Plot
# ───────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 7))

# Cuadrícula mayor y menor
ax.set_xticks(np.arange(-6, 8, 1))
ax.set_yticks(np.arange(-6, 8, 1))
ax.set_xticks(np.arange(-6, 8, 0.5), minor=True)
ax.set_yticks(np.arange(-6, 8, 0.5), minor=True)
ax.grid(True, which='major', color='lightgray', linewidth=0.6)
ax.grid(True, which='minor', color='lightgray', linewidth=0.3)

# Ejes centrados
ax.axhline(0, color='black', linewidth=1.2)
ax.axvline(0, color='black', linewidth=1.2)

# Curva azul (fija)
ax.plot(x, f_azul,
        color='steelblue', linewidth=2.5,
        label=r'$f(x) = x^3 + 4$  (fija)')

# Curva roja punteada (desplazada)
ax.plot(x, f_roja,
        color='firebrick', linewidth=2.5, linestyle='--',
        label=rf'$g(x) = x^3$  desplazada  $(\Delta x={dx:+.1f},\ \Delta y={dy:+.1f})$')

ax.set_xlim(-6.5, 7)
ax.set_ylim(-6, 6)
ax.set_aspect('equal')
ax.legend(loc='upper left', fontsize=11, framealpha=0.9)
ax.set_title('Curva roja desplazable — usa los sliders del panel izquierdo',
             fontsize=13, pad=10)

# Ajustar ticks para que se vean bien
ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
ax.yaxis.set_major_locator(ticker.MultipleLocator(2))

plt.tight_layout()

# ───────────────────────────────────────────────────────────────
# Mostrar en Streamlit
# ───────────────────────────────────────────────────────────────
st.pyplot(fig)

# ──────────────────────────────────────────────────────────────
# Información adicional
# ───────────────────────────────────────────────────────────────
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Desplazamiento X", f"{dx:+.1f}")
with col2:
    st.metric("Desplazamiento Y", f"{dy:+.1f}")
with col3:
    st.metric("Punto de inflexión roja", f"({dx:.1f}, {dy:.1f})")
