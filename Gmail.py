import smtplib
import time
import imaplib
import email

FROM_EMAIL = "incidntmgmt@gmail.com"
FROM_PWD = "Python3.8"

conn = imaplib.IMAP4_SSL("imap.gmail.com", 993)

conn.login(FROM_EMAIL, FROM_PWD)
conn.select()

status, all_folders = conn.list()  #Check status for 'OK'

#print(all_folders)

status, message_ids = conn.search(None, 'X-GM-RAW', 'Google')

for id in message_ids[0].split():
    status, data = conn.fetch(id, '(RFC822)')
    #print(data) 
    for i in data[0]:
        print(i)
