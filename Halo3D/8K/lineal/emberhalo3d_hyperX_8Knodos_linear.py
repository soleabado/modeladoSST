import sst
from sst.merlin.base import *
from sst.merlin.endpoint import *
from sst.merlin.interface import *
from sst.merlin.topology import *

from sst.ember import *

def example():
    PlatformDefinition.setCurrentPlatform("firefly-defaults")

    ### Setup the topology

    topo = topoHyperX()
    topo.shape = "8x8x8"
    topo.width = "2x2x2"
    topo.local_ports = 16
    topo.algorithm = "DOAL"
 
    # Set up the routers
    router = hr_router()
    router.link_bw = "100GB/s"
    router.flit_size = "256B"
    router.xbar_bw = "128GB/s"
    router.input_latency = "640ns"
    router.output_latency = "640ns"
    router.input_buf_size = "128kB"
    router.output_buf_size = "128kB"
    router.num_vns = 2
    router.xbar_arb = "merlin.xbar_arb_lru"

    topo.router = router
    topo.link_latency = "40ns"

    ### set up the endpoint
    networkif = ReorderLinkControl()
    networkif.link_bw = "100GB/s"
    networkif.input_buf_size = "32kB"
    networkif.output_buf_size = "32kB"

    ep = EmberMPIJob(0,topo.getNumNodes())
    ep.network_interface = networkif
    ep.addMotif("Init")
    ep.addMotif("Halo3D26")
    ep.addMotif("Fini")
    ep.nic.nic2host_lat= "200ns"

    system = System()
    system.setTopology(topo)
    system.allocateNodes(ep,"linear")
    #system.allocateNodes(ep,"random")

    system.build()

    sst.setStatisticLoadLevel(9)

    sst.setStatisticOutput("sst.statOutputCSV");
    sst.setStatisticOutputOptions({
	"filepath" : "emberhalo3d_8Knodos_hyperX_linear.csv",
	"separator" : ", "
	})
	
    sst.enableAllStatisticsForAllComponents()


if __name__ == "__main__":
    example()