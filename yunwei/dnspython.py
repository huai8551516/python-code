import dns.resolver
import requests
import httplib

domain = raw_input('Please input domain:')
A = dns.resolver.query(domain, 'A')

appdomain = 'www.google.com.hk'
ip_list = []
get_content = []
httplib.socket.setdefaulttimeout(5)
for i in A.response.answer:
    for j in i.items:
        ip_list.append(j.address)
for ip in ip_list:
    check_url = ip + ':80'
    conn = httplib.HTTPConnection(check_url)
    conn.request('GET', '/', headers = {'Host': appdomain})
    res = httplib.getresponse()
    get_content = res.read(15)
    if get_content == '!<doctype html>':
        print ip + ' [OK]'