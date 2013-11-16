# -*- coding: utf-8 -*-

from pexpect import run
from re import split
from PyQt4.QtCore import QObject, pyqtSignal

class HostsDetector(QObject):
    fin = pyqtSignal()
    hosts = pyqtSignal(list, name='hosts')
    
    def __init__(self):
        QObject.__init__(self)
    
    def setup(self):
        rangoIP = self.detectaRangoIP()
        cmd = "nmap -sP " + rangoIP + "/24"
         
        stdout = run(cmd)
        
        self.detectaHosts(stdout)
        self.hosts.emit(self.listaHosts)
        self.fin.emit()
    
    def detectaRangoIP(self):
        stdout = split("\n", run("ifconfig"))
        
        # Buscamos la línea con 'inet'
        for e in stdout:
            if "inet6" in e:
                pass
            elif "inet" in e:
                if "127.0.0.1" in e:
                    pass
                else:
                    inet = split("  ", e)
        
        for e in inet:
            if "inet" in e:
                inet = e
        
        i = 0
        for letra in inet:
            i += 1
            if letra == ":":
                break
            else:
                continue
        
        ip = inet[i:]
        
        return ip
    
    def detectaHosts(self, stdout):
        self.listaHosts = []
        patron = "Nmap scan report for "
        hostsBruto = split(patron, stdout)
        i = 0
        for hostBruto in hostsBruto:
            if i == 0:
                i = 1
            else:
                host = split("\n", hostBruto)[0]
                self.listaHosts.append(host)
