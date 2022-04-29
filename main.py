import os
import subprocess
from multiprocessing import Pool
from datetime import datetime

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
online = True
# Save as File?
save = True
# Print at end?
print_out = False


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
        if result and not online:
            return ip
        if online and not result:
            return ip


if __name__ == '__main__':
    with Pool(processes=process) as pool:
        check_list = pool.map(check_ip, range(seach_start, seach_end))

    # Generate a list with free IPs
    ip_collection = list(ip for ip in check_list if ip)
    # Maybe Save as file or something else
    dateTimeObj = datetime.now()
    day = dateTimeObj.day
    month = dateTimeObj.month
    year = dateTimeObj.year
    if save:
        with open(f"output_{day}_{month}_{year}.txt","w") as textfile:
            for ip in ip_collection:
                dateTimeObj = datetime.now()
                textfile.writelines(f"{dateTimeObj} - {ip}\n")
    if print_out:
        print(ip_collection)
