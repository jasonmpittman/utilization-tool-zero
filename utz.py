
__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2021"
__credits__ = ["Jason M. Pittman"]
__license__ = "GPLv3"
__version__ = "0.1.0"
__maintainer__ = "Jason M. Pittman"
__email__ = "jpittman@highpoint.edu"
__status__ = "Research"

import psutil
import configparser

class utz:

    __AMOUNTS = {
        "KB": 1,
        "MB": 2,
        "GB": 3
    }

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')

        self.__interval = config['options']['cpu_interval']
        self.__interface = config['options']['net_interface']
        self.__log_file = config['output']['log']

    def cpu(self):
        """returns percent utilization on all CPU cores as a tuple"""
        return psutil.cpu_percent(float(self.__interval), True)

    def ram(self, amount=None):
        """returns amount of RAM used in GB by default. KB or MB can be passed for different amounts"""
        mem = psutil.virtual_memory()
        used = mem[3]

        if amount is None:
            return self.__convertAmount(used, self.__AMOUNTS.get("GB"))
        else:
            return self.__convertAmount(used, self.__AMOUNTS.get(amount))
        

    def disk(self, amount=None):
        """returns amount of disk free in GB by default. KB or MB can be passed for different amounts"""
        space = psutil.disk_usage('/')
        free = space[2]
        
        if amount is None:
            return self.__convertAmount(free, self.__AMOUNTS.get("GB"))
        else:
            return self.__convertAmount(free, self.__AMOUNTS.get(amount))
        

    def net(self):
        """returns network counters for interface specified in config.ini"""
        networks = psutil.net_io_counters(True)
          
        return networks.get(self.__interface)

    def log(self):
        return self.__log_file

    def __convertAmount(self, value, amount):
        """private method to convert bytes to specified amount"""
        for i in range(amount):
            value = (value / 1024)
        
        return value
