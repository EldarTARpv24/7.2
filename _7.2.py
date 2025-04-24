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

# import smtplib, ssl
# from email.message import EmailMessage
# import random
# import string

# def Loe_failist(filename:str):
#     email = []
#     parool = []
#     try:
#         with open(filename, 'r', encoding="utf-8-sig") as skibidi:
#             for rida in skibidi:
#                 parts = rida.strip().split(',')
#                 if len(parts) == 2:
#                     email.append(parts[0])
#                     parool.append(parts[1])
#     except ValueError:
#         print(f"Fail {filename} ei ole olemas, loo uus.")
#     return email, parool 

# def randomni_random(length=8):
#     characters = string.ascii_letters + string.digits + string.punctuation
#     return ''.join(random.choice(characters) for _ in range(length))

# def saada_kiri(kellele, new_password):
#     smtp_server = "smtp.gmail.com"
#     smtp_port = 587
#     kellelt = "eldar040503@gmail.com"
#     salasõna = input("Sisesta oma Gmail salasõna või rakenduse parool: ")

#     msg = EmailMessage()
#     msg.set_content(f"Teie uus parool on: {new_password}")
#     msg['Subject'] = 'Teie uus parool'
#     msg['From'] = kellelt
#     msg['To'] = kellele

#     try:
#         context = ssl.create_default_context()
#         with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
#             server.login(kellelt, salasõna)  
#             server.sendmail(kellelt, kellele, msg.as_string()) 
#         print("Uus parool on saadetud e-mailile!")
#     except Exception as e:
#         print(f"Tekkis viga e-maili saatmisel: {e}")

# valik = input("Mida sa teha tahad?? (reg/auto/uus parool/lõpp): ")

# filename = 'module1.txt'
# email, parool = Loe_failist(filename)

# if valik.lower() == "reg":
#     email1 = input("Sisesta oma e-mail: ")
#     email.append(email1)
#     parool1 = input("Sisesta oma parool: ")
#     parool.append(parool1)

#     with open(filename, 'a', encoding="utf-8-sig") as f:
#         f.write(f"{email1},{parool1}\n")
    
#     print("Olete registreeritud!")

# elif valik.lower() == "auto":
#     email2 = input("Sisesta oma e-mail: ")
#     parool2 = input("Sisesta oma parool: ")

#     if email2 in email and parool2 in parool:
#         print("Olete sisse logitud!")
#     else:
#         print("Vale e-mail või parool!")

# elif valik.lower() == "uus parool":
#     email3 = input("Sisesta oma e-mail: ")
#     if email3 in email:
#         uus_parool = randomni_random()  
#         parool[email.index(email3)] = uus_parool
#         with open(filename, 'w', encoding="utf-8-sig") as f:
#             for e, p in zip(email, parool):
#                 f.write(f"{e},{p}\n")
        
#         saada_kiri(email3, uus_parool)
#         print("Teie parool on muudetud ja saadetud e-mailile!")
#     else:
#         print("Vale e-mail!")

# elif valik.lower() == "lõpp":
#     print("Head aega!")
#--------------------------------------------------------------------------------------------------------------------------------------

#ül 1
# def modele(fail:str): 
#     f=open(fail,'r',encoding="utf-8-sig")
#     jarjend=[] 
#     for rida in f:
#         jarjend.append(rida.strip())
#     f.close() 
#     return jarjend 

# a = modele("module1.txt")
# for i in a:
#     k, v = i.split(";")
#     vastus = str(input(k)).lower()
#     if vastus == v.lower():
#         print("õige")
#     else:
#         print("vale")

import random
import smtplib
from email.message import EmailMessage
import ssl

def send_email_notification(email, subject, body):
    """Отправка уведомления на e-mail."""
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  
    sender_email = "eldar040503@gmail.com"
    sender_password = "wqwp zjly akcd rwyp"

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = email
    msg.set_content(body)

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
            print("Teavitus saadetud!")
    except Exception as e:
        print(f"Teavituse saatmine nurjus: {e}")


def loe_kusimused():
    kys_vas = {}
    with open("kusimused_vastused.txt", "r", encoding="utf-8") as f:
        for rida in f:
            if ":" in rida:
                osad = rida.strip().split(":", 1)
                kysimus = osad[0].strip()
                vastus = osad[1].strip()
                kys_vas[kysimus] = vastus
    return kys_vas


def alusta_testi():
    kysimused = loe_kusimused()
    kasutajad = []
    M = 3  # vastajate arv
    N = 5  # küsimusi korraga

    for i in range(M):
        print(f"\nTestija {i+1}")
        nimi = input("Sisesta oma nimi (Eesnimi Perenimi): ")
        email = input("Sisesta oma e-posti aadress: ")

        if nimi in kasutajad:
            print("Selle nimega on juba test tehtud.")
            continue
        kasutajad.append(nimi)

        kysimused_list = list(kysimused.items())
        random.shuffle(kysimused_list)
        valitud = kysimused_list[:N]

        oiged = 0
        for kysimus, oige in valitud:
            vastus = input(kysimus + " ")
            if vastus.strip().lower() == oige.lower():
                oiged += 1

        tulemus_rida = nimi + " – " + str(oiged) + " õigesti"

        if oiged >= (N // 2 + 1):
            with open("oiged.txt", "a", encoding="utf-8") as f:
                f.write(tulemus_rida + "\n")
            seis = "Sa sooritasid testi edukalt."
        else:
            with open("valed.txt", "a", encoding="utf-8") as f:
                f.write(nimi + "\n")
            seis = "Kahjuks testi ei sooritatud edukalt."

        with open("koik.txt", "a", encoding="utf-8") as f:
            f.write(nimi + " – " + str(oiged) + " – " + email + "\n")

        # Saada e-mail kasutajale
        subject = "Küsimustiku tulemus"
        body = f"Tere {nimi}!\nSinu õigete vastuste arv: {oiged}.\n{seis}"
        send_email_notification(email, subject, body)

    print("\nKõik testid on tehtud.")
    print("Tulemused saadetud e-posti aadressidele.")


def lisa_kysimus():
    uus = input("Sisesta uus küsimus: ")
    vastus = input("Sisesta õige vastus: ")
    with open("kusimused_vastused.txt", "a", encoding="utf-8") as f:
        f.write(uus + ":" + vastus + "\n")
    print("Küsimus lisatud!")


def menuu():
    while True:
        print("\n1. Alusta küsimustikku")
        print("2. Lisa uus küsimus")
        print("3. Välju")

        valik = input("Vali tegevus (1-3): ")
        if valik == "1":
            alusta_testi()
        elif valik == "2":
            lisa_kysimus()
        elif valik == "3":
            print("Programmist väljutakse.")
            break
        else:
            print("Vale valik. Proovi uuesti.")

menuu()

def saada_koondraport():
   
    raport_email = "igoralekseje@gmail.com"
    subject = "Tänased küsimustiku tulemused"

    body = "Tere!\n\nTänased küsimustiku tulemused:\n\n"

    with open("koik.txt", "r", encoding="utf-8") as f:
        body += f.read()

    send_email_notification(raport_email, subject, body)
    print("Koondraport saadetud tööandjale!")


print("\nKõik testid on tehtud.")
print("Tulemused saadetud e-posti aadressidele.")
saada_koondraport()

