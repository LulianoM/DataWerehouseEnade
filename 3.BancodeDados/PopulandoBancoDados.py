from sqlite3.dbapi2 import Cursor
import pandas as pd
import sqlite3

def inserirDados(caminho, colunas):
    conn = sqlite3.connect("ENADE.db")
    cursor = conn.cursor()

    df = pd.read_csv(caminho, sep=";", decimal=",", usecols= colunas)

    for row in range(len(df)):
        
        cursor.execute(f'''
        INSERT INTO instituicao (CO_IES, CO_CATEGAD)
        VALUES ({df["CO_IES"][row]},{df["CO_CATEGAD"][row]})
        ''')

        cursor.execute(f'''
        INSERT INTO curso (CO_CURSO, CO_GRUPO)
        VALUES ({df["CO_CURSO"][row]},{df["CO_GRUPO"][row]})
        ''')

        cursor.execute(f'''
        INSERT INTO localidade (CO_MUNIC_CURSO,CO_UF_CURSO,CO_REGIAO_CURSO)
        VALUES ({df['CO_MUNIC_CURSO'][row]},{df['CO_UF_CURSO'][row]},{df['CO_REGIAO_CURSO'][row]})
        ''')

        cursor.execute(f'''
        INSERT INTO percepcao_prova (tempo_gasto,Grau_FG,Grau_CE)
        VALUES ({df["CO_RS_I9"][row]},{df["CO_RS_I1"][row]},{df["CO_RS_I2"][row]})
        ''')

        cursor.execute(f'''
        INSERT INTO avaliacao_CE (NU_ITEM_OCE, DS_VT_GAB_OCE_FIN)
        VALUES ({df["NU_ITEM_OCE"][row]},{df["DS_VT_GAB_OCE_FIN"][row]})
        ''')
        
        cursor.execute(f'''
        INSERT INTO avaliacao_FG (NU_ITEM_OFG, DS_VT_GAB_OFG_FIN)
        VALUES ({df["NU_ITEM_OFG"][row]},{df["DS_VT_GAB_OFG_FIN"][row]})
        ''')

        cursor.execute(f'''
        INSERT INTO notas_fg (NT_FG)
        VALUES ({df["NT_FG"][row]})
        ''')

        cursor.execute(f'''
        INSERT INTO notas_ce (NT_CE)
        VALUES ({df["NT_CE"][row]})
        ''')

        cursor.execute(f'''
        INSERT INTO tipo_presenca (TP_PRES,TP_PR_GER)
        VALUES ({df["TP_PRES"][row]},{df["TP_PR_GER"][row]})
        ''')

        cursor.execute(f'''
        INSERT INTO info_estudante (NU_IDADE, TP_SEXO, ESTADO_CIVIL, RACA, NACIONALIDADE)
        VALUES ({df["NU_IDADE"][row]},{df["TP_SEXO"][row]},{df["QE_I01"][row]},{df["QE_I02"][row]},{df["QE_I03"][row]})
        ''')
        
        cursor.execute(f'''
        INSERT INTO tabela_fatos (NU_ANO, NOTA_GERAL)
        VALUES ({df["NU_ANO"][row]}, {df["NT_GER"][row]})
        ''')
        conn.commit()
    conn.close()

    print("Arquivo importado com sucesso")


columns = ["NU_ANO","CO_IES","CO_CATEGAD","CO_GRUPO","CO_CURSO","CO_MUNIC_CURSO","CO_UF_CURSO","CO_REGIAO_CURSO",
"NU_IDADE","TP_SEXO","NU_ITEM_OFG","NU_ITEM_OCE","DS_VT_GAB_OFG_FIN","DS_VT_GAB_OCE_FIN","TP_PRES",
"TP_PR_GER","NT_GER","NT_FG","NT_CE","CO_RS_I1","CO_RS_I2","CO_RS_I9","QE_I01","QE_I02","QE_I03"]

caminho_arquivo = ["DadosENADE/3.Dados/MICRODADOS_ENADE_2017.txt","DadosENADE/3.Dados/microdados_enade_2018.txt","DadosENADE/3.Dados/microdados_enade_2019.txt"]

for arq in caminho_arquivo:
    inserirDados(arq, columns)