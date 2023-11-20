import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Srvidor smtp
smtp_server = 'smtp.office365.com'
#porta smtp que será usada
smtp_port = 587
#usuario do servidor smtp
smtp_username = '211928@facens.br'
#senha do usuario do servidor smtp
smtp_password = 'G@br!3l1746612345'

#o e-mail que sera enviado
para_email = 'galexandrerosa@gmail.com'
#o e-mail do remetente
remetente_email = '211928@facens.br'

#criação da mensagem
mensagem = MIMEMultipart()
#de quem é o e-mail
mensagem['From'] = remetente_email
#para quem é o e-mail
mensagem['To'] = para_email
#assunto do e-mail
mensagem['Subject'] = 'Teste'

#corpo do e-mail
corpo_email = 'Teste'
mensagem.attach(MIMEText(corpo_email, 'plain'))

# Conexão com o servidor SMTP
with smtplib.SMTP(smtp_server, smtp_port) as server:
    #Inicia a comunicação TLS
    server.starttls()

    #Login no servidor
    server.login(smtp_username, smtp_password)

    #Envio do e-mail
    server.send_message(mensagem)

print('E-mail enviado com sucesso.')
