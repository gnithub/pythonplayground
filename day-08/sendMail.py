import json
import smtplib

# =============================================================================
# SEND EMAIL FUNCTION
# =============================================================================
def send_email():
    # Change the items with: ######Change Me#######
    gmail_user = 'upadhyay.nitin.mca@gmail.com'
    gmail_app_password = "####"
    sent_from = gmail_user
    sent_to = ['er.upadhyaynitin@gmail.com']
    sent_subject = "Hello World"
    sent_body = "Its me World"

    email_text = """\
From: %s
To: %s
Subject: %s
%s
""" % (sent_from, ", ".join(sent_to), sent_subject, sent_body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        #server.starttls()
        server.login(gmail_user, gmail_app_password)
        server.sendmail(sent_from, sent_to, email_text.encode("utf-8"))
        server.close()
        print(email_text)
        print('Email sent!')
    except Exception as exception:
        print("Error: %s!\n\n" % exception)
# =============================================================================
# END OF SEND EMAIL FUNCTION
# =============================================================================
send_email()