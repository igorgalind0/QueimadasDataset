import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import matplotlib.pyplot as plt

# Nome do banco e da tabela
BANCO = 'queimadas.db'
TABELA = 'dados_queimadas'

# Conexão com o banco
def conectar():
    return sqlite3.connect(BANCO)

# Funções principais
def consultar():
    estado = entry_estado.get().strip().upper()
    ano = entry_ano.get().strip()

    query = f"SELECT * FROM {TABELA} WHERE 1=1"
    params = []
    if estado:
        query += " AND estado = ?"
        params.append(estado)
    if ano:
        query += " AND ano = ?"
        params.append(ano)

    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(query, params)
        resultados = cursor.fetchall()
        conn.close()

        tree.delete(*tree.get_children())
        for linha in resultados:
            tree.insert('', 'end', values=linha)
    except Exception as e:
        messagebox.showerror("Erro", str(e))

def comparar():
    ano1 = entry_ano.get().strip()
    ano2 = entry_ano_comparar.get().strip()
    estado = entry_estado.get().strip().upper()

    if not (ano1 and ano2):
        messagebox.showwarning("Atenção", "Informe os dois anos para comparar.")
        return

    query = f"""
    SELECT ano, estado, COUNT(*) as total_queimadas
    FROM {TABELA}
    WHERE ano IN (?, ?)
    """
    params = [ano1, ano2]

    if estado:
        query += " AND estado = ?"
        params.append(estado)

    query += " GROUP BY ano, estado ORDER BY ano"

    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(query, params)
        resultados = cursor.fetchall()
        conn.close()

        tree.delete(*tree.get_children())
        for linha in resultados:
            tree.insert('', 'end', values=linha)
    except Exception as e:
        messagebox.showerror("Erro", str(e))

def inserir():
    try:
        dados = [entrys[col].get() for col in colunas]
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(f"""
            INSERT INTO {TABELA} ({','.join(colunas)})
            VALUES ({','.join(['?'] * len(colunas))})
        """, dados)
        conn.commit()
        conn.close()
        consultar()
    except Exception as e:
        messagebox.showerror("Erro", str(e))

def atualizar():
    item = tree.focus()
    if not item:
        messagebox.showwarning("Atenção", "Selecione um registro para atualizar.")
        return
    try:
        dados = [entrys[col].get() for col in colunas]
        selecionado = tree.item(item)['values']
        condicoes = " AND ".join([f"{col} = ?" for col in colunas])
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(f"""
            UPDATE {TABELA}
            SET {', '.join([f"{col} = ?" for col in colunas])}
            WHERE {condicoes}
        """, dados + selecionado)
        conn.commit()
        conn.close()
        consultar()
    except Exception as e:
        messagebox.showerror("Erro", str(e))

def deletar():
    item = tree.focus()
    if not item:
        messagebox.showwarning("Atenção", "Selecione um registro para deletar.")
        return
    try:
        valores = tree.item(item)['values']
        condicoes = " AND ".join([f"{col} = ?" for col in colunas])
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {TABELA} WHERE {condicoes}", valores)
        conn.commit()
        conn.close()
        consultar()
    except Exception as e:
        messagebox.showerror("Erro", str(e))

def gerar_grafico():
    ano = entry_ano.get().strip()
    if not ano:
        messagebox.showwarning("Aviso", "Informe o ano para gerar o gráfico.")
        return

    query = f"""
    SELECT estado, COUNT(*) as total
    FROM {TABELA}
    WHERE ano = ?
    GROUP BY estado
    ORDER BY total DESC
    """
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(query, (ano,))
        dados = cursor.fetchall()
        conn.close()

        estados = [linha[0] for linha in dados]
        totais = [linha[1] for linha in dados]

        plt.figure(figsize=(10, 6))
        plt.bar(estados, totais, color='orange')
        plt.xlabel("Estado")
        plt.ylabel("Queimadas")
        plt.title(f"Total de Queimadas por Estado - {ano}")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        messagebox.showerror("Erro", str(e))

# Layout da janela principal
janela = tk.Tk()
janela.title("Consulta de Queimadas")
janela.geometry("1000x700")

# Filtros
frame_filtros = ttk.LabelFrame(janela, text="Filtros")
frame_filtros.pack(fill="x", padx=10, pady=5)

ttk.Label(frame_filtros, text="Estado:").grid(row=0, column=0, padx=5, pady=5)
entry_estado = ttk.Entry(frame_filtros)
entry_estado.grid(row=0, column=1)

ttk.Label(frame_filtros, text="Ano:").grid(row=0, column=2)
entry_ano = ttk.Entry(frame_filtros)
entry_ano.grid(row=0, column=3)

ttk.Label(frame_filtros, text="Comparar com ano:").grid(row=0, column=4)
entry_ano_comparar = ttk.Entry(frame_filtros)
entry_ano_comparar.grid(row=0, column=5)

ttk.Button(frame_filtros, text="Consultar", command=consultar).grid(row=1, column=0, padx=5, pady=10)
ttk.Button(frame_filtros, text="Comparar Anos", command=comparar).grid(row=1, column=1)
ttk.Button(frame_filtros, text="Gerar Gráfico", command=gerar_grafico).grid(row=1, column=2)

# Tabela de visualização
tree_frame = ttk.Frame(janela)
tree_frame.pack(fill="both", expand=True, padx=10, pady=10)

colunas = ("ano", "estado", "mes", "municipio", "bioma", "diasemchuva", "precipitacao", "riscofogo", "latitude", "longitude")
tree = ttk.Treeview(tree_frame, columns=colunas, show='headings')
for col in colunas:
    tree.heading(col, text=col.upper())
    tree.column(col, width=90)
tree.pack(fill="both", expand=True)

# Entradas para edição/inserção
frame_edit = ttk.LabelFrame(janela, text="Editar/Inserir Registro")
frame_edit.pack(fill="x", padx=10, pady=10)

entrys = {}
for idx, col in enumerate(colunas):
    ttk.Label(frame_edit, text=col.upper()).grid(row=0, column=idx, padx=5)
    e = ttk.Entry(frame_edit, width=10)
    e.grid(row=1, column=idx, padx=5)
    entrys[col] = e

ttk.Button(frame_edit, text="Inserir", command=inserir).grid(row=2, column=0, pady=10)
ttk.Button(frame_edit, text="Atualizar", command=atualizar).grid(row=2, column=1)
ttk.Button(frame_edit, text="Deletar", command=deletar).grid(row=2, column=2)

# Rodapé
ttk.Label(janela, text="Projeto de Análise de Queimadas no Brasil", anchor="center").pack(pady=5)

consultar()
janela.mainloop()
