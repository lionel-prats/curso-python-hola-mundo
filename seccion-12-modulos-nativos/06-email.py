# ref. v119/v120

# 16/11/25 -> ni intente enviarme un correo a gmail como propone el v120, porque hacerlo implica habilitar una configuracion desde las settings de Gmail
# lo quise hacer pero no pude, asi que simplemente transcribi el codigo del v120 como referencia

# path en el que deberia de haber podido habilitar la configuracion necesaria segun muestra el profesor vvv
# https://myaccount.google.com/u/1/lesssecureapps

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib

# MIME = Multipurpose Internet Mail Extensions (standard utilizado en Internet para poder enviar correos)

path = Path("seccion-12-modulos-nativos/imagen-fake.jpg")
mime_image = MIMEImage(path.read_bytes())

mensaje = MIMEMultipart()
mensaje["from"] = "Nombre Remitente"
mensaje["to"] = "mailfake-smtp-habilitado@gmail.com"
mensaje["subject"] = "Asunto de prueba"
cuerpo = MIMEText("Mail de prueba")
mensaje.attach(cuerpo)
mensaje.attach(mime_image)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()

    smtp.starttls()
    # TLS -> Transport Layer Security

    smtp.login("mailfake-smtp-habilitado@gmail.com", "passfake")
    smtp.send_message(mensaje)
    print("Mensaje Enviado!")
