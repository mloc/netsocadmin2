# stdlib
from typing import List

# lib
import sendgrid
from sendgrid.helpers.mail import Content, Email, From, Mail, To

# local
import config


def send_mail(from_mail: str, to_mail: str, subject: str, content: str, cc: List[str] = None) -> object:
    sg = sendgrid.SendGridAPIClient(config.SENDGRID_KEY)

    mail = Mail()
    mail.from_email = From(from_mail, "UCC Netsoc")
    mail. subject = subject
    mail.content = Content("text/plain", content)

    p = sendgrid.Personalization()
    p.add_to(To(to_mail))
    if cc:
        for email in cc:
            p.add_cc(Email(email))
    mail.add_personalization(p)
    return sg.send(mail)
