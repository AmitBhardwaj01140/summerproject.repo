#!/usr/bin/python3

import cgi

print("Content-type:text/html")
print()

form = cgi.FieldStorage()
data1=form.getvalue("c")


#myname="vimal"
#print("i am {} ".format(myname))

import boto3
import botocore.exceptions
mybucket=boto3.client("s3")

try:
    mybucket.create_bucket(Bucket=data1,
                       CreateBucketConfiguration={
                              'LocationConstraint':'ap-south-1'
                       }
                      )
    print("bucket created successfully..")
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
            print("Bucket already exists.")
    else:
            print("Error creating bucket")

print()
print()
print("<form action= http://3.108.228.1/menu.html>")
print("<input type='submit' value='Back to Main menu'></form>")
