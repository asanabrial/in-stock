import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from src.constants import EMAIL_SMTP_SERVER, EMAIL_SMTP_PORT


class Email:
    def __init__(self, email, password):
        self.email_from = email
        self.email_password = password
        self.smtp_server = EMAIL_SMTP_SERVER
        self.smtp_port = EMAIL_SMTP_PORT

    def send(self, subject, body, to_email):
        msg = MIMEMultipart()
        msg["From"] = self.email_from
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        try:
            server = smtplib.SMTP_SSL(self.smtp_server, self.smtp_port)
            server.login(self.email_from, self.email_password)
            server.sendmail(self.email_from, to_email, msg.as_string())
            server.quit()
            print("Email sent successfully.")
        except Exception as e:
            print(f"Error sending email: {e}")
