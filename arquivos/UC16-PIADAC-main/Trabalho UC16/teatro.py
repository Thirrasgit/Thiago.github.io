import tkinter
import webbrowser
from tkinter import PhotoImage
from customtkinter import CTkFrame, CTkLabel, CTkButton

class FrontEndTeatro():
    def abrir_link(self, url):
        webbrowser.open_new(url)

    def menu_teatro(self):
        self.frame_principal.place_forget()
        self.frame_teatro = CTkFrame(self, fg_color='white', width=1350, height=600)
        self.frame_teatro.place(x=-5, y=100)

        # Imagem de destaque1
        self.imagem_destaque1 = PhotoImage(file="Trabalho UC16/Imagens/teatro1.png")
        self.posicao_imagem_destaque1 = CTkButton(self.frame_teatro, image=self.imagem_destaque1, fg_color="#1e192c", text='', width=260, height=180, hover=None, hover_color=None)
        self.posicao_imagem_destaque1.place(x=40, y=20)

        # Texto de apresentação1        
        self.texto_apresentacao1 = CTkLabel(self.frame_teatro, text_color='black', text="Quatro professores recolhidos em um manicômio vão à sala de psiquiatria, no qual passarão por uma sessão de análise investigativa, em que serão tiradas conclusões sobre os fatos narrados, provocando no público uma tensão entre a comédia e o drama.", font=("Arial", 21), fg_color='white', bg_color='black', width=80, height=5, justify='left', wraplength=900)
        self.texto_apresentacao1.place(x=380, y=70)


        self.info = CTkLabel(self.frame_teatro, text_color='black', text="DATA: 16 mai - 2023 • 20:00     LOCAL: Teatro Municipal", font=("Arial", 19, "bold"), width=80, height=5, justify='left')
        self.info.place(x=380, y=155)

        self.texto_saiba_mais = CTkLabel(self.frame_teatro, text="Saiba mais...", font=("Arial", 20, "bold"), text_color='black', fg_color='lightblue', width=80, height=5, justify='left')
        self.texto_saiba_mais.place(x=380, y=188)

        self.texto_saiba_mais.bind("<Button-1>", lambda event: self.abrir_link("https://www.google.com/maps/place/R.+Assis+Andrade,+540+-+Ros%C3%A1rio,+Conselheiro+Lafaiete+-+MG,+36400-067/@-20.6627158,-43.7884897,3a,75y,183.36h,90t/data=!3m7!1e1!3m5!1sbLV41O0JQlVQflPgg6EfFA!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fpanoid%3DbLV41O0JQlVQflPgg6EfFA%26cb_client%3Dsearch.gws-prod.gps%26w%3D86%26h%3D86%26yaw%3D183.3578%26pitch%3D0%26thumbfov%3D100!7i16384!8i8192!4m7!3m6!1s0xa3df885f14ac9b:0x1de77b554c8dde80!8m2!3d-20.6628552!4d-43.7884965!10e5!16s%2Fg%2F11c0w3ts3f"))

        

        # Imagem de destaque2
        self.imagem_destaque2 = PhotoImage(file="Trabalho UC16/Imagens/teatro2.png")
        self.posicao_imagem_destaque2 = CTkButton(self.frame_teatro, image=self.imagem_destaque2, fg_color="#1e192c", text='', width=260, height=180, hover=None, hover_color=None)
        self.posicao_imagem_destaque2.place(x=910, y=200)

        # Texto de apresentação2        
        self.texto_apresentacao2 = CTkLabel(self.frame_teatro, text_color='black', text="Não perca a peça 'Só Risos', em cartaz no Teatro Municipal.\nTrês palhaços encaram o caos e a comédia da vida em uma jornada hilária e emocionante.", font=("Arial", 21), fg_color='white', bg_color='black', width=50, height=5, justify='right', wraplength=900)
        self.texto_apresentacao2.place(x=40, y=260)

        self.info2 = CTkLabel(self.frame_teatro, text_color='black', text="DATA: 25/05/2023    HORÁRIO: 20h     LOCAL: Teatro Municipal", font=("Arial", 19, "bold"), width=80, height=5, justify='right')
        self.info2.place(x=90, y=330)

        self.texto_saiba_mais2 = CTkLabel(self.frame_teatro, text="Saiba mais...", text_color='black', font=("Arial", 20, "bold"), fg_color='lightblue', width=80, height=5, justify='right')
        self.texto_saiba_mais2.place(x=690, y=329)

        self.texto_saiba_mais2.bind("<Button-1>", lambda event: self.abrir_link("https://www.google.com/maps/place/R.+Assis+Andrade,+540+-+Ros%C3%A1rio,+Conselheiro+Lafaiete+-+MG,+36400-067/@-20.6627158,-43.7884897,3a,75y,183.36h,90t/data=!3m7!1e1!3m5!1sbLV41O0JQlVQflPgg6EfFA!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fpanoid%3DbLV41O0JQlVQflPgg6EfFA%26cb_client%3Dsearch.gws-prod.gps%26w%3D86%26h%3D86%26yaw%3D183.3578%26pitch%3D0%26thumbfov%3D100!7i16384!8i8192!4m7!3m6!1s0xa3df885f14ac9b:0x1de77b554c8dde80!8m2!3d-20.6628552!4d-43.7884965!10e5!16s%2Fg%2F11c0w3ts3f"))
        


        # Imagem de destaque3
        self.imagem_destaque3 = PhotoImage(file="Trabalho UC16/Imagens/teatro3.png")
        self.posicao_imagem_destaque3 = CTkButton(self.frame_teatro, image=self.imagem_destaque3, fg_color="#1e192c", text='', width=150, height=150, hover=None, hover_color=None)
        self.posicao_imagem_destaque3.place(x=40, y=380)

        # Texto de apresentação3        
        self.texto_apresentacao3 = CTkLabel(self.frame_teatro, text_color='black', text="Não perca 'Cortina Final', a peça que celebra a magia do teatro e mostra que, mesmo quando tudo parece perdido, a arte sempre encontra um caminho.", font=("Arial", 21), fg_color='white', bg_color='black', width=50, height=5, justify='left', wraplength=900)
        self.texto_apresentacao3.place(x=380, y=455)

        self.info3 = CTkLabel(self.frame_teatro, text_color='black', text="DATA: 15/06/2023     HORÁRIO: 20h     LOCAL: Teatro Municipal", font=("Arial", 19, "bold"), width=80, height=5, justify='right')
        self.info3.place(x=380, y=530)

        self.texto_saiba_mais3 = CTkLabel(self.frame_teatro, text="Saiba mais...", text_color='black', font=("Arial", 20, "bold"), fg_color='lightblue', width=80, height=5, justify='left')
        self.texto_saiba_mais3.place(x=985, y=528)

        self.texto_saiba_mais3.bind("<Button-1>", lambda event: self.abrir_link("https://www.google.com/maps/place/R.+Assis+Andrade,+540+-+Ros%C3%A1rio,+Conselheiro+Lafaiete+-+MG,+36400-067/@-20.6627158,-43.7884897,3a,75y,183.36h,90t/data=!3m7!1e1!3m5!1sbLV41O0JQlVQflPgg6EfFA!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fpanoid%3DbLV41O0JQlVQflPgg6EfFA%26cb_client%3Dsearch.gws-prod.gps%26w%3D86%26h%3D86%26yaw%3D183.3578%26pitch%3D0%26thumbfov%3D100!7i16384!8i8192!4m7!3m6!1s0xa3df885f14ac9b:0x1de77b554c8dde80!8m2!3d-20.6628552!4d-43.7884965!10e5!16s%2Fg%2F11c0w3ts3f"))


        
