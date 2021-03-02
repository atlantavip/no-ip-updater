from ipgetter2 import ipgetter1 as ipgetter
import requests, logging, sys, socket, smtplib, time, json
from requests.auth import HTTPBasicAuth

try:
    import http.client as http_client
except ImportError:
    # Python 2
    import httplib as http_client

publicIP = ipgetter.myip()

ddnsUserName = 'xyz'
ddnsPassword = 'P@ssw0rd123'
ddnsHostName = 'xyz.ddns.net'

## logs
log_f = open('router.log', 'w+')
log = []
log.append(time.strftime('run: %Y-%m-%d %H:%M'))
log.append ('Actual public IP: ' + publicIP)

lastPublicIP = socket.gethostbyname(ddnsHostName)

log.append ('last public IP: ' + lastPublicIP)


if (publicIP == lastPublicIP):
 log.append ('we don\'t do anything')
 log_f.write('\n'.join(log))
 log_f.close()
 sys.exit()
else:
 log.append ('needs to be updated')


## update
url = 'https://dynupdate.no-ip.com/nic/update'

payload = {'hostname' : ddnsHostName, 'myip' : publicIP}
headers = {'user-agent': 'Atlanta DDNS Updater/0.0.1 info@atlanta-web.hu'}

r = requests.get(url, params=payload, headers=headers, auth=HTTPBasicAuth(ddnsUserName, ddnsPassword))

print(json.dumps(payload), r.status_code)

gethost = socket.gethostbyname(ddnsHostName)
print ('get host:', json.dumps(gethost))
