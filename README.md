# **Remote Syslog Network Connector**

## 1. Introduction
Remote Syslog Network Connector is a ssh connector written in python to configure device with SSH support.
This connector can be used on multiple vendors. Tested for Ubiquiti and Cisco devices.

Capabilities: Configure multiple devices with the same configuration. All output will be written to a plain text file.

Created for: To update logging configuration for all network devices of the same type.

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

## 3 Donation

Crypto:

```
XRP/Ripple: rHdkpJr3qYqBYY3y3S9ZMr4cFGpgP1eM6B
BTC/Bitcoin: 1JVmexqGBQyGv9fVkSynHapi2U6ZCyjTUJ
LTC/Litecoin Segwit: MAH8ATCK6X7biiTQrW7jUZ6L9eg1YBo5qS
ETH/Ethereum: 0xd617391076F9bEa628f657606DEAB7a189199AF5
```
PayPal:

[![paypal](https://www.paypalobjects.com/en_US/NL/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=KQKRPDQYHYR7W&currency_code=EUR&source=url)

## 4 Help

To improve the code and functions we like to have you help. Send your idea or code to: info@remotesyslog.com or create a pull request. We will review it and add it to this project.
