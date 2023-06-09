from customtkinter import *
from tkinter import PhotoImage
from tkinter import messagebox
import smtplib # Biblioteca utilizada para enviar e-mails
import email.message # Biblioteca utilizada para formatar e-mails

class FrontEndContato():
    def menu_contato(self):
            self.frame_contato = CTkFrame(self, fg_color='white', width=1350, height=600)
            self.frame_contato.place(x=-5, y=100)

            self.photo = PhotoImage(file='Trabalho UC16/Imagens/foto contato1.png')
            self.image_label = CTkLabel(self.frame_contato, text ='', image = self.photo)
            self.image_label.place(x=0, y=0)

            self.frame_secun_contato = CTkFrame(self, fg_color='#1e192c', width=1350, height=390, corner_radius=-10)
            self.frame_secun_contato.place(x=0, y=210)

            self.frame_consertar_cont = CTkFrame(self, fg_color='#1e192c', width=1350, height=6, corner_radius=-10)
            self.frame_consertar_cont.place(x=0, y=599)

            self.frame_info_contato = CTkFrame(self, fg_color='#F8F8F8', width=500, height=500, border_color='#1e192c', border_width=2, corner_radius=-10)
            self.frame_info_contato.place(x=700, y=150)

            self.titulo_contato = CTkLabel(self.frame_info_contato, text='ENTRE EM CONTATO \nCONOSCO', text_color='#1e192c', fg_color='#F8F8F8', font=('Verdana', 35, 'bold'))
            self.titulo_contato.place(x=50, y=20)

            self.telefone_contato = CTkLabel(self.frame_secun_contato, text='TELEFONE', text_color='white', fg_color='#1e192c', font=('Verdana', 20, 'bold'))
            self.telefone_contato.place(x=285, y=30)

            self.info_tele_contato = CTkLabel(self.frame_secun_contato, text='(31) 94002-8922 -- (31) 91234-5678', text_color='white', fg_color='#1e192c', font=('Arial', 17))
            self.info_tele_contato.place(x=200, y=70)

            self.localizacao_contato = CTkLabel(self.frame_secun_contato, text='LOCALIZAÇÃO', text_color='white', fg_color='#1e192c', font=('Verdana', 20, 'bold'))
            self.localizacao_contato.place(x=260, y=140)

            self.info_local_contato = CTkLabel(self.frame_secun_contato, text='Rua Tavares de Melo - 630 - Centro \n Cons. Lafaiete/MG', text_color='white', fg_color='#1e192c', font=('Arial', 17))
            self.info_local_contato.place(x=200, y=180)

            self.redes_sociais_contato = CTkLabel(self.frame_secun_contato, text='REDES SOCIAIS', text_color='white', fg_color='#1e192c', font=('Verdana', 20, 'bold'))
            self.redes_sociais_contato.place(x=250, y=260)

            self.info_redes_contato = CTkLabel(self.frame_secun_contato, text='Instagram: @lafacult \nFacebook: Lafaiete Cultural \nE-mail: lafaietecultural@gmail.com', text_color='white', fg_color='#1e192c', font=('Arial', 17))
            self.info_redes_contato.place(x=210, y=300)

            self.cabecalho = CTkEntry(self.frame_info_contato, width=350, height=45, border_color='#1e192c', bg_color='white',fg_color='#F8F8F8', placeholder_text= 'Cabeçalho.', text_color='#1e192c', placeholder_text_color='#7C7C7C', font=('Verdana', 15))
            self.cabecalho.place(x=75, y=140)

            self.email_contato = CTkEntry(self.frame_info_contato, width=350, height=45, border_color='#1e192c', bg_color='white',fg_color='#F8F8F8', placeholder_text= 'Seu E-mail.', text_color='#1e192c', placeholder_text_color='#7C7C7C', font=('Verdana', 15))
            self.email_contato.place(x=75, y=220)

            self.assunto = CTkEntry(self.frame_info_contato, text_color='#1e192c', width=350, height=45, border_color='#1e192c', bg_color='white',fg_color='#F8F8F8', placeholder_text= 'Assunto', placeholder_text_color='#7C7C7C', font=('Verdana', 15))
            self.assunto.place(x=75, y=300)

            self.botao_conf_contato = CTkButton(self.frame_info_contato, width=270, height=55, text= 'CONFIRMAR', font=('Verdana', 20, 'bold'), fg_color='#1e192c', hover_color='#615E6B', command=self.enviar_email)
            self.botao_conf_contato.place(x=115, y=390)

    def enviar_email(self): 
        corpo_email = f"""Você recebeu um e-mail de: {self.email_contato.get()}.<br>{self.assunto.get()}
        """
        
        mensagem = email.message.Message() # Instanciando a classe email.message.Message
        
        # Atribuindo as informações do e-mail (assunto, remetente e destinatário) e o tipo de texto como HTML
        mensagem['Subject'] = self.cabecalho.get()
        mensagem['From'] = "trabalhosenacuc16@gmail.com"
        mensagem['To'] = "trabalhosenacuc16@gmail.com"
        mensagem.add_header('Content-Type', 'text/html')
        
        mensagem.set_payload(corpo_email) #Definindo a variável "corpo_email" como conteúdo do e-mail a ser enviado
        
        senha = "qizkujqesroyigwv"
        servidor = smtplib.SMTP('smtp.gmail.com: 587') # Acessando o endereço do servidor e porta do Outlook
        servidor.starttls() # Ativando a criptografia TLS
        servidor.login(mensagem['From'], senha) # Autenticando o remetente, com nome de usuário e senha
        
        try:
            servidor.sendmail(mensagem['From'], [mensagem['To']], mensagem.as_string().encode('latin1')) # Envia a mensagem para o destinatário
            messagebox.showinfo(title='ATENÇÃO', message='E-MAIL ENVIADO')
        except:
            messagebox.showerror(title='ATENÇÃO', message='E-MAIL NÂO ENCONTRADO OU NÃO ENVIADO')