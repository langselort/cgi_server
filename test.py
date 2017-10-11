# -*- coding: UTF-8 -*-
from img_server.cls.rabbit_cls import RabbitClient
from img_server.Img_Service import ImgService
from img_server.Img_Service.ttypes import *

from web_cgi import WebCgiService
from web_cgi.ttypes import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

def test_thrif():
	
	try:
		request = GeneralRequest()
		request.img_file = '1.jpg'
		
		transport = TSocket.TSocket('localhost', 9090)
		transport = TTransport.TBufferedTransport(transport)
		protocol = TBinaryProtocol.TBinaryProtocol(transport)
		client = ImgService.Client(protocol)
		
		transport.open()
		result = client.upload_img(request)
		print result
		transport.close()
	except Exception as e:
		print e

def test_rabbit():
	fibonacci_rpc = RabbitClient()
	print("Requesting ")
	response = fibonacci_rpc.call('ooo')
	print("Got %r" % response)

def test_web_cgi():
	try:
		request = GeneralRequest()
		request.code = 1
		request.msg = '123'
		request.data = '213'
		
		transport = TSocket.TSocket('localhost', 9090)
		transport = TTransport.TBufferedTransport(transport)
		protocol = TBinaryProtocol.TBinaryProtocol(transport)
		client = WebCgiService.Client(protocol)
		
		transport.open()
		result = client.transport(request)
		print result
		transport.close()
	except Exception as e:
		print e

if __name__ == '__main__':
	test_web_cgi()


