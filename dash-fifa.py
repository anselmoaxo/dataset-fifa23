import streamlit as st
import pandas as pd
import plotly.express as px



st.set_page_config(
        page_title="DataSET - FIFA 2023",
        page_icon="chart_with_upwards_trend",
        layout="wide",
    )
st.sidebar.write(" # FIFA23 OFICIAL DATASET! ")
st.sidebar.caption(" ### Estatiscas de Jogadores ###")


df = pd.read_csv('data/FIFA23_official_data.csv', index_col=0)


#Selecionando todos os Clubes do data
clubes = df['Club'].value_counts().index
club = st.sidebar.selectbox('Clubes', clubes)

#Filtrando Jogaodores pelo Clube correspondente
df_jogadores = df[df['Club'] == club]
jogadores = df_jogadores['Name'].value_counts().index
jogador = st.sidebar.selectbox('Jogadores', jogadores)

#montando a estaticas dos jogadores pelo filtro de cada jogador.
jogador_estatistica = df[df['Name'] == jogador].iloc[0]

st.title(jogador_estatistica['Name'])
st.image(jogador_estatistica['Photo'])



col1,col2,col3 = st.columns(3)
col1.markdown(f"**Nacionalidade :** {jogador_estatistica['Nationality']}")

col2.image(jogador_estatistica['Flag'])


col1,col2,col3= st.columns(3)
col1.markdown(f"**Clube:** {jogador_estatistica['Club']}")
col2.image(jogador_estatistica['Club Logo'])





col1,col2,col3,col4 = st.columns(4)

col1.markdown(f"**Idade:** {jogador_estatistica['Age']}")
col2.markdown(f"**Altura:** {jogador_estatistica['Height']}")
col3.markdown(f"**Peso:** {jogador_estatistica['Weight']}")

st.divider()
st.subheader(f"**Overall:** {jogador_estatistica['Overall']}")
st.progress(int(jogador_estatistica['Overall']))


col1,col2,col3,col4 = st.columns(4)
col1.metric(label="Valor do Mercado", value= jogador_estatistica['Value'])
col2.metric(label="Remuneração Semanal", value= jogador_estatistica['Wage'])
col3.metric(label="Cláusula de Recisão", value= jogador_estatistica['Release Clause'])

