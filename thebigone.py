import sys
from optparse import OptionParser

#options bingcache
parser.add_option("-b", "--bing", dest='bing', help="Bing Search", action='store')
#options webcache
parser.add_option("-w", "--web", dest='web', help="Google Web Cache Search", action='store')
#options translate
parser.add_option("-t", "--tran", dest='tran', help="translate", action='store')
#options Ipv4 range
parser.add_option("-I", "--ipv4", dest='ipv4', help="ipv4 Full range", action='store')
#options domain
parser.add_option("-d", "--dom", dest='dom', help="domain", action='store')
#options proxylist
parser.add_option("-p", "--prox", dest='prox', help="proxy file", action='store')
#options autoproxy
parser.add_option("-a", "--auto", dest='auto', help="autoproxy", action='store')
#options waybackurls collect
parser.add_option("-W", "--wbu", dest='wayback', help="Collect waybackurls", action='store')
#options crt.sh for domains to waybackurls
parser.add_option("-c", "--crt", dest='crt', help="crt.sh domain collector", action='store')
#options useragenthop
parser.add_option("-u", "--user", dest='user', help="Useragenthop", action='store')
#options facebookcookiefile
parser.add_option("-C", "--cookie", dest='cookie', help="facebook cookie file", action='store')
#options grepreqs
parser.add_option("-g", "--gr", dest='gr', help="Grep requests", action='store')
#options grepurls
parser.add_option("-G", "--gu", dest='gu', help="Grep Urls", action='store')

def bingcache():

def webcache():

def translate():

def ipv4range():

def domain():

def proxylis():

def autoproxy():

def wbud():

def crtsh():

def useragents():

def cookie():

def grepreqs():

def grepurls():

def alltogether():
    if cookie:
        cookie()
    else:
        print("!cookie required! [OPT] -c cookiefile.txt!")
        print("Format: {'xs': '[cookie]', 'c_user': '[cookie]'}")
    if bing:
        bingcache()
    if web:
        webcache()
    if tran:
        translate()
    if ipv4:
        ipv4range()
    if dom:
        domain()
    if prox:
        proxylist()
    if auto:
        autoproxy()
    if wayback:
        wbud()
    if crt:
        crtsh()
    if user:
        useragents()
    if gr:
        grepreqs()
    if gu:
        grepurls()
    
if __name__ == "__main__":
    alltogether()
