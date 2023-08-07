#!/usr/bin/python3
import boto3

print("Content-type:text/html")
print()

print("fsdfafa")

import subprocess as s
out=s.getoutput("aws ec2 run-instances --image-id ami-0ded8326293d3201b  --instance-type t2.micro")
print("<pre>")
print(out)
print("</pre>")

print()
print()
print("<form action= http://3.108.228.1/menu.html>")
print("<input type='submit' value='Back to Main menu'></form>")


