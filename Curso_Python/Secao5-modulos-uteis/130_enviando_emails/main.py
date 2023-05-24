from string import Template
from datetime import datetime
from dados import my_email, my_password

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

with open('index.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    body_msg = template.safe_substitute(nome='Pedro Henrique', data=data_atual)

msg = MIMEMultipart()
msg['from'] = 'Meu nomes'
msg['to'] = 'pedrohdpf21@gmail.com'  # Email do cliente
msg['subject'] = 'Assunto do email'

body = MIMEText(body_msg, 'html')
msg.attach(body)

# Aq envia imagem Em anexo
# with open('imagem.jpg', 'rb') as img:
#     img = MIMEImage(img.read())
#     msg.attach(img)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(my_email, my_password)
        smtp.send_message(msg)
        print('E-mail enviado com sucesso.')
    except Exception as e:
        print('E-mail não enviado...')
        print('Erro: ', e)

