import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
load_dotenv()

def send_mail(to_email, subject, message):
    from_email = os.getenv('EMAIL_USER_SISVITA')
    from_password = os.getenv('EMAIL_PASS_SISVITA')
    
    # Configuración del servidor SMTP
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Crear el objeto de mensaje
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Conectar al servidor SMTP y enviar el correo
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Iniciar el TLS para seguridad
        server.login(from_email, from_password)  # Iniciar sesión
        server.send_message(msg)  # Enviar mensaje
        server.quit()  # Cerrar conexión

        print('Correo enviado exitosamente')

    except Exception as e:
        print(f'Error al enviar correo: {e}')



