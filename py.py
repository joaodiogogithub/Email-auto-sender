import smtplib
import email.message

def send_email():

    body_email = "<h1>Hello this is an mail test</h1> <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum</p><footer>By: <strong>João .P</strong></footer>"

    msg = email.message.Message()
    msg['Subject'] = 'Test email'
    msg['From'] = 'sender_mail'
    msg['To'] = 'receiver_mail'
    password = 'sender_password'   

    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(body_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Mail sent')

send_email()