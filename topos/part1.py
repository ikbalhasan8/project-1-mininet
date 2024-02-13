from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology of six switches and six hosts"

    def __init__( self ):
        "Custom topology"

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        host1 = self.addHost( 'h1' )
        host2 = self.addHost( 'h2' )
        host3 = self.addHost( 'h3' )
        host4 = self.addHost( 'h4' )
        switch1 = self.addSwitch( 's1' )

        # Add links between SW and Hosts
        self.addLink( host1, switch1 )
        self.addLink( host2, switch1 )
        self.addLink( host3, switch1 )
        self.addLink( host4, switch1 )

topos = { 'mytopo': ( lambda: MyTopo() ) }
