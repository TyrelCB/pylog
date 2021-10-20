#!/usr/bin/env python

## Tiny Syslog Server in Python.
##
## This is a tiny syslog server that is able to receive UDP based syslog
## entries on a specified port and save them to a file.
## That's it... it does nothing else...
## There are a few configuration parameters.



HOST, PORT = "0.0.0.0", 514


import datetime as dt
import Write_Output as wo
import socketserver


class SyslogUDPHandler(socketserver.BaseRequestHandler):

	def handle(self):
		data = bytes.decode(self.request[0].strip())
		socket = self.request[1]
		client_address = self.client_address[0]
		timestamp = dt.datetime.now()
		date = timestamp.date()
		logfile = client_address+'_syslog_'+str(date)+'.log'
		logdata = '<From:> '+client_address+' <Timestamp:> '+str(timestamp)+' <Syslog Data:> '+data
		print(logdata)
		wo.append_to_file(logfile, logdata)

if __name__ == "__main__":
	try:
		server = socketserver.UDPServer((HOST,PORT), SyslogUDPHandler)
		server.serve_forever(poll_interval=0.5)
	except (IOError, SystemExit):
		raise
	except KeyboardInterrupt:
		print ("Crtl+C Pressed. Shutting down.")
