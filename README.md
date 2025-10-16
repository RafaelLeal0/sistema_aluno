🎓 Sistema de Gestão de Alunos
https://img.shields.io/badge/Python-3.6%252B-blue
https://img.shields.io/badge/GUI-Tkinter-green
https://img.shields.io/badge/Data-Pandas-orange
https://img.shields.io/badge/License-MIT-lightgrey

Um sistema completo e intuitivo para cadastro, gerenciamento e relatórios de alunos desenvolvido em Python.

✨ Funcionalidades
Funcionalidade	Descrição
📝 Cadastro de Alunos	Formulário completo com validação de dados
📊 Visualização em Tabela	Interface organizada para visualizar todos os alunos
🔍 Filtros Inteligentes	Filtre alunos por nota mínima personalizada
💾 Persistência de Dados	Salve e carregue dados em arquivo CSV
📈 Relatórios Exportáveis	Gere relatórios filtrados em CSV
🚀 Começando
Pré-requisitos
Python 3.6 ou superior

Gerenciador de pacotes pip

Instalação Rápida
Instale as dependências:

bash
pip install pandas
Execute o sistema:

bash
python main.py
🖥️ Interface do Sistema
🎯 Layout Principal
text
┌─────────────────────────────────────────────────────────────┐
│                SISTEMA DE GESTÃO DE ALUNOS                  │
├───────────────┬─────────────────────────────────────────────┤
│                                                             │
│   📝 CADASTRAR ALUNO          📋 ALUNOS CADASTRADOS        │
│   ───────────────────          ┌─────────────────────┐     │
│   Nome: ___________            │ Nome       Idade    │     │
│   Idade: __________            │ João Silva   20     │     │
│   Curso: ___________           │ Maria Santos 22     │     │
│   Nota: ___________            │ Pedro Costa  19     │     │
│                                 └─────────────────────┘     │
│   [ Cadastrar Aluno ]                                       │
│                                                             │
│   ⚙️ CONTROLES                                              │
│   Nota mínima: [6.0] [Aplicar Filtro] [Exportar Relatório]  │
│   [Salvar CSV] [Carregar CSV] [Mostrar Todos]               │
│                                                             │
│   Status: ✅ Sistema pronto | Total: 3 alunos              │
└─────────────────────────────────────────────────────────────┘
📋 Como Usar
1. 🎓 Cadastrar Aluno
Preencha todos os campos do formulário

Clique em "Cadastrar Aluno"

O aluno aparecerá automaticamente na tabela

2. 🔍 Filtrar Alunos
Digite a nota mínima desejada (ex: 7.5)

Clique em "Aplicar Filtro"

A tabela mostrará apenas alunos com nota ≥ ao valor informado

3. 💾 Salvar Dados
Clique em "Salvar CSV" para persistir os dados no arquivo alunos.csv

4. 📂 Carregar Dados
Clique em "Carregar CSV" para restaurar dados salvos anteriormente

5. 📊 Exportar Relatório
Aplique um filtro (ex: nota ≥ 8.0)

Clique em "Exportar Relatório"

Será gerado o arquivo relatorio_nota_acima_8.0.csv

🗂 Estrutura do Projeto
text
sistema_alunos/
├── 📄 main.py                          # Código principal
├── 💾 alunos.csv                       # Banco de dados (automático)
├── 📊 relatorio_nota_acima_*.csv       # Relatórios (automático)
└── 📖 README.md                        # Documentação
📊 Exemplo de Dados
csv
Nome,Idade,Curso,Nota Final
João Silva,20,Desenvolvimento de Sistemas,8.5
Maria Santos,22,Análise e Desenvolvimento de Sistemas,9.0
Pedro Costa,19,Desenvolvimento de Sistemas,7.5
⚙️ Validações Implementadas
Campo	Validação
Nome	Campo obrigatório
Idade	Número inteiro (0-100)
Curso	Campo obrigatório
Nota Final	Número decimal (0.0-10.0)
🛠 Tecnologias Utilizadas
Tecnologia	Finalidade
Python	Linguagem de programação
Tkinter	Interface gráfica do usuário
Pandas	Manipulação e análise de dados
CSV	Armazenamento persistente de dados
🐛 Solução de Problemas
❌ Erro: "Módulo pandas não encontrado"
✅ Solução:

bash
pip install pandas
❌ Erro: "No columns to parse from file"
✅ Solução: O arquivo CSV está vazio. Delete alunos.csv e execute novamente.

❌ Interface não carrega
✅ Solução: Verifique se o Tkinter está instalado:

bash
python -m tkinter
📝 Exemplos de Uso
🏫 Cenário Educacional
python
# Cadastro de aluno exemplo:
Nome: "Ana Oliveira"
Idade: 21
Curso: "Desenvolvimento de Sistemas"
Nota: 8.8
📈 Geração de Relatórios
python
# Alunos aprovados (nota ≥ 6.0)
Filtro: 6.0 → Exportar → "relatorio_nota_acima_6.0.csv"

# Alunos destaque (nota ≥ 8.5)
Filtro: 8.5 → Exportar → "relatorio_nota_acima_8.5.csv"
🤝 Contribuindo
Faça um fork do projeto

Crie uma branch para sua feature (git checkout -b feature/AmazingFeature)

Commit suas mudanças (git commit -m 'Add some AmazingFeature')

Push para a branch (git push origin feature/AmazingFeature)

Abra um Pull Request

📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para detalhes.

👨‍💻 Desenvolvido por
Projeto desenvolvido para exercício de fixação em Python com Tkinter e Pandas.

<div align="center">
🎊 Divirta-se usando o sistema!
💡 Dica: Sempre faça backup do arquivo alunos.csv antes de grandes modificações!

</div>
