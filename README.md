# Eindopdracht Python Joris Koenraadt & Yaro Frere-Jean 

# Requirements
- Een netwerk met werkende internet verbinding
- 1 Management server (Windows 2012 R2)
- 1 of meerdere Agent clients (Windows)

# Installeren Management Server
1. Kopieer de setup.exe naar de management server.
2. Controleer voor het uitvoeren van de setup.exe of de computer internet verbinding heeft.
3. Voer setup.exe uit, er worden nu snelkoppelingen op het bureaublad geplaatst.
4. Start het installatiescript met behulp van de snelkoppeling, rechtermuisknop uitvoeren met powershell.
5. Volg de instructies in het scherm.
6. Om Python werkend te krijgen i.c.m. IIS dient er nog 1 wijziging gedaan te worden.
7. Open IIS manager, ga naar Default Website en open vervolgens in het scherm "Handler Mappings".
8. Zoek Python op en open deze, zet een spatie achteraan bij executebles en verwijder deze weer, sla dit op en klik vervolgens op ja.
9. De website is te bezoeken via localhost/index.py of <ipadres>/index.py

# Uitvoeren Agent Client
1. Kopieer de setup.exe naar de management server.
2. Controleer voor het uitvoeren van de setup.exe of de computer internet verbinding heeft.
3. Voer setup.exe uit, er worden nu snelkoppelingen op het bureaublad geplaatst.
4. Op het bureaublad komt nu een snelkoppeling Agent Script, voer deze uit.
5. De Agent software draait nu.

# Aanpassingen
Doordat wij gebruik hebben gemaakt van XML files is het mogelijk om de IP Adressen van de Agents in het dropdown menu te krijgen.
- Open hiervoor het volgende bestand: C:\inetpub\wwwroot\dropdown.xml.
- Voeg of wijzig hier de ipadressen en het aantal, hierna komen de ip adressen in het dropdown menu te voorschijn.