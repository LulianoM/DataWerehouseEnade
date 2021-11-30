import sqlite3

bd_connection = sqlite3.connect("ENADE.db")

cursor = bd_connection.cursor()

sql_script = open(
    "/Users/lulianom/Documents/Codes/Data-Warehouse-2021-1/ENADE/2.ModelagemDimensional/SCRIPT_BD_ENADE.sql"
)

sql_str = sql_script.read()

cursor.executescript(sql_str)

bd_connection.commit()

bd_connection.close()
