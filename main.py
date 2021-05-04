from teste_filtro import Armstrong_Modulator
import streamlit as st

def main():
    st.header("Modulador Armstrong")

    st.header(" Entrada ")
    f1_1 = st.number_input("Quem é f1?", value = 400.0, step = 0.1)
    und_f1 = st.selectbox("Qual a unidade de f1?", ["Hz", "kHz", "MHz"])
    df1_1 = st.number_input("Qual desvio de f1?", value = 20.0, step = 0.1)
    und_df1 = st.selectbox("Qual a unidade do desvio de f1?", ["Hz", "kHz", "MHz"])
    st.header(" Saída ")
    f1_4 = st.number_input("Quem é f4?", value = 400.0, step = 0.1)
    und_f4 = st.selectbox("Qual a unidade de f4?", ["Hz", "kHz", "MHz"])
    df1_4 = st.number_input("Qual desvio de f4?", value = 20.0, step = 0.1)
    und_df4 = st.selectbox("Qual a unidade do desvio de f4?", ["Hz", "kHz", "MHz"])

    st.header("Intervalo do Oscilador")
    f0_0 = st.number_input("Quem a primeira frequência do intervalo?", value = 1.0, step = 0.1)
    und_f0_0 = st.selectbox("Qual a unidade da primeira frequência do intervalo?", ["Hz", "kHz", "MHz"])
    f0_1 = st.number_input("Qual a última frequência do intervalo", value = 10.0, step = 0.1)
    und_f0_1 = st.selectbox("Qual a unidade da última frequência do intervalo?", ["Hz", "kHz", "MHz"])

    if und_f1 == "Hz":
        mult_f1 = 0
    if und_f1 == "kHz":
        mult_f1 = 3
    if und_f1 == "MHz":
        mult_f1 = 6

    if und_df1 == "Hz":
        mult_df1 = 0
    if und_df1 == "kHz":
        mult_df1 = 3
    if und_df1 == "MHz":
        mult_df1 = 6

    if und_f4 == "Hz":
        mult_f4 = 0
    if und_f4 == "kHz":
        mult_f4 = 3
    if und_f4 == "MHz":
        mult_f4 = 6

    if und_df4 == "Hz":
        mult_df4 = 0
    if und_df4 == "kHz":
        mult_df4 = 3
    if und_df4 == "MHz":
        mult_df4 = 6

    if und_f0_0 == "Hz":
        mult_f0_0 = 0
    if und_f0_0 == "kHz":
        mult_f0_0 = 3
    if und_f0_0 == "MHz":
        mult_f0_0 = 6

    if und_f0_1 == "Hz":
        mult_f0_1 = 0
    if und_f0_1 == "kHz":
        mult_f0_1 = 3
    if und_f0_1 == "MHz":
        mult_f0_1 = 6

    f1_1 = f1_1*10**mult_f1
    df1_1 = df1_1*10**mult_df1
    f4_1 = f1_4*10**mult_f4
    df4_1 = df1_4*10**mult_df4
    df0_1 = [f0_0*10**mult_f0_0, f0_1*10**mult_f0_1]

    st.header(" Resposta ")
    resposta = Armstrong_Modulator(f1 = f1_1, df1 = df1_1, f4 = f4_1, df4=df4_1, f0=df0_1).f2_f3_f0()

if __name__ == '__main__':
    main()


