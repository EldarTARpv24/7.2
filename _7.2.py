# import smtplib,ssl
# from email.message import EmailMessage
# from tkinter import filedialog

# def saada_kiri():
#     kellele = input("Kellele saata: ") #wqwp zjly akcd rwyp
#     teema = input("Teema: ")
#     sisu = input("Sisu:")
#     smtp_server = "smtp.gmail.com"
#     smtp_port = 587
#     kellelt = "eldar040503@gmail.com"
#     salasõna = input("Salasõna: ")
#     msg = EmailMessage()
#     msg["Subject"] = teema
#     msg["From"] = kellele
#     msg["To"] = kellele
#     msg.set_content(sisu)
#     fail= filedialog.askopenfilename(title= "Vali fail", filetypes = [("All files", "*.*")])
#     with open(fail, "rb") as f:
#         faili_sisu = f.read()
#         faili_nimi = fail.split("/")[-1]
#         msg.add_attachment(faili_sisu, maintype="application", subtype="octet-stream", filename=faili_nimi)
#     try:
#         with smtplib.SMTP(smtp_server, smtp_port) as server:
#             server.starttls(context=ssl. create_default_context())
#             server.login(kellelt, salasõna)
#             server.send_message(msg)
#             print("Kiri saadetud")
#     except Exception as e:
#         print("Viga:", e)

# saada_kiri()

import smtplib, ssl
from email.message import EmailMessage
import random
import string

def Loe_failist(filename:str):
    email = []
    parool = []
    try:
        with open(filename, 'r', encoding="utf-8-sig") as skibidi:
            for rida in skibidi:
                parts = rida.strip().split(',')
                if len(parts) == 2:
                    email.append(parts[0])
                    parool.append(parts[1])
    except ValueError:
        print(f"Fail {filename} ei ole olemas, loo uus.")
    return email, parool 

def randomni_random(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def saada_kiri(kellele, new_password):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    kellelt = "eldar040503@gmail.com"
    salasõna = input("Sisesta oma Gmail salasõna või rakenduse parool: ")

    msg = EmailMessage()
    msg.set_content(f"Teie uus parool on: {new_password}")
    msg['Subject'] = 'Teie uus parool'
    msg['From'] = kellelt
    msg['To'] = kellele

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
            server.login(kellelt, salasõna)  
            server.sendmail(kellelt, kellele, msg.as_string()) 
        print("Uus parool on saadetud e-mailile!")
    except Exception as e:
        print(f"Tekkis viga e-maili saatmisel: {e}")

valik = input("Mida sa teha tahad?? (reg/auto/uus parool/lõpp): ")

filename = 'module1.txt'
email, parool = Loe_failist(filename)

if valik.lower() == "reg":
    email1 = input("Sisesta oma e-mail: ")
    email.append(email1)
    parool1 = input("Sisesta oma parool: ")
    parool.append(parool1)

    with open(filename, 'a', encoding="utf-8-sig") as f:
        f.write(f"{email1},{parool1}\n")
    
    print("Olete registreeritud!")

elif valik.lower() == "auto":
    email2 = input("Sisesta oma e-mail: ")
    parool2 = input("Sisesta oma parool: ")

    if email2 in email and parool2 in parool:
        print("Olete sisse logitud!")
    else:
        print("Vale e-mail või parool!")

elif valik.lower() == "uus parool":
    email3 = input("Sisesta oma e-mail: ")
    if email3 in email:
        uus_parool = randomni_random()  
        parool[email.index(email3)] = uus_parool
        with open(filename, 'w', encoding="utf-8-sig") as f:
            for e, p in zip(email, parool):
                f.write(f"{e},{p}\n")
        
        saada_kiri(email3, uus_parool)
        print("Teie parool on muudetud ja saadetud e-mailile!")
    else:
        print("Vale e-mail!")

elif valik.lower() == "lõpp":
    print("Head aega!")