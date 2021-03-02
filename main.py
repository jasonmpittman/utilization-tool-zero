#!/usr/bin/env python3

__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2021"
__credits__ = ["Jason M. Pittman"]
__license__ = "GPLv3"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__email__ = "jpittman@highpoint.edu"
__status__ = "Research"

import logging
from utz import utz


def main():
    utilization_tool = utz()
    
    log_file = utilization_tool.log()
  
    logging.basicConfig(
        level="INFO",
        format='%(asctime)s - %(message)s',
        datefmt='%d-%b-%y %H:%M:%S',
        force=True,
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ])
    
    try:
        logging.info(utilization_tool.ram())
        logging.info(utilization_tool.net())
        
        while True:
            try:
                logging.info(utilization_tool.cpu())
            except KeyboardInterrupt:
                break
            
        logging.info(utilization_tool.ram())
        logging.info(utilization_tool.net())

    except Exception as e:
        logging.error("An exception occured", exc_info=True)
        print(e)


if __name__ == "__main__":
    main()