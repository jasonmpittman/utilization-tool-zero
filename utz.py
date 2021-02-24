
__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2021"
__credits__ = ["Jason M. Pittman"]
__license__ = "GPLv3"
__version__ = "0.1.0"
__maintainer__ = "Jason M. Pittman"
__email__ = "jpittman@highpoint.edu"
__status__ = "Research"

import psutil

class utz:

    def cpu(self):
	    return psutil.cpu_percent(1, True)

    def ram(self):
        mem = psutil.virtual_memory()
        used = mem[3]
        return (used / 1024 / 1024 / 1024) #KB, MB, GB

    def disk(self):
        space = psutil.disk_usage('/')
        free = space[2]
        return (free / 1024 / 1024 / 1024)

    def net(self):
        return psutil.net_io_counters(True)

u = utz()

#for i in range(10):
print(u.cpu())
#print(u.ram())
#print(u.disk())