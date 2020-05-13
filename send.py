import os
from dotenv import load_dotenv
load_dotenv()

username = os.getenv('EMAIL')
password = os.getenv('PASSWORD')


def send_mail(text='Email Body', subject='Hello World', to_emails=None):
    assert isinstance(to_emails, list)
