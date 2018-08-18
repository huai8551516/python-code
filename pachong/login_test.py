# -*- coding: utf-8 -*-
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#http://passport.17k.com/login.action?jsonp=true
#
session = requests.session()
print session.post('http://passport.17k.com/login.action?jsonp=true').text
login_url = 'http://passport.17k.com/login.action?jsonp=true'
mcode_url = 'http://passport.17k.com/mcode.jpg'
mcode = raw_input('输入验证码：')
userData = {
	'userName': '15579305610',
    'password': 'huaimima1234+',
    'verificationCode': mcode,
    'isCode': 0,
    'isAutoLogin': 'false',
    'postCallback': 'parent.Q.post_artwc_callback'
}
res = session.post(login_url, data=userData)
print res.text