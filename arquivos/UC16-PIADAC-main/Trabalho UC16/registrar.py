from customtkinter import *
from tkinter import PhotoImage
from backend import BackEnd

class FrontEndRegistrar(BackEnd):  
    def menu_registrar(self):
        self.criar_tabela_db()
        self.frame_registrar = CTkFrame(self, fg_color='white', width=1350, height=601, corner_radius=-10)
        self.frame_registrar.place(x=-5, y=100)

        self.foto_cad = PhotoImage(file='Trabalho UC16/Imagens/imagem_cad.png')
        self.image_label_cad = CTkLabel(self.frame_registrar, text ='', image = self.foto_cad)
        self.image_label_cad.place(x=-200, y=0)


        self.titulo_cad = CTkLabel(self.frame_registrar, text='CENTRAL DE CADASTRO ', text_color='#1e192c', fg_color='transparent', font=('Verdana', 25, 'bold'))
        self.titulo_cad.place(x=835, y=40)

        self.empresa_cad = CTkEntry(self.frame_registrar, width=350, height=45, border_color='#1e192c', bg_color='white',fg_color='#F8F8F8', placeholder_text= 'Insira o seu nome ou o nome da empresa.', placeholder_text_color='#1E192C', text_color='#1E192C', font=('Verdana', 15))
        self.empresa_cad.place(x=830, y=105)

        self.cnpj_cad = CTkEntry(self.frame_registrar, width=350, height=45, border_color='#1e192c', bg_color='white',fg_color='#F8F8F8', placeholder_text='Insira o CNPJ/CPF.', placeholder_text_color='#1E192C', text_color='#1E192C', font=('Verdana', 15))
        self.cnpj_cad.place(x=830, y=170)

        self.email_cad = CTkEntry(self.frame_registrar, width=350, height=45, border_color='#1e192c', bg_color='white',fg_color='#F8F8F8', placeholder_text='Insira o E-mail.', placeholder_text_color='#1E192C', text_color='#1E192C', font=('Verdana', 15))
        self.email_cad.place(x=830, y=235)

        self.senha_cad = CTkEntry(self.frame_registrar, width=350, height=45, border_color='#1e192c', bg_color='white',fg_color='#F8F8F8', placeholder_text= 'Insira a senha.', placeholder_text_color='#1E192C', text_color='#1E192C', font=('Verdana', 15), show='*')
        self.senha_cad.place(x=830, y=300)

        self.conf_senha_cad = CTkEntry(self.frame_registrar, width=350, height=45, border_color='#1e192c', bg_color='white',fg_color='#F8F8F8', placeholder_text= 'Confirme a senha.', placeholder_text_color='#1E192C', text_color='#1E192C', font=('Verdana', 15), show='*')
        self.conf_senha_cad.place(x=830, y=365)

        self.ver_senha_cadastro = StringVar()
        self.botao_ver_senha_cad = CTkCheckBox(self.frame_registrar, onvalue='on', offvalue='off', text='Visualizar senha.', text_color='#1e192c', bg_color='white', fg_color='#1E192C', hover_color='#1E192C', border_color='#1E192C', font=('Verdana', 14), corner_radius=25, variable=self.ver_senha_cadastro, command=self.ver_senha_cad)
        self.botao_ver_senha_cad.place(x=830, y=420)

        self.botao_registrar = CTkButton(self.frame_registrar, width=270, height=55, text= 'CADASTRAR', font=('Verdana', 20, 'bold'), fg_color='#1e192c', hover_color='#1E192C', command=self.confirmar_cadastro)
        self.botao_registrar.place(x=870, y=475)

        self.ja_possui_uma_conta  = CTkLabel(self.frame_registrar, text='Já possui uma conta?', bg_color='transparent', fg_color=None, text_color='#1e192c', font=('Verdana', 17))
        self.ja_possui_uma_conta .place(x=855, y=550)

        self.botao_voltar_pag_login = CTkButton(self.frame_registrar, text='Faça login.', text_color='#494454', bg_color='white', fg_color='white', height=5, width=5, hover=None, hover_color=None, font=('Verdana', 17, 'bold'), command=self.menu_login)
        self.botao_voltar_pag_login.place(x=1045, y=550)