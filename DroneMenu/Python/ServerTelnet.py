import gevent, gevent.server, sys, os, json, requests, bluetooth
from bluetooth import *
from wifi import *
from telnetsrv.green import TelnetHandler, command
class MyTelnetHandler(TelnetHandler):
	Welcome = "Welcome to the drone menu."
	@command(["echo", "copy", "repeat"])
	def command_echo(self, params):
		self.writeresponse(' '.join(params))
	@command(["help"])
	def command_help(self, params):
		self.writeresponse("Help menu\nscan\t-\tScan for nearby networks")
	@command(["scan"])
	def command_scan(self, params):
		try:
			if params[0]:
				if params[0] == "device_bluetooth":
					self.writeresponse("Scanning for bluetooth devices...")
                                        freeDevices = discover_devices(lookup_names = True)
                                        self.writeresponse("Found a total of " + len(freeDevices) + "!")
                                        if len(freeDevices) != 0:
                                            for name, addr in freeDevices:
                                                    print addr + "\t-\t" + name
                                elif params[0] == "device_wifi":
                                        self.writerespons("Scanning for devices in the current network...")
                                elif params[0] == "wifi_network":
                                        self.writeresponse("Scanning for WiFi networks...")
                                        wifiNetworks = []
                                        self.writeresponse("found a total of "+str(len(Cell.all("wlan0")))+" Wifi networks!")
                                        for index,name in enumerate(Cell.all("wlan0")):
                                            self.writeresponse("["+str(index)+"] "+str(name.ssid)) 
                                                    
                                else:
                                        self.writeresponse("Please provide parameter 1!\nwifi_network/device_wifi/device_bluetooth")
		except IndexError:
			self.writeresponse("Please provide parameter 1!\nwifi_network/device_wifi/device_bluetooth/wifi_network")
server = gevent.server.StreamServer(("", 1312), MyTelnetHandler.streamserver_handle)
server.serve_forever()
