from pysimplesoap.client import SoapClient, SoapFault
import cgitb
import logging
import os
import csv
import sqlite3
cgitb.enable()

#logging management script
logging.getLogger('').handlers = []
logger = logging.getLogger('')
hdlr = logging.FileHandler('management.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)
logger.info('Start management sessie')

try:
	# create a simple consumer
	form=cgi.FieldStorage()
	dropdown = form.getvalue('ip')
	if dropdown == 'Anders':
		ipadress = form.getvalue('invoer_ip')
	else:
		ipadress = dropdown
	print ipadress
	client = SoapClient(
		location = "http://"+ipadress+":8008/",
		action = "http://"+ipadress+":8008/", # SOAPAction
		namespace = "http://example.com/sample.wsdl",
		soap_ns='soap',
		ns = False)
	# call a few remote methods
	print '<h3>'
	r1=str(client.get_value(number=1).resultaat)
	print r1
	print '</h3><br>'
	r2=str(client.get_value(number=2).resultaat)
	print "Resultaat platform :", r2.rstrip()
	print '<br>'
	r3=str(client.get_value(number=3).resultaat)
	print "Resultaat encoding :", r3.rstrip()
	print '<br>'
	r4=str(client.get_value(number=4).resultaat)
	print "Resultaat poort :", r4.rstrip() 
	print '<br>'
	r5=str(client.get_value(number=5).resultaat)
	print "Resultaat Temperatuur :", r5.rstrip()
	print '<br>'
	r6=str(client.get_value(number=6).resultaat)
	print "Resultaat Fysiek geheugen :", r6.rstrip()
	print '<br>'
	r7=str(client.get_value(number=7).resultaat)
	print "Resultaat Aantal Services :", r7.rstrip()
	print '<br>'
	r8=str(client.get_value(number=8).resultaat)
	print "Resultaat Vrije Schijfruimte :", r8.rstrip()
	print '<br>'
	r9=str(client.get_value(number=9).resultaat)
	print "Resultaat Aantal ingelogde gebruikers :", r9.rstrip()
	print '<br>'
	r10=str(client.get_value(number=10).resultaat)
	print "Uptime :", r10.rstrip()
	print '<br>'
	r11=str(client.get_value(number=11).resultaat)
	print "Beschikbare werkgeheugen :", r11.rstrip()
	print '<br>'
	r12=str(client.get_value(number=12).resultaat)
	print "IPv4 Adressen :", r12.rstrip()
	print '<br>'
	logger.info('Einde management sessie')

	#export CSV
	logger.info('Start CSV sessie')
	b = os.path.isfile('gegevens.csv')
	a = open('gegevens.csv', ('ab'))

	write = csv.writer(a,delimiter=';')
	if b == False:
		write.writerow(['Hostname','Platform','Tekenset','Poort nummer','Temperatuur','Fysiek geheugen','Aantal services','Vrije schijfruimte','Aantal ingelogdegebruikers','Uptime','Vrije werkgeheugen','IPv4 Addressen'])
	else:
		pass
	write = csv.writer(a,delimiter=';')
	write.writerow([r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12])
	a.close()
	logger.info('Einde CSV sessie')
	print 'Gegevens geexporteert naar gegevens.csv'
	print '</p>'
	print '</html>'
	
	#Export database
	conn=sqlite3.connect('gegevens.db')
	c=conn.cursor()
	if os.path.exists('gegevens.db') == False:
		c.execute("Create table gegevens ('Hostname' text,'Platform' text,'Tekenset' text,'Poort nummer' text,'Temperatuur' text,'Fysiek geheugen' text,'Aantal services' text,'Vrije schijfruimte' text,'Aantal ingelogdegebruikers' text,'Uptime' text,'Vrije werkgeheugen' text,'IPv4 Addressen' text)")
		c.execute("insert into gegevens values(?,?,?,?,?,?,?,?,?,?,?,?);", (r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12))
	else:
		c.execute("insert into gegevens values(?,?,?,?,?,?,?,?,?,?,?,?);", (r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12))
	conn.commit()
	conn.close()
except:
	#Error
	print('<h3 > Warning: Gegevens ophalen mislukt!</h3>')
	print('<h1 style="font-size:150px">&#9749;</h1>')