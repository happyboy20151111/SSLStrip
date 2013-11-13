# -*- coding: utf-8 -*-

from os import popen
from re import split
from PyQt4.QtCore import QObject, pyqtSignal

class InterfaceDetector(QObject):
    fin = pyqtSignal()
    interfaces = pyqtSignal(list, name='interfaces')
    
    def setup(self):
        f = popen("ifconfig")
        stdout = f.read()
        f.close()
        self.detectaInterfaces(stdout)
        self.interfaces.emit(self.listaInterfaces)
        self.fin.emit()
    
    def detectaInterfaces(self, stdout):
        self.listaInterfaces = []
        interfacesBruto = split("\n\n", stdout)
        
        for interfazBruto in interfacesBruto:
            interfaz = split(" ", interfazBruto)[0]
                        
            if interfaz != "" and interfaz != "lo":
                self.listaInterfaces.append(interfaz)