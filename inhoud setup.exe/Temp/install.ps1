echo "Deze installatie kan ongeveer 5 minuten duren... Voordat u verder gaat moet u er zeker van zijn dat deze computer internet verbinding heeft"
Import-Module ServerManager
Add-WindowsFeature Web-Server -IncludeAllSubFeature
Remove-Item C:\inetpub\wwwroot\*
Copy-Item -Path C:\Temp\web.config -Destination C:\inetpub\wwwroot
Copy-Item -Path C:\scripts\* -Destination C:\inetpub\wwwroot
C:\Temp\python-2.7.11.amd64.msi /quiet
echo "Python wordt geïnstalleerd dit kan 2 minuten duren..."
Start-Sleep -Seconds 30 
echo "Installeer nu PySimpleSOAP, u kunt op next drukken tot het voltooid is."
pause
C:\Temp\PySimpleSOAP-1.08d.win32.exe
Start-Sleep -Seconds 60 
& C:\Temp\xml.bat
powershell Remove-Item C:\Temp\*
echo "Deze installatie is voldaan☕"
pause