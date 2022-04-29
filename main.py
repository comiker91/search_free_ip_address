import os
import subprocess
from multiprocessing import Pool

# Settings
# IP search range
seach_ip = "192.168.2."
# first ip (last ip section)
seach_start = 0
# last ip (last ip section)
seach_end = 255
# Process to use
process = 60
# What to seach?
offine = False


def check_ip(ip_end: int):
    """Check a IP

    Args:
        ip_end (int): last ip section

    Returns:
        IP: return a IP if usable if not None
    """
    with open(os.devnull, "wb") as limbo:
        ip = seach_ip+str(ip_end)
        result = subprocess.Popen(["ping", "-n", "1", "-w", "200", ip],
                                  stdout=limbo, stderr=limbo).wait()
        if result and not offine:
            return ip
        if offine and not result:
            return ip


if __name__ == '__main__':
    with Pool(processes=process) as pool:
        check_list = pool.map(check_ip, range(seach_start, seach_end))

    # Generate a list with free IPs
    ip_collection = list(ip for ip in check_list if ip)
    # Maybe Save as file or something else
    print(ip_collection)
