from tkinter import PhotoImage
from PIL import Image, ImageTk
from customtkinter import *

class FrontEndMusica():
    def menu_musica(self):
        self.frame_principal.pack_forget()
        self.frame_musica = CTkFrame(self, fg_color='black', width=1350, height=600)
        self.frame_musica.place(x=-5, y=100)

        #Imagem de fundo
        img_fundo_musica = Image.open("Trabalho UC16/Imagens/fundo.png")
        img_fundo_musica = img_fundo_musica.resize((1350, 600))
        bg_img_fundo_musica = ImageTk.PhotoImage(img_fundo_musica)
        label_img_fundo_musica = CTkLabel(self.frame_musica, image=bg_img_fundo_musica,text='')
        label_img_fundo_musica.place(x=0, y=0, relwidth=1,relheight=1)
        self.imagem1 = PhotoImage(file="Trabalho UC16/Imagens/img_musica1.png")
        self.local_imagem1 = CTkButton(self.frame_musica, text='',image= self.imagem1 , fg_color="white", width=100, height=100, hover_color=None, hover=None, command=self.exibir_musica)
        self.local_imagem1.place(x=0, y=100)

        self.imagem2 = PhotoImage(file="Trabalho UC16/Imagens/img_musica2.png")
        self.local_imagem2 = CTkButton(self.frame_musica, text='',image= self.imagem2 , fg_color="white", width=100, height=100, hover_color=None, hover=None, command=self.exibir_musica2)
        self.local_imagem2.place(x=450, y=100)

        self.imagem3 = PhotoImage(file="Trabalho UC16/Imagens/img_musica3.png")
        self.local_imagem3 = CTkButton(self.frame_musica, text='',image= self.imagem3 , fg_color="white", width=100, height=100, hover_color=None, hover=None, command=self.exibir_musica3)
        self.local_imagem3.place(x=900, y=100)

        self.imagem4 = PhotoImage(file="Trabalho UC16/Imagens/img_musica4.png")
        self.local_imagem4 = CTkButton(self.frame_musica, text='',image= self.imagem4 , fg_color="white", width=100, height=100, hover_color=None, hover=None, command=self.exibir_musica4)
        self.local_imagem4.place(x=0, y=350)

        self.imagem5 = PhotoImage(file="Trabalho UC16/Imagens/img_musica5.png")
        self.local_imagem5 = CTkButton(self.frame_musica, text='',image= self.imagem5 , fg_color="white", width=100, height=100, hover_color=None, hover=None, command=self.exibir_musica5)
        self.local_imagem5.place(x=450, y=350)

        self.imagem6 = PhotoImage(file="Trabalho UC16/Imagens/img_musica6.png")
        self.local_imagem6 = CTkButton(self.frame_musica, text='',image= self.imagem6 , fg_color="white", width=100, height=100, hover_color=None, hover=None, command=self.exibir_musica6)
        self.local_imagem6.place(x=900, y=350)
            
    def exibir_musica(self):
        self.frame_principal.place_forget()
        self.frame_musica = CTkFrame(self, fg_color='#1C1C1C', width=1350, height=600)
        self.frame_musica.place(x=-5,y=100)
        
        self.img = PhotoImage(file="Trabalho UC16/Imagens/img1B_musica.png")
        self.local_img = CTkButton(self.frame_musica, text='',image=self.img, fg_color="transparent", width=100, height=100, hover_color=None, hover=None)
        self.local_img.place(x=-3, y=-5)
        

        self.text_evento2= CTkLabel(self.frame_musica, text='Descrição do evento',fg_color="transparent",text_color= "white",font=("Arial", 30, "bold"))
        self.text_evento2.place(x=100, y=360)

        self.text_evento2= CTkLabel(self.frame_musica, text='Open Food\nOpen Chopp e Bebidas Típicas\n Open Refrigerante e Águas\nAtrações Musicais: \n@trioforrozeando (Forró ) / @raylanoliveira ( modão de viola)',fg_color="transparent",text_color= "white",font=("Arial", 15, 'bold'))
        self.text_evento2.place(x=40, y=430)

        self.text_evento2= CTkLabel(self.frame_musica, text='20 mai - 2023 • 16:00 > 21 mai - 2023 • 00:00',fg_color="transparent", text_color= "white",font=("Arial", 17,"bold" ))
        self.text_evento2.place(x=860, y=385)
        self.text_evento2= CTkLabel(self.frame_musica, text='Evento presencial em Rancho do Sheriff ,\n Conselheiro Lafaiete - MG',fg_color="transparent", text_color= "white",font=("Arial", 17,"bold" ))
        self.text_evento2.place(x=860, y=460)
        self.text_evento2.bind("<Button-1>", lambda event: self.abrir_link("https://www.google.com/maps/@-20.6601919,-43.7691515,3a,75y,274.13h,79.63t/data=!3m7!1e1!3m5!1sKQi87LLVwPN9qxnCXfSntA!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fpanoid%3DKQi87LLVwPN9qxnCXfSntA%26cb_client%3Dmaps_sv.tactile.gps%26w%3D203%26h%3D100%26yaw%3D323.20914%26pitch%3D0%26thumbfov%3D100!7i16384!8i8192"))


        self.icone_calendadario=PhotoImage(file="Trabalho UC16/Imagens/cale.png")
        self.posicaocale=CTkLabel(self.frame_musica,text="", image=self.icone_calendadario, width=50, height=50)
        self.posicaocale.place(x=780, y=370)
        self.icone_calendadario=PhotoImage(file="Trabalho UC16/Imagens/local.png")
        self.posicaocale=CTkLabel(self.frame_musica,text="", image=self.icone_calendadario, width=50, height=50)
        self.posicaocale.place(x=780, y=440)

    def exibir_musica2(self):
        self.frame_principal.place_forget()
        self.frame_musica = CTkFrame(self, fg_color='#1C1C1C', width=1350, height=600)
        self.frame_musica.place(x=-5,y=100)
        
        self.img = PhotoImage(file="Trabalho UC16/Imagens/img2B_musica.png")
        self.local_img = CTkButton(self.frame_musica, text='',image=self.img, fg_color="transparent", width=100, height=100, hover_color=None, hover=None)
        self.local_img.place(x=-3, y=-5)
        

        self.text_evento2= CTkLabel(self.frame_musica, text='Descrição do evento',fg_color="transparent",text_color= "white",font=("Arial", 30, "bold"))
        self.text_evento2.place(x=100, y=360)

        self.text_evento2= CTkLabel(self.frame_musica, text='GRAVAÇÃO DVD SUNSET - MADU CAMPOS',fg_color="transparent",text_color= "white",font=("Arial", 15, 'bold'))
        self.text_evento2.place(x=100, y=430)

        self.text_evento2= CTkLabel(self.frame_musica, text='14 mai - 2023 • 13:00 > 14 mai - 2023 • 22:30',fg_color="transparent", text_color= "white",font=("Arial", 17,"bold" ))
        self.text_evento2.place(x=860, y=385)
        self.text_evento2= CTkLabel(self.frame_musica, text='Evento presencial em Local a definir,\nConselheiro Lafaiete - MG',fg_color="transparent", text_color= "white",font=("Arial", 17,"bold" ))
        self.text_evento2.place(x=860, y=460)
        


        self.icone_calendadario=PhotoImage(file="Trabalho UC16/Imagens/cale.png")
        self.posicaocale=CTkLabel(self.frame_musica,text="", image=self.icone_calendadario, width=50, height=50)
        self.posicaocale.place(x=780, y=370)
        self.icone_calendadario=PhotoImage(file="Trabalho UC16/Imagens/local.png")
        self.posicaocale=CTkLabel(self.frame_musica,text="", image=self.icone_calendadario, width=50, height=50)
        self.posicaocale.place(x=780, y=440)

    def exibir_musica3(self):
        self.frame_principal.place_forget()
        self.frame_musica = CTkFrame(self, fg_color='#1C1C1C', width=1350, height=600)
        self.frame_musica.place(x=-5,y=100)
        
        self.img = PhotoImage(file="Trabalho UC16/Imagens/img3B_musica.png")
        self.local_img = CTkButton(self.frame_musica, text='',image=self.img, fg_color="transparent", width=100, height=100, hover_color=None, hover=None)
        self.local_img.place(x=-3, y=-5)
        

        self.text_evento2= CTkLabel(self.frame_musica, text='Descrição do evento',fg_color="transparent",text_color= "white",font=("Arial", 30, "bold"))
        self.text_evento2.place(x=100, y=360)

        self.text_evento2= CTkLabel(self.frame_musica, text='Preparados para o melhor rolezinho universitário da cidade?\nVem com a Arcada para mais um rolê sensacional!\nCom atrações imperdíveis\nJean e FelipProfex  \nDj Lukas Moura',fg_color="transparent",text_color= "white",font=("Arial", 15, 'bold'))
        self.text_evento2.place(x=40, y=430)

        self.text_evento2= CTkLabel(self.frame_musica, text='20 mai - 2023 • 16:00 > 21 mai - 2023 • 00:00',fg_color="transparent", text_color= "white",font=("Arial", 17,"bold" ))
        self.text_evento2.place(x=860, y=385)
        self.text_evento2= CTkLabel(self.frame_musica, text='Evento presencial em Rooftop Bhuda, \nConselheiro Lafaiete - MG',fg_color="transparent", text_color= "white",font=("Arial", 17,"bold" ))
        self.text_evento2.place(x=860, y=460)
        self.text_evento2.bind("<Button-1>", lambda event: self.abrir_link("https://www.google.com/maps/place/Rooftop+Bhuda/@-20.6868935,-43.7868926,3a,75y,90t/data=!3m8!1e1!3m6!1sAF1QipPBQLaeGmleGRe0aeTXXqCxiu1vGCZQ6TfN3X7Y!2e10!3e11!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipPBQLaeGmleGRe0aeTXXqCxiu1vGCZQ6TfN3X7Y%3Dw86-h86-k-no-pi-0-ya0-ro-0-fo100!7i6080!8i3040!4m15!1m7!3m6!1s0xa3df63915e7d2d:0x67c8e28a8de8944a!2sRooftop+Bhuda!8m2!3d-20.653965!4d-43.7905385!16s%2Fg%2F11ngtpmjsn!3m6!1s0xa3df63915e7d2d:0x67c8e28a8de8944a!8m2!3d-20.653965!4d-43.7905385!10e5!16s%2Fg%2F11ngtpmjsn"))


        self.icone_calendadario=PhotoImage(file="Trabalho UC16/Imagens/cale.png")
        self.posicaocale=CTkLabel(self.frame_musica,text="", image=self.icone_calendadario, width=50, height=50)
        self.posicaocale.place(x=780, y=370)

        self.icone_calendadario=PhotoImage(file="Trabalho UC16/Imagens/local.png")
        self.posicaocale=CTkLabel(self.frame_musica,text="", image=self.icone_calendadario, width=50, height=50)
        self.posicaocale.place(x=780, y=440)


    def exibir_musica4(self):
        self.frame_principal.place_forget()
        self.frame_musica = CTkFrame(self, fg_color='#1C1C1C', width=1350, height=600)
        self.frame_musica.place(x=-5,y=100)
        
        self.img = PhotoImage(file="Trabalho UC16/Imagens/img4B_musica.png")
        self.local_img = CTkButton(self.frame_musica, text='',image=self.img, fg_color="transparent", width=100, height=100, hover_color=None, hover=None)
        self.local_img.place(x=-3, y=-5)
        

        self.text_evento2= CTkLabel(self.frame_musica, text='Descrição do evento',fg_color="transparent",text_color= "white",font=("Arial", 30, "bold"))
        self.text_evento2.place(x=140, y=360)

        self.text_evento2= CTkLabel(self.frame_musica, text='O evento contará com a participação de 16 artistas, que se apresentarão \n em um palco 360º interativo, em um rooftop nas alturas.\n\n Confira a escalação de peso para essa edição:\n\n Buda Fuse • Hotway • Tallez • Jackal • Shire • Hypers\n • Kast • Roaz • Loskar • The Ghost  •\n Lowaresbass • Dahauz • Walto • Rafael Miranda • + 02 Dj contest',fg_color="transparent",text_color= "white",font=("Arial", 15, 'bold'))
        self.text_evento2.place(x=40, y=430)

        self.text_evento2= CTkLabel(self.frame_musica, text='13 mai - 2023 • 13:00 > 14 mai - 2023 • 00:00',fg_color="transparent", text_color= "white",font=("Arial", 17,"bold" ))
        self.text_evento2.place(x=860, y=385)
        self.text_evento2= CTkLabel(self.frame_musica, text='Evento presencial em Rooftop Bhuda, \nConselheiro Lafaiete - MG',fg_color="transparent", text_color= "white",font=("Arial", 17,"bold" ))
        self.text_evento2.place(x=860, y=460)
        self.text_evento2.bind("<Button-1>", lambda event: self.abrir_link("https://www.google.com/maps/place/Rooftop+Bhuda/@-20.6868935,-43.7868926,3a,75y,90t/data=!3m8!1e1!3m6!1sAF1QipPBQLaeGmleGRe0aeTXXqCxiu1vGCZQ6TfN3X7Y!2e10!3e11!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipPBQLaeGmleGRe0aeTXXqCxiu1vGCZQ6TfN3X7Y%3Dw86-h86-k-no-pi-0-ya0-ro-0-fo100!7i6080!8i3040!4m15!1m7!3m6!1s0xa3df63915e7d2d:0x67c8e28a8de8944a!2sRooftop+Bhuda!8m2!3d-20.653965!4d-43.7905385!16s%2Fg%2F11ngtpmjsn!3m6!1s0xa3df63915e7d2d:0x67c8e28a8de8944a!8m2!3d-20.653965!4d-43.7905385!10e5!16s%2Fg%2F11ngtpmjsn"))


        self.icone_calendadario=PhotoImage(file="Trabalho UC16/Imagens/cale.png")
        self.posicaocale=CTkLabel(self.frame_musica,text="", image=self.icone_calendadario, width=50, height=50)
        self.posicaocale.place(x=780, y=370)
        self.icone_calendadario=PhotoImage(file="Trabalho UC16/Imagens/local.png")
        self.posicaocale=CTkLabel(self.frame_musica,text="", image=self.icone_calendadario, width=50, height=50)
        self.posicaocale.place(x=780, y=440)
        
    def exibir_musica5(self):
        self.frame_principal.place_forget()
        self.frame_musica = CTkFrame(self, fg_color='#1C1C1C', width=1350, height=600)
        self.frame_musica.place(x=-5,y=100)
        
        self.img = PhotoImage(file="Trabalho UC16/Imagens/img5B_musica.png")
        self.local_img = CTkButton(self.frame_musica, text='',image=self.img, fg_color="transparent", width=100, height=100, hover_color=None, hover=None)
        self.local_img.place(x=-3, y=-5)
        

        self.text_evento2= CTkLabel(self.frame_musica, text='Descrição do evento',fg_color="transparent",text_color= "white",font=("Arial", 30, "bold"))
        self.text_evento2.place(x=100, y=360)

        self.text_evento2= CTkLabel(self.frame_musica, text='Bem-vindos , bem-vindas e bem-vindes à nossa festa\nNesta festa vamos deixar de lado nossas identidades!\ncotidianas e nos permitir experimentar um pouco de\n mistério e muita diversão.\n\nATRAÇÕES:\nDyogho - Dj/Tribal/CL\nJeff - Dj/Funk/BH ',fg_color="transparent",text_color= "white",font=("Arial", 15, 'bold'))
        self.text_evento2.place(x=40, y=430)

        self.text_evento2= CTkLabel(self.frame_musica, text='27 mai - 2023 • 23:00 > 28 mai - 2023 • 06:00',fg_color="transparent", text_color= "white",font=("Arial", 17,"bold" ))
        self.text_evento2.place(x=860, y=385)
        self.text_evento2= CTkLabel(self.frame_musica, text='Evento presencial em Milênio Danceteria \n Conselheiro Lafaiete - MG',fg_color="transparent", text_color= "white",font=("Arial", 17,"bold" ))
        self.text_evento2.place(x=860, y=460)
        self.text_evento2.bind("<Button-1>", lambda event: self.abrir_link("https://www.google.com/maps/@-20.6647449,-43.786072,3a,75y,348.26h,79.93t/data=!3m6!1e1!3m4!1sf5EQOJCEPQMZ_5uhCsBKng!2e0!7i16384!8i8192"))


        self.icone_calendadario=PhotoImage(file="Trabalho UC16/Imagens/cale.png")
        self.posicaocale=CTkLabel(self.frame_musica,text="", image=self.icone_calendadario, width=50, height=50)
        self.posicaocale.place(x=780, y=370)

        self.icone_calendadario=PhotoImage(file="Trabalho UC16/Imagens/local.png")
        self.posicaocale=CTkLabel(self.frame_musica,text="", image=self.icone_calendadario, width=50, height=50)
        self.posicaocale.place(x=780, y=440)

    def exibir_musica6(self):
        self.frame_principal.place_forget()
        self.frame_musica = CTkFrame(self, fg_color='#1C1C1C', width=1350, height=600)
        self.frame_musica.place(x=-5,y=100)
        
        self.img = PhotoImage(file="Trabalho UC16/Imagens/img6B_musica.png")
        self.local_img = CTkButton(self.frame_musica, text='',image=self.img, fg_color="transparent", width=100, height=100, hover_color=None, hover=None)
        self.local_img.place(x=-3, y=-5)
        

        self.text_evento2= CTkLabel(self.frame_musica, text='Descrição do evento',fg_color="transparent",text_color= "white",font=("Arial", 30, "bold"))
        self.text_evento2.place(x=100, y=360)

        self.text_evento2= CTkLabel(self.frame_musica, text='Censura: 18 anos.\nIndispensável apresentação de documento com foto.\n Não aceitamos fotos de documentos.',fg_color="transparent",text_color= "white",font=("Arial", 15, 'bold'))
        self.text_evento2.place(x=40, y=430)

        self.text_evento2= CTkLabel(self.frame_musica, text='20 mai - 2023 • 22:00 > 21 mai - 2023 • 04:00',fg_color="transparent", text_color= "white",font=("Arial", 17,"bold" ))
        self.text_evento2.place(x=860, y=385)
        self.text_evento2= CTkLabel(self.frame_musica, text='Evento presencial em 147 Club,\n Conselheiro Lafaiete - MG',fg_color="transparent", text_color= "white",font=("Arial", 17,"bold" ))
        self.text_evento2.place(x=860, y=460)
        self.text_evento2.bind("<Button-1>", lambda event: self.abrir_link("https://www.google.com/maps/@-20.658916,-43.787386,3a,75y,181.81h,94.72t/data=!3m6!1e1!3m4!1s_mkc9TVkWcmaWmTuJA2hjA!2e0!7i16384!8i8192"))


        self.icone_calendadario=PhotoImage(file="Trabalho UC16/Imagens/cale.png")
        self.posicaocale=CTkLabel(self.frame_musica,text="", image=self.icone_calendadario, width=50, height=50)
        self.posicaocale.place(x=780, y=370)
        self.icone_calendadario=PhotoImage(file="Trabalho UC16/Imagens/local.png")
        self.posicaocale=CTkLabel(self.frame_musica,text="", image=self.icone_calendadario, width=50, height=50)
        self.posicaocale.place(x=780, y=440)