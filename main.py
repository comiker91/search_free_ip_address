import logging
import os
import subprocess
from multiprocessing import Pool
from datetime import datetime
from functools import partial

import src.config_ini
import src.log_ini

config = src.config_ini.conf_ini(filepath="config.ini")
src.log_ini.log_ini(config=config)
logger = logging.getLogger("IP Checker")


def check_ip(ip_end: int, config):
    """Check a IP

    Args:
        ip_end (int): last ip section

    Returns:
        IP: return a IP if usable if not None
    """
    with open(os.devnull, "wb") as limbo:
        ip = config.search_ip+str(ip_end)
        logger.debug(f"Check IP: {ip}")
        result = subprocess.Popen(["ping", "-n", "1", "-w", "200", ip],
                                  stdout=limbo, stderr=limbo).wait()
        if result and not config.online:
            return ip
        if config.online and not result:
            return ip


if __name__ == '__main__':
    logging.info("*************************************************")
    logger.info("Starting IP check")
    ip_range = range(config.search_start, config.search_end)

    with Pool(processes=config.process) as pool:
        check_list = pool.map(partial(check_ip, config=config), ip_range)
    
    # Generate a list with free IPs
    ip_collection = list(ip for ip in check_list if ip)

    dateTimeObj = datetime.now()
    day = dateTimeObj.day
    month = dateTimeObj.month
    year = dateTimeObj.year
    hour = dateTimeObj.hour
    min = dateTimeObj.minute
    if config.save:
        with open(f"{config.output}output_{day}_{month}_{year}_{hour}_{min}.txt","w") as textfile:
            for ip in ip_collection:
                dateTimeObj = datetime.now()
                textfile.writelines(f"{dateTimeObj} - {ip}\n")
            logger.info("File created")
    if config.print_out:
        print(ip_collection)
    logger.info("Finished IP Check")