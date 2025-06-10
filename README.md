# 🔥 Monitoramento de Queimadas

## 📌 Sobre o Projeto

Este projeto tem como objetivo o monitoramento e análise de ocorrências de queimadas no Brasil, utilizando um dataset público e detalhado da plataforma **Base dos Dados**. A proposta envolve a aplicação de técnicas de análise de dados para identificar padrões e tendências, auxiliando na mitigação de incêndios florestais e na preservação ambiental.

## 📂 Base de Dados

### 📊 Origem dos Dados
Os dados utilizados foram obtidos do **Instituto Nacional de Pesquisas Espaciais (INPE)**, garantindo credibilidade e precisão nas análises. Este dataset abrange um período extenso, de **2003 a 2025**, permitindo uma compreensão ampla do fenômeno das queimadas no Brasil.

### 📝 Formato dos Dados
- **Formato**: CSV
- **Principais colunas**:
  - **Data**: Indica a data específica do foco de queimada.
  - **Estado**: Estado brasileiro afetado pela queimada.
  - **Município**: Município onde o foco de queimada foi detectado.
  - **Focos**: Quantidade proporcional de queimadas registradas na região.

### ⚙️ Pré-processamento Realizado
Inicialmente, foi identificado um impacto na performance ao carregar o dataset completo. Para otimizar o desempenho e a fluidez do projeto, foi aplicado um filtro, utilizando apenas os **dados referentes ao ano de 2024**. Com essa abordagem, conseguimos:
- Melhorar significativamente a execução da aplicação.
- Reduzir o tempo de processamento.
- Facilitar a análise de um período temporal relevante.

## 🏆 Objetivo do Projeto

O projeto tem como propósito:
- **Analisar padrões e tendências das queimadas** em diferentes biomas e regiões.
- **Desenvolver métodos de mitigação** para preservar a fauna e flora.
- **Reduzir emissões de gases poluentes**, contribuindo para a diminuição dos efeitos do aquecimento global.

## 🚀 Ferramentas e Tecnologias Utilizadas

### 🛠️ Linguagem e Frameworks
- **Python**
- **CustomTkinter**
- **VSCode**
- **GitHub**
- **SQLite**
- **Pandas**
- **Plotly**

### 🔬 Metodologia
O desenvolvimento segue o modelo **Desenvolvimento Rápido de Aplicações (RAD)**, permitindo:
- **Resposta ágil** às mudanças e necessidades do monitoramento.
- **Prototipagem contínua**, garantindo validação rápida por especialistas.
- **Flexibilidade e adaptabilidade**, ajustando-se a novos requisitos e dados.
- **Geração rápida de insights**, facilitando tomadas de decisão eficientes.

# 🚀 Como Executar o Sistema de Monitoramento de Queimadas

Siga os passos abaixo para rodar o sistema localmente:

---

## 1️⃣ Clone o Repositório

```bash
git clone https://github.com/seu-usuario/queimadados.git
cd queimadados
```

---

## 2️⃣ Instale as Dependências

Certifique-se de ter o Python 3.8 ou superior instalado.  
Depois, instale as bibliotecas necessárias com:

```bash
pip install pandas matplotlib customtkinter plotly pillow
```

---

## 3️⃣ Execute o Sistema

Na raiz do projeto, execute o arquivo principal:

```bash
python app.py
```

---

## 4️⃣ Faça Login

- **Usuário:** `admin`  
- **Senha:** `1234`

Após o login, você poderá acessar a interface completa com filtros, tabela de dados, exportações, gráficos e mapa de calor.

---
### 🖼️ Capturas de Tela do Projeto


Tela de Login![telaLogin](https://github.com/user-attachments/assets/6441eead-0e8a-45ff-9fad-60b6193111ea)

Página Inicial![PaginaInicial](https://github.com/user-attachments/assets/b900761d-312e-45f7-bab1-d87ed1e843b9)

Consulta![Consulta](https://github.com/user-attachments/assets/391d5c18-f615-4fad-8a7a-461edf3d16da)

Editar Registro![ButtonEdit](https://github.com/user-attachments/assets/327c467b-8a2d-45e8-bb9c-22718683aa8e)

Gráfico![Grafico](https://github.com/user-attachments/assets/822f23e7-c9d8-413e-81f4-5ad6cc8e3e71)

Mapa de Calor![MapaDeCalor](https://github.com/user-attachments/assets/7a3870cc-c82b-4ec8-8c63-3af3bd3e0985)

### 📄 Relatório do Projeto

[📥 Clique aqui para visualizar ou baixar o relatório em PDF](https://github.com/Users/mathe/OneDrive/Desktop/DatasetQueimadas/Relat%C3%B3rio.pdf)
