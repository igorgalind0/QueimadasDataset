🔥 Monitoramento de Queimadas
📌 Sobre o Projeto
Este projeto tem como objetivo o monitoramento e análise de ocorrências de queimadas no Brasil, utilizando um dataset público e detalhado da plataforma Base dos Dados. A proposta envolve a aplicação de técnicas de análise de dados para identificar padrões e tendências, auxiliando na mitigação de incêndios florestais e na preservação ambiental.
📂 Base de Dados
📊 Origem dos Dados
Os dados utilizados foram obtidos do Instituto Nacional de Pesquisas Espaciais (INPE), garantindo credibilidade e precisão nas análises. Este dataset abrange um período extenso, de 2003 a 2025, permitindo uma compreensão ampla do fenômeno das queimadas no Brasil.
📝 Formato dos Dados
- Formato: CSV
- Principais colunas:
- Data: Indica a data específica do foco de queimada.
- Estado: Estado brasileiro afetado pela queimada.
- Município: Município onde o foco de queimada foi detectado.
- Focos: Quantidade proporcional de queimadas registradas na região.
⚙️ Pré-processamento Realizado
Inicialmente, foi identificado um impacto na performance ao carregar o dataset completo. Para otimizar o desempenho e a fluidez do projeto, foi aplicado um filtro, utilizando apenas os dados referentes ao ano de 2024. Com essa abordagem, conseguimos:
- Melhorar significativamente a execução da aplicação.
- Reduzir o tempo de processamento.
- Facilitar a análise de um período temporal relevante.
🏆 Objetivo do Projeto
O projeto tem como propósito:
- Analisar padrões e tendências das queimadas em diferentes biomas e regiões.
- Desenvolver métodos de mitigação para preservar a fauna e flora.
- Reduzir emissões de gases poluentes, contribuindo para a diminuição dos efeitos do aquecimento global.
🚀 Ferramentas e Tecnologias Utilizadas
🛠️ Linguagem e Frameworks
- Python
- CustomTkinter
- VSCode
- GitHub
- SQLite
- Pandas
- Plotly
🔬 Metodologia
O desenvolvimento segue o modelo Desenvolvimento Rápido de Aplicações (RAD), permitindo:
- Resposta ágil às mudanças e necessidades do monitoramento.
- Prototipagem contínua, garantindo validação rápida por especialistas.
- Flexibilidade e adaptabilidade, ajustando-se a novos requisitos e dados.
- Geração rápida de insights, facilitando tomadas de decisão eficientes.
⚡ Como Rodar o Projeto
- Clone o repositório:
git clone <URL_DO_REPOSITÓRIO>
- Instale as dependências:
pip install -r requirements.txt
- Execute os scripts de análise:
python src/main.py
- Visualize os relatórios gerados na pasta outputs.
📸 Imagens e Demonstrações
Inclua aqui capturas de tela ou gráficos gerados pelo sistema.
📑 Relatório do Projeto
O relatório completo do projeto pode ser acessado em relatorio.pdf.
