# OrkSec Drone
## Hack the Air
### preword
I used a Promark GPS drone from wallmart for this project, as its flying range is high enough for my purposes and as it is still in a normal budget and not overpriced.

### Installation
run the `Install.sh` file on a linux machine. Make sure to run it with sudo, in order to run it in one rush, without the need of having to provide passwords for every single command.
### Assembling
This project is based on a Drone (`Promark GPS`, in my case) equiqqed with a Raspberry pi, running a linux distro (Kali linux, for example). 
You will have to burn a power port to the existing power port, to power the raspberry pi. If you want to have a better shell signal, go ahead and buy a antenna.
### Accessing the shell
run `telnet <ip> 1337` where `<ip` is the global/local ip address of your raspberry pi. If you get a unknown host error, make sure that you've runned the install script.
### Functions
The OrkSec Drone will be eqquiqed with a wide range of functions, such as scanning for nearby devices or wifi networks, capturing wifi handshakes and much more. keep in mind that a better antenna may solve a bad shell connection Problem.
### Wiring and setting up hardware
#### Things you will need:
- a Drone that can handle a weight of a raspberry pi 3 (Promark GPS)
- a Raspberry pi 3
- a mini USB cable
- a set of screwdrivers to open the drone
- a soldering iron					(optional)
#### Step 1	Basic connections
disassemble to drone case, as deep as needed to see the connectors which connect the battery with 2 other cables, for the drone self. Now open up the mini USB cable, so you can see the two cables inside. One is for plus, one is for minus.
If you never did something like this, the Promark drone has a red cable for plus and a black cable for minus inside, so you will see where to connect them.
Now take the plus cable of the mini USB cable, and solder it to the inner power port of the drone (red).
Do the same with the minus cable and the inner drone power port (black).
You could now try to start the drone and check if the raspberry pi boots, but as the Promark drone for example has a 7.4V battery and the raspberry pi 3 takes a 5V input,
you would have to decrease the power, incoming into the raspberry pi in the next step.
#### Step 2	Reducing power
The raspberry pi 3 can handle up to 5V incoming, into the mini USB port. We have 7V, and that would make the raspberry pi overheat and just dont work after a very short time. So we need to limit the incoming power somehow.

