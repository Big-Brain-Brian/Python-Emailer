import smtplib
server = smtplib.SMTP('smtp.gmail.com:587')
fromemail = "Your email here"
pw = "Your password here"
toemail = ["Enter their emails here (compatable with multiple)"]
sub = "Email Subject"
body = """
Email Body

This was an automated message sent by
Big Brain Bryan's Emailer.
https://github.com/Big-Brain-Brian/Python-Emailer
"""
msg = "Subject: {}\n\n{}".format(sub, body)

TargetTimesEmailed = int(input("How many times do you want them emailed: "))
TimesEmailed = 0
server.starttls()
server.login(fromemail, pw)
while TimesEmailed < TargetTimesEmailed:
    for x in toemail:
        server.sendmail(fromemail, x, msg)
        TimesEmailed = TimesEmailed + 1
    print("Emails sent: {}/{}".format(TimesEmailed, TargetTimesEmailed))
print("Done.")
