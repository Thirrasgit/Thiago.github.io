from customtkinter import *
from tkinter import messagebox
import sqlite3
from hashlib import sha256
import re


class BackEnd():
    def transformar_senha_em_cripto(self, senha):
        self.senha_byte_log = senha.encode()
        self.senha_hash_log = sha256(self.senha_byte_log)
        self.senha_criptografada = self.senha_hash_log.hexdigest()
        return self.senha_criptografada     

    def verificar_email(self, email):

        # Verifica se o e-mail corresponde ao padrão definido 
        if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            #print('E-mail válido')
            return True
        else:
            #print('E-mail inválido')
            return False
        
    def verificar_senha(self, senha):

        if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$", senha):
            #print("A senha atende aos critérios.")
            return True
        
        else:
            #print("A senha deve ter pelo menos 8 caracteres, uma letra maiúscula, uma letra minúscula e um número.")
            return False
    
    def ver_senha_cad(self):
        if self.botao_ver_senha_cad.get() == 'on':
            self.senha_cad.configure(show='') 
            self.conf_senha_cad.configure(show='') 
                     
        else:
            self.senha_cad.configure(show='*')
            self.conf_senha_cad.configure(show='*')

    def ver_senha_log(self):
        if self.visu_senha_log.get() == 'on':
            self.senha_login.configure(show='') 
                     
        else:
            self.senha_login.configure(show='*')

    def ver_senha_alt(self):
        if self.visu_senha_alt.get() == 'on':
            self.senha_alt.configure(show='')
            self.conf_senha_alt.configure(show='')
                    
        else:
            self.senha_alt.configure(show='*')
            self.conf_senha_alt.configure(show='*')

    def limpar_dados_cadastros(self):
        self.empresa_cad.delete(0, END) 
        self.cnpj_cad.delete(0, END) 
        self.email_cad.delete(0, END)
        self.senha_cad.delete(0, END)
        self.conf_senha_cad.delete(0, END)
    
    
    def limpar_dados_login(self):
        self.cnpj_login.delete(0, END) 
        self.senha_login.delete(0, END)

        #Inserindo novamente as informações da placeholder
        self.cnpj_login.configure(placeholder_text='Insira o CNPJ/CPF.', font=('Verdana', 15))
        self.senha_login.configure(placeholder_text='Insira a senha.', font=('Verdana', 15), show='*')
    
    #Criando banco de dados
    def conectar_db(self):
        self.conexao = sqlite3.connect('Trabalho UC16/Cadastros.db') #Conectando e criando o BD
        self.cursor = self.conexao.cursor() #Cursor é o ponto de entrada de comandos pro BD
        print('Conectando ao Banco de Dados...')
        
    
    def desconectar_db(self):
        self.conexao.close()
        print('Desconectando do Banco de Dados...')
        

    def criar_tabela_db(self):
        #Conectando ao BD
        self.conectar_db()

        #Criando os dados do BD
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Empresas(
            CNPJ TEXT NOT NULL UNIQUE,
            Empresa TEXT NOT NULL,
            Email TEX NOT NULL UNIQUE,
            Senha TEXT NOT NULL
        );
        ''')
        self.conexao.commit()#Faz com que os dados sejam colocados na tabela ou que a tabela seja criada
        print('Banco de Dados criado com sucesso!')
        self.desconectar_db()
    
    def confirmar_cadastro(self):
        self.conectar_db()
        self.receber_cnpj_cad = self.cnpj_cad.get()
        self.receber_empresa = self.empresa_cad.get()
        self.receber_email_cad = self.email_cad.get()
        self.receber_senha_cad = self.transformar_senha_em_cripto(self.senha_cad.get())
        self.receber_confirmar_senha_cad = self.transformar_senha_em_cripto(self.conf_senha_cad.get())

        if self.cnpj_cad.get() == '' or self.empresa_cad.get() == '' or self.email_cad.get() == '' or self.senha_cad.get() == '' or self.conf_senha_cad.get() == '':
            messagebox.showerror(title='Erro no Cadastro', message='Erro!\nPor favor preencha todos os campos.')
            self.desconectar_db()

        elif self.empresa_cad.get() == '' or self.empresa_cad.get().isnumeric() or len(self.empresa_cad.get()) < 3:
            self.desconectar_db()
            messagebox.showerror(title='Erro no Cadastro', message='Nome deve conter mais de 3 dígitos e conter somente letras')

        elif (self.cnpj_cad.get().isalpha()) or (len(self.cnpj_cad.get()) < 11) or (self.cnpj_cad.get().isalpha()) or (len(self.cnpj_cad.get()) > 14):
            self.desconectar_db()
            messagebox.showerror(title='Erro no Cadastro', message='Erro!\nCPF/CNPJ deve ser preenchido somente com números e conter apenas 11 ou 14 dígitos sem os caracteres especiais inseridos')
        
        elif not self.verificar_email(self.email_cad.get()):
            self.desconectar_db()
            messagebox.showerror(title='Erro no Cadastro', message='Erro!\nDomínio de e-mail não encontrado.')

        elif not self.verificar_senha(self.senha_cad.get()):
            self.desconectar_db()
            messagebox.showerror(title='Erro no Cadastro', message='Erro!\nSenha inválida, para uma senha válida, deverá conter:\n8 dígitos\n1 Letra Maiúscula\n1 Letra Minúscula\n1 Número')
        
        elif self.senha_cad.get() != self.conf_senha_cad.get():
            self.desconectar_db()
            messagebox.showerror(title='Erro no Cadastro', message='Erro!\nA senha e confirmação de senha não se coincidem.')

        else:
            try:
                #Conectando ao DB e inserindo dados
                self.cursor.execute(f'''
                INSERT INTO Empresas(CNPJ, Empresa, Email, Senha)
                VALUES (?,?,?,?)''',(self.cnpj_cad.get(), self.empresa_cad.get(), self.email_cad.get(), self.receber_senha_cad))
                self.conexao.commit()

                messagebox.showinfo(title='Cadastro concluído', message='Obrigado por fazer parte do nosso projeto\nAgora é possível nos enviar um e-mail com o seu feedback!')
                
                print('Os dados estão sendo inseridos ao Banco de Dados...')
                
                #Desconectando do db para não salvar repentinamente os mesmos dados
                self.desconectar_db()

                #Saindo da tela de cadastro e voltando ao menu principal
                self.menu_login()
                
                #Mostrando que sua empresa esta logada
                #self.'

                #Saindo da sua conta do BD (apenas um configure q vai sumir o nome quando clicar no botao de sair ao lado do icone de logout)

            except sqlite3.IntegrityError:
                messagebox.showerror(title="Erro de Integridade", message="O CNPJ/CPF e/ou o email já estão em uso.")
                self.desconectar_db()
            
    def confirmar_login(self):
        self.receber_nome_log = self.cnpj_login.get()
        self.receber_senha_log = self.transformar_senha_em_cripto(self.senha_login.get())

        self.conectar_db()

        self.cursor.execute(f"SELECT * FROM Empresas WHERE CNPJ = '{self.cnpj_login.get()}'")
        self.verificar_dados_log = self.cursor.fetchall()

        try:

            if self.cnpj_login.get() in self.verificar_dados_log[0][0] and self.transformar_senha_em_cripto(self.senha_login.get()) in self.verificar_dados_log[0][3]:
                messagebox.showinfo(title='Login', message=f'Bem-vindo!\n Seu login foi concedido')
                self.limpar_dados_login()
                self.desconectar_db()
                self.menu_principal()
                # self.logado = CTkLabel(self.frame_cabecalho, text=f'{self.empresa_cad.get()}', font=('Verdana', 15))
                # self.logado.place(x=1250, y= 50)

            elif self.receber_nome_log == '' or self.receber_senha_log == '':
                messagebox.showerror(title='Login', message=f'Campo CNPJ vazios\nInsira os dados em ambos os campos')
                self.limpar_dados_login()
                self.desconectar_db()

            elif self.cnpj_login.get() not in self.verificar_dados_log[0][0] and self.transformar_senha_em_cripto(self.senha_login.get()) not in self.verificar_dados_log[0][3]:
                messagebox.showerror(title='Login', message='Não foi possível encontrar este usuário, altere as credenciais e tente novamente')

            else:
                messagebox.showerror(title='Login', message='Dados incorretos ou usuário não cadastrado')
                self.limpar_dados_login()
                self.desconectar_db()

        except IndexError: messagebox.showerror(title='Erro de Integridade', message='Dados inválidos ou campos nulos'), self.limpar_dados_login(), self.desconectar_db()
        #except sqlite3.OperationalError: messagebox.showerror(title='Erro de Integridade', message='Dados inválidos'), self.limpar_dados_login(), self.desconectar_db()

    def alterar_senha_usuario(self):
        self.conectar_db()
        self.cursor.execute(f"SELECT * FROM Empresas WHERE CNPJ = ? AND Email = ?", (self.cnpj_alt.get(), self.email_alt.get()))
        self.verificar_dados_alt_senha = self.cursor.fetchall()
        print(self.senha_alt.get())

        try:
            if self.senha_alt.get() == '' or self.conf_senha_alt.get() == '' or self.email_alt.get() == '' or self.cnpj_alt.get() == '':
                messagebox.showerror(title='Alteração de senha', message='Campos inválidos ou nulos\nPor favor preencha todos os campos')
                self.desconectar_db()
            
            elif self.senha_alt.get() != self.conf_senha_alt.get():
                messagebox.showerror(title='Alteração de senha', message='Nova senha e confirmação de nova senha não se coincidem!')
                self.desconectar_db()

            elif not self.verificar_senha(self.senha_alt.get()):
                self.desconectar_db()
                print('senha incorreta')
                messagebox.showerror(title='Erro no Cadastro', message='Erro!\nSenha inválida, para uma senha válida, deverá conter:\n8 dígitos\n1 Letra Maiúscula\n1 Letra Minúscula\n1 Número')

            elif self.transformar_senha_em_cripto(self.senha_alt.get()) and self.email_alt.get() in self.verificar_dados_alt_senha[0][2] and self.cnpj_alt.get() in self.verificar_dados_alt_senha[0][0]:
                self.cursor.execute(f"UPDATE Empresas SET Senha = ? WHERE CNPJ = ? AND Email = ?", (self.transformar_senha_em_cripto(self.senha_alt.get()), self.cnpj_alt.get(), self.email_alt.get()))
                self.conexao.commit()
                self.desconectar_db()
                messagebox.showinfo(title='Alteração de senha', message='Você redefiniu a sua senha')
                self.menu_login()

            else:
                messagebox.showerror(title='Alteração de senha', message='Dados não encontrados no banco de dados')
                self.desconectar_db()

        except TypeError: messagebox.showerror(title='ERRO', message='Ops, alguma credencial está incorreta ou algum campo está nulo'), self.desconectar_db()
        except IndexError: messagebox.showerror(title='ERRO', message='Ops, alguma credencial está incorreta ou algum campo está nulo'), self.desconectar_db()
