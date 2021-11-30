import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import plotly.express as px


st.header("Interface para visualização e aprendizado de dados do ENADE")
st.subheader("Selecione qual informação queira visualizar abaixo")

report_type = st.selectbox(
    "Selecione:", ["Visualização de dados", "Aprendizagem de dados"]
)


def visualizacao_dados():

    # df = pd.read_sql()

    st.subheader("1. Quais foram as distribuições de notas de cada ano?")
    fig = px.box(
        df,
        x="time",
        y="total_bill",
    )
    st.plotly_chart(fig)
    st.text(" ")

    st.subheader("2. Quais foram os cursos mais presentes no ENADE de cada ano?")
    fig = px.box(df, x="time", y="total_bill", points="all")
    st.plotly_chart(fig)
    st.text("")

    st.subheader("3. Quais regiões estão mais presentes no ENADE de cada ano?")
    fig = px.box(df, x="time", y="total_bill", points="all")
    st.plotly_chart(fig)
    st.text("")

    st.subheader("4. Há mais homens ou mulheres fazendo a prova?")
    fig = px.box(df, x="time", y="total_bill", points="all")
    st.plotly_chart(fig)
    st.text("")

    st.subheader("5. Como é a distribuição de notas por sexo?")
    fig = px.box(df, x="time", y="total_bill", points="all")
    st.plotly_chart(fig)
    st.text("")


def linear_regression(test_size):
    # Load the diabetes dataset
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.33, random_state=42
    )
    # Treinando modelo
    model = LinearRegression().fit(x_train, y_train)
    y_pred = LinearRegression().predict(x_test)

    # Score do modelo
    # The coefficient of determination: 1 is perfect prediction
    r_sq = model.score(x, y)
    st.text("coefficient of determination:", r_sq)
    st.text("slope:", model.coef_)

    # Plotando dado real + previsão
    plt.scatter(x_test, y_test, color="black")
    plt.plot(x_test, y_pred, color="blue", linewidth=3)
    plt.xticks(())
    plt.yticks(())
    plt.show()


def aprendizagem_dados():
    st.subheader("Predição dos dados de Dezembro com Regressão Linear")
    test_size = st.slider("Qual tamanho você quer para os dados de test?", 0, 1, 0.33)
    # linear_regression(test_size)


if report_type == "Visualização de dados":
    visualizacao_dados()
else:
    aprendizagem_dados()
