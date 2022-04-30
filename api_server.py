import os
import glob
import logging
from multiprocessing import Pool
from typing import Optional


import fastapi
from fastapi import HTTPException
import uvicorn

import src.config_ini as Config
import src.log_ini as Log
import src.ip_handler as IPhandler
import src.api.modeling as apimodel
import src.api.metadata as metadata

# Initial config
config = Config.conf_ini(filepath="config.ini")

# Initial Log
Log.log_ini(config=config)
logger = logging.getLogger("IP Checker")


app = fastapi.FastAPI(title=metadata.name, version=metadata.version,
                      docs_url="/testdocs", redoc_url="/docs", description=metadata.description, openapi_tags=metadata.tags_metadata)
ip_handler = IPhandler.IP(config=config, logger=logger)



# get the last script data
@app.get("/v1/ip/last", tags=["ip"])
async def read_ip():
    """Read the last scripted Data
    """
    logger.debug("Get the latest File...")
    # * means all if need specific format then *.csv
    list_of_files = glob.glob('output/*')
    latest_file = max(list_of_files, key=os.path.getctime)
    logger.debug(f"latest file: {latest_file}")
    with open(latest_file, "r") as reading:
        data = reading.readlines()
        ip = [d.replace("\n", "").split("- ")[-1] for d in data]
    logger.debug("Send result back")
    return {"msg": "last ip check", "ip": ip}


# check the ip range
@app.post("/v1/ip/check", response_model=apimodel.IPCheckResponse, tags=["ip"])
async def check_ip(check: Optional[apimodel.IPCheck] = apimodel.IPCheck(first_ip=0, last_ip=255)):
    """Check the IPs
    """
    first = check.first_ip
    last = check.last_ip
    logger.debug(f"Checking IP Range: {first} - {last}")
    ip_range = ip_handler.get_ip_range(start_ip=first, last_ip=last)
    logger.debug(f"Starting {config.process} process")
    with Pool(processes=config.process) as pool:
        check_list = pool.map(ip_handler.check_ip, ip_range)
    logger.debug("Get the result dict")
    results = ip_handler.get_dict(
        checked_list=check_list, start=first, last=last)
    logger.debug("Send result back")
    return {"msg": "check_list", "ip_adress": results}


# Check system is Running
@app.get("/v1/system/check", tags=["System Check"], response_model=apimodel.SystemCheckResponse)
async def check_system():
    try:
        logger.debug("Try send ...")
        return {"msg":"Server is running"}
    except:
        logger.warning("Send faild!")
        raise HTTPException(status_code=404, detail="Server is not running correkt!")

if __name__ == "__main__":
    logger.info("Start API Server")
    uvicorn.run(app=app, host=config.host, port=config.port)
    logger.info("Stopped API Server")
