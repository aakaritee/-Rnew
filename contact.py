#!C:\Python313\python.exe
import os
import urllib.parse
#**********Get the Query String Variables**********


query_string = os.environ.get('QUERY_STRING', '')  #assumes data is being sent GET
qs_values = urllib.parse.parse_qs(query_string, keep_blank_values=True)

name = qs_values('name' [''])[0]
email = qs_values.get('email', [''])[0]
subject = qs_values.get('subject', [''])[0]
message = qs_values.get('message', [''])[0]



#**********Output HTML**********

print ("Content-type:text/html\r\n\r\n") #Must have this header
print ("<!DOCTYPE html>")
print ("<html>")
print ("<head>")
print ("<title>Hello Somebody</title>")
print ("</head>")
print ("<body>")



print(f"<h2>Thank you, {name}!</h2>")
print("<h3>Here is the information you submitted:</h3>")
print("<ul>")
print(f"<li><strong>Name:</strong> {name}</li>")
print(f"<li><strong>Email:</strong> {email}</li>")
print(f"<li><strong>Subject:</strong> {subject}</li>")
print(f"<li><strong>Message:</strong> {message}</li>")
print("</ul>")
print("<div class='alert alert-success'>Your message has been sent successfully!</div>")

print ("</body>")
print ("</html>")
