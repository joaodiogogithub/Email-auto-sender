import smtplib
import email.message

def send_email():

    corpo_email = "Ola email de teste."

    msg = email.message.Message()
    msg['Subject'] = 'Email de teste'
    msg['From'] = 'email'
    msg['To'] = 'email'
    password = "senha"    

    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

send_email()