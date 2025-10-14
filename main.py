import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import os

class SistemaAlunos:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestão de Alunos")
        self.root.geometry("800x600")
        
        self.df = pd.DataFrame(columns=['Nome', 'Idade', 'Curso', 'Nota Final'])
 
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

        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        title_label = tk.Label(main_frame, text="Sistema de Cadastro de Alunos", 
                              font=('Arial', 14, 'bold'))
        title_label.pack(pady=10)
        
        frame_cadastro = ttk.LabelFrame(main_frame, text="Cadastrar Aluno", padding=10)
        frame_cadastro.pack(fill=tk.X, pady=5)
        
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
        
        ttk.Button(frame_cadastro, text="Cadastrar Aluno", 
                  command=self.cadastrar_aluno).grid(row=4, column=1, pady=10, sticky="e")
        
        frame_controles = ttk.LabelFrame(main_frame, text="Controles", padding=10)
        frame_controles.pack(fill=tk.X, pady=5)
        
        ttk.Label(frame_controles, text="Filtrar por nota mínima:").grid(row=0, column=0, sticky="w")
        self.entry_filtro = ttk.Entry(frame_controles, width=10)
        self.entry_filtro.insert(0, "6.0")
        self.entry_filtro.grid(row=0, column=1, padx=5)
        
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
        
        frame_tabela = ttk.LabelFrame(main_frame, text="Alunos Cadastrados", padding=10)
        frame_tabela.pack(fill=tk.BOTH, expand=True, pady=5)
        
        tree_frame = ttk.Frame(frame_tabela)
        tree_frame.pack(fill=tk.BOTH, expand=True)
        
        self.tree = ttk.Treeview(tree_frame, columns=('Nome', 'Idade', 'Curso', 'Nota Final'), 
                                show='headings', height=12)
        
        colunas = [
            ('Nome', 200),
            ('Idade', 80),
            ('Curso', 150),
            ('Nota Final', 100)
        ]
        
        for col, width in colunas:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width, anchor='center')
        
        scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

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

        novo_aluno = {
            'Nome': nome,
            'Idade': idade_int,
            'Curso': curso,
            'Nota Final': nota_float
        }
        
        self.df = pd.concat([self.df, pd.DataFrame([novo_aluno])], ignore_index=True)

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