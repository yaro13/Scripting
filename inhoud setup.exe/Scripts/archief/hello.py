##print 'Content-type: text/html'
##print ''
##print '<h2>'
##print 'See this is just like most other HTML'
##print '</h2>'
import cgitb
import cgi
from subprocess import Popen

cgitb.enable()
#execfile('management.bat')

p = Popen("management.bat", cwd=r"C:\scripts")
stdout, stderr = p.communicate()