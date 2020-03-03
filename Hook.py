### GRAPPLING HOOK - HOOK MODULE
### HOOK parses the signal strength from target clients CTS packets
### Displays as received signal strength indicated (RSSI) in dB
### python3

from scapy.all import *
import optparse
from time import sleep
import sys

#takes the RSSI value and creates a bar for display
#the stronger the signal, the longer the bar
#TODO: error handling
def barlength(rssi):
    len = 100 + int(rssi)
    bar = ""
    x=0
    while x<len:
      bar = bar + "x"
      x=x+1
    return bar

def ctscap(p):
    if p.haslayer(Dot11):
        if p.type == 1 and p.subtype == 12 and str(p.addr1).upper() == str(receiveclient).upper(): #Its a CTS frame headed to your capture tool
            sys.stdout.write("RSSI of "+str(receiveclient).upper()+" = "+str(p.dBm_AntSignal)+" ::"+str(barlength(p.dBm_AntSignal)+"\n"))
            sys.stdout.flush()
def main():
    parser = optparse.OptionParser('usage%prog '+'-r <receiveclient> -i <interface>')
    parser.add_option('-r', dest='receiveclient', type='string', help='specify listener MAC address')
    parser.add_option('-i', dest='interface', type='string', help='specify receive interface')
    (options, args) = parser.parse_args()
    global receiveclient
    receiveclient = options.receiveclient
    global interface
    interface = options.interface   
   
    sniff(iface=interface, prn=ctscap) #Begin SCAPY sniffer and apply function "ctscap" to every packet

if __name__ == '__main__':
    main()
