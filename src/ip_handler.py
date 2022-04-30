import logging
import os
import subprocess

class IP(object):

    def __init__(self, config, logger:logging.Logger):
        self.config = config
        self.logger = logger

    def check_ip(self,ip_end: int):
        """Check a IP

        Args:
            ip_end (int): last ip section

        Returns:
            IP: return a IP if usable if not None
        """
        with open(os.devnull, "wb") as limbo:
            ip = self.config.search_ip+str(ip_end)
            self.logger.debug(f"Check IP: {ip}")
            result = subprocess.Popen(["ping", "-n", "1", "-w", "200", ip],
                                    stdout=limbo, stderr=limbo).wait()
            if result and not self.config.online:
                return ip
            if self.config.online and not result:
                return ip

    def get_ip_range(self,start_ip:int, last_ip:int) -> range:
        """Genertate the IP range

        Args:
            start_ip (int): First IP
            last_ip (int): Last IP

        Returns:
            range: IP range
        """
        ip_range = range(start_ip, last_ip)
        return ip_range

    def get_list(self, ip_list:list) -> list:
        """Genertate a list with IP

        Args:
            ip_list (list): List with the IPs

        Returns:
            list: List with the IPs
        """
        self.logger.debug("Creating ip list")
        ip_collection = list(ip for ip in ip_list if ip)
        return ip_collection
            