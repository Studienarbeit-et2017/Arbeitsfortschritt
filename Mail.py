from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

class EMail(object) :

    __aAddressSend = 'studienarbeit19@gmx.de'
    __aAddressReceiver = ''


    def setAdresseEmpf(self, pAddressReceiver):
         self.__aAddressReceiver = pAddressReceiver

    def getAdresseEmpf(self):
        return self.__aAddressReceiver

    def getMailrdy(self):
        if (self.__aAddressReceiver == ""):
            return False
        else:
            return True
         

    def MailSend(self):     

        msg = MIMEMultipart()
        msg['From'] = self.__aAddressSend
        msg['To'] = self.__aAddressReceiver
        msg['Subject'] = "Pflanzenbewässerungssystem Wassermangel"

        emailText = "Ihr Wasserstand hat das Minimum erreich! <b>Bitte Wasser nachfüllen!</b>"
        msg.attach(MIMEText(emailText, 'html'))

        server = smtplib.SMTP(host='mail.gmx.net', port= 587)   # Die Server Daten Senderemail
        print(msg.attach)
        server.starttls()
        server.login(self.__aAddressSend, "Studienarbeit19")            # Das Passwort E-Mailadresse sender
        server.sendmail(self.__aAddressSend, self.__aAddressReceiver ,msg.as_string())
        server.quit()


        
