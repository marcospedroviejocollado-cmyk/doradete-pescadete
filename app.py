import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Calculadora de Rebajas", page_icon="✔")

# Título y Descripción
st.title("🛒 Calculadora de Rebajas")
st.markdown("Introduce el precio original y el descuento para ver el precio final.")
st.write("---")

# 2. Entrada de Datos (Barra Lateral)
st.sidebar.header("Datos del Producto")
precio = st.sidebar.number_input("Precio original (€)", min_value=0.0, max_value=10000.0, value=50.0)
descuento = st.sidebar.slider("Descuento (%)", 0, 100, 20)

# 3. Botón de Cálculo y Lógica
if st.button("Calcular precio final"):
    
    # Cálculo del descuento
    cantidad_descuento = precio * (descuento / 100)
    precio_final = precio - cantidad_descuento
    
    # 4. Mostrar Resultado con Diseño
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric(label="Precio final:", value=f"{precio_final:.2f} €")
        
    with col2:
        st.success(f"muy buen descuento, ahorras {cantidad_descuento:.2f} € 👌")
        if descuento >= 50:
            st.balloons()

     with col3:
        st.success(f" Nada mal tio,Ahorras {cantidad_descuento:.2f} € 💸")
        if descuento >= 30:
            st.balloons()

 with col4:
        st.success(f"podria estar mejor ahorras {cantidad_descuento:.2f} € 💸")
        if descuento >= 15:
            st.💕()

    # Extra: Fórmula usada
    st.write("---")
    st.info("Fórmula utilizada:")
    st.latex(r''' Precio\ final = Precio\ original \times (1 - \frac{descuento}{100}) ''')
