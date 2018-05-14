
from urllib.request import urlopen
import json
import socket

from tkinter import *

rootWindow = Tk()
rootWindow.title('IP Addresses')

localIP = Label(rootWindow, font = ('fixed', 20),)
localIP.grid(sticky = N, row = 2, column = 1, padx = 5, pady = (20,20))
publicIP = Label(rootWindow, font = ('fixed', 20),)
publicIP.grid(sticky = N, row = 3, column = 1, padx = 5, pady = (20,20))
hostName = Label(rootWindow, font = ('fixed', 20),)
hostName.grid(sticky = N, row = 1, column = 1, padx = 5, pady = (20,20))

ip = urlopen('http://httpbin.org/ip').read()
ip = ip.decode('utf-8')
ip = json.loads(ip)
testIP = "8.8.8.8"
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((testIP, 0))
ipaddr = s.getsockname()[0]
host = socket.gethostname()
localIP.config(text=ipaddr)
publicIP.config(text=ip['origin'])
hostName.config(text=host)

rootWindow.mainloop()
