# Some examples below...
(Get-WmiObject -Class MSAcpi_ThermalZoneTemperature -Namespace root/wmi | measure-object CurrentTemperature -Average).Average/10-273.15 #gemiddelde temperatuur /10 = kelvin -273.15 = celcius
(Get-WmiObject Win32_PhysicalMemory | measure-object Capacity -sum).sum/1gb
(get-service | where {$_.status -eq 'Running'}).count

#ps | measure-object | select count | Out-File C:\scripts\log\agent_counters.txt
ps | Export-Clixml c:\scripts\log\magweg.xml
ps | Export-Csv C:\scripts\log\magweg.csv -Force -NoTypeInformation
$a = ps | measure-object
$a.Count
#ps | measure-object | select -expandproperty count