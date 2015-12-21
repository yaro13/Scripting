from pysimplesoap.client import SoapClient, SoapFault
import cgitb
import logging
import os
import csv
cgitb.enable()

#logging management script
logging.getLogger('').handlers = []
logger = logging.getLogger('')
##logging.basicConfig(filename=locatie,level=logging.DEBUG,filemode='w')
hdlr = logging.FileHandler('management.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)
logger.info('Start management sessie')

print 'Status: 200 OK'
print 'Content-type: text/html'
print

print '<HTML><HEAD><TITLE>Python Sample CGI</TITLE></HEAD>'
print '<BODY>'
print '<H1>Server Gegevens</H1>'
print '<p>'

# create a simple consumer
client = SoapClient(
    location = "http://192.168.0.108:8008/",
    action = 'http://192.168.0.108:8008/', # SOAPAction
    namespace = "http://example.com/sample.wsdl",
    soap_ns='soap',
    ns = False)
# call a few remote methods
r1=str(client.get_value(number=1).resultaat)
print "Resultaat Platform :", r1
print '<br>'
r2=str(client.get_value(number=2).resultaat)
print "Resultaat Tekenset :", r2.rstrip()
print '<br>'
r3=str(client.get_value(number=3).resultaat)
print "Resultaat Poort :", int(r3) # r3 is a number!
print '<br>'
r4=str(client.get_value(number=4).resultaat)
print "Resultaat Temperatuur :", r4.rstrip() # This is a multiline: strip the newline from the result!
print '<br>'
r5=str(client.get_value(number=5).resultaat)
print "Resultaat Fysiek geheugen :", r5.rstrip()
print '<br>'
r6=str(client.get_value(number=6).resultaat)
print "Resultaat Aantal Services :", r6.rstrip()
print '<br>'
r7=str(client.get_value(number=7).resultaat)
print "Resultaat Vrije Schijfruimte :", r7.rstrip()
print '<br>'
r8=str(client.get_value(number=8).resultaat)
print "Resultaat Aantal ingelogde gebruikers :", r8.rstrip()
print '<br>'
r9=str(client.get_value(number=9).resultaat)
print "Resultaat Uptime :", r9.rstrip()
print '<br>'
r10=str(client.get_value(number=10).resultaat)
print "Beschikbare werkgeheugen :", r10.rstrip()
print '<br>'
r11=str(client.get_value(number=11).resultaat)
print "Beschikbare IPv4 Adressen :", r11.rstrip()
print '<br>'
logger.info('Einde management sessie')

#export CSV
logger.info('Start CSV sessie')
b = os.path.isfile('gegevens.csv')
a = open('gegevens.csv', ('ab'))

write = csv.writer(a,delimiter=';')
if b == False:
    write.writerow(['Platform','Tekenset','Poort nummer','Temperatuur','Fysiek geheugen','Aantal services','Vrije schijfruimte','Aantal ingelogdegebruikers','Uptime','Vrije werkgeheugen','IPv4 Addressen'])
else:
    pass
write = csv.writer(a,delimiter=';')
write.writerow([r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11])
a.close()
logger.info('Einde CSV sessie')
print 'Gegevens geexporteert naar gegevens.csv'
print '</p>'
print '</html>'