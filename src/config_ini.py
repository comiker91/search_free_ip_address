import configparser
from types import SimpleNamespace

# Default Config:
# IP search range
search_ip = "192.168.2."
# first ip (last ip section)
search_start = 0
# last ip (last ip section)
search_end = 255
# Process to use
process = 10
# What to seach?
online = True
# Save as File?
save = True
# Print at end?
print_out = False
# Output Path
output = "output/"
# log file
log_file = "service.log"
# log level
log_level = "info"
# log path
log_path = "."

# API Settings
host = "127.0.0.1"
port = 8000

def conf_ini(filepath: str):
    """Initial the Config

    Args:
        filepath (str): Path to config.ini

    Returns:
        SimpleNamespace: Config Data
    """
    config = configparser.ConfigParser()
    config.read(filenames=filepath)
    config_data = SimpleNamespace(
        search_ip=config.get("settings", "search_ip", fallback=search_ip),
        search_start=config.getint("settings", "start", fallback=search_start),
        search_end=config.getint("settings","end",fallback=search_end),
        process=config.getint("settings","process",fallback=process),
        online=config.getboolean("settings","online",fallback=online),
        save=config.getboolean("settings","save",fallback=save),
        print_out=config.getboolean("settings","print",fallback=print_out),
        output = config.get("settings","output", fallback=output),
        log_file=config.get("log","log_file", fallback=log_file),
        log_level=config.get("log","level",fallback=log_level),
        log_path=config.get("log","path",fallback=log_path),
        host=config.get("api","host",fallback=host),
        port=config.getint("api","port",fallback=port)
    )

    return config_data
