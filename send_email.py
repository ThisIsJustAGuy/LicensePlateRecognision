#!/usr/bin/python
import httplib2
import os
import oauth2client
from oauth2client import client, tools, file
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from apiclient import errors, discovery

SCOPES = 'https://www.googleapis.com/auth/gmail.send'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Python Send Email'


def bad_sector_email(dest_email, title1, title2, description, subdescription, msgHTML):
    title1.string.replace_with("Rossz")
    title2.string.replace_with("szektor")
    description.string.replace_with(
        "Olyan szektorba próbált parkolni, ahova nincs érvényes bérlete. Az alábbi linken megtekintheti hova van érvényes bérlete:\nwww.example.com")
    subdescription.string.replace_with(
        "Az alábbi linken vásárolhat új bérletet:\nwww.example2.com")
    msgPLAIN = "Rossz szektor"
    msgSubject = "Rossz szektor"
    start_email_process(dest_email, msgHTML, msgPLAIN, msgSubject)


def no_ticket_email(dest_email, title1, title2, description, subdescription, msgHTML):
    title1.string.replace_with("Nincs érvényes")
    title2.string.replace_with("bérlet")
    description.string.replace_with(
        "Sajnos ennek az autójának egyáltalán nincs érvényes bérlete.")
    subdescription.string.replace_with(
        "Az alábbi linken vásárolhat új bérletet:\nwww.example2.com")
    msgPLAIN = "Nincs érvényes bérlete"
    msgSubject = "Nincs érvényes bérlete"
    start_email_process(dest_email, msgHTML, msgPLAIN, msgSubject)


def get_credentials():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(
        credential_dir, 'gmail-python-email-send.json')
    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        credentials = tools.run_flow(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def SendMessage(sender, to, subject, msgHtml, msgPlain):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)
    message1 = CreateMessage(sender, to, subject, msgHtml, msgPlain)
    SendMessageInternal(service, "me", message1)


def SendMessageInternal(service, user_id, message):
    try:
        message = (service.users().messages().send(
            userId=user_id, body=message).execute())
        print('Message Id: %s' % message['id'])
        return message
    except errors.HttpError as error:
        print('An error occurred: %s' % error)


def CreateMessage(sender, to, subject, msgHtml, msgPlain):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = to
    msg.attach(MIMEText(msgPlain, 'plain'))
    msg.attach(MIMEText(msgHtml, 'html'))
    raw = base64.urlsafe_b64encode(msg.as_bytes())
    raw = raw.decode()
    body = {'raw': raw}
    return body


def start_email_process(dest_email, msgHTML, msgPLAIN, msgSubject):
    to = dest_email
    sender = "mrpiplaterecogniser@gmail.com"
    subject = msgSubject
    msgHtml = msgHTML
    msgPlain = msgPLAIN
    SendMessage(sender, to, subject, msgHtml, msgPlain)

# ezt lehet időnként le kell frissíteni
# pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
