# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

class Cargador(QtGui.QDialog):
    
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(QtCore.Qt.ToolTip)
        self.setupUi()
        self.centrar()
        
    def setupUi(self):
        self.resize(92, 65)
        self.setMinimumSize(QtCore.QSize(92, 65))
        self.setMaximumSize(QtCore.QSize(92, 65))
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        
        font = QtGui.QFont()
        font.setFamily("TeX Gyre Adventor")
        self.setFont(font)
        
        gif = QtGui.QMovie("img/cargando.gif")
        GIFDisplayer = QtGui.QLabel(self)
        GIFDisplayer.setMovie(gif)
        GIFDisplayer.setAlignment(QtCore.Qt.AlignCenter)
        GIFDisplayer.setScaledContents(True)
        GIFDisplayer.setGeometry(QtCore.QRect(30, 10, 31, 31))
        gif.start()
        
        etiquetaCargando = QtGui.QLabel(self)
        etiquetaCargando.setAlignment(QtCore.Qt.AlignCenter)
        etiquetaCargando.setText("Cargando...")
        etiquetaCargando.setGeometry(QtCore.QRect(10, 40, 72, 18))
    
    def centrar(self):        
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())