#!/usr/bin/env python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

  net = Mininet( topo=None,
                 build=False,
                 ipBase='10.0.0.0/8')

  info( '*** Adding controller\n' )
  c0=net.addController(name='c0',
                       controller=Controller,
                       protocol='tcp',
                       port=6633)

  info( '*** Add switches\n')
  s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
  s2 = net.addSwitch('s2', cls=OVSKernelSwitch)
  r3 = net.addHost('r3', cls=Node, ip='10.0.1.1/8')
  r3.cmd('sysctl -w net.ipv4.ip_forward=1')
  r4 = net.addHost('r4', cls=Node, ip='192.168.1.1/24')
  r4.cmd('sysctl -w net.ipv4.ip_forward=1')
  r5 = net.addHost('r5', cls=Node, ip='10.0.1.2/8')
  r5.cmd('sysctl -w net.ipv4.ip_forward=1')

  info( '*** Add hosts\n')
  h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute='10.0.1.1/8')
  h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute='10.0.1.1/8')
  h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute='10.0.1.2/8')
  h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute='10.0.1.2/8')

  info( '*** Add links\n')
  net.addLink(h1, s1)
  net.addLink(h2, s1)
  net.addLink(h3, s2)
  net.addLink(h4, s2)
  net.addLink(s2, r5)
  net.addLink(s1, r3)
  net.addLink(r3, r4, intfName1='r3-eth1', params1={'ip': '192.168.1.1/24'})
  net.addLink(r4, r5, intfName1='r4-eth1', params1={'ip': '10.0.1.2/8'})

  info( '*** Starting network\n')
  net.build()
  info( '*** Starting controllers\n')
  for controller in net.controllers:
    controller.start()

  info( '*** Starting switches\n')
  net.get('s2').start([c0])
  net.get('s1').start([c0])

  info( '*** Post configure switches and hosts\n')

  CLI(net)
  net.stop()

if __name__ == '__main__':
  setLogLevel( 'info' )
  myNetwork()

