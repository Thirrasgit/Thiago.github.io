from customtkinter import *
from tkinter import PhotoImage
from backend import BackEnd

class FrontEndAlterar(BackEnd):
    def menu_alterar(self):
        self.frame_alterar = CTkFrame(self, fg_color='white', width=1350, height=601, corner_radius=-10)
        self.frame_alterar.place(x=-5, y=100)

        self.foto_alterar_senha = PhotoImage(file='Trabalho UC16/Imagens/tela alterar.png')
        self.image_label = CTkLabel(self.frame_alterar, text ='', image = self.foto_alterar_senha)
        self.image_label.place(x=-120, y=0)

        self.titulo_alt = CTkLabel(self.frame_alterar, text='ALTERAR A SENHA', text_color='#1e192c', fg_color='transparent', font=('Verdana', 25, 'bold'))
        self.titulo_alt.place(x=890, y=35)

        self.email_alt = CTkEntry(self.frame_alterar, width=350, height=50, border_color='#1e192c', bg_color='white',fg_color='#F8F8F8', placeholder_text= 'Insira o E-mail.', text_color='#1E192C', placeholder_text_color='#7C7C7C', font=('Verdana', 15))
        self.email_alt.place(x=870, y=100)

        self.cnpj_alt = CTkEntry(self.frame_alterar, width=350, height=50, border_color='#1e192c', bg_color='white',fg_color='#F8F8F8', placeholder_text='Insira o CNPJ.', text_color='#1E192C', placeholder_text_color='#7C7C7C', font=('Verdana', 15))
        self.cnpj_alt.place(x=870, y=175)

        self.senha_alt = CTkEntry(self.frame_alterar, width=350, height=50, border_color='#1e192c', bg_color='white',fg_color='#F8F8F8', placeholder_text= 'Insira a nova senha.', text_color='#1E192C', placeholder_text_color='#7C7C7C', font=('Verdana', 15), show='*')
        self.senha_alt.place(x=870, y=250)

        self.conf_senha_alt = CTkEntry(self.frame_alterar, width=350, height=50, border_color='#1e192c', bg_color='white',fg_color='#F8F8F8', placeholder_text= 'Confirme a nova senha.', placeholder_text_color='#7C7C7C', text_color='#1E192C', font=('Verdana', 15), show='*')
        self.conf_senha_alt.place(x=870, y=325)

        self.ver_senha_alterar = StringVar()
        self.visu_senha_alt = CTkCheckBox(self.frame_alterar, onvalue='on', offvalue='off', text='Visualizar senha.', text_color='#1e192c', bg_color='transparent', font=('Verdana', 14), border_color='#1E192C', corner_radius=25, hover_color='#1E192C', variable=self.ver_senha_alterar, fg_color='#1E192C', command=self.ver_senha_alt)
        self.visu_senha_alt.place(x=880, y=395)

        self.botao_alt = CTkButton(self.frame_alterar, width=270, height=55, text= 'CONFIRMAR ALTERAÇÃO', font=('Verdana', 20, 'bold'), fg_color='#1e192c', hover_color='#615E6B', command=self.alterar_senha_usuario)
        self.botao_alt.place(x=900, y=445)

        self.botao_ir_pag_login_alt = CTkButton(self.frame_alterar, text=' Clique aqui para voltar à Página do Login.', text_color='#494454', bg_color='white', fg_color='white', height=5, width=5, hover=None, hover_color=None, font=('Verdana', 16, 'bold'), command=self.menu_login)
        self.botao_ir_pag_login_alt.place(x=860, y=530)
