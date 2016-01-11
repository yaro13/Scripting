##print 'Content-type: text/html'
##print ''
##print '<h2>'
##print 'See this is just like most other HTML'
##print '</h2>'
import cgitb
import cgi
import subprocess

cgitb.enable()
#execfile('management.bat')

p = subprocess.Popen("management.bat", cwd=r"C:\scripts", stdout = subprocess.PIPE)
output = p.stdout.read()
print output
