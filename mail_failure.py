#!/bin/bash/python3
import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("sanjaytripathi1998@gmail.com", "866966366566$$")

# message to be sent
message = "your App is not Working,Something went WRONG Please check the System."

# sending the mail
s.sendmail("sanjaytripathi1998@gmail.com", "sanjaytripathi@gmail.com", message)

# terminating the session
s.quit()
