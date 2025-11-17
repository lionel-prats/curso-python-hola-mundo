# ref. v121

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

ref_plantilla = Path("seccion-12-modulos-nativos/plantilla.html")
plantilla = ref_plantilla.read_text("utf-8")

template = Template(plantilla)

cuerpo = template.substitute(usuario="Chanchito feliz")

path = Path("seccion-12-modulos-nativos/imagen-fake.jpg")
mime_image = MIMEImage(path.read_bytes())

mensaje = MIMEMultipart()
mensaje["from"] = "Nombre Remitente"
mensaje["to"] = "mailfake-smtp-habilitado@gmail.com"
mensaje["subject"] = "Asunto de prueba"
cuerpo = MIMEText(cuerpo, "html")
mensaje.attach(cuerpo)
mensaje.attach(mime_image)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()

    smtp.starttls()
    # TLS -> Transport Layer Security

    smtp.login("mailfake-smtp-habilitado@gmail.com", "passfake")
    smtp.send_message(mensaje)
    print("Mensaje Enviado!")
