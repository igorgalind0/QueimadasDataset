#--------- Adicionando Bibliotecas ----------
import pandas as pd
import matplotlib.pyplot as plt
import customtkinter as ctk
from tkinter import messagebox, ttk, filedialog
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image, ImageTk

root = ctk.CTk()

#Definindo usuário e senha de login
USUARIO_VALIDO = "admin"
SENHA_VALIDA = "1234"

#Definindo o Banco de Dados
df = pd.read_csv('focos_br_todos-sats_2024.csv', parse_dates=['data_pas'], nrows=100000)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
df['data_pas'] = pd.to_datetime(df['data_pas'], errors='coerce')
df_atual = df.copy()

#Variável global para manter o filtro atual do município
filtro_municipio = ""

#Função para validar o Login
def validar_login(root):
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    if usuario == USUARIO_VALIDO and senha == SENHA_VALIDA:
        messagebox.showinfo("Login", "Login efetuado com sucesso!")
        for widget in root.winfo_children():
            widget.destroy()
        pagina_intro(root)
    else:
        messagebox.showerror("Erro", "Usuário ou senha inválidos. Tente novamente.")
        entry_senha.delete(0, ctk.END)
        entry_usuario.focus_set()

#Criando Tela de Login
def tela_login(root):
    for widget in root.winfo_children():
        widget.destroy()
    
    global entry_usuario, entry_senha
    root.title("Login")
    root.geometry("700x400")
    root.resizable(True, True)

    bg_color = "#242424"
    root.configure(bg=bg_color)

    container = ctk.CTkFrame(root, fg_color=bg_color)
    container.place(relx=0.5, rely=0.5, anchor="center")

    frame_principal = ctk.CTkFrame(container, fg_color=bg_color, border_width=0)
    frame_principal.pack()

    frame_esquerda = ctk.CTkFrame(frame_principal, fg_color=bg_color, border_width=0)
    frame_esquerda.grid(row=0, column=0, sticky="nsew", padx=(0, 100))

    frame_direita = ctk.CTkFrame(frame_principal, fg_color=bg_color, border_width=0)
    frame_direita.grid(row=0, column=1, sticky="nsew")

    frame_principal.grid_columnconfigure(0, weight=1)
    frame_principal.grid_columnconfigure(1, weight=1)
    frame_principal.grid_rowconfigure(0, weight=1)

    logo_img = ctk.CTkImage(Image.open("logo.png"), size=(106, 32))

    label_logo = ctk.CTkLabel(frame_esquerda, image=logo_img, text="")
    label_logo.pack(anchor="w", pady=(0, 20))

    label_bem_vindos = ctk.CTkLabel(frame_esquerda, text="Bem vindos", font=ctk.CTkFont(size=20), fg_color=bg_color)
    label_bem_vindos.pack(anchor="w")

    label_ao_sistema = ctk.CTkLabel(
        frame_esquerda,
        text="Ao Sistema",
        font=ctk.CTkFont(family="Arial Black", size=32),
        text_color="#1F6AA5",
        fg_color=bg_color
    )
    label_ao_sistema.pack(anchor="w", pady=(0, 10))

    label_descricao = ctk.CTkLabel(
        frame_esquerda,
        text="Sistema de monitoramento de queimadas através de banco de dados atualizado.",
        font=ctk.CTkFont(size=16),
        wraplength=250,
        justify="left",
        fg_color=bg_color
    )
    label_descricao.pack(anchor="w", pady=(0, 20))

    label_instrucao = ctk.CTkLabel(
        frame_esquerda,
        text="Faça seu login no sistema.",
        font=ctk.CTkFont(size=16),
        justify="left",
        fg_color=bg_color
    )
    label_instrucao.pack(anchor="w")

    label_user = ctk.CTkLabel(frame_direita, text="Usuário:", font=ctk.CTkFont(size=16), fg_color=bg_color)
    label_user.pack(pady=(30, 5))

    entry_usuario = ctk.CTkEntry(frame_direita, width=220)
    entry_usuario.pack()

    label_pass = ctk.CTkLabel(frame_direita, text="Senha:", font=ctk.CTkFont(size=16), fg_color=bg_color)
    label_pass.pack(pady=(20, 5))

    entry_senha = ctk.CTkEntry(frame_direita, show="*", width=220)
    entry_senha.pack()

    btn_entrar = ctk.CTkButton(frame_direita, text="Entrar", width=120, command=lambda: validar_login(root))
    btn_entrar.pack(pady=30)

    entry_usuario.focus_set()

#Executa a tela de login
tela_login(root)

#-----------------------------------------

#Criando tela página introdução
def pagina_intro(root):
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Página Inicial")
    root.geometry("1280x720")
    root.resizable(True, True)

    bg_color = "#242424"
    root.configure(bg=bg_color)

    # ------------ Seção 1 ------------
    # Container centralizador
    container1 = ctk.CTkFrame(root, fg_color=bg_color)
    container1.pack(pady=40, padx=20, fill="x")

    frame_principal1 = ctk.CTkFrame(container1, fg_color=bg_color)
    frame_principal1.pack()

    # Esquerda
    frame_esquerda1 = ctk.CTkFrame(frame_principal1, fg_color=bg_color)
    frame_esquerda1.grid(row=0, column=0, sticky="nsew", padx=(0, 60))

    # Logo
    try:
        logo_img = ctk.CTkImage(Image.open("logo.png"), size=(106, 32))
        label_logo = ctk.CTkLabel(frame_esquerda1, image=logo_img, text="")
        label_logo.pack(anchor="w", pady=(0, 20))
    except:
        ctk.CTkLabel(frame_esquerda1, text="[LOGO AQUI]", font=ctk.CTkFont(size=16)).pack(anchor="w")

    # Título
    titulo1 = ctk.CTkLabel(frame_esquerda1,
        text="O que é o QueimaDados",
        font=ctk.CTkFont(size=28, family="Arial Black"),
        wraplength=500,
        justify="left",
        text_color="#1F6AA5"
    )
    titulo1.pack(anchor="w", pady=(0, 20))

    # Parágrafo
    texto1 = ctk.CTkLabel(frame_esquerda1,
        text="O QueimaDados é um sistema interativo para consultar, comparar e gerenciar dados de queimadas. Com poucos cliques, você acessa mapas, gráficos e relatórios para entender melhor o cenário ambiental do país.",
        font=ctk.CTkFont(size=16),
        wraplength=500,
        justify="left"
    )
    texto1.pack(anchor="w")

    # Direita (Imagem)
    frame_direita1 = ctk.CTkFrame(frame_principal1, fg_color=bg_color)
    frame_direita1.grid(row=0, column=1, sticky="nsew")

    try:
        imagem1 = ctk.CTkImage(Image.open("queimadas1.png"), size=(400, 250))
        label_img1 = ctk.CTkLabel(frame_direita1, image=imagem1, text="")
        label_img1.pack()
    except:
        ctk.CTkLabel(frame_direita1, text="[IMAGEM]", font=ctk.CTkFont(size=16)).pack()

    # ------------ Seção 2 ------------

    container2 = ctk.CTkFrame(root, fg_color=bg_color)
    container2.pack(pady=40, padx=20, fill="x")

    frame_principal2 = ctk.CTkFrame(container2, fg_color=bg_color)
    frame_principal2.pack()

    # Esquerda (Imagem)
    frame_esquerda2 = ctk.CTkFrame(frame_principal2, fg_color=bg_color)
    frame_esquerda2.grid(row=0, column=0, sticky="nsew", padx=(0, 60))

    try:
        imagem2 = ctk.CTkImage(Image.open("queimadas2.png"), size=(400, 250))
        label_img2 = ctk.CTkLabel(frame_esquerda2, image=imagem2, text="")
        label_img2.pack()
    except:
        ctk.CTkLabel(frame_esquerda2, text="[IMAGEM]", font=ctk.CTkFont(size=16)).pack()

    # Direita (Texto)
    frame_direita2 = ctk.CTkFrame(frame_principal2, fg_color=bg_color)
    frame_direita2.grid(row=0, column=1, sticky="nsew")

    titulo2 = ctk.CTkLabel(frame_direita2,
        text="QueimaDados: Monitoramento das queimadas em 2024",
        font=ctk.CTkFont(size=28, family="Arial Black"),
        wraplength=500,
        justify="left",
        text_color="#1F6AA5"
    )
    titulo2.pack(anchor="w", pady=(0, 20))

    texto2 = ctk.CTkLabel(frame_direita2,
        text="Acompanhe os focos de queimadas no Brasil em tempo real. Com o QueimaDados, você visualiza mapas de calor, gráficos comparativos e acessa informações atualizadas sobre os incêndios que marcaram 2024.",
        font=ctk.CTkFont(size=16),
        wraplength=500,
        justify="left"
    )
    texto2.pack(anchor="w")

    frame_botoes_lado_a_lado = ctk.CTkFrame(frame_direita2, fg_color="transparent")
    frame_botoes_lado_a_lado.pack(anchor="w", pady=(30, 0))

    # Botão Ver dados
    botao_ver_dados = ctk.CTkButton(
        frame_botoes_lado_a_lado,
        text="Ver dados",
        width=140,
        height=40,
        font=ctk.CTkFont(size=16),
        fg_color="#1F6AA5",
        hover_color="#155A8A",
        text_color="white",
        corner_radius=8,
        command=lambda: pagina_principal(root)
    )
    botao_ver_dados.pack(side="left", padx=(0, 10))

    # Botão Voltar
    botao_voltar = ctk.CTkButton(
        frame_botoes_lado_a_lado,
        text="Voltar",
        width=140,
        height=40,
        font=ctk.CTkFont(size=16),
        fg_color="#757575",
        hover_color="#616161",
        text_color="white",
        corner_radius=8,
        command=lambda: tela_login(root)
    )
    botao_voltar.pack(side="left")
#-----------------------------------

#Criando página principal (dados)
def pagina_principal(root):
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Consulta de Queimadas - 2024")
    root.geometry("1280x720")
    root.configure(bg=ctk.ThemeManager.theme["CTk"]["fg_color"])

    # Frame topo principal
    frame_top = ctk.CTkFrame(root)
    frame_top.pack(pady=10, padx=10, fill="x")

    # Frame linha 1 (filtros)
    frame_linha1 = ctk.CTkFrame(frame_top, fg_color="transparent")
    frame_linha1.pack(fill="x", pady=(0, 5))

    # Frame linha 2 (botões de ação)
    frame_linha2 = ctk.CTkFrame(frame_top, fg_color="transparent")
    frame_linha2.pack(fill="x")

    # Filtros - dentro da linha 1
    frame_filtros = ctk.CTkFrame(frame_linha1, fg_color="transparent")
    frame_filtros.pack(side="left", padx=5, pady=5)

    # Filtro Estado
    global combo_uf
    ufs = ['Todos'] + sorted(df['estado'].unique())
    label_filtro = ctk.CTkLabel(frame_filtros, text="Filtrar por Estado:", font=ctk.CTkFont(size=14))
    label_filtro.pack(side="left", padx=(0,5))
    combo_uf = ctk.CTkComboBox(frame_filtros, values=ufs, width=150, font=ctk.CTkFont(size=13))
    combo_uf.set("Todos")
    combo_uf.pack(side="left", padx=(0,15))
    combo_uf.configure(command=filtrar_uf)

    # Filtro Município
    global entry_municipio_filter
    label_muni = ctk.CTkLabel(frame_filtros, text="Filtrar por Município:", font=ctk.CTkFont(size=14))
    label_muni.pack(side="left", padx=(0,5))
    entry_municipio_filter = ctk.CTkEntry(frame_filtros, width=150, font=ctk.CTkFont(size=13))
    entry_municipio_filter.pack(side="left", padx=(0,15))
    entry_municipio_filter.bind("<KeyRelease>", lambda e: filtrar_municipio())

    # Botão resetar filtros
    btn_reset_filtros = ctk.CTkButton(frame_filtros, text="Resetar Filtros", width=130, command=resetar_filtros)
    btn_reset_filtros.pack(side="left")

    # Botões de ação - dentro da linha 2
    frame_botoes = ctk.CTkFrame(frame_linha2, fg_color="transparent")
    frame_botoes.pack(side="left", padx=5, pady=5)

    btn_atualizar = ctk.CTkButton(frame_botoes, text="Editar Registro", width=140, command=editar_linha)
    btn_atualizar.pack(side="left", padx=8)
    criar_tooltip(btn_atualizar, "Editar a linha selecionada")

    btn_excluir = ctk.CTkButton(frame_botoes, text="Excluir Registro(s)", fg_color="#f44336", hover_color="#e53935", width=140, command=excluir_linhas)
    btn_excluir.pack(side="left", padx=8)
    criar_tooltip(btn_excluir, "Excluir as linhas selecionadas")

    btn_grafico = ctk.CTkButton(frame_botoes, text="Gerar Gráfico", fg_color="#43ac47", hover_color="#43a047", width=140, command=gerar_grafico)
    btn_grafico.pack(side="left", padx=8)
    criar_tooltip(btn_grafico, "Gerar gráfico comparativo dos itens selecionados")

    btn_mapa_calor = ctk.CTkButton(frame_botoes, text="Mapa de Calor", fg_color="#ff9102", hover_color="#5c0b0b", width=140, command=gerar_mapa_calor)
    btn_mapa_calor.pack(side="left", padx=8)
    criar_tooltip(btn_mapa_calor, "Gerar mapa de calor")

    btn_exportar = ctk.CTkButton(frame_botoes, text="Exportar CSV", fg_color="#1976d2", hover_color="#0d47a1", width=140, command=exportar_csv)
    btn_exportar.pack(side="left", padx=8)
    criar_tooltip(btn_exportar, "Exportar dados filtrados para CSV")

    # Frame tabela
    frame_tabela = ctk.CTkFrame(root)
    frame_tabela.pack(padx=10, pady=10, fill="both", expand=True)

    global tree
    colunas = ("Data", "Estado", "Município", "Focos (FRP)")
    tree = ttk.Treeview(frame_tabela, columns=colunas, show="headings", selectmode="extended")
    for col in colunas:
        tree.heading(col, text=col, command=lambda c=col: ordenar_tabela(c, False))
        tree.column(col, anchor="center", width=250)

    scroll_y = ctk.CTkScrollbar(frame_tabela, orientation="vertical", command=tree.yview)
    scroll_x = ctk.CTkScrollbar(frame_tabela, orientation="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

    scroll_y.pack(side="right", fill="y")
    scroll_x.pack(side="bottom", fill="x")
    tree.pack(fill="both", expand=True)

    atualizar_tabela()

    btn_voltar = ctk.CTkButton(root, text="Voltar", width=120, fg_color="#757575", hover_color="#616161", command=lambda: pagina_intro(root))
    btn_voltar.pack(pady=(0, 15))
    criar_tooltip(btn_voltar, "Voltar para a tela de login")

#Função atualizar dados
def atualizar_tabela(filtro_estado=None, filtro_muni=None):
    global df_atual
    for row in tree.get_children():
        tree.delete(row)
    df_filtrado = df

    if filtro_estado and filtro_estado != 'Todos':
        df_filtrado = df_filtrado[df_filtrado['estado'] == filtro_estado]

    if filtro_muni:
        df_filtrado = df_filtrado[df_filtrado['municipio'].str.contains(filtro_muni, case=False, na=False)]

    df_atual = df_filtrado

    for row in df_filtrado.itertuples():
        data_str = row.data_pas.date().isoformat() if pd.notnull(row.data_pas) else 'Data Inválida'
        tree.insert("", "end", iid=row.Index, values=(data_str, row.estado, row.municipio, row.frp))

#Função filtrar estado
def filtrar_uf(valor_selecionado):
    global filtro_municipio
    filtro_uf = valor_selecionado
    muni = entry_municipio_filter.get().strip() if entry_municipio_filter else ""
    atualizar_tabela(filtro_estado=filtro_uf, filtro_muni=muni)

#Função filtrar município
def filtrar_municipio():
    global filtro_municipio
    filtro_municipio = entry_municipio_filter.get().strip()
    filtro_uf = combo_uf.get() if combo_uf else 'Todos'
    atualizar_tabela(filtro_estado=filtro_uf, filtro_muni=filtro_municipio)

#Função resetar filtros
def resetar_filtros():
    combo_uf.set("Todos")
    entry_municipio_filter.delete(0, ctk.END)
    atualizar_tabela()

#Função ordenar tabela
def ordenar_tabela(coluna, reverse):
    # Mapeia o nome da coluna para a coluna do DataFrame
    col_map = {
        "Data": "data_pas",
        "Estado": "estado",
        "Município": "municipio",
        "Focos (FRP)": "frp"
    }
    col_df = col_map.get(coluna, None)
    if not col_df:
        return

    global df_atual
    df_atual = df_atual.sort_values(by=col_df, ascending=not reverse)
    atualizar_tabela_simples(df_atual)

    # Alterna a ordem para próxima vez que clicar
    # Remonta os comandos dos cabeçalhos com o inverso
    for col in tree["columns"]:
        if col == coluna:
            tree.heading(col, command=lambda c=col, rev=not reverse: ordenar_tabela(c, rev))
        else:
            tree.heading(col, command=lambda c=col: ordenar_tabela(c, False))

#Função atualizar tabela simples
def atualizar_tabela_simples(df_filtrado):
    for row in tree.get_children():
        tree.delete(row)
    for row in df_filtrado.itertuples():
        data_str = row.data_pas.date().isoformat() if pd.notnull(row.data_pas) else 'Data Inválida'
        tree.insert("", "end", iid=row.Index, values=(data_str, row.estado, row.municipio, row.frp))

#Função exportar CSV
def exportar_csv():
    # Obter os itens selecionados na Treeview
    selecionados = tree.selection()
    if not selecionados:
        messagebox.showinfo("Nenhuma seleção", "Selecione pelo menos um registro para exportar.")
        return

    # Extrair os dados selecionados
    dados_selecionados = []
    for item in selecionados:
        valores = tree.item(item, 'values')
        dados_selecionados.append(valores)

    # Criar DataFrame com os dados selecionados
    df_selecionado = pd.DataFrame(dados_selecionados, columns=["Data", "Estado", "Município", "Focos (FRP)"])

    # Solicitar local para salvar o arquivo
    arquivo = filedialog.asksaveasfilename(defaultextension=".csv",
                                           filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
    if arquivo:
        try:
            df_selecionado.to_csv(arquivo, index=False)
            messagebox.showinfo("Sucesso", f"Arquivo salvo em:\n{arquivo}")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao salvar arquivo:\n{e}")

#Função Gerar Gráficos
def gerar_grafico():
    selecionados = tree.selection()
    if len(selecionados) < 2:
        messagebox.showwarning("Seleção insuficiente", "Selecione pelo menos duas linhas para comparar.")
        return

    indices = [int(iid) for iid in selecionados]
    dados = df.loc[indices]

    municipios = dados['municipio']
    focos = dados['frp']

    fig = go.Figure(data=[
        go.Bar(
            x=municipios,
            y=focos,
            marker_color='indianred',
            hovertemplate='<b>%{x}</b><br>FRP: %{y}<extra></extra>'
        )
    ])

    fig.update_layout(
        title="Comparação de Focos (FRP) entre Municípios",
        xaxis_title="Municípios",
        yaxis_title="Fire Radiative Power (FRP)",
        template="plotly_white",
        xaxis_tickangle=-45,
        height=600,
        width=1000
    )

    fig.show()

#Gerar mapa de calor
def gerar_mapa_calor():
    selecionados = tree.selection()
    if not selecionados:
        messagebox.showwarning("Nenhuma seleção", "Selecione pelo menos uma linha para visualizar o mapa de calor.")
        return

    indices = [int(iid) for iid in selecionados]
    dados = df.loc[indices]

    if 'latitude' not in dados.columns or 'longitude' not in dados.columns:
        messagebox.showerror("Erro de dados", "O arquivo CSV precisa conter as colunas 'latitude' e 'longitude'.")
        return

    # Filtra dados válidos (sem NaN)
    dados = dados.dropna(subset=['latitude', 'longitude', 'frp'])

    if dados.empty:
        messagebox.showerror("Erro de dados", "As linhas selecionadas não contêm coordenadas válidas.")
        return

    fig = px.density_mapbox(
        dados,
        lat='latitude',
        lon='longitude',
        z='frp',
        radius=20,
        center=dict(lat=dados['latitude'].mean(), lon=dados['longitude'].mean()),
        zoom=4,
        mapbox_style="open-street-map",
        color_continuous_scale="Hot",
        title="Mapa de Calor - FRP (Fire Radiative Power)"
    )

    fig.show()

#Função Excluir Registros
def excluir_linhas():
    selecionados = tree.selection()
    if not selecionados:
        messagebox.showinfo("Nenhuma seleção", "Selecione pelo menos uma linha para excluir.")
        return
    if messagebox.askyesno("Confirmar exclusão", f"Excluir {len(selecionados)} linha(s)?"):
        global df
        indices = [int(iid) for iid in selecionados]
        df = df.drop(indices)
        atualizar_tabela(combo_uf.get())
        messagebox.showinfo("Sucesso", "Linhas excluídas com sucesso!")

#Função Editar Registros
def editar_linha():
    selecionados = tree.selection()
    if len(selecionados) != 1:
        messagebox.showwarning("Seleção inválida", "Selecione exatamente uma linha para editar.")
        return
    idx = int(selecionados[0])
    linha = df.loc[idx]

    edit_win = ctk.CTkToplevel(root)
    edit_win.title("Editar Registro")
    edit_win.geometry("400x320")
    edit_win.transient(root)
    edit_win.grab_set()

    ctk.CTkLabel(edit_win, text="Data (AAAA-MM-DD):").pack(pady=5)
    entry_data = ctk.CTkEntry(edit_win)
    entry_data.pack()
    entry_data.insert(0, linha['data_pas'].date().isoformat() if pd.notnull(linha.data_pas) else '')

    ctk.CTkLabel(edit_win, text="Estado:").pack(pady=5)
    entry_estado = ctk.CTkEntry(edit_win)
    entry_estado.pack()
    entry_estado.insert(0, linha['estado'])

    ctk.CTkLabel(edit_win, text="Município:").pack(pady=5)
    entry_municipio = ctk.CTkEntry(edit_win)
    entry_municipio.pack()
    entry_municipio.insert(0, linha['municipio'])

    ctk.CTkLabel(edit_win, text="Focos (FRP):").pack(pady=5)
    entry_frp = ctk.CTkEntry(edit_win)
    entry_frp.pack()
    entry_frp.insert(0, str(linha['frp']))

    def salvar():
        try:
            nova_data = pd.to_datetime(entry_data.get(), errors='raise')
            novo_estado = entry_estado.get().strip()
            novo_municipio = entry_municipio.get().strip()
            novo_frp = float(entry_frp.get())

            if not novo_estado or not novo_municipio:
                raise ValueError("Estado e Município não podem estar vazios.")

            df.at[idx, 'data_pas'] = nova_data
            df.at[idx, 'estado'] = novo_estado
            df.at[idx, 'municipio'] = novo_municipio
            df.at[idx, 'frp'] = novo_frp

            atualizar_tabela(combo_uf.get())
            messagebox.showinfo("Sucesso", "Registro atualizado com sucesso!")
            edit_win.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar: {e}")

    btn_salvar = ctk.CTkButton(edit_win, text="Salvar", fg_color="#4caf50", hover_color="#43a047", command=salvar)
    btn_salvar.pack(pady=15)

#Função Criar Tooltip
def criar_tooltip(widget, texto):
    tip = ctk.CTkToplevel(widget)
    tip.withdraw()
    tip.overrideredirect(True)
    tip_label = ctk.CTkLabel(tip, text=texto, fg_color="#FFFFE0", text_color="black", corner_radius=5, font=ctk.CTkFont(size=10))

    def enter(event):
        x = event.x_root + 10
        y = event.y_root + 10
        tip.geometry(f"+{x}+{y}")
        tip.deiconify()

    def leave(event):
        tip.withdraw()

    widget.bind("<Enter>", enter)
    widget.bind("<Leave>", leave)
    tip_label.pack(padx=5, pady=2)

root.mainloop()