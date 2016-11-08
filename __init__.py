# -*- coding: UTF-8 -*-
'''
Get paper after releasing (NEU)
Author: dmzitnzc@gmail.com
License: GPLv3
'''

import socket
from bs4 import  BeautifulSoup

__author__ = 'Eleflea'
__version__ = '0.0.1'
__all__ = ['getExamIfo', 'linkWrapper', 'PRO', 'COMPLEX', 'MATHE']

PRO = '概率统计_GL'
COMPLEX = '复变函数_FB'
MATHE = '高等数学_GS'

def getExamIfo(studentNumber, dataSource):
	data = """POST /WebService/StudentService.asmx HTTP/1.1
User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; MS Web Services Client Protocol 4.0.30319.42000)
Content-Type: text/xml; charset=utf-8
SOAPAction: "http://tempuri.org/getTemplate"
Host: 202.118.26.80
Content-Length: 414
Expect: 100-continue

<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><soap:Body><getTemplate xmlns="http://tempuri.org/"><key>_3[#$%wd*</key><studentNumber>{0:d}</studentNumber><type>1</type><dataSource>{1:s}</dataSource></getTemplate></soap:Body></soap:Envelope>"""
	data = data.format(studentNumber ,dataSource)

	examSocket = socket.socket()
	examSocket.settimeout(3)
	examSocket.connect(('202.118.26.80', 80))
	examSocket.sendall(data.encode('utf-8'))
	data_recv = examSocket.recv(9999).decode('utf-8', errors = 'ignore')

	examSoup = BeautifulSoup(data_recv, "html.parser")
	#print(examSoup.prettify())
	l_name = map(lambda x: x.get_text(), examSoup.findAll('name'))
	l_src = map(lambda x: linkWrapper(x.get_text()), examSoup.findAll('src'))
	return(list(zip(l_name, l_src)))

def linkWrapper(src):
	return('http://202.118.26.80/PublishChoice/' + src)

if __name__ == '__main__':
	stuNum = 20124321
	l_exam = getExamIfo(stuNum, COMPLEX)
	print(l_exam)
