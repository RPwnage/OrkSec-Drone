# OrkSec Drone
## Hack the Air
### Installation
run the `Install.sh` file on a linux machine. Make sure to run it with sudo, in order to run it in one rush, without the need of having to provide passwords for every single command.
### Assembling
This project is based on a Drone (`Promark GPS`, in my case) equiqqed with a Raspberry pi, running a linux distro (Kali linux, for example). 
You will have to burn a power port to the existing power port, to power the raspberry pi. If you want to have a better shell signal, go ahead and buy a antenna.
### Accessing the shell
run `telnet <ip> 1337` where `<ip` is the global/local ip address of your raspberry pi. If you get a unknown host error, make sure that you've runned the install script.
### Functions
The OrkSec Drone will be eqquiqed with a wide range of functions, such as scanning for nearby devices or wifi networks, capturing wifi handshakes and much more. keep in mind that a better antenna may solve a bad shell connection Problem.
