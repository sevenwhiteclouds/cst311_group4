#!/usr/bin/python
import os

from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.net import Mininet
from mininet.node import Controller, Node
from mininet.node import Host
from mininet.node import OVSKernelSwitch
from mininet.term import makeTerm


def myNetwork():

  # Runs certificate creation script
  os.system("python3 CertGenerate.py")

  net = Mininet(topo=None, build=False, ipBase='10.0.0.0/24')

  info('*** Adding controller\n')
  c0 = net.addController(name='c0',
                         controller=Controller,
                         protocol='tcp',
                         port=6633)

  info('*** Add switches\n')
  s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
  s2 = net.addSwitch('s2', cls=OVSKernelSwitch)
  r5 = net.addHost('r5', cls=Node, ip='10.0.2.1/24')
  r5.cmd('sysctl -w net.ipv4.ip_forward=1')
  r4 = net.addHost('r4', cls=Node, ip='192.168.1.1/24')
  r4.cmd('sysctl -w net.ipv4.ip_forward=1')
  r3 = net.addHost('r3', cls=Node, ip='10.0.1.1/24')
  r3.cmd('sysctl -w net.ipv4.ip_forward=1')

  info('*** Add hosts\n')
  h1 = net.addHost('h1', cls=Host, ip='10.0.1.2/24', defaultRoute='via 10.0.1.1')
  h2 = net.addHost('h2', cls=Host, ip='10.0.1.4/24', defaultRoute='via 10.0.1.1')
  h3 = net.addHost('h3', cls=Host, ip='10.0.2.2/24', defaultRoute='via 10.0.2.1')
  h4 = net.addHost('h4', cls=Host, ip='10.0.2.4/24', defaultRoute='via 10.0.2.1')

  info('*** Add links\n')
  net.addLink(h1, s1)
  net.addLink(h2, s1)
  net.addLink(h3, s2)
  net.addLink(h4, s2)
  net.addLink(s2, r5, intfName2='r5-eth1', params2={'ip': '10.0.2.3/24'})
  net.addLink(s1, r3, intfName2='r3-eth1', params2={'ip': '10.0.1.3/24'})
  net.addLink(r3, r4, intfName1='r3-eth0', params1={'ip': '192.168.1.2/24'}, intfName2='r4-eth0', params2={'ip': '192.168.1.4/24'})
  net.addLink(r4, r5, intfName1='r4-eth1', params1={'ip': '192.168.3.4/24'}, intfName2='r5-eth0', params2={'ip': '192.168.3.6/24'})

  info('*** Starting network\n')
  net.build()

  #Static Route: 1
  info(net["r4"].cmd("ip route add 10.0.1.0/24 via 192.168.1.2 dev r4-eth0"))

  #Static Route: 2
  info(net["r3"].cmd("ip route add 10.0.2.0/24 via 192.168.1.1 dev r3-eth0"))

  #Static Route: 3
  info(net["r5"].cmd("ip route add 10.0.1.0/24 via 192.168.3.4 dev r5-eth0"))

  #Static Route: 4
  info(net["r4"].cmd("ip route add 10.0.2.0/24 via 192.168.3.6 dev r4-eth1"))

  #Static Route: 5
  info(net["r5"].cmd("ip route add 192.168.1.0/24 via 192.168.3.4 dev r5-eth0"))

  #Static Route: 6
  info(net["r3"].cmd("ip route add 192.168.3.0/24 via 192.168.1.1 dev r3-eth0"))

  info('*** Starting controllers\n')
  for controller in net.controllers:
    controller.start()

  info('*** Starting switches\n')
  net.get('s2').start([c0])
  net.get('s1').start([c0])

  info('*** Post configure switches and hosts\n')

  # Creates xterm windows and automatically runs commands
  makeTerm(h4, title='Chat Server', term='xterm', display=None, cmd='python3 chat_server.py && bash')
  makeTerm(h1, title='Chat Client 1', term='xterm', display=None, cmd='python3 chat_client.py && bash')
  makeTerm(h3, title='Chat Client 2', term='xterm', display=None, cmd='python3 chat_client.py && bash')
  makeTerm(h2, title='Web Server', term='xterm', display=None, cmd='python3 webserver.py && bash')

  CLI(net)

  net.stop()

  # Closes all active xterm windows
  net.stopXterms()


if __name__ == '__main__':
  setLogLevel('info')
  myNetwork()