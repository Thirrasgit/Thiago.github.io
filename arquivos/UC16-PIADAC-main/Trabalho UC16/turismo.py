from tkinter import PhotoImage
from PIL import Image, ImageTk
from customtkinter import *

class FrontEndTurismo():
    def menu_turismo(self):
        self.frame_principal.pack_forget()
        self.frame_turismo = CTkFrame(self, fg_color='black', width=1350, height=600)
        self.frame_turismo.place(x=-5, y=100)

        #Imagem de fundo
        background = Image.open("Trabalho UC16/Imagens/fundo_escuro.png")
        background = background.resize((1350, 600))
        bg_background = ImageTk.PhotoImage(background)
        label_background = CTkLabel(self.frame_turismo, image=bg_background,text='')
        label_background.place(x=0, y=0, relwidth=1,relheight=1)

        self.matriz_cristo = PhotoImage(file="Trabalho UC16/Imagens/img1_turismo.png")
        self.local_cristo = CTkButton(self.frame_turismo, text='',image= self.matriz_cristo , fg_color="black", width=100, height=100, hover_color=None, hover=None, command=self.exibir_cristo)
        self.local_cristo.place(x=0, y=35)
        self.texto_cristo = CTkFrame(self.frame_turismo, bg_color="white", width=100, height=20).place()

        self.matriz = PhotoImage(file="Trabalho UC16/Imagens/img2_turismo.png")
        self.local_matriz = CTkButton(self.frame_turismo, text='',image= self.matriz , fg_color="black", width=100, height=100, hover_color=None, hover=None, command=self.exibir_matriz)
        self.local_matriz.place(x=470, y=35)

        self.trem = PhotoImage(file="Trabalho UC16/Imagens/img3_turismo.png")
        self.local_trem = CTkButton(self.frame_turismo, text='',image= self.trem , fg_color="black", width=100, height=100, hover_color=None, hover=None, command=self.exibir_trem)
        self.local_trem.place(x=940, y=35)

        self.parque = PhotoImage(file="Trabalho UC16/Imagens/img4_turismo.png")
        self.local_parque = CTkButton(self.frame_turismo, text='',image= self.parque , fg_color="black", width=100, height=100, hover_color=None, hover=None, command=self.exibir_parque)
        self.local_parque.place(x=0, y=315)

        self.sao_sebastiao = PhotoImage(file="Trabalho UC16/Imagens/img5_turismo.png")
        self.local_sao_sebastiao = CTkButton(self.frame_turismo, text='',image= self.sao_sebastiao , fg_color="black", width=100, height=100, hover_color=None, hover=None, command=self.exibir_sao_sebastiao)
        self.local_sao_sebastiao.place(x=470, y=315)

        self.museu = PhotoImage(file="Trabalho UC16/Imagens/img6_turismo.png")
        self.local_museu = CTkButton(self.frame_turismo, text='',image= self.museu , fg_color="black", width=100, height=100, hover_color=None, hover=None, command=self.exibir_museu)
        self.local_museu.place(x=940, y=315)
            
    def exibir_cristo(self):
        self.frame_principal.place_forget()
        self.frame_cristo = CTkFrame(self, width=1350, height=600)
        self.frame_cristo.place(x=-5, y=100)

        self.bg_cristo = Image.open("Trabalho UC16/Imagens/bg_cristo.png")
        self.bg_cristo = self.bg_cristo.resize((1350, 600))
        self.bg_cristo = ImageTk.PhotoImage(self.bg_cristo)
        self.label_fundo_cristo = CTkLabel(self.frame_cristo, image=self.bg_cristo, text= "")
        self.label_fundo_cristo.place(x=0, y=0, relwidth=1, relheight=1)

        self.cristo_titulo = CTkLabel(self.frame_cristo, text="Praça do Cristo Redentor", fg_color="#6495ED",
        text_color="white", font=("Arial", 30, "bold"), width=500, height=80).place(x=40, y=70)

        self.cristo_texto = CTkLabel(self.frame_cristo, text="A praça é famosa pela estátua do Cristo Redentor,\nque fica no topo de uma colina e é visível de muitos pontos da cidade.", fg_color="#4682B4",  text_color ="white",bg_color="white", font=("Arial", 20), width=200, height=0).place(x=80, y=500)


    def exibir_matriz(self):
        self.frame_principal.place_forget()
        self.frame_matriz = CTkFrame(self, width=1350, height=600)
        self.frame_matriz.place(x=-5, y=100)

        self.bg_matriz = Image.open("Trabalho UC16/Imagens/bg_matriz.png")
        self.bg_matriz = self.bg_matriz.resize((1350, 600))
        self.bg_matriz = ImageTk.PhotoImage(self.bg_matriz)
        self.label_fundo_matriz = CTkLabel(self.frame_matriz, image=self.bg_matriz, text= "")
        self.label_fundo_matriz.place(x=0, y=0, relwidth=1, relheight=1)

        self.matriz_titulo = CTkLabel(self.frame_matriz, text="Praça da Matriz", fg_color="#6495ED",
        text_color="white", font=("Arial", 30, "bold"), width=500, height=80).place(x=40, y=70)

        self.matriz_texto = CTkLabel(self.frame_matriz, text="Sendo palco de eventos culturais, feiras e celebrações religiosas.\nA praça ainda conserva monumentos históricos, como a estátua do bandeiras\n Fernão Dias e o obelisco em homenagem aos combatentes da Revolução de 1930.", fg_color="#4682B4",  text_color ="white",bg_color="white", font=("Arial", 20), width=200, height=0).place(x=80, y=500)
        
    def exibir_trem(self):
        self.frame_principal.place_forget()
        self.frame_trem = CTkFrame(self, width=1350, height=600)
        self.frame_trem.place(x=-5, y=100)

        self.bg_trem = Image.open("Trabalho UC16/Imagens/bg_trem.png")
        self.bg_trem = self.bg_trem.resize((1350, 600))
        self.bg_trem = ImageTk.PhotoImage(self.bg_trem)
        self.label_fundo_trem = CTkLabel(self.frame_trem, image=self.bg_trem, text= "")
        self.label_fundo_trem.place(x=0, y=0, relwidth=1, relheight=1)

        self.trem_titulo = CTkLabel(self.frame_trem, text="Museu Ferroviário", fg_color="#6495ED",
        text_color="white", font=("Arial", 30, "bold"), width=500, height=80).place(x=40, y=70)

        self.trem_texto = CTkLabel(self.frame_trem, text="O Museu mostra a importante atração turística da cidade foi fundada por \n uma organização sem fins lucrativos com a finalidade de manter a história ferroviária da região.", fg_color="#4682B4",  text_color ="white",bg_color="white", font=("Arial", 20), width=200, height=0).place(x=80, y=500)  

    def exibir_parque(self):
        self.frame_principal.place_forget()
        self.frame_parque = CTkFrame(self, width=1350, height=600)
        self.frame_parque.place(x=-5, y=100)

        self.bg_parque = Image.open("Trabalho UC16/Imagens/bg_parque.png")
        self.bg_parque = self.bg_parque.resize((1350, 600))
        self.bg_parque = ImageTk.PhotoImage(self.bg_parque)
        self.label_fundo_parque = CTkLabel(self.frame_parque, image=self.bg_parque, text= "")
        self.label_fundo_parque.place(x=0, y=0, relwidth=1, relheight=1)

        self.parque_titulo = CTkLabel(self.frame_parque, text="Parque de Exposições ", fg_color="#6495ED",
        text_color="white", font=("Arial", 30, "bold"), width=500, height=80).place(x=40, y=70)

        self.parque_texto = CTkLabel(self.frame_parque, text="inaugurado em 1973 com o objetivo de sediar eventos agropecuários, industriais, comerciais e culturais na região.\n O terreno de 130 mil metros quadrados foi doado pela Companhia Siderúrgica Belgo-Mineira,\n que tinha interesse em incentivar o desenvolvimento da cidade.", fg_color="#4682B4",  text_color ="white",bg_color="white", font=("Arial", 20), width=200, height=0).place(x=80, y=500)
        
    def exibir_sao_sebastiao(self):
        self.frame_principal.place_forget()
        self.frame_sao_sebastiao = CTkFrame(self, width=1350, height=600)
        self.frame_sao_sebastiao.place(x=-5, y=100)

        self.bg_sao_sebastiao = Image.open("Trabalho UC16/Imagens/bg_sao_sebatiao.png")
        self.bg_sao_sebastiao = self.bg_sao_sebastiao.resize((1350, 600))
        self.bg_sao_sebastiao = ImageTk.PhotoImage(self.bg_sao_sebastiao)
        self.label_fundo_sao_sebastiao = CTkLabel(self.frame_sao_sebastiao, image=self.bg_sao_sebastiao, text= "")
        self.label_fundo_sao_sebastiao.place(x=0, y=0, relwidth=1, relheight=1)

        self.sao_sebastiao_titulo = CTkLabel(self.frame_sao_sebastiao, text="Praça São Sebastião", fg_color="#6495ED",
        text_color="white", font=("Arial", 30, "bold"), width=500, height=80).place(x=40, y=70)

        self.sao_sebastiao_texto = CTkLabel(self.frame_sao_sebastiao, text="A Praça São Sebastião era um lugar de comércio e entretenimento com feiras e música,\n mas em 1970 foi transformada em um parque públicocom áreas verdes e playgrounds.\n Com o tempo, o parque se tornou um lugar popular para esportes, relaxamento e socialização.\n Em 2010, foi revitalizado com melhorias como uma pista de skate e um anfiteatro.", fg_color="#4682B4",  text_color ="white",bg_color="white", font=("Arial", 20), width=200, height=0).place(x=80, y=500)

    def exibir_museu(self):
        self.frame_principal.place_forget()
        self.frame_museu = CTkFrame(self, width=1350, height=600)
        self.frame_museu.place(x=-5, y=100)

        self.bg_museu = Image.open("Trabalho UC16/Imagens/bg_museu.png")
        self.bg_museu = self.bg_museu.resize((1350, 600))
        self.bg_museu = ImageTk.PhotoImage(self.bg_museu)
        self.label_fundo_museu = CTkLabel(self.frame_museu, image=self.bg_museu, text= "")
        self.label_fundo_museu.place(x=0, y=0, relwidth=1, relheight=1)

        self.museu_titulo = CTkLabel(self.frame_museu, text="Museu", fg_color="#6495ED",
        text_color="white", font=("Arial", 30, "bold"), width=500, height=80).place(x=40, y=70)

        self.museu_texto = CTkLabel(self.frame_museu, text="o Museu de Conselheiro Lafaiete, que foi criado em 1954 por Antônio Perdigão a partir de sua coleção de arte e objetos históricos.\n O museu possui mais de 6.000 peças que contam a história da região e está localizado em uma antiga residência adaptada.\n Suas principais atrações são a Sala das Carruagens, Sala dos Troféus, acervo de arte sacra e peças arqueológicas.\n O museu é um ponto turístico importante e oferece exposições temporárias, eventos culturais e atividades educativas.", fg_color="#4682B4",  text_color ="white",bg_color="white", font=("Arial", 20), width=200, height=0).place(x=80, y=500)

        