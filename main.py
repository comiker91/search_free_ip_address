import logging
from multiprocessing import Pool
from datetime import datetime

import src.config_ini as Config
import src.log_ini as Log
import src.ip_handler as IPhandler

# Initial config
config = Config.conf_ini(filepath="config.ini")

# Initial Log
Log.log_ini(config=config)
logger = logging.getLogger("IP Checker")


if __name__ == '__main__':
    logging.info("*************************************************")
    logger.info("Starting IP check")
    # initial ip handler
    ip_handler = IPhandler.IP(config=config, logger=logger)

    # Generate the IP Range
    ip_range = ip_handler.get_ip_range(config.search_start, config.search_end)

    # Check the IPs
    with Pool(processes=config.process) as pool:
        check_list = pool.map(ip_handler.check_ip, ip_range)
    
    # Generate a list with free IPs
    ip_collection = ip_handler.get_list(ip_list=check_list)

    # Create the datetimeObject for the output filename
    dateTimeObj = datetime.now()
    day = dateTimeObj.day
    month = dateTimeObj.month
    year = dateTimeObj.year
    hour = dateTimeObj.hour
    min = dateTimeObj.minute

    # Save the file if set
    if config.save:
        with open(f"{config.output}output_{day}_{month}_{year}_{hour}_{min}.txt","w") as textfile:
            for ip in ip_collection:
                dateTimeObj = datetime.now()
                textfile.writelines(f"{dateTimeObj} - {ip}\n")
            logger.info("File created")

    # Print if set
    if config.print_out:
        print(ip_collection)
    
    logger.info("Finished IP Check")
