#!/bin/bash
echo "Welcome to the OrkDrone installation menu."
echo "checking if tcpserver command is aviable..."
if which tcpserver >/dev/null ; then
	echo -e "[CHECK]\tTCPServer Command working already\t\t(ucspi-tcp)"
else
	echo -e "[WARN]\tInstalling TCPServer..."
	sudo apt-get install ucspi-tcp --yes
fi
echo -e "[CHECK]\tInstalling and enabling the SystemService\t(Telnet)"
if [ ! -f /etc/systemd/system/DroneTelnet.service ]; then
	sudo cp System-Services/DroneTelnet.service /etc/systemd/system/
	sudo systemctl enable DroneTelnet.service >/dev/null
	sudo systemctl start DroneTelnet.service >/dev/null
	echo -e "[CHECK]\tTelnet setten up on port 1337"
else
	echo -e "[CHECK]\tTelnet seems to be setten up already."
fi
