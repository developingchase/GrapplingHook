# GrapplingHook
Open Source 802.11 Direction Finder

Grappling Hook utilizes a wireless RTS/CTS flood attack as a carrier signal to conduct physical direction finding and terminal guidance of wi-fi enabled devices. Thanks to nikseetharaman for the original project!

Python3 Library Requirements:
scapy

# Usage:
Run as sudo because access to the wireless adapter is required.
You can use one or two cards in monitor mode.

`python Grapple.py -h`

`python Hook.py -h`

1. Set card(s) to monitor mode.
2. Determine which channel device of interest is on.

`sudo airodump-ng wlan0mon --band abg`

3. Lock card(s) to that channel.

`sudo airodump-ng wlan0mon -c11`

4. Launch Hook.py to report RSSI values from the device's received CTS frames. Preferably, use a directional antenna on this card.

```
sudo python3 Hook.py -r 4C:FC:AA:00:00:01 -i wlan0mon
RSSI of 4C:FC:AA:00:00:01 = -70 ::xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
RSSI of 4C:FC:AA:00:00:01 = -68 ::xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
RSSI of 4C:FC:AA:00:00:01 = -68 ::xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
RSSI of 4C:FC:AA:00:00:01 = -70 ::xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
RSSI of 4C:FC:AA:00:00:01 = -66 ::xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
RSSI of 4C:FC:AA:00:00:01 = -68 ::xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
RSSI of 4C:FC:AA:00:00:01 = -32 ::xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
RSSI of 4C:FC:AA:00:00:01 = -68 ::xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
RSSI of 4C:FC:AA:00:00:01 = -66 ::xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
RSSI of 4C:FC:AA:00:00:01 = -68 ::xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
RSSI of 4C:FC:AA:00:00:01 = -68 ::xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
RSSI of 4C:FC:AA:00:00:01 = -66 ::xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
RSSI of 4C:FC:AA:00:00:01 = -70 ::xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
RSSI of 4C:FC:AA:00:00:01 = -68 ::xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
RSSI of 4C:FC:AA:00:00:01 = -72 ::xxxxxxxxxxxxxxxxxxxxxxxxxxxx
RSSI of 4C:FC:AA:00:00:01 = -70 ::xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
RSSI of 4C:FC:AA:00:00:01 = -30 ::xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
RSSI of 4C:FC:AA:00:00:01 = -68 ::xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
RSSI of 4C:FC:AA:00:00:01 = -72 ::xxxxxxxxxxxxxxxxxxxxxxxxxxxx
RSSI of 4C:FC:AA:00:00:01 = -28 ::xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
5. If needed, launch Grapple.py to stimulate the device of interest. Preferably, use a second device for this.

`sudo python3 Grapple.py -t 4C:FC:AA:00:00:01 -r 00:00:00:00:00:00 -i wlan0mon`

6. Move around and attempt to locate the device.

# TODO:

Error handling

Experiment with rate throttling Grapple for more effectiveness

Add an audible tone

Handle multiple clients in Hook (Color code?)

Log output

Add GPS to log output

