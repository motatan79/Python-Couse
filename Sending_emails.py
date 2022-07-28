import smtplib
import getpass
smtp_object = smtplib.SMTP('smtp.gmail.com', 587)

# Greet the server and establish the connection

smtp_object.ehlo()

smtp_object.starttls()

# Para ocultar la contraseña
password = getpass.getpass('Password please: ')

# Generated an app password




