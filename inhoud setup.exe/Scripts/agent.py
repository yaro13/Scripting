"""
Usage:
Portable Python installed in c:\P2.7.6.1 and agent script in c:\scripts\agent.py
Open the firewall if needed and start this agent:
<cmd>
c:\\P2\App\python.exe c:\scripts\agent.py
"""

from pysimplesoap.server import SoapDispatcher, SOAPHandler
from BaseHTTPServer import HTTPServer
import sys,subprocess
import re
from lxml import etree

# ---------------------------------------------------------
#Commando's importeren vanuit XML bestand
tree = etree.parse('C:\scripts\commando.xml')
xml_open = tree.xpath('/commandos/windows/powershell/open[1]/text()')[0]
xml_hostname = tree.xpath('/commandos/windows/powershell/hostname[1]/text()')[0]
xml_temperatuur = tree.xpath('/commandos/windows/powershell/temperatuur[1]/text()')[0]
xml_ram = tree.xpath('/commandos/windows/powershell/ram[1]/text()')[0]
xml_services = tree.xpath('/commandos/windows/powershell/services[1]/text()')[0]
xml_schijfruimte = tree.xpath('/commandos/windows/powershell/schijfruimte[1]/text()')[0]
xml_gebruikers = tree.xpath('/commandos/windows/powershell/gebruikers[1]/text()')[0]
xml_scriptuptime = tree.xpath('/commandos/windows/powershell/scriptuptime[1]/text()')[0]
xml_executionpolicy = tree.xpath('/commandos/windows/powershell/parameters/executionpolicy[1]/text()')[0]
xml_unrestricted = tree.xpath('/commandos/windows/powershell//parameters/unrestricted[1]/text()')[0]
xml_werkgeheuden_vrij = tree.xpath('/commandos/windows/powershell/werkgeheugenvrij[1]/text()')[0]
xml_ipv4adressen = tree.xpath('/commandos/windows/powershell/ipv4adressen[1]/text()')[0]

# List of all your agent functions that can be called from within the management script.
# A real developer should do this differently, but this is more easy.
def get_value(number):
    "return the result of one of the pre-define numbers"
    print "get_value, of of item with number=",number

    # Vraag Hostname op van het systeem via Powershell
    if number == 1:
        p=subprocess.Popen([xml_open, xml_hostname],
        stdout=subprocess.PIPE)                  # Zorg ervoor dat je de STDOUT kan opvragen.
        output = p.stdout.read()                 # De stdout
        return output.split('\r\n')[0]

    # An example of a value that is acquired using Python only.
    # Laat zien welk platform er wordt gebruikt
    if number == 2:
        return sys.platform

    # Another example of a value that is acquired using Python only.
    # Welke karakter tabel wordt er gebruikt
    if number == 3:
        return sys.getdefaultencoding()

    # Useless of course but returning an int
    if number == 4:
        return 8888

    # Temperatuur opvragen, geeft fout in VM
    if number == 5:
        p=(subprocess.Popen([xml_open , xml_temperatuur],
        stdout=subprocess.PIPE))                  # Zorg ervoor dat je de STDOUT kan opvragen.
        output = (p.stdout.read())
        boolean = bool(re.search(r'^Get-WmiObject.',output))
        if boolean == True:
            temperatuur = 'Temperatuur kan niet worden opgevraagd'
        else:
            temperatuur = output.split('\r')[0] + ' &#8451'
        return temperatuur

    # Hoeveel RAM is er beschikbaar
    if number == 6:
        p=subprocess.Popen([xml_open, xml_ram],
        stdout=subprocess.PIPE)                  # Zorg ervoor dat je de STDOUT kan opvragen.
        output = p.stdout.read()                # De stdout
        return output.split('\r\n')[0]+' GB'

    # Hoeveel services draaien er
    if number == 7:
        p=subprocess.Popen([xml_open, xml_services],
        stdout=subprocess.PIPE)                  # Zorg ervoor dat je de STDOUT kan opvragen.
        output = p.stdout.read()                 # De stdout
        return output.split('\r\n')[0]

    # Hoeveel schijfruimte is er
    if number == 8:
        p=subprocess.Popen([xml_open, xml_schijfruimte],
        stdout=subprocess.PIPE)                  # Zorg ervoor dat je de STDOUT kan opvragen.
        output = p.stdout.read()                 # De stdout
        output1 =  output.split('\r\n')
        return output1[0] + output1[1]

    # Hoeveel gebruikers zijn er ingelogd op de Agent
    if number == 9:
        p=subprocess.Popen([xml_open, xml_gebruikers],
        stdout=subprocess.PIPE)                  # Zorg ervoor dat je de STDOUT kan opvragen.
        output = p.stdout.read()                 # De stdout
        if output == "":
            output = 1
        else:
            pass
        return output

    # Wat is de uptime van de agent
    if number == 10:
        p=subprocess.Popen([xml_open,    # Atlijd gelijk of volledig pad naar powershell.exe
            xml_executionpolicy, xml_unrestricted ,  # Override current Execution Policy
            xml_scriptuptime],  # Naam van en pad naar je PowerShell script
        stdout=subprocess.PIPE)                  # Zorg ervoor dat je de STDOUT kan opvragen.
        output = p.stdout.read()                 # De stdout
        return output.split('\r\n')[0]

    # Hoeveel werkgeheugen is er vrij?
    if number == 11:
        p=subprocess.Popen([xml_open, xml_werkgeheuden_vrij],
        stdout=subprocess.PIPE)                  # Zorg ervoor dat je de STDOUT kan opvragen.
        output = p.stdout.read()                 # De stdout
        output1 = output.split(':')[1]
        return output1.split('\r\n')[0]

    # Welke ipv4 adressen zijn er beschikbaar
    if number == 12:
        p=subprocess.Popen([xml_open, xml_ipv4adressen],
        stdout=subprocess.PIPE)                  # Zorg ervoor dat je de STDOUT kan opvragen.
        output = p.stdout.read()                 # De stdout
        return output.split(':')[0]

    # Last value
    return None


# ---------------------------------------------------------

# do not change anything unless you know what you're doing.
port=8008
dispatcher = SoapDispatcher(
    'my_dispatcher',
    location = "http://localhost:8008/",
    action = 'http://localhost:8008/', # SOAPAction
    namespace = "http://example.com/sample.wsdl", prefix="ns0",
    trace = True,
    ns = True)

# do not change anything unless you know what you're doing.
dispatcher.register_function('get_value', get_value,
    returns={'resultaat': str},   # return data type
    args={'number': int}         # it seems that an argument is mandatory, although not needed as input for this function: therefore a dummy argument is supplied but not used.
    )

# Let this agent listen forever, do not change anything unless needed.
print "Starting server on port",port,"..."
httpd = HTTPServer(("", port), SOAPHandler)
httpd.dispatcher = dispatcher
httpd.serve_forever()

