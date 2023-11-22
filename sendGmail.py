import base64
from email.mime.text import MIMEText
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import google.auth

def send_gmail_message():
    try:
        # Load credentials from a JSON file
        creds_path = 'Credentials.json'
        creds = google.auth.load_credentials_from_file(creds_path)

        # Create Gmail API service
        service = build('gmail', 'v1', credentials=creds)
        user_id = 'me'

        # Create a MIME message
        message = MIMEText("This is the body of the email.")
        message['to'] = 'dennis.mohle@fresnocitycollege.edu'
        message['from'] = 'dmohle@gmail.com'
        message['subject'] = 'Hello From Google Gmail API'

        # Encode the message as base64
        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')

        # Create the Gmail message
        message_body = {'raw': raw_message}
        draft = service.users().messages().send(userId=user_id, body=message_body).execute()

        print(f'Message sent with ID: {draft["id"]}')

    except HttpError as error:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    send_gmail_message()
