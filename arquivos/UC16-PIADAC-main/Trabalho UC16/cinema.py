from customtkinter import *
from PIL import Image, ImageTk
from tkinter import PhotoImage

class FrontEndCinema():    
    def menu_cinema(self):
        self.frame_principal.place_forget()
        self.frame_cinema = CTkFrame(self, width=1350, height=600)
        self.frame_cinema.place(x=-5, y=100)

        #Imagem de fundo
        self.img_fundo_cinema = Image.open("Trabalho UC16/Imagens/cinema.png")
        self.img_fundo_cinema = self.img_fundo_cinema.resize((1350, 600))
        self.bg_img_fundo_cinema = ImageTk.PhotoImage(self.img_fundo_cinema)
        self.label_img_fundo_cinema = CTkLabel(self.frame_cinema, image=self.bg_img_fundo_cinema)
        self.label_img_fundo_cinema.place(x=0, y=0, relwidth=1,relheight=1)

        #Cartaz 1
        self.img1_cinema = PhotoImage(file="Trabalho UC16/Imagens/img1_cinema.png")
        self.posicao_img1_cinema = CTkButton(self.frame_cinema, command=self.frame_cine_img1, image=self.img1_cinema, text='',
                                                   width=100, height=100, hover_color=None, hover=None, fg_color="white")
        self.posicao_img1_cinema.place(x=60, y=60)

        #Cartaz 2
        self.img2_cinema = PhotoImage(file="Trabalho UC16/Imagens/img2_cinema.png")
        self.posicao_img2_cinema = CTkButton(self.frame_cinema, command=self.frame_cine_img2, image=self.img2_cinema, text='',
                                             width=10, height=10, hover_color=None, hover=None, fg_color="white")
        self.posicao_img2_cinema.place(x=480, y=60)

        # Cartaz 3
        self.img3_cinema = PhotoImage(file="Trabalho UC16/Imagens/img3_cinema.png")
        self.posicao_img3_cinema = CTkButton(self.frame_cinema, command=self.frame_cine_img3, image=self.img3_cinema, text='',
                                             width=10, height=10, hover_color=None, hover=None, fg_color="white")
        self.posicao_img3_cinema.place(x=910, y=60)

    #Botão cartaz cinema 1
    def frame_cine_img1(self):
        self.frame_principal.place_forget()
        self.frame_img1 = CTkFrame(self, width=1350, height=600)
        self.frame_img1.place(x=-5, y=100)

        self.img_fundo2_cinema = Image.open("Trabalho UC16/Imagens/cinema.png")
        self.img_fundo2_cinema = self.img_fundo2_cinema.resize((1350, 600))
        self.bg_img_fundo2_cinema = ImageTk.PhotoImage(self.img_fundo2_cinema)
        self.label_fundo_cinema2 = CTkLabel(self.frame_img1, image=self.bg_img_fundo2_cinema, text= "")
        self.label_fundo_cinema2.place(x=0, y=0, relwidth=1, relheight=1)

        self.img1_cinema_frame = PhotoImage(file="Trabalho UC16/Imagens/img1_cinema.png")
        self.posicao_img1_cinema_frame = CTkButton(self.frame_img1, command="", image=self.img1_cinema_frame, text="",
                                             width=100, height=100, hover_color=None, hover=None, fg_color="white")
        self.posicao_img1_cinema_frame.place(x=200, y=60)

        self.label_tit1_cinema_frame = CTkLabel(self.frame_img1, text="GUARDIÕES DA GALÁXIA - VOL. 3", fg_color="#CC1100",
                                      text_color="white", font=("Verdana", 30, "bold"), width=500, height=80)
        self.label_tit1_cinema_frame.place(x=690, y=70)
        self.label_cinema_frame_img1 = CTkLabel(self.frame_img1, text="\nAventura | Dublado | +12 anos \nSessões todos os dias: 11 à 16/05/2023\n15H40 - Exibição 2D\n18H40 - Exibição 3D\n21H30 - Exibição 2D", fg_color="black",  text_color ="white", font=("Roboto", 28, "bold"), width=500, height=250)
        self.label_cinema_frame_img1.place(x=650, y=150)

    # Botão cartaz cinema 2
    def frame_cine_img2(self):
        self.frame_principal.place_forget()
        self.frame_img2 = CTkFrame(self, width=1350, height=600)
        self.frame_img2.place(x=-5, y=100)

        self.img_fundo2_cinema = Image.open("Trabalho UC16/Imagens/cinema.png")
        self.img_fundo2_cinema = self.img_fundo2_cinema.resize((1350, 600))
        self.bg_img_fundo2_cinema = ImageTk.PhotoImage(self.img_fundo2_cinema)
        self.label_fundo_cinema2 = CTkLabel(self.frame_img2, image=self.bg_img_fundo2_cinema, text= "")
        self.label_fundo_cinema2.place(x=0, y=0, relwidth=1, relheight=1)

        self.img2_cinema_frame = PhotoImage(file="Trabalho UC16/Imagens/img2_cinema.png")
        self.posicao_img2_cinema_frame = CTkButton(self.frame_img2, command="", image=self.img2_cinema_frame, text="",
                                             width=100, height=100, hover_color=None, hover=None, fg_color="white")
        self.posicao_img2_cinema_frame.place(x=200, y=60)

        self.label_tit2_cinema_frame = CTkLabel(self.frame_img2, text="VELOZES E FURIOSOS 10", fg_color="#CC1100",
                                      text_color="white", font=("Verdana", 30, "bold"), width=500, height=80)
        self.label_tit2_cinema_frame.place(x=670, y=70)
        self.label_cinema_frame_img2 = CTkLabel(self.frame_img2, text="\nAventura e ação | Dublado | +12 anos \nSessões a partir de 17 de Maio!\n18H40 - Exibição 3D\n21H30 - Exibição 2D", fg_color="black",  text_color ="white", font=("Roboto", 28, "bold"), width=500, height=250)
        self.label_cinema_frame_img2.place(x=650, y=150)

    def frame_cine_img3(self):
        self.frame_principal.place_forget()
        self.frame_img3 = CTkFrame(self, width=1350, height=600)
        self.frame_img3.place(x=-5, y=100)

        self.img_fundo2_cinema = Image.open("Trabalho UC16/Imagens/cinema.png")
        self.img_fundo2_cinema = self.img_fundo2_cinema.resize((1350, 600))
        self.bg_img_fundo2_cinema = ImageTk.PhotoImage(self.img_fundo2_cinema)
        self.label_fundo_cinema2 = CTkLabel(self.frame_img3, image=self.bg_img_fundo2_cinema, text="")
        self.label_fundo_cinema2.place(x=0, y=0, relwidth=1, relheight=1)

        self.img3_cinema_frame = PhotoImage(file="Trabalho UC16/Imagens/img3_cinema.png")
        self.posicao_img3_cinema_frame = CTkButton(self.frame_img3,  image=self.img3_cinema_frame, text="",
                                             width=100, height=100, hover_color=None, hover=None, fg_color="white")
        self.posicao_img3_cinema_frame.place(x=200, y=60)

        self.label_tit3_cinema_frame = CTkLabel(self.frame_img3, text="A PEQUENA SEREIA", fg_color="#CC1100",
                                      text_color="white", font=("Verdana", 30, "bold"), width=500, height=80)
        self.label_tit3_cinema_frame.place(x=670, y=70)
        self.label_cinema_frame_img3 = CTkLabel(self.frame_img3, text="\nFantasia | Dublado | Livre \nSessões a partir de 25 de Maio!", fg_color="black",  text_color ="white", font=("Roboto", 28, "bold"), width=500, height=250)
        self.label_cinema_frame_img3.place(x=650, y=150)