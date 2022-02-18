import socket
import sys
import os
from time import *
from datetime import datetime
os.system("clear")
######################################

print ("\033[1;31m         _,.-------.,_")
print ("\033[1;31m     ,;~'             '~;,")
print ("\033[1;31m   ,;                     ;,")
print ("\033[1;31m  ;                         ;")
print ("\033[1;31m ,'                         ',")
print ("\033[1;31m,;                           ;,")
print ("\033[1;31m; ;      .           .      ; ;")
print ("\033[1;31m| ;   ______       ______   ; |")
print ("\033[1;31m|  `/~-     ~+ . -~     +~\-  |")
print ("\033[1;31m|  ~  ,-~~~^~, | ,~^~~~-,  ~  |")
print ("\033[1;31m |   |        }:{        |   |")
print ("\033[1;31m |   l       / | \       !   |")
print ("\033[1;31m .~  (__,.--- .^. +--.,__)  ~.")
print ("\033[1;31m |     ---;' / | \ `;---     |")
print ("\033[1;31m  \__.       \/^\/       .__/")
print ("\033[1;31m   V| \                 / |V")
print ("\033[1;31m    | |T~\___!___!___/~T| |")
print ("\033[1;31m    | |`IIII_I_I_I_IIII'| |")
print ("\033[1;31m    |  \,III I I I III,/  |")
print ("\033[1;31m     \   `~~~~~~~~~~'    /")
print ("\033[1;31m       \   .       .   /    \033[1;33m  DARK-ERROR (4/15/95)")
print ("\033[1;31m         \.    ^    ./")
print ("\033[1;31m           ^~~~^~~~^")

######################################
password = "DARK-ERROR"
enter = input ("\033[1;32m enter the password: ")
if enter == password :
    pass
    print ("correct password")
    os.system("clear")
else:
     exit ('try again')

######################################
print ("\033[1;33m ,------.    ,---.  ,------. ,--. ,--.       ,------.,------. ,------.  ,-----. ,------.     ,--------.,------.  ,---.  ,--.   ,--.") 
print ("\033[1;34m |  .-.  \  /  O  \ |  .--. '|  .'   /,-----.|  .---'|  .--. '|  .--. ''  .-.  '|  .--. '    '--.  .--'|  .---' /  O  \ |   `.'   | ")
print ("\033[1;31m |  |  \  :|  .-.  ||  '--'.'|  .   ' '-----'|  `--, |  '--'.'|  '--'.'|  | |  ||  '--'.'       |  |   |  `--, |  .-.  ||  |'.'|  | ")
print ("\033[1;35m |  '--'  /|  | |  ||  |\  \ |  |\   \       |  `---.|  |\  \ |  |\  \ '  '-'  '|  |\  \        |  |   |  `---.|  | |  ||  |   |  | ")
print ("\033[1;36m `-------' `--' `--'`--' '--'`--' '--'       `------'`--' '--'`--' '--' `-----' `--' '--'       `--'   `------'`--' `--'`--'   `--' ")
#####################################
ip= input ("\033[1;33m =====>ENTER YOUR IP TO START: ")
t1= datetime.now()
print ("scanning start %s please wait"%ip)
sleep(1)
#####################################
try:
    for port in range (1,6553) :
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        if(s.connect_ex((ip,port))==0):
            try:
                serv=socket.getservbyport(port)
            except socket.error:
                serv= "Unknown Service"
            print ("Port %s 0pen Service:%s "%(port, serv))
        t2=datetime.now()
        t3=t2-t1
    print ("Scanning Completed")
except KeyboardInterrupt:
    print ("See You Soon...!")

