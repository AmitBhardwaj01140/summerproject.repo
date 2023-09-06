#!/usr/bin/python3

import cgi

print("Content-type:text/html")
print()

form = cgi.FieldStorage()
data1=form.getvalue("a")

data2=form.getvalue("b")

#myname="vimal"
#print("i am {} ".format(myname))



import smtplib


sender_email = "rrsahani21@gmail.com"
sender_password = "uvhzbahtuixlnokf"
recipient_email = data1
subject = "Test Email from Python" 
body = data2

message = f"Subject: {subject}\n\n{body}"

try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message)
    print("Email sent successfully.")
except Exception as e:
    print("Error sending email")


print()
print()
print("<form action= http://3.108.228.1/menu.html>")
print("<input type='submit' value='Back to Main menu'></form>")
