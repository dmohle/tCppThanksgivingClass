import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, receiver_email, password, subject, body):
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Create a secure SSL context and send the email
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully")
    except Exception as e:
        print(f"Error: {e}")

# Usage
sender = "dmohle@gmail.com"
receiver = "dennis.mohle@fresnocitycollege.edu"
app_password = "rwmi ocpd atko qogt"  # Consider using a more secure method to store and retrieve this
subject = "Hello From Python!"
body = """This is yet and yet another message  of the email. This message

with another line from my computre to yours!
was sent from my office at fresno city college
let me know if you received it!
"""

send_email(sender, receiver, app_password, subject, body)

