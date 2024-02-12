import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, timedelta

# Replace these with your details
sender_email = "your_email@gmail.com"
sender_password = "your_password"
receiver_email = "receiver_email@example.com"

evaluations = [
    {"name": "Math Exam", "date": "2024-03-10"},
    {"name": "History Paper", "date": "2024-03-15"},
    {"name": "Science Project", "date": "2024-03-20"},
]

def send_notification(evaluation):
    try:
        # Setup the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = f"Upcoming Evaluation: {evaluation['name']}"

        # Email body
        body = f"Reminder: '{evaluation['name']}' is scheduled for {evaluation['date']}. This is a week away!"
        msg.attach(MIMEText(body, 'plain'))

        # Create server connection
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)
        text = msg.as_string()

        # Send the email
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print(f"Email sent for {evaluation['name']}")
    except Exception as e:
        print(f"Failed to send email for {evaluation['name']}. Error: {e}")

def check_for_upcoming_evaluations(evaluations):
    today = datetime.today().date()
    for evaluation in evaluations:
        eval_date = datetime.strptime(evaluation['date'], "%Y-%m-%d").date()
        if eval_date - today == timedelta(days=7):
            send_notification(evaluation)

if __name__ == "__main__":
    check_for_upcoming_evaluations(evaluations)
