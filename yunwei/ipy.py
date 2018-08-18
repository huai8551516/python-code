# -*- coding: utf-8 -*-
from IPy import IP

ip = IP('192.168.0.1')
print ip.len()#主机地址个数
for x in ip:
    print x
print ip.reverseNames()#ip反向解析地址
print ip.iptype()#ip地址类型 公有地址/私有地址
print IP('124.160.226.98').iptype()
print ip.int()#ip地址整型
print ip.strHex()#ip地址16进制
print ip.strBin()#ip地址2进制
print IP('0xffffffff')#16进制转ip地址

#ip地址网络地址转换

print IP('192.168.1.1').make_net('255.255.255.0')
print IP('192.168.1.1/255.255.255.0', make_net=True)
print IP('192.168.1.0-192.168.1.255', make_net=True)

#与上相反
print IP('192.168.1.0/24').strNormal(0)
print IP('192.168.1.0/24').strNormal(1)
print IP('192.168.1.0/24').strNormal(2)
print IP('192.168.1.0/24').strNormal(3)


ip_s = raw_input('Please input ip or net-range:')
ips = IP(ip_s)
if len(ips) > 1: #网络地址
    print 'net: %s' % ips.net()#网络地址
    print 'netmask: %s' % ips.netmask()#子网掩码
    print 'broadcast: %s' % ips.broadcast()#广播地址
    print 'reverse address: %s' % ips.reverseNames()[0] #反向解析地址
    print 'subnet: %s' % len(ips) #子网个数
else: 
    print 'reverse address: %s' % ips.reverseNames()
print 'Hexadecimal: %s' % ips.strHex()
print 'Binary: %s' % ips.strBin()
print 'iptype: %s' % ips.iptype()