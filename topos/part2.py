#!/usr/bin/python3

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import RemoteController, OVSSwitch
from mininet.link import TCLink


class part2_topo(Topo):
    def build(self):
        s1 = self.addSwitch("s1")
        h1 = self.addHost("h1", mac="00:00:00:00:00:01", ip="10.0.1.2/24")
        h2 = self.addHost("h2", mac="00:00:00:00:00:02", ip="10.0.0.2/24")
        h3 = self.addHost("h3", mac="00:00:00:00:00:03", ip="10.0.0.3/24")
        h4 = self.addHost("h4", mac="00:00:00:00:00:04", ip="10.0.1.3/24")
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s1)
        self.addLink(h4, s1)


topos = {"part2": part2_topo}


def configure():
    topo = part2_topo()
    net = Mininet(topo=topo, controller=RemoteController)

    c1 = net.addController('c1', controller=RemoteController, ip='127.0.0.1', port=6633)
    
    net.start()

    # Add firewall rule: accept ICMP traffic from any source IP to any destination IP
    s1 = net.get("s1")
    s1.cmd('ovs-ofctl add-flow s1 "priority=100,dl_type=0x0800,nw_proto=1,actions=normal"')
    s1.cmd('ovs-ofctl add-flow s1 "priority=100,dl_type=0x0806,actions=normal"')

    CLI(net)

    net.stop()


if __name__ == "__main__":
    configure()
