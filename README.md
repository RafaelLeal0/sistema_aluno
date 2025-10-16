Sistema de Gestão de Alunos
Sistema simples para cadastro e gerenciamento de alunos desenvolvido em Python com interface gráfica Tkinter.

Funcionalidades
Cadastro de Alunos: Adicione novos alunos com nome, idade, curso e nota final

Visualização de Dados: Veja todos os alunos cadastrados em uma tabela organizada

Filtros: Filtre alunos por nota mínima

Exportação de Dados: Salve e carregue dados em arquivo CSV

Relatórios: Exporte relatórios filtrados para CSV

Requisitos
Python 3.6 ou superior

Biblioteca Pandas

Instalação
Instale a biblioteca Pandas:

bash
pip install pandas
Execute o sistema:

bash
python main.py
Como Usar
Cadastrar Aluno
Preencha os campos no formulário:

Nome completo

Idade (número inteiro)

Curso

Nota final (0 a 10)

Clique em "Cadastrar Aluno"

Filtrar Alunos
Digite a nota mínima no campo "Filtrar por nota mínima"

Clique em "Aplicar Filtro"

Salvar Dados
Clique em "Salvar CSV" para salvar todos os dados no arquivo alunos.csv

Carregar Dados
Clique em "Carregar CSV" para carregar dados salvos anteriormente

Exportar Relatório
Aplique um filtro (ex: nota ≥ 6.0)

Clique em "Exportar Relatório" para gerar um arquivo CSV com os dados filtrados

Estrutura de Arquivos
main.py - Código principal do sistema

alunos.csv - Arquivo de dados dos alunos (criado automaticamente)

relatorio_nota_acima_X.csv - Relatórios exportados (criados automaticamente)

Validações
O sistema inclui validações para:

Campos obrigatórios

Idade entre 0 e 100 anos

Nota entre 0 e 10

Formato correto dos dados numéricos

Tecnologias Utilizadas
Python

Tkinter (Interface gráfica)

Pandas (Manipulação de dados)

CSV (Armazenamento)

Desenvolvido para fins educacionais
Sistema desenvolvido como exercício de fixação em Python com interface gráfica e manipulação de dados.
