# Free IP Checker

## Usage

Just set your settings like you need in the config.ini
If done just run the main.py

## Requirements

Python >= 3.9

## Settings

### IP search range
seach_ip = "192.168.2."
The IP range
### first ip (last ip section)
seach_start = 0
First IP in the last section
### last ip (last ip section)
seach_end = 255
Last IP in the last section
### Process to use
process = 10
How many process should check the IPs
### What to Search?
online = True
If online = True you get all omline IPs
### Save as File?
save = True
Save the IP to a file
### Print at end?
print_out = False
Print the IP at the end?
### Output
output = output/
Path to save the output. Be shure dont forget the / at the end!

## Log
### Log File
log_file = service.log
File to save the log
### Log Level
level = info
Level to log
### Log Path
path = .
Path to save the log