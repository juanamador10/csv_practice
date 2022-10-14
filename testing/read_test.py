import pandas as pd
import mariadb

# Import CSV
data = pd.data = pd.read_csv ('codigos_postales.csv', encoding='latin-1')
df = pd.DataFrame(data)

# Connect to SQL Server
conn = mariadb.connect(user='root', 
                               password='', 
                               host='localhost', 
                               database='csvdatabase')
cursor = conn.cursor()

# Create Table
cursor.execute('''CREATE TABLE IF NOT EXISTS codigos_postales (
        d_codigo int(8),
        d_asenta varchar(45),
        d_tipo_asenta varchar(25),
        D_mnpio varchar(20),
        d_estado varchar(20),
        d_ciudad varchar(45),
        d_CP int(8),
        c_estado int(8),
        c_oficina int(8),
        c_CP int(8),
        c_tipo_asenta int(5),
        c_mnpio int(8),
        id_asenta_cpcons int(8),
        d_zona varchar(30),
        c_cve_ciudad int(5))''')

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
        INSERT INTO products (d_codigo, d_asenta, d_tipo_asenta,
                              D_mnpio, d_estado, d_ciudad,
                              d_CP, c_estado, c_oficina, c_CP,
                              c_tipo_asenta, c_mnpio, id_asenta_cpcons,
                              d_zona, c_cve_ciudad,
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        ''',
        row.d_codigo,
        row.d_asenta,
        row.d_tipo_asenta,
        row.D_mnpio,
        row.d_estado,
        row.d_ciudad,
        row.d_CP,
        row.c_estado,
        row.c_oficina,
        row.c_CP,
        row.c_tipo_asenta,
        row.c_mnpio,
        row.id_asenta_cpcons,
        row.d_zona,
        row.c_cve_ciudad,
    )
conn.commit()