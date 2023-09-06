#!/usr/bin/python3

import cgi

print("Content-type:text/html")
print()

#form = cgi.FieldStorage()
#data=form.getvalue("q")
#myname="vimal"
#print("i am {} ".format(myname))

import subprocess as s
out=s.getoutput("date")
print("<pre>")
print(out)
print("</pre>")

print()
print()
print("<form action= http://3.108.228.1/menu.html>")
print("<input type='submit' value='Back to Main menu'></form>")
