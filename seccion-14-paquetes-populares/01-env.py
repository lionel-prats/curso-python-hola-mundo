# Variables de entorno (ref. v130)
# Sendgrid (ref. v131)

import os 
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient

os.system('cls' if os.name == 'nt' else 'clear')

email = os.environ.get("SENGRID_EMAIL")

mensaje = Mail(
    from_email=email,
    to_emails='destinatario@correo.com',
    subject="Asunto de prueba",
    html_content="Curso de <b>Ultimate Python</b>"
)

try:
    apikey = os.environ.get("SENGRID_API_KEY")
    sg = SendGridAPIClient(apikey)
    respuesta = sg.send(mensaje)
    print(
        respuesta.status_code,
        respuesta.body,
        respuesta.headers,
    )
except Exception as e:
    print(e)