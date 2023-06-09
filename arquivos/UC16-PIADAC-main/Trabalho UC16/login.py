from customtkinter import *
from tkinter import PhotoImage
from registrar import FrontEndRegistrar
from alterar_senha import FrontEndAlterar
from backend import BackEnd

class FrontEndLogin(FrontEndRegistrar, FrontEndAlterar, BackEnd):
    def menu_login(self):
        self.frame_login = CTkFrame(self, fg_color='white', width=1350, height=601, corner_radius=-10)
        self.frame_login.place(x=-5, y=100)

        self.foto_login = PhotoImage(file='Trabalho UC16/Imagens/imagem_login.png')
        self.image_label = CTkLabel(self.frame_login, text ='', image = self.foto_login)
        self.image_label.place(x=-120, y=0)


        self.titulo_login = CTkLabel(self.frame_login, text='BEM-VINDO(A)', text_color='#1e192c', fg_color='transparent', font=('Verdana', 25, 'bold'))
        self.titulo_login.place(x=940, y=70)

        self.cnpj_login = CTkEntry(self.frame_login, width=350, height=55, border_color='#1e192c', text_color='#1E192C', bg_color='white',fg_color='#F8F8F8', placeholder_text='Insira o CNPJ.', placeholder_text_color='#7C7C7C', font=('Verdana', 15))
        self.cnpj_login.place(x=870, y=145)

        self.senha_login = CTkEntry(self.frame_login, width=350, height=55, border_color='#1e192c', bg_color='white',fg_color='#F8F8F8', placeholder_text= 'Insira a senha.', placeholder_text_color='#7C7C7C', text_color='#1E192C', font=('Verdana', 15), show='*')
        self.senha_login.place(x=870, y=220)

        self.ver_senha_login = StringVar()
        self.visu_senha_log = CTkCheckBox(self.frame_login, onvalue='on', offvalue='off', text='Visualizar senha.', text_color='#1e192c', bg_color='transparent', font=('Verdana', 14), border_color='#1E192C', corner_radius=25, hover_color='#1E192C', fg_color='#1E192C', command=self.ver_senha_log)
        self.visu_senha_log.place(x=880, y=300)

        self.info_alt = CTkLabel(self.frame_login, text='Esqueceu a senha? ', bg_color='transparent', fg_color=None, text_color='#1e192c', font=('Verdana', 15))
        self.info_alt.place(x=865, y=340)

        self.botao_ir_pag_alt = CTkButton(self.frame_login, text='  Altere o seu usuário aqui.', text_color='#494454', bg_color='white', fg_color='white', height=5, width=5, hover=None, hover_color=None, font=('Verdana', 16, 'bold'), command=self.menu_alterar)
        self.botao_ir_pag_alt.place(x=1005, y=342)

        self.botao_login = CTkButton(self.frame_login, width=270, height=55, text= 'CONFIRMAR LOGIN', font=('Verdana', 20, 'bold'), fg_color='#1e192c', hover_color='#615E6B', command=self.confirmar_login)
        self.botao_login.place(x=910, y=400)

        self.info_login = CTkLabel(self.frame_login, text='Não possui um conta? ', bg_color='transparent', fg_color=None, text_color='#1e192c', font=('Verdana', 17))
        self.info_login.place(x=885, y=480)

        self.botao_ir_pag_cadastro = CTkButton(self.frame_login, text='  Cadastre-se.', text_color='#494454', bg_color='white', fg_color='white', height=5, width=5, hover=None, hover_color=None, font=('Verdana', 17, 'bold'), command=self.menu_registrar)
        self.botao_ir_pag_cadastro.place(x=1075, y=480)