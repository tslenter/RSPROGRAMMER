#License:
#"Remote Syslog Network Connector" is a free application what can be used to control network devices via SSH
#Copyright (C) 2020 Tom Slenter
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#For more information contact the author:
#Name author: Tom Slenter
#E-mail: info@remotesyslog.com

#Examples:
#Commands
#Example commands for Ubiquiti
#/opt/vyatta/bin/vyatta-op-cmd-wrapper show configuration
#/opt/vyatta/bin/vyatta-op-cmd-wrapper configure
#/opt/vyatta/sbin/vyatta-cfg-cmd-wrapper begin
#/opt/vyatta/bin/vyatta-op-cmd-wrapper set service dhcp-server shared-network-name LAN subnet 10.0.1.0/24 dns-server 4.2.2.2
#/opt/vyatta/sbin/vyatta-cfg-cmd-wrapper commit
#/opt/vyatta/sbin/vyatta-cfg-cmd-wrapper save
#/opt/vyatta/sbin/vyatta-cfg-cmd-wrapper end

#Example commands for Cisco
#show run
#show int gi1/1

import paramiko
import time
import os
import argparse
import datetime

#Global information
print("Script is created by T.Slenter")
print("The switches input is as following: hostname or ip,hostname or ip,hostname or ip")
print('Running from directory: ', os.getcwd())

#Set variables to None
host = None
file = None
singlecommand = None
username = None
password = None
lines = None

#Add arguments for optional use
parser = argparse.ArgumentParser()
parser.add_argument('-n', '--host',  help='Enter a hostname or ip, multiple hostname and ips are supported use seperator=,')
parser.add_argument('-u','--username', help='Add a username')
parser.add_argument('-p', '--password', help='Add a password')
parser.add_argument('-s', '--singlecommand', help='Enter a single command')
parser.add_argument('-f', '--file', help='Add file with commands')
args = parser.parse_args()

#Extract variables from namespace to global
globals().update(vars(args))

#Functions
# Create loop to view output
def outp():
    output = ""
    print("Show output:")
    for line in ssh_stdout:
        output += line
    if output != "":
        with open('output.txt', 'a') as f:
            print(datetime.datetime.now(), file=f)
            print(output, file=f)
        print(output)
    else:
        print("Nothing here!")
    # Closing file
    f.close()

#Check if interactive mode or arguments are going to be used
if host == None and file == None and singlecommand == None:
    print("Interactive mode is loaded!")
    #Ask questions
    host = str(input("Enter switch: "))
    username = str(input("Enter username: "))
    password = str(input("Enter password: "))
    file = str(input("Enter filename or press enter for single command option: "))
    if file == "":
        file = None
else:
    print("Running in non interactive mode!")

#Extract words from list
server_list = list(host.split(','))

#Clear old output files
open('output.txt', 'w').close()

#Load file or enter a single command
if file != None:
    fileupdated = os.getcwd() + "\\" + file
    openfile = open(fileupdated, "r")
    lines = openfile.readlines()
else:
    if singlecommand == None:
        file = None
        singlecommand = str(input("Enter command: "))
    else:
        print("Single command option found!")

#Loop list with hostnames
for ser in server_list:
    #Initiate connection
    print("Open SSH connection!")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ser, username=username, password=password)

    #Loop down commands or run single command
    if file != None:
        for line in lines:
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(line)
            print("Running command: " + line)
            ssh_stdout = ssh_stdout.readlines()
            outp()
    elif singlecommand != "":
        #Run single command
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(singlecommand)
        print("SSH Connection succeeded!")
        ssh_stdout = ssh_stdout.readlines()
        outp()
    else:
        print("Something went wrong!, no input found ...")

    #Closing down connection
    ssh.close()
    print("Connection closed!")

#Fix "AttributeError: 'NoneType' object has no attribute 'time'"
time.sleep(2.5)