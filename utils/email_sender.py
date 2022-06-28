# import smtplib as smtp
# from email.message import EmailMessage
# from datetime import datetime
# from models import Config
#
#
# def assemble_message(from_email: str, to_email: list, text: str, subject: str) -> EmailMessage:
#     """Возвращает сформированное письмо для отправки"""
#     msg: EmailMessage = EmailMessage()
#     msg["From"] = from_email
#     msg["To"] = ", ".join(to_email)
#     msg["Subject"] = subject
#     msg.set_content(text)
#     msg.a
#
#     return msg
#
#
# def send_message(email: str, password: str, message: EmailMessage) -> str:
#     """Возвращает строку состояния"""
#     try:
#         server = smtp.SMTP_SSL(host="smtp.yandex.ru", port=465)
#         server.login(email, password)
#         server.auth_plain()
#         server.send_message(msg=message)
#         server.quit()
#         return "Successfully logged in, message sent"
#     except Exception:
#         return "Couldn't connect or send message"
#
#
# def mail_sender(text: str, today: datetime) -> str:
#     config = Config.config_parser('config')
#
#     email = config["email"]
#     password = config["password"]
#     to_email = config["to_email"]
#     subject = config["subject"] + today.strftime("%d.%m.%Y")
#
#     message = assemble_message(from_email=email, to_email=to_email, text=text, subject=subject)
#     log = send_message(email=email, password=password, message=message)
#     return log

import asyncio
import aiosmtplib
import sys

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MAIL_PARAMS = {'TLS': True, 'host': 'xxxxxxxx', 'password': 'xxxxxxxx', 'user': 'xxxxxxxx', 'port': 587}

if sys.platform == 'win32':
    loop = asyncio.get_event_loop()
    if not loop.is_running() and not isinstance(loop, asyncio.ProactorEventLoop):
        loop = asyncio.ProactorEventLoop()
        asyncio.set_event_loop(loop)


async def send_mail_async(sender, to, subject, text, textType='plain', **params):
    """Send an outgoing email with the given parameters.

    :param sender: From whom the email is being sent
    :type sender: str

    :param to: A list of recipient email addresses.
    :type to: list

    :param subject: The subject of the email.
    :type subject: str

    :param text: The text of the email.
    :type text: str

    :param textType: Mime subtype of text, defaults to 'plain' (can be 'html').
    :type text: str

    :param params: An optional set of parameters. (See below)
    :type params; dict

    Optional Parameters:
    :cc: A list of Cc email addresses.
    :bcc: A list of Bcc email addresses.
    """

    # Default Parameters
    cc = params.get("cc", [])
    bcc = params.get("bcc", [])
    mail_params = params.get("mail_params", MAIL_PARAMS)

    # Prepare Message
    msg = MIMEMultipart()
    msg.preamble = subject
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(to)
    if len(cc): msg['Cc'] = ', '.join(cc)
    if len(bcc): msg['Bcc'] = ', '.join(bcc)

    msg.attach(MIMEText(text, textType, 'utf-8'))

    # Contact SMTP server and send Message
    host = mail_params.get('host', 'localhost')
    isSSL = mail_params.get('SSL', False);
    isTLS = mail_params.get('TLS', False);
    port = mail_params.get('port', 465 if isSSL else 25)
    smtp = aiosmtplib.SMTP(hostname=host, port=port, use_tls=isSSL)
    await smtp.connect()
    if isTLS:
        await smtp.starttls()
    if 'user' in mail_params:
        await smtp.login(mail_params['user'], mail_params['password'])
    await smtp.send_message(msg)
    await smtp.quit()


if __name__ == "__main__":
    email = "xxxxxxxx";
    co1 = send_mail_async(email,
              [email],
              "Test 1",
              'Test 1 Message',
              textType="plain")
    co2 = send_mail_async(email,
              [email],
              "Test 2",
              'Test 2 Message',
              textType="plain")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(co1, co2))
    loop.close()