import pandas as pd
import matplotlib.pyplot as plt
import customtkinter as ctk
from tkinter import messagebox, ttk

# Configura o tema do customtkinter
ctk.set_appearance_mode("System")  # "Dark" ou "Light" ou "System"
ctk.set_default_color_theme("blue")  # blue, dark-blue, green

# Usuário e senha válidos (exemplo)
USUARIO_VALIDO = "admin"
SENHA_VALIDA = "1234"

# --- Carregar CSV ---
df = pd.read_csv('focos_br_todos-sats_2024.csv', parse_dates=['data_pas'], nrows=100000)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
df['data_pas'] = pd.to_datetime(df['data_pas'], errors='coerce')

df_atual = df.copy()

def validar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    if usuario == USUARIO_VALIDO and senha == SENHA_VALIDA:
        messagebox.showinfo("Login", "Login efetuado com sucesso!")
        montar_interface_principal()
    else:
        messagebox.showerror("Erro", "Usuário ou senha inválidos. Tente novamente.")
        entry_senha.delete(0, ctk.END)
        entry_usuario.focus_set()

def montar_interface_principal():
    # Limpa a janela
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Consulta de Queimadas - 2024")
    root.geometry("1000x650")
    root.configure(bg=ctk.ThemeManager.theme["CTk"]["fg_color"])

    # Frame topo
    frame_top = ctk.CTkFrame(root)
    frame_top.pack(pady=10, padx=10, fill="x")

    label_filtro = ctk.CTkLabel(frame_top, text="Filtrar por Estado:", font=ctk.CTkFont(size=14))
    label_filtro.pack(side="left", padx=5)

    global combo_uf
    ufs = ['Todos'] + sorted(df['estado'].unique())
    combo_uf = ctk.CTkComboBox(frame_top, values=ufs, width=180, font=ctk.CTkFont(size=13))
    combo_uf.set("Todos")
    combo_uf.pack(side="left")
    combo_uf.configure(command=filtrar_uf)  # CORREÇÃO AQUI

    btn_atualizar = ctk.CTkButton(frame_top, text="Editar Registro", width=140, command=editar_linha)
    btn_atualizar.pack(side="left", padx=10)
    criar_tooltip(btn_atualizar, "Editar a linha selecionada")

    btn_excluir = ctk.CTkButton(frame_top, text="Excluir Registro(s)", fg_color="#f44336", hover_color="#e53935", width=140, command=excluir_linhas)
    btn_excluir.pack(side="left", padx=10)
    criar_tooltip(btn_excluir, "Excluir as linhas selecionadas")

    btn_grafico = ctk.CTkButton(frame_top, text="Gerar Gráfico", fg_color="#4caf50", hover_color="#43a047", width=140, command=gerar_grafico)
    btn_grafico.pack(side="left", padx=10)
    criar_tooltip(btn_grafico, "Gerar gráfico comparativo dos itens selecionados")

    # Frame tabela
    frame_tabela = ctk.CTkFrame(root)
    frame_tabela.pack(padx=10, pady=10, fill="both", expand=True)

    global tree
    colunas = ("Data", "Estado", "Município", "Focos (FRP)")
    tree = ttk.Treeview(frame_tabela, columns=colunas, show="headings", selectmode="extended")
    for col in colunas:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=220)

    scroll_y = ctk.CTkScrollbar(frame_tabela, orientation="vertical", command=tree.yview)
    scroll_x = ctk.CTkScrollbar(frame_tabela, orientation="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

    scroll_y.pack(side="right", fill="y")
    scroll_x.pack(side="bottom", fill="x")
    tree.pack(fill="both", expand=True)

    atualizar_tabela()

def atualizar_tabela(filtro=None):
    global df_atual
    for row in tree.get_children():
        tree.delete(row)
    df_filtrado = df
    if filtro and filtro != 'Todos':
        df_filtrado = df[df['estado'] == filtro]
    df_atual = df_filtrado
    for row in df_filtrado.itertuples():
        data_str = row.data_pas.date().isoformat() if pd.notnull(row.data_pas) else 'Data Inválida'
        tree.insert("", "end", iid=row.Index, values=(data_str, row.estado, row.municipio, row.frp))

def filtrar_uf(valor_selecionado):
    uf = valor_selecionado
    if uf == 'Todos':
        atualizar_tabela()
    else:
        atualizar_tabela(filtro=uf)

def gerar_grafico():
    selecionados = tree.selection()
    if len(selecionados) < 2:
        messagebox.showwarning("Seleção insuficiente", "Selecione pelo menos duas linhas para comparar.")
        return
    indices = [int(iid) for iid in selecionados]
    dados = df.loc[indices]

    municipios = dados['municipio']
    focos = dados['frp']

    plt.figure(figsize=(10,6))
    plt.bar(municipios, focos, color='red')
    plt.title("Comparação de fogo (FRP) entre municípios")
    plt.ylabel("Fire Radiative Power (FRP)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

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

# --- Interface inicial: janela de login ---
root = ctk.CTk()
root.title("Login")
root.geometry("320x280")
root.resizable(False, False)

label_user = ctk.CTkLabel(root, text="Usuário:", font=ctk.CTkFont(size=14))
label_user.pack(pady=(30, 5))
entry_usuario = ctk.CTkEntry(root, width=220)
entry_usuario.pack()

label_pass = ctk.CTkLabel(root, text="Senha:", font=ctk.CTkFont(size=14))
label_pass.pack(pady=(20, 5))
entry_senha = ctk.CTkEntry(root, show="*", width=220)
entry_senha.pack()

btn_entrar = ctk.CTkButton(root, text="Entrar", width=120, command=validar_login)
btn_entrar.pack(pady=30)

entry_usuario.focus_set()
root.mainloop()
