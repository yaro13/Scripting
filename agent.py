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

# ---------------------------------------------------------

# List of all your agent functions that can be called from within the management script.
# A real developer should do this differently, but this is more easy.
def get_value(number):
    "return the result of one of the pre-define numbers"
    print "get_value, of of item with number=",number

    # An example of a value that is acquired using Python only.
    # returns a string
    if number == 1:
        return sys.platform

    # Another example of a value that is acquired using Python only.
    # returns a string
    if number == 2:
        return sys.getdefaultencoding()

    # Useless of course but returning an int
    if number == 3:
        return 8888

    # Example in which a PowerShell script is used. The STDOUT is used to pass results back to python.
    # Exporting with export-csv and reading the CSV using Python is also possible of course.
    if number == 4:
        p=subprocess.Popen(['powershell',
            '''(Get-WmiObject -Class MSAcpi_ThermalZoneTemperature -Namespace root/wmi | measure-object CurrentTemperature -Average).Average/10-273.15 #gemiddelde temperatuur /10 = kelvin -273.15 = celcius'''],
        stdout=subprocess.PIPE)                  # Zorg ervoor dat je de STDOUT kan opvragen.
        output = p.stdout.read()                 # De stdout
        return output

    # Example of sing a PowerShell oneliner. Useful for simple PowerShell commands.
    if number == 5:
        p=subprocess.Popen(['powershell',
            '''(Get-WmiObject Win32_PhysicalMemory | measure-object Capacity -sum).sum/1gb #Totaal geheugen op apparaat'''],
        stdout=subprocess.PIPE)                  # Zorg ervoor dat je de STDOUT kan opvragen.
        output = p.stdout.read()                 # De stdout
        return output

	    # Example of sing a PowerShell oneliner. Useful for simple PowerShell commands.
    if number == 6:
        p=subprocess.Popen(['powershell',
            '''(get-service | where {$_.status -eq 'Running'}).count #aantal draaiende processen'''],
        stdout=subprocess.PIPE)                  # Zorg ervoor dat je de STDOUT kan opvragen.
        output = p.stdout.read()                 # De stdout
        return output

	    # Example of sing a PowerShell oneliner. Useful for simple PowerShell commands.
    if number == 7:
        p=subprocess.Popen(['powershell',
            '''Get-CimInstance win32_logicaldisk | foreach-object {write " $($_.caption) $('{0:N2}' -f ($_.FreeSpace/1gb)) GB"} #Vrije ruimte op schijven in GB'''],
        stdout=subprocess.PIPE)                  # Zorg ervoor dat je de STDOUT kan opvragen.
        output = p.stdout.read()                 # De stdout
        return output

			    # Example of sing a PowerShell oneliner. Useful for simple PowerShell commands.
    if number == 8:
        p=subprocess.Popen(['powershell',
            '''(Get-WmiObject -Class win32_process ` -Filter "name='explorer.exe'" | Foreach-Object {$_.GetOwner()} | Select User).count #Controleer wie explorer.exe draait geeft info terug gefilterd op User, en telt op'''],
        stdout=subprocess.PIPE)                  # Zorg ervoor dat je de STDOUT kan opvragen.
        output = p.stdout.read()                 # De stdout
        return output

    # Example in which a PowerShell script is used. The STDOUT is used to pass results back to python.
    # Exporting with export-csv and reading the CSV using Python is also possible of course.
    if number == 9:
        p=subprocess.Popen(['powershell.exe',    # Atlijd gelijk of volledig pad naar powershell.exe
            '-ExecutionPolicy', 'Unrestricted',  # Override current Execution Policy
            'c:\\scripts\\Get-Uptime.ps1'],  # Naam van en pad naar je PowerShell script
        stdout=subprocess.PIPE)                  # Zorg ervoor dat je de STDOUT kan opvragen.
        output = p.stdout.read()                 # De stdout
        return output

				    # Example of sing a PowerShell oneliner. Useful for simple PowerShell commands.
    if number == 10:
        p=subprocess.Popen(['powershell',
            '''systeminfo | find "Available Physical Memory"'''],
        stdout=subprocess.PIPE)                  # Zorg ervoor dat je de STDOUT kan opvragen.
        output = p.stdout.read()                 # De stdout
        return output

					# Example of sing a PowerShell oneliner. Useful for simple PowerShell commands.
    if number == 11:
        p=subprocess.Popen(['powershell',
            '''Get-NetIPAddress -AddressFamily IPv4 | select IPAddress | Foreach-Object {write " $($_.caption) $('{0:N2}' -f ($_.IPAddress))"}'''],
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

