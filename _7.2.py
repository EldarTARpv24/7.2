import smtplib,ssl
from email.message import EmailMessage

def saada_kiri():
    kellele = ("Kellele saata: ")
    teema = input("Teema: ")
    sisu = input("Sisu:")
    smtp_server = "setp.gmail.com"
    smtp_port = 587
    kellelt = "eldar040503@gmail.com"
    salasõna = input("Salasõna: ")
    msg = EmailMessage()
    msg["Subject"] = teema
    msg["From"] = kellele
    msg["To"] = kellele
    msg.set_content(sisu)
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls(context=ssl. create_default_context())
            server.login(kellelt, salasõna)
            server.send_message(msg)
            print("Kiri saadetud")
    except:
        print("Viga:", e)