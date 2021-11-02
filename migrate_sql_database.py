import sqlite3
import pandas as pd
import tqdm



def migrate_values(filepath):
    conn = sqlite3.connect('dadosenade.db')
    cursor = conn.cursor()
    columns = ["NU_ANO", "CO_GRUPO", "CO_MODALIDADE", "CO_UF_CURSO", "CO_REGIÃO_CURSO", "NU_IDADE",
    "TP_SEXO", "CO_TURNO_GRADUCAO", "QE_I02"]
    df = pd.read_csv(filepath= filepath, sep= ";", usecols= columns)
    for row in tqdm(df):
        cursor.execute(f"""
        INSERT INTO TABELA FATO (NU_ANO, CO_GRUPO, CO_MODALIDADE, CO_UF_CURSO, CO_REGIÃO_CURSO, NU_IDADE,TP_SEXO, CO_TURNO_GRADUCAO, QE_I02)
        VALUES ({df["NU_ANO"][row]}, {df["CO_GRUPO"][row]}, {df["CO_MODALIDADE"][row]}, {df["CO_UF_CURSO"][row]}, {df["CO_REGIÃO_CURSO"][row]}, {df["NU_IDADE"][row]}, {df["TP_SEXO"][row]},{df["CO_TURNO_GRADUCAO"][row]}, {df["QE_I02"][row]})
        """)
        conn.commit()
    conn.close()

# gravando no bd
print("\n Migrando dados 2017\n")
migrate_values("DadosENADE/3.Dados/MICRODADOS_ENADE_2017.txt")
print("\n Migrando dados 2018\n")
migrate_values("DadosENADE/3.Dados/microdados_enade_2018.txt")
print("\n Migrando dados 2019\n")
migrate_values("DadosENADE/3.Dados/microdados_enade_2019.txt")


print('Dados inseridos com sucesso.')