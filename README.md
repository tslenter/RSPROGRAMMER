# **Remote Syslog Programmer**

## 1. Introduction
Remote Syslog Programmer is a ssh connector written in python to configure device with SSH support.
This connector can be used on multiple vendors. Tested for Ubiquiti and Cisco devices.

Capabilities: Configure multiple devices with the same configuration. All output will be written to a plain text file.

Created for: To update logging configuration for all network devices of the same type. Can be used for other configurations!

## 2. Usage
Run as single cli command with multiple remote commands do:
```
python ssh_connect.py -n 172.16.9.1,172.16.10.1 -u <username> -p <strong_pw> -f commands.txt
or for 1 host:
python ssh_connect.py -n 172.16.9.1 -u <username> -p <strong_pw> -f commands.txt
```
Run as single cli command with a single commands do:
```
python ssh_connect.py -n 172.16.9.1,172.16.10.1 -u <username>  -p <strong_pw> -f "sh int status"
or for 1 host:
python ssh_connect.py -n 172.16.9.1 -u <username>  -p <strong_pw> -f "sh int status"
```
Run in interactive mode:
```
python ssh_connect.py

=================================
Interactive mode is loaded!
Enter switch: mysw001,mysw002
Enter username: <username>
Enter password: <strong_pw>
Enter filename or press enter for single command option: <enter file name like command.txt or press enter>
If you pressed enter the next question appears:
Enter command: <Type command>
```
The output of the commands will be written to: output.txt.

All options:
```
python ssh_connect.py -h

Script is created by T.Slenter
The switches input is as following: hostname or ip,hostname or ip,hostname or ip
Running from directory:  F:\ssh_connector\ssh_connector
usage: ssh_connect.py [-h] [-n HOST] [-u USERNAME] [-p PASSWORD]
                      [-s SINGLECOMMAND] [-f FILE]

optional arguments:
  -h, --help            				show this help message and exit
  -n HOST, --host HOST  				Enter a hostname or ip, multiple hostname and ips are supported use seperator=,
  -u USERNAME, --username USERNAME 			Add a username
  -p PASSWORD, --password PASSWORD			Add a password
  -s SINGLECOMMAND, --singlecommand SINGLECOMMAND	Enter a single command
  -f FILE, --file FILE  				Add file with commands
```
## 3. Donation

Crypto:

```
XRP/Ripple: rHdkpJr3qYqBYY3y3S9ZMr4cFGpgP1eM6B
BTC/Bitcoin: 1JVmexqGBQyGv9fVkSynHapi2U6ZCyjTUJ
LTC/Litecoin Segwit: MAH8ATCK6X7biiTQrW7jUZ6L9eg1YBo5qS
ETH/Ethereum: 0xd617391076F9bEa628f657606DEAB7a189199AF5
```
PayPal:

[![paypal](https://www.paypalobjects.com/en_US/NL/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=KQKRPDQYHYR7W&currency_code=EUR&source=url)

## 4. Help

To improve the code and functions we like to have you help. Send your idea or code to: info@remotesyslog.com or create a pull request. We will review it and add it to this project.

## 5. License
"Remote Syslog Network Connector" is a free application what can be used to control network devices via SSH.

Copyright (C) 2020 Tom Slenter

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.

For more information contact the author:

Name author: Tom Slenter

E-mail: info@remotesyslog.com
