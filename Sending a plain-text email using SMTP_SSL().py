import smtplib
import ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "my@gmail.com"  # Enter your gmail address
receiver_email = "your@gmail.com"  # Enter receiver's gmail address
password = input("Type your password and press enter: ")
message = """\
Subject: Hi there

This is a sample message."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
