#/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from SSLStrip import SSLStrip
from Ui_SSLStrip import Ui_SSLStrip
from interfaceDetector import InterfaceDetector as ID
from hostsDetector import HostsDetector as HD
from cargador import Cargador
from pexpect import run
import sys

class Root(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        
        self.ventana = Ui_SSLStrip()
        self.ventana.setupUi(self)
        
        self.centrar()
        
        #self.compruebaDependencias()
        
        self.obtienePasswd()
        
        self.connect(self.ventana.botonActualizar, QtCore.SIGNAL("clicked()"),
                     self.actualizaDatos)
        self.connect(self.ventana.botonIniciar, QtCore.SIGNAL("clicked()"),
                     self.iniciarSSLStrip)
        self.connect(self.ventana.botonParar, QtCore.SIGNAL("clicked()"),
                     self.pararSSLStrip)
        
    def obtienePasswd(self):
        zenity = '''zenity --password --title="Autenticación"'''
        self.passwd = run(zenity).replace('\n', '')
        
        if self.passwd == "":
            self.obtienePasswd()
        else:
            self.testPasswd()
    
    def testPasswd(self):
        try:
            cmd = "sudo echo 'Prueba'"
            event = {"(?i)password":self.passwd + "\n"}        
            stdout = run(cmd, events=event)
            if "Sorry, try again." in stdout:
                texto = "<p><font color='#ffffff'>Password incorrecta!</font></p>"
                QtGui.QMessageBox.warning(self, "Advertencia", texto,
                                          buttons=QtGui.QMessageBox.Ok)
                self.obtienePasswd()
        except Exception as e:
            sys.exit(e)
    
    def inicioCarga(self):
        self.cargador = Cargador()
        self.cargador.show()
    
    def finCarga(self):
        self.cargador.close()
    
    def actualizaDatos(self):
        self.borraDatosPrevios()
        self.setEnabled(False)
        
        self.inicioCarga()
        # Actualizamos interfaces
        self.threadActualizaInterfaces = QtCore.QThread()
                        
        self.interfaces = ID()
        self.interfaces.moveToThread(self.threadActualizaInterfaces)
        self.interfaces.fin.connect(self.threadActualizaInterfaces.quit)
        self.interfaces.interfaces.connect(self.actualizaInterfaces)
        
        self.threadActualizaInterfaces.started.connect(self.interfaces.setup)
        
        self.threadActualizaInterfaces.start()
        
        # Actualizamos hosts
        self.threadActualizaHosts = QtCore.QThread()
        
        self.hosts = HD(self.passwd)                     
        self.hosts.moveToThread(self.threadActualizaHosts)
        self.hosts.fin.connect(self.threadActualizaHosts.quit)
        self.hosts.hosts.connect(self.actualizaHosts)
        
        self.threadActualizaHosts.started.connect(self.hosts.setup)
        
        self.threadActualizaHosts.start()
    
    def borraDatosPrevios(self):
        self.ventana.boxInterface.clear()
        self.ventana.boxRHost.clear()
        self.ventana.boxGateway.clear()
        
    def actualizaInterfaces(self, interfaces):        
        for interfaz in interfaces:
            self.ventana.boxInterface.addItem(interfaz)
    
    def actualizaHosts(self, hosts):
        for host in hosts:
            self.ventana.boxRHost.addItem(host)
            self.ventana.boxGateway.addItem(host)
        self.finCarga()
        self.setEnabled(True)
    
    def iniciarSSLStrip(self):
        interfaz = str(self.ventana.boxInterface.currentText())
        rhost = str(self.ventana.boxRHost.currentText())
        gateway = str(self.ventana.boxGateway.currentText())
        
        if self.ventana.checkMatarSesionesActivas.isChecked():
            matarSesiones = True
        else:
            matarSesiones = False
        
        self.ventana.visor.clear()
        
        if interfaz != "" and rhost != "" and gateway != "":
            self.ventana.botonIniciar.setDisabled(True)
            self.ventana.botonParar.setEnabled(True)
            
            self.threadSSLStrip = QtCore.QThread()
            
            self.sslstrip = SSLStrip(interfaz, rhost, gateway, self.passwd,
                                     matarSesiones)
            self.sslstrip.moveToThread(self.threadSSLStrip)
            self.sslstrip.fin.connect(self.threadSSLStrip.quit)
            self.sslstrip.texto.connect(self.imprimeProceso)
            
            self.threadSSLStrip.started.connect(self.sslstrip.setup)
            
            self.threadSSLStrip.start()
            
        else:            
            msjAdvertencia = QtGui.QMessageBox()
            msjAdvertencia.setText("Indicar interfaz, host remoto y gateway!")
            msjAdvertencia.setWindowTitle("Advertencia")
            msjAdvertencia.setIcon(msjAdvertencia.Warning)
            msjAdvertencia.setButtonText(0x00000400, "Aceptar")
            msjAdvertencia.exec_()
    
    def pararSSLStrip(self):
        self.ventana.botonIniciar.setEnabled(True)
        self.ventana.botonParar.setDisabled(True)    
        self.sslstrip.parar()
    
    def imprimeProceso(self, texto):
        self.ventana.visor.append(QtGui.QApplication.translate("SSLStrip", texto, None, QtGui.QApplication.UnicodeUTF8))
    
    def centrar(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def closeEvent(self, event):
        try:
            self.ventana.visor.clear()
            self.pararSSLStrip()
        except:
            pass
        
        msjPregunta = QtGui.QMessageBox()
        msjPregunta.setText("Realmente deseas salir")
        msjPregunta.setWindowTitle("Mensaje")
        msjPregunta.setIcon(msjPregunta.Question)
        msjPregunta.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        msjPregunta.setButtonText(0x00004000, "Si")
        respuesta = msjPregunta.exec_()

        if respuesta == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

def main():
    app = QtGui.QApplication(sys.argv)
    root = Root()
    root.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
        
        
