from pysimplesoap.client import SoapClient, SoapFault
import commands

# create a simple consumer
client = SoapClient(
    location = "http://192.168.0.109:8008/",
    action = 'http://192.168.0.109:8008/', # SOAPAction
    namespace = "http://example.com/sample.wsdl",
    soap_ns='soap',
    ns = False)

# call a few remote methods
r1=str(client.get_value(number=1).resultaat)
print "Resultaat Platform :", r1

r2=str(client.get_value(number=2).resultaat)
print "Resultaat Tekenset :", r2.rstrip()

r3=str(client.get_value(number=3).resultaat)
print "Resultaat Poort :", int(r3) # r3 is a number!

r4=str(client.get_value(number=4).resultaat)
print "Resultaat Temperatuur :", r4.rstrip() # This is a multiline: strip the newline from the result!

r5=str(client.get_value(number=5).resultaat)
print "Resultaat Fysiek geheugen :", r5.rstrip()

r6=str(client.get_value(number=6).resultaat)
print "Resultaat Aantal Services :", r6.rstrip()

r7=str(client.get_value(number=7).resultaat)
print "Resultaat Vrije Schijfruimte :", r7.rstrip()

r8=str(client.get_value(number=8).resultaat)
print "Resultaat Aantal ingelogde gebruikers :", r8.rstrip()

r9=str(client.get_value(number=9).resultaat)
print "Resultaat Uptime :", r9.rstrip()

r10=str(client.get_value(number=10).resultaat)
print "Beschikbare werkgeheugen :", r10.rstrip()

r11=str(client.get_value(number=11).resultaat)
print "IP adressen :", r11.rstrip()