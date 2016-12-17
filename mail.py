import smtplib
import email
import os
import requests
from email.MIMEMultipart import MIMEMultipart
from email.Utils import COMMASPACE
from email.MIMEBase import MIMEBase
from email.parser import Parser
from email.MIMEImage import MIMEImage
from email.MIMEText import MIMEText
from email.MIMEAudio import MIMEAudio
import mimetypes
import json
def func1():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    #Next, log in to the server
    server.login("2013ecs35@smvdu.ac.in", "9419204147")
    fromaddr='2013ecs35@smvdu.ac.in'
    tolist='2013ecs53@smvdu.ac.in'
    res = requests.get("https://contesttrackerapi.herokuapp.com/")
    #convert to py dict
    res = json.loads(res.text)
    upcoming = res["result"]["upcoming"]
    tw="Hi there!\n Improve your skills with this upcoming challenge recommended for you."
    tw = "Next contest: " + upcoming[0]["StartTime"] + "on " + upcoming[0]["Platform"] +". "+ upcoming[0]["url"]
    tw="Happy coding!"
    #Send the mail
    sub="Invitation to Coding Challenges"
    msg = email.MIMEMultipart.MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = email.Utils.COMMASPACE.join(tolist)
    msg['Subject'] = sub
    msg.attach(MIMEText(tweet))
    msg.attach(MIMEText('sent via python', 'plain'))
    server.sendmail('2013ecs35@smvdu.ac.in',tolist,msg.as_string())
    server.quit()

def main():
        func1()
if __name__ == "__main__": main()
    

    
