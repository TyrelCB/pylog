# Import smtplib for the actual sending function
import smtplib
import mimetypes
# Import the email modules we'll need
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders
import codecs

# Import the sensitive credentials
from Email import creds



def send_email(mail_server,subject, from_address, to_address, data):
    # Define SMTP Server
    server = smtplib.SMTP(mail_server, 25)

    # Build MIME container (email)
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject
    contents = MIMEText(data)
    msg.attach(contents)

    # Send the msg/email and quit
    try:
        server.send_message(msg)
        print('email sent to',to_address,'from',from_address)
    except:
        print('failed to send email')
