from customtkinter import *
from tkinter import PhotoImage
from PIL import Image, ImageTk
from teatro import FrontEndTeatro
from musica import FrontEndMusica
from cinema import FrontEndCinema
from login import FrontEndLogin
from turismo import FrontEndTurismo
from contato import FrontEndContato

class FrontEndMenu(CTk, FrontEndTeatro, FrontEndMusica, FrontEndCinema, FrontEndLogin, FrontEndContato, FrontEndTurismo):
    def __init__(self):
        super().__init__()
        self.janela_principal()
        self.cabecalho()
        self.menu_principal()
        self.rodape()
        
    #Janela principal
    def janela_principal(self):        
        self.title("Lafaiete Cultural")
        self.geometry("1310x740")
        self.resizable(False,False)
        self.iconbitmap('Trabalho UC16/Imagens/icone_logo.ico')
        self.numero = 1

    #Cabeçalho
    def cabecalho(self):    
        
        #Frame divisor do cabeçalho
        self.frame_cabecalho = CTkFrame(self, fg_color="#1e192c", height=100, width=1350)
        self.frame_cabecalho.place(x=-10, y=0)

        #Logo do site
        self.logo = PhotoImage(file="Trabalho UC16/Imagens/logo.png")
        self.app_logo = CTkButton(self.frame_cabecalho, image=self.logo, fg_color="#1e192c", text='', hover=None, hover_color=None, command=self.menu_principal)
        self.app_logo.place(x=20, y=-5)

        # Botões e icones dos botões do menu

        #Música
        self.icone_botao_musica = PhotoImage(file="Trabalho UC16/Imagens/icone_musica.png")
        self.posicao_icone_botao_musica = CTkLabel(self.frame_cabecalho, text_color='black', image=self.icone_botao_musica, fg_color="#1e192c", text='', width=10, height=10)
        self.posicao_icone_botao_musica.place(x=180, y=28)
        self.botao_musica = CTkButton(self.frame_cabecalho, text="MÚSICA", command=self.menu_musica, fg_color="#1e192c", font=("Arial", 22, 'bold'), width=50, height=50, hover_color=None, hover=None)
        self.botao_musica.place(x=230, y= 30)

        #Cinema
        self.icone_botao_cinema = PhotoImage(file="Trabalho UC16/Imagens/icone_cinema.png")
        self.posicao_icone_botao_cinema = CTkLabel(self.frame_cabecalho, text_color='black', image=self.icone_botao_cinema, fg_color="#1e192c", text='', width=10, height=10)
        self.posicao_icone_botao_cinema.place(x=360, y=33)
        self.botao_cinema = CTkButton(self.frame_cabecalho, text="CINEMA", command=self.menu_cinema, fg_color="#1e192c", font=("Arial", 22, 'bold'), width=50, height=50, hover_color=None, hover=None)
        self.botao_cinema.place(x=410, y= 30)

        #Teatro
        self.icone_botao_teatro = PhotoImage(file="Trabalho UC16/Imagens/icone_teatro.png")
        self.posicao_icone_botao_teatro = CTkLabel(self.frame_cabecalho, text_color='black', image=self.icone_botao_teatro, fg_color="#1e192c", text='', width=10, height=10)
        self.posicao_icone_botao_teatro.place(x=535, y=30)
        self.botao_teatro = CTkButton(self.frame_cabecalho, text="TEATRO", command=self.menu_teatro, fg_color="#1e192c", font=("Arial", 22, 'bold'), width=50, height=50, hover_color=None, hover=None)
        self.botao_teatro.place(x=585, y= 30)

        #Turismo
        self.icone_botao_turismo = PhotoImage(file="Trabalho UC16/Imagens/icone_turismo.png")
        self.posicao_icone_botao_turismo = CTkLabel(self.frame_cabecalho, text_color='black', image=self.icone_botao_turismo, fg_color="#1e192c", text='', width=10, height=10)
        self.posicao_icone_botao_turismo.place(x=715, y=29)
        self.botao_turismo = CTkButton(self.frame_cabecalho, text="TURISMO", command=self.menu_turismo, fg_color="#1e192c", font=("Arial", 22, 'bold'), width=50, height=50, hover_color=None, hover=None)
        self.botao_turismo.place(x=780, y= 30)

        #Contato
        self.icone_botao_contato = PhotoImage(file="Trabalho UC16/Imagens/icone_contato.png")
        self.posicao_icone_botao_contato = CTkLabel(self.frame_cabecalho, text_color='black', image=self.icone_botao_contato, fg_color="#1e192c", text='', width=10, height=10)
        self.posicao_icone_botao_contato.place(x=915, y=29)
        self.botao_contatoicone_botao_contato = CTkButton(self.frame_cabecalho, text="CONTATO", command=self.menu_contato, fg_color="#1e192c", font=("Arial", 22, 'bold'), width=50, height=50, hover_color=None, hover=None)
        self.botao_contatoicone_botao_contato.place(x=975, y= 30)

        #Login
        self.icone_botao_login = PhotoImage(file="Trabalho UC16/Imagens/icone_login.png")
        self.posicao_icone_botao_login = CTkLabel(self.frame_cabecalho, text_color='black', image=self.icone_botao_login, fg_color="#1e192c", text='', width=10, height=10)
        self.posicao_icone_botao_login.place(x=1120, y=29)
        self.botao_loginicone_botao_login = CTkButton(self.frame_cabecalho, text="LOGIN", command=self.menu_login, fg_color="#1e192c", font=("Arial", 22, 'bold'), width=50, height=50, hover_color=None, hover=None)
        self.botao_loginicone_botao_login.place(x=1170, y= 30)

    def menu_principal(self):
        self.numero_cinema = 1
        self.numero_teatro = 1
        self.numero_musica = 1
        self.numero_turismo = 1
        self.numero_turismo2 = 4
        
        self.frame_principal = CTkFrame(self, fg_color='white', width=1350, height=600)
        self.frame_principal.place(x=-5, y=100)

        # self.img_fundo_menu = Image.open("Trabalho UC16/Imagens/gradiente_cinza.png")
        # self.img_fundo_menu = self.img_fundo_menu.resize((1350, 600))
        # self.bg_img_fundo_menu = ImageTk.PhotoImage(self.img_fundo_menu)
        # self.label_img_fundo_menu = CTkLabel(self.frame_principal, image=self.bg_img_fundo_menu,text='')
        # self.label_img_fundo_menu.place(x=0, y=0, relwidth=1,relheight=1)

        
        self.label_destaque = CTkLabel(self.frame_principal, text_color='black',text='DESTAQUES MENSAIS',font=('Arial',50,'bold'),fg_color='white')
        self.label_destaque.place(x=385,y=10)

        self.img_destaque_teatro = PhotoImage(file="Trabalho UC16/Imagens/teatro1.png")
        self.posicao_destaque_teatro = CTkButton(self.frame_principal, image=self.img_destaque_teatro, fg_color="#1e192c", text='', width=220,height=100, hover=None, hover_color=None, command='')
        self.posicao_destaque_teatro.place(x=80, y=89)

        self.img_destaque_musica = PhotoImage(file="Trabalho UC16/Imagens/img_musica1.png")
        self.posicao_destaque_musica = CTkButton(self.frame_principal, image=self.img_destaque_musica, fg_color="#1e192c", text='',width=100, height=100, hover=None, hover_color=None, command='')
        self.posicao_destaque_musica.place(x=450, y=89) 

        self.img_destaque_cinema = PhotoImage(file="Trabalho UC16/Imagens/img1_cinema.png")
        self.posicao_destaque_cinema = CTkButton(self.frame_principal, image=self.img_destaque_cinema, fg_color="#1e192c", text='', width=220,height=100, hover=None, hover_color=None, command='')
        self.posicao_destaque_cinema.place(x=920, y=89)

        self.img_destaque_turismo = PhotoImage(file="Trabalho UC16/Imagens/img1_turismo.png")
        self.posicao_destaque_turismo = CTkButton(self.frame_principal, image=self.img_destaque_turismo, fg_color="#1e192c", text='', width=220,height=100, hover=None, hover_color=None, command='')
        self.posicao_destaque_turismo.place(x=80, y=330)
        
        self.img_destaque_turismo2 = PhotoImage(file="Trabalho UC16/Imagens/img4_turismo.png")
        self.posicao_destaque_turismo2 = CTkButton(self.frame_principal, image=self.img_destaque_turismo2, fg_color="#1e192c", text='', width=220,height=100, hover=None, hover_color=None, command='')
        self.posicao_destaque_turismo2.place(x=490, y=330)

        self.alterar_imagens_cinema()
        self.alterar_imagens_teatro()
        self.alterar_imagens_musica()
        self.alterar_imagens_turismo()
        self.alterar_imagens_turismo2()
    
    def alterar_imagens_cinema(self):
        if self.numero_cinema == 4:
            self.numero_cinema = 1

        self.img_destaque_cinema.configure(file=f"Trabalho UC16/Imagens/img{self.numero_cinema}_cinema.png")
        
        if self.numero_cinema == 1:
            self.posicao_destaque_cinema.configure(self.frame_principal, image=self.img_destaque_cinema, command=self.frame_cine_img1)    
        
        elif self.numero_cinema == 2:
            self.posicao_destaque_cinema.configure(self.frame_principal, image=self.img_destaque_cinema, command=self.frame_cine_img2)
        
        elif self.numero_cinema == 3:
            self.posicao_destaque_cinema.configure(self.frame_principal, image=self.img_destaque_cinema, command=self.frame_cine_img3)

        self.numero_cinema += 1
        self.frame_principal.after(4000, self.alterar_imagens_cinema)


    def alterar_imagens_teatro(self):
        if self.numero_teatro == 4:
            self.numero_teatro = 1

        self.img_destaque_teatro.configure(file=f"Trabalho UC16/Imagens/teatro{self.numero_teatro}.png")
        
        if self.numero_teatro == 1:
            self.posicao_destaque_teatro.configure(self.frame_principal, image=self.img_destaque_teatro, command=self.menu_teatro)
            
        
        elif self.numero_teatro == 2:
            self.posicao_destaque_teatro.configure(self.frame_principal, image=self.img_destaque_teatro, command=self.menu_teatro)
            
        
        elif self.numero_teatro == 3:
            self.posicao_destaque_teatro.configure(self.frame_principal, image=self.img_destaque_teatro, command=self.menu_teatro)
            
        
        self.numero_teatro += 1
        self.frame_principal.after(4000, self.alterar_imagens_teatro)
        
    def alterar_imagens_musica(self):
        if self.numero_musica == 7:
            self.numero_musica = 1

        self.img_destaque_musica.configure(file=f"Trabalho UC16/Imagens/img_musica{self.numero_musica}.png")
        
        if self.numero_musica == 1:
            self.posicao_destaque_musica.configure(self.frame_principal, image=self.img_destaque_musica, command=self.exibir_musica)
            
        
        elif self.numero_musica == 2:
            self.posicao_destaque_musica.configure(self.frame_principal, image=self.img_destaque_musica, command=self.exibir_musica2)
            
        
        elif self.numero_musica == 3:
            self.posicao_destaque_musica.configure(self.frame_principal, image=self.img_destaque_musica, command=self.exibir_musica3)

        elif self.numero_musica == 4:
            self.posicao_destaque_musica.configure(self.frame_principal, image=self.img_destaque_musica, command=self.exibir_musica4)

        elif self.numero_musica == 5:
            self.posicao_destaque_musica.configure(self.frame_principal, image=self.img_destaque_musica, command=self.exibir_musica5)

        elif self.numero_musica == 6:
            self.posicao_destaque_musica.configure(self.frame_principal, image=self.img_destaque_musica, command=self.exibir_musica6)
            
        self.numero_musica += 1
        self.frame_principal.after(4000, self.alterar_imagens_musica)

    def alterar_imagens_turismo(self):
        if self.numero_turismo == 4:
            self.numero_turismo = 1

        self.img_destaque_turismo.configure(file=f"Trabalho UC16/Imagens/img{self.numero_turismo}_turismo.png")
        
        if self.numero_turismo == 1:
            self.posicao_destaque_turismo.configure(self.frame_principal, image=self.img_destaque_turismo, command=self.exibir_cristo)
            
        
        elif self.numero_turismo == 2:
            self.posicao_destaque_turismo.configure(self.frame_principal, image=self.img_destaque_turismo, command=self.exibir_matriz)
            
        
        elif self.numero_turismo == 3:
            self.posicao_destaque_turismo.configure(self.frame_principal, image=self.img_destaque_turismo, command=self.exibir_trem)
  
        self.numero_turismo += 1
        self.frame_principal.after(4000, self.alterar_imagens_turismo)

    def alterar_imagens_turismo2(self):
        if self.numero_turismo2 == 7:
            self.numero_turismo2 = 4

        self.img_destaque_turismo2.configure(file=f"Trabalho UC16/Imagens/img{self.numero_turismo2}_turismo.png")
        
        if self.numero_turismo2 == 4:
            self.posicao_destaque_turismo2.configure(self.frame_principal, image=self.img_destaque_turismo2, command=self.exibir_parque)
        
        elif self.numero_turismo2 == 5:
            self.posicao_destaque_turismo2.configure(self.frame_principal, image=self.img_destaque_turismo2, command=self.exibir_sao_sebastiao)
            
        
        elif self.numero_turismo2 == 6:
            self.posicao_destaque_turismo2.configure(self.frame_principal, image=self.img_destaque_turismo2, command=self.exibir_museu)

  
        self.numero_turismo2 += 1
        self.frame_principal.after(4000, self.alterar_imagens_turismo2)

    #Rodapé do site
    def rodape(self):
        #Frame divisor do rodapé
        self.frame_rodape = CTkFrame(self, fg_color="#1e192c", height=50, width=1500)
        self.frame_rodape.place(x=-10, y=700)
        
        #Texto do rodapé
        self.texto_rodape = CTkLabel(self.frame_rodape, text="Lafacult © 2023 - Todos os direitos reservados", font=("Georgia", 12), fg_color="#1e192c", text_color='white')
        self.texto_rodape.place(x=500, y=10)
        
    

if __name__ == '__main__':
    app = FrontEndMenu()
    app.mainloop()