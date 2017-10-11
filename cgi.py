# -*- coding: UTF-8 -*-
from web_cgi import WebCgiService
from web_cgi.ttypes import *


from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


class WebCgiHandler:
	def __init__(self):
		pass
	
	def transport(self, request):
		try:
			response = GeneralResponse()
			response.code = 1
			response.msg = '123'
			response.data = '213'
			print 'response'
			return response
		except Exception as e:
			print e


try:
	handler = WebCgiHandler()
	processor = WebCgiService.Processor(handler)
	transport = TSocket.TServerSocket(port=9090)
	tfactory = TTransport.TBufferedTransportFactory()
	pfactory = TBinaryProtocol.TBinaryProtocolFactory()
	server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
	
	# You could do one of these for a multithreaded server
	# server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)
	# server = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory)
	
	print 'Starting the server...'
	server.serve()
	print 'done.'
except Exception as e:
	print e


