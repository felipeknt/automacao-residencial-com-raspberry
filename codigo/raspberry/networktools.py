from os import popen,system

def local_ip():
   ip = popen("ifconfig | grep 'inet '").read().split(" ")[21]
   return ip


 
