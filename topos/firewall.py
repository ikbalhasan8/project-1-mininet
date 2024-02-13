from mininet.net import Mininet
from mininet.node import OVSSwitch, RemoteController
from mininet.link import TCLink
from mininet.cli import CLI

def create_firewall_net():
    net = Mininet(controller=RemoteController, switch=OVSSwitch, link=TCLink)

    # Add controller
    c0 = net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6653)

    # Add switches
    s1 = net.addSwitch('s1')

    # Add hosts
    h1 = net.addHost('h1', ip='10.0.0.1')
    h2 = net.addHost('h2', ip='10.0.0.2')

    # Add links
    net.addLink(h1, s1)
    net.addLink(h2, s1)

    # Start network
    net.start()

    # Add firewall rule: drop traffic from h1 to h2
    s1.cmd('ovs-ofctl add-flow s1 "priority=100,dl_type=0x0800,nw_src=10.0.0.1,nw_dst=10.0.0.2,actions=drop"')

    # Start CLI
    CLI(net)

    # Stop network
    net.stop()

if __name__ == '__main__':
    create_firewall_net()
