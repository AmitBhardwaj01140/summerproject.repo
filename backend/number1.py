#!/usr/bin/python3

import subprocess

print("Content-type:text/html")
print()

output=subprocess.getoutput("aws ec2 describe-instances --query 'Reservations[].Instances[].InstanceId' --output text | wc -w")

print("Total No. Instances are: {}".format(output))

print()
print()
print("<form action= http://15.206.173.164/menu.html>")
print("<input type='submit' value='Back to Main menu'></form>")
