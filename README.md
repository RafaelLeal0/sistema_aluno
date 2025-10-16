<<<<<<< HEAD
# 🎓 Sistema de Gestão de Alunos
https://img.shields.io/badge/Python-3.6%252B-blue
https://img.shields.io/badge/GUI-Tkinter-green
https://img.shields.io/badge/Data-Pandas-orange
https://img.shields.io/badge/License-MIT-lightgrey

Um sistema completo e intuitivo para cadastro, gerenciamento e relatórios de alunos desenvolvido em Python.

# ✨ Funcionalidades
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
Layout Principal
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
# 📋 Como Usar
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

# 🗂 Estrutura do Projeto
text
sistema_alunos/
├── main.py                          # Código principal
├── alunos.csv                       # Banco de dados (automático)
├── relatorio_nota_acima_*.csv       # Relatórios (automático)
└── README.md                        # Documentação
Exemplo de Dados
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
# 📝 Exemplos de Uso
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
📄 Licença
Este projeto está sob a licença MIT.

# 👨‍💻 Desenvolvido por
Projeto desenvolvido pelo Rafael Leal para exercício de fixação em Python com Tkinter e Pandas.

<div align="center">
🎊 Divirta-se usando o sistema!
💡 Dica: Sempre faça backup do arquivo alunos.csv antes de grandes modificações!

</div>
🗂 Arquivos do Projeto
📄 main.py
python
import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import os

class SistemaAlunos:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestão de Alunos")
        self.root.geometry("800x600")
        
        # DataFrame para armazenar os dados
        self.df = pd.DataFrame(columns=['Nome', 'Idade', 'Curso', 'Nota Final'])
        
        # Carregar dados existentes
        self.carregar_csv_silencioso()
        
        self.criar_interface()
    
    def carregar_csv_silencioso(self):
        """Carrega CSV silenciosamente sem mostrar mensagens de erro"""
        try:
            if os.path.exists('alunos.csv'):
                if os.path.getsize('alunos.csv') > 0:
                    self.df = pd.read_csv('alunos.csv')
                else:
                    self.df = pd.DataFrame(columns=['Nome', 'Idade', 'Curso', 'Nota Final'])
            else:
                self.df = pd.DataFrame(columns=['Nome', 'Idade', 'Curso', 'Nota Final'])
                
        except Exception as e:
            self.df = pd.DataFrame(columns=['Nome', 'Idade', 'Curso', 'Nota Final'])
    
    def criar_interface(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        title_label = tk.Label(main_frame, text="Sistema de Cadastro de Alunos", 
                              font=('Arial', 14, 'bold'))
        title_label.pack(pady=10)
        
        # Frame para cadastro
        frame_cadastro = ttk.LabelFrame(main_frame, text="Cadastrar Aluno", padding=10)
        frame_cadastro.pack(fill=tk.X, pady=5)
        
        # Campos de entrada
        campos = [
            ("Nome:", "entry_nome"),
            ("Idade:", "entry_idade"), 
            ("Curso:", "entry_curso"),
            ("Nota Final (0-10):", "entry_nota")
        ]
        
        for i, (label, entry_var) in enumerate(campos):
            ttk.Label(frame_cadastro, text=label).grid(row=i, column=0, sticky="w", padx=5, pady=2)
            entry = ttk.Entry(frame_cadastro, width=30)
            entry.grid(row=i, column=1, padx=5, pady=2)
            setattr(self, entry_var, entry)
        
        # Botão de cadastro
        ttk.Button(frame_cadastro, text="Cadastrar Aluno", 
                  command=self.cadastrar_aluno).grid(row=4, column=1, pady=10, sticky="e")
        
        # Frame para controles
        frame_controles = ttk.LabelFrame(main_frame, text="Controles", padding=10)
        frame_controles.pack(fill=tk.X, pady=5)
        
        # Filtro
        ttk.Label(frame_controles, text="Filtrar por nota mínima:").grid(row=0, column=0, sticky="w")
        self.entry_filtro = ttk.Entry(frame_controles, width=10)
        self.entry_filtro.insert(0, "6.0")
        self.entry_filtro.grid(row=0, column=1, padx=5)
        
        # Botões de controle
        botoes = [
            ("Aplicar Filtro", self.filtrar_alunos),
            ("Exportar Relatório", self.exportar_relatorio),
            ("Salvar CSV", self.salvar_csv),
            ("Carregar CSV", self.carregar_csv),
            ("Mostrar Todos", self.mostrar_todos)
        ]
        
        for i, (texto, comando) in enumerate(botoes):
            ttk.Button(frame_controles, text=texto, 
                      command=comando).grid(row=0, column=i+2, padx=2)
        
        # Frame da tabela
        frame_tabela = ttk.LabelFrame(main_frame, text="Alunos Cadastrados", padding=10)
        frame_tabela.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Treeview com scrollbar
        tree_frame = ttk.Frame(frame_tabela)
        tree_frame.pack(fill=tk.BOTH, expand=True)
        
        self.tree = ttk.Treeview(tree_frame, columns=('Nome', 'Idade', 'Curso', 'Nota Final'), 
                                show='headings', height=12)
        
        # Configurar colunas
        colunas = [
            ('Nome', 200),
            ('Idade', 80),
            ('Curso', 150),
            ('Nota Final', 100)
        ]
        
        for col, width in colunas:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width, anchor='center')
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set(f"Total de alunos: {len(self.df)}")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN)
        status_bar.pack(fill=tk.X, pady=5)
        
        self.atualizar_tabela()
    
    def cadastrar_aluno(self):
        nome = self.entry_nome.get().strip()
        idade = self.entry_idade.get().strip()
        curso = self.entry_curso.get().strip()
        nota = self.entry_nota.get().strip()
        
        # Validação
        if not all([nome, idade, curso, nota]):
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
            return
        
        try:
            idade_int = int(idade)
            nota_float = float(nota)
            
            if nota_float < 0 or nota_float > 10:
                messagebox.showerror("Erro", "A nota deve estar entre 0 e 10!")
                return
            
            if idade_int < 0 or idade_int > 100:
                messagebox.showerror("Erro", "Idade deve ser entre 0 e 100 anos!")
                return
                
        except ValueError:
            messagebox.showerror("Erro", "Idade deve ser número inteiro e Nota deve ser número decimal")
            return
        
        # Adicionar aluno
        novo_aluno = {
            'Nome': nome,
            'Idade': idade_int,
            'Curso': curso,
            'Nota Final': nota_float
        }
        
        self.df = pd.concat([self.df, pd.DataFrame([novo_aluno])], ignore_index=True)
        
        # Limpar campos
        for entry in [self.entry_nome, self.entry_idade, self.entry_curso, self.entry_nota]:
            entry.delete(0, tk.END)
        
        self.atualizar_tabela()
        self.status_var.set(f"Aluno cadastrado! Total: {len(self.df)} alunos")
        
        messagebox.showinfo("Sucesso", f"Aluno '{nome}' cadastrado com sucesso!")
    
    def atualizar_tabela(self, dataframe=None):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        df_to_show = dataframe if dataframe is not None else self.df
        
        if len(df_to_show) == 0:
            self.tree.insert('', 'end', values=("Nenhum aluno cadastrado", "", "", ""))
            return
        
        for _, row in df_to_show.iterrows():
            self.tree.insert('', 'end', values=(
                row['Nome'], 
                row['Idade'], 
                row['Curso'], 
                f"{row['Nota Final']:.1f}"
            ))
    
    def filtrar_alunos(self):
        try:
            nota_minima = float(self.entry_filtro.get())
            df_filtrado = self.df[self.df['Nota Final'] >= nota_minima]
            self.atualizar_tabela(df_filtrado)
            self.status_var.set(f"Filtrado: {len(df_filtrado)} aluno(s) com nota ≥ {nota_minima}")
        except ValueError:
            messagebox.showerror("Erro", "Digite um valor numérico válido para a nota!")
    
    def mostrar_todos(self):
        self.atualizar_tabela()
        self.status_var.set(f"Mostrando todos os {len(self.df)} aluno(s)")
    
    def salvar_csv(self):
        if self.df.empty:
            messagebox.showwarning("Aviso", "Não há dados para salvar!")
            return
        
        try:
            self.df.to_csv('alunos.csv', index=False, encoding='utf-8')
            messagebox.showinfo("Sucesso", "Dados salvos em 'alunos.csv'!")
            self.status_var.set(f"Dados salvos | Total: {len(self.df)} alunos")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar: {str(e)}")
    
    def carregar_csv(self):
        try:
            if os.path.exists('alunos.csv'):
                if os.path.getsize('alunos.csv') > 0:
                    self.df = pd.read_csv('alunos.csv')
                    self.atualizar_tabela()
                    messagebox.showinfo("Sucesso", f"Dados carregados! {len(self.df)} aluno(s).")
                    self.status_var.set(f"Dados carregados | Total: {len(self.df)} alunos")
                else:
                    messagebox.showinfo("Info", "Arquivo 'alunos.csv' está vazio.")
            else:
                messagebox.showinfo("Info", "Arquivo 'alunos.csv' não encontrado.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar CSV: {str(e)}")
            self.df = pd.DataFrame(columns=['Nome', 'Idade', 'Curso', 'Nota Final'])
            self.atualizar_tabela()
    
    def exportar_relatorio(self):
        if self.df.empty:
            messagebox.showwarning("Aviso", "Não há dados para exportar!")
            return
        
        try:
            nota_minima = float(self.entry_filtro.get())
            df_filtrado = self.df[self.df['Nota Final'] >= nota_minima]
            
            if df_filtrado.empty:
                messagebox.showinfo("Info", f"Nenhum aluno com nota ≥ {nota_minima}")
                return
            
            filename = f"relatorio_nota_acima_{nota_minima}.csv"
            df_filtrado.to_csv(filename, index=False, encoding='utf-8')
            
            messagebox.showinfo("Sucesso", 
                              f"Relatório exportado: '{filename}'\n"
                              f"{len(df_filtrado)} aluno(s) com nota ≥ {nota_minima}")
        except ValueError:
            messagebox.showerror("Erro", "Digite um valor numérico válido!")

def main():
    try:
        root = tk.Tk()
        app = SistemaAlunos(root)
        root.mainloop()
    except Exception as e:
        print(f"Erro ao executar: {e}")
        input("Pressione Enter para sair...")

if __name__ == "__main__":
    main()
📋 requirements.txt
text
pandas>=1.3.0
⭐ Se este projeto foi útil, deixe uma estrela no repositório!
=======
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
>>>>>>> 37c765fb45f8b6d4e3a5b2125d27cbb02649351b
