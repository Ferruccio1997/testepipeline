import streamlit as st
from datetime import datetime, time

def main():
    st.title("Sistema de CRM e Vendas da ZapFlow - Frontend Simples")
    email = st.text_input("Campo de texto para inserção do email do vendedor")
    data = st.date_input("Campo para selecionar a data em que a venda foi realizada", datetime.now())
    hora = st.time_input("Campo para selecionar a hora em que a venda foi realizada", value=time(9, 0))
    valor = st.number_input("Campo numérico para inserir o valor monetário da venda realizada", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Campo numérico para inserir a quantidade de produtos vendidos", min_value=1, step=1)
    produto = st.selectbox("Campo de seleção para escolher o produto vendido", ["ZapFlow com Gemini","ZapFlow com ChatGPT", "ZapFlow com Llama 3.0"])


    if st.button("Salvar"):

        data_hora = datetime.combine(data, hora)
        st.write("**Dados de venda:**")
        st.write(f"Email do vendedor: {email}")
        st.write(f"Data e Hora da Compra: {data_hora}")
        st.write(f"Valor da Venda: R$ {valor:.2f}")
        st.write(f"Quantidade de Produtos: {quantidade}")
        st.write(f"Produto: {produto}")


if __name__=="__main__":
    main()