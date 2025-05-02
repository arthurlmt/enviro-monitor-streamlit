import streamlit as st
import random
import pandas as pd
import time

st.set_page_config(layout="wide")
st.title("🫁 Monitoramento da Qualidade do Ar")

placeholder = st.empty()
historico = []

for _ in range(100):
    valor = round(random.uniform(0, 300), 2)  # índice AQI
    historico.append({"valor": valor, "tempo": pd.Timestamp.now()})
    if len(historico) > 50:
        historico.pop(0)

    df = pd.DataFrame(historico).set_index("tempo")

    with placeholder.container():
        st.subheader("📈 Sensor 1")
        st.line_chart(df)

        st.subheader("📈 Sensor 2")
        st.line_chart(df)

        st.subheader("📈 Sensor 3")
        st.line_chart(df)

    time.sleep(1)
