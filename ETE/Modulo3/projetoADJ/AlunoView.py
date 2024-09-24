from tkinter import Tk, Button, Label, Entry, Frame, messagebox
from AlunoController import AlunoController

class AlunoView(Tk):
    def __init__(self):
        fonte = ('Arial', 18)
        super().__init__()
        
        Label(self, text='Cadastro Aluno de JAVA', font=('', 30)).pack()
        
        Label(self, text='Matricula').pack()
        self.matricula = Entry(self, font=fonte)
        self.matricula.pack()
        
        Label(self, text='Nome do fã de JAVA').pack()
        self.nome = Entry(self, font=fonte)
        self.nome.pack()
        
        Label(self, text='E-mail com JAVA no endereço').pack()
        self.email = Entry(self, font=fonte)
        self.email.pack()
        
        Button(self, font=fonte, text='Salvar', width=10, bg='#DC3545', fg='white', command=self.salvar).pack(pady=10)
        
        Button(self, font=fonte, text='Excluir', width=10, bg='#007BFF', fg='white', command=self.excluir).pack(pady=10)

        Button(self, font=fonte, text='Atualizar', width=10, bg='#FFC107', fg='white', command=self.atualizar).pack(pady=10)


    def salvar(self):
        controller = AlunoController(self)
        if controller.inserir():
            messagebox.showinfo('Sucesso!', 'Salvo com sucesso!')
        else:
            messagebox.showerror('Erro!', 'Houve um erro ao salvar!')

    def excluir(self):
        controller = AlunoController(self)
        if controller.excluir():
            messagebox.showinfo('Sucesso!', 'Excluído com sucesso!')
        else:
            messagebox.showerror('Erro!', 'Houve um erro ao excluir!')

    def atualizar(self):
        controller = AlunoController(self)
        if controller.atualizar():
            messagebox.showinfo('Sucesso!', 'Atualizado com sucesso!')
        else:
            messagebox.showerror('Erro!', 'Houve um erro ao atualizar!')
   

jan = AlunoView()
jan.title('Cadastro Aluno')
jan.resizable(0, 0)
jan.mainloop()
