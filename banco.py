import sqlite3

BANCO = 'queimadas.db'
TABELA = 'dados_queimadas'

# Cria conexão com o banco (arquivo local)
conn = sqlite3.connect(BANCO)
cursor = conn.cursor()

# Cria tabela (se não existir)
cursor.execute(f'''
CREATE TABLE IF NOT EXISTS {TABELA} (
    ano TEXT,
    estado TEXT,
    mes TEXT,
    municipio TEXT,
    bioma TEXT,
    diasemchuva INTEGER,
    precipitacao REAL,
    riscofogo INTEGER,
    latitude REAL,
    longitude REAL
)
''')

# Dados de exemplo
dados = [
    ('2020', 'SP', '01', 'São Paulo', 'Amazônia', 10, 20.5, 3, -23.55, -46.63),
    ('2020', 'MG', '01', 'Belo Horizonte', 'Cerrado', 15, 5.0, 2, -19.92, -43.94),
    ('2021', 'SP', '02', 'Campinas', 'Mata Atlântica', 5, 30.0, 1, -22.90, -47.06),
    ('2021', 'RJ', '03', 'Rio de Janeiro', 'Mata Atlântica', 7, 12.3, 4, -22.90, -43.21),
    ('2022', 'BA', '01', 'Salvador', 'Caatinga', 20, 0.0, 5, -12.97, -38.51),
    ('2022', 'SP', '04', 'Sorocaba', 'Cerrado', 8, 22.1, 3, -23.50, -47.46),
]

# Insere dados (limpando antes para não duplicar)
cursor.execute(f'DELETE FROM {TABELA}')
cursor.executemany(f'INSERT INTO {TABELA} VALUES (?,?,?,?,?,?,?,?,?,?)', dados)

conn.commit()
conn.close()

print("Banco criado e dados inseridos com sucesso!")
