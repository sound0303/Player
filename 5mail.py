#! /usr/bin/python3
import smtplib
s = smtplib.SMTP('smtp.soundaryapowndurai@gmail.com',587)
s.starttls() 
s.login("www.soundaryapowndurai@gmail.com","powndurai03")
message ="Message_you_need_send"
s.sendmail("www.soundaryapowndurai@gamil.com","www.soundaryapowndurai@gmail.com")
s.quit()s









