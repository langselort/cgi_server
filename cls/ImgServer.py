# -*- coding: UTF-8 -*-
import sys
sys.path.append("..")

from img_server.Img_Service import ImgService
from img_server.Img_Service.ttypes import *
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


class ImgServer(object):
	
	def __init__(self):
		pass
	
	def upload_img(self):
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
			return result
		except Exception as e:
			print e
			
if __name__ == '__main__':
    img_server = ImgServer()
    print(img_server.upload_img())