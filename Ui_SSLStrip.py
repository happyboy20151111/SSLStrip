# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SSLStrip.ui'
#
# Created: Mon Aug  5 11:06:48 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SSLStrip(object):
    def setupUi(self, SSLStrip):
        SSLStrip.setObjectName(_fromUtf8("SSLStrip"))
        SSLStrip.setWindowModality(QtCore.Qt.ApplicationModal)
        SSLStrip.resize(454, 380)
        SSLStrip.setMinimumSize(QtCore.QSize(454, 380))
        SSLStrip.setMaximumSize(QtCore.QSize(454, 380))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("TeX Gyre Adventor"))
        SSLStrip.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("img/favicon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SSLStrip.setWindowIcon(icon)
        SSLStrip.setStyleSheet(_fromUtf8("background-image: url(:/img/img/bg.png);"))
        self.frameInferior = QtGui.QFrame(SSLStrip)
        self.frameInferior.setGeometry(QtCore.QRect(0, 0, 461, 381))
        self.frameInferior.setMinimumSize(QtCore.QSize(461, 381))
        self.frameInferior.setMaximumSize(QtCore.QSize(461, 381))
        self.frameInferior.setFrameShape(QtGui.QFrame.NoFrame)
        self.frameInferior.setFrameShadow(QtGui.QFrame.Raised)
        self.frameInferior.setObjectName(_fromUtf8("frameInferior"))
        self.boxRHost = QtGui.QComboBox(self.frameInferior)
        self.boxRHost.setGeometry(QtCore.QRect(110, 180, 111, 25))
        self.boxRHost.setMinimumSize(QtCore.QSize(111, 25))
        self.boxRHost.setMaximumSize(QtCore.QSize(111, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("TeX Gyre Adventor"))
	font.setPointSize(9)
        self.boxRHost.setFont(font)
        self.boxRHost.setFocusPolicy(QtCore.Qt.NoFocus)
        self.boxRHost.setStyleSheet(_fromUtf8("selection-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(255, 85, 0);"))
        self.boxRHost.setFrame(True)
        self.boxRHost.setModelColumn(0)
        self.boxRHost.setObjectName(_fromUtf8("boxRHost"))
        self.botonIniciar = QtGui.QPushButton(self.frameInferior)
        self.botonIniciar.setGeometry(QtCore.QRect(160, 320, 61, 51))
        self.botonIniciar.setMinimumSize(QtCore.QSize(61, 51))
        self.botonIniciar.setMaximumSize(QtCore.QSize(61, 51))
        self.botonIniciar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.botonIniciar.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("img/iniciar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botonIniciar.setIcon(icon1)
        self.botonIniciar.setIconSize(QtCore.QSize(48, 48))
        self.botonIniciar.setFlat(True)
        self.botonIniciar.setObjectName(_fromUtf8("botonIniciar"))
        self.boxInterface = QtGui.QComboBox(self.frameInferior)
        self.boxInterface.setGeometry(QtCore.QRect(110, 120, 111, 25))
        self.boxInterface.setMinimumSize(QtCore.QSize(111, 25))
        self.boxInterface.setMaximumSize(QtCore.QSize(111, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("TeX Gyre Adventor"))
	font.setPointSize(9)
        self.boxInterface.setFont(font)
        self.boxInterface.setFocusPolicy(QtCore.Qt.NoFocus)
        self.boxInterface.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(255, 85, 0);"))
        self.boxInterface.setFrame(True)
        self.boxInterface.setModelColumn(0)
        self.boxInterface.setObjectName(_fromUtf8("boxInterface"))
        self.botonParar = QtGui.QPushButton(self.frameInferior)
        self.botonParar.setEnabled(False)
        self.botonParar.setGeometry(QtCore.QRect(80, 320, 61, 51))
        self.botonParar.setMinimumSize(QtCore.QSize(61, 51))
        self.botonParar.setMaximumSize(QtCore.QSize(61, 51))
        self.botonParar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.botonParar.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("img/parar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botonParar.setIcon(icon2)
        self.botonParar.setIconSize(QtCore.QSize(48, 48))
        self.botonParar.setFlat(True)
        self.botonParar.setObjectName(_fromUtf8("botonParar"))
        self.visor = QtGui.QTextEdit(self.frameInferior)
        self.visor.setGeometry(QtCore.QRect(230, 100, 211, 271))
        self.visor.setMinimumSize(QtCore.QSize(211, 271))
        self.visor.setMaximumSize(QtCore.QSize(211, 271))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Monospace"))
        font.setPointSize(9)
        self.visor.setFont(font)
        self.visor.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.visor.setFrameShape(QtGui.QFrame.Box)
        self.visor.setUndoRedoEnabled(True)
        self.visor.setReadOnly(True)
        self.visor.setObjectName(_fromUtf8("visor"))
        self.etiquetaRHost = QtGui.QLabel(self.frameInferior)
        self.etiquetaRHost.setGeometry(QtCore.QRect(10, 180, 81, 31))
        self.etiquetaRHost.setMinimumSize(QtCore.QSize(81, 31))
        self.etiquetaRHost.setMaximumSize(QtCore.QSize(81, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("TeX Gyre Adventor"))
        font.setPointSize(9)
        self.etiquetaRHost.setFont(font)
        self.etiquetaRHost.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.etiquetaRHost.setObjectName(_fromUtf8("etiquetaRHost"))
        self.boxGateway = QtGui.QComboBox(self.frameInferior)
        self.boxGateway.setGeometry(QtCore.QRect(110, 240, 111, 25))
        self.boxGateway.setMinimumSize(QtCore.QSize(111, 25))
        self.boxGateway.setMaximumSize(QtCore.QSize(111, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("TeX Gyre Adventor"))
	font.setPointSize(9)
        self.boxGateway.setFont(font)
        self.boxGateway.setFocusPolicy(QtCore.Qt.NoFocus)
        self.boxGateway.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(255, 85, 0);\n"
"selection-color: rgb(0, 0, 0);"))
        self.boxGateway.setFrame(True)
        self.boxGateway.setObjectName(_fromUtf8("boxGateway"))
        self.etiquetaGateway = QtGui.QLabel(self.frameInferior)
        self.etiquetaGateway.setGeometry(QtCore.QRect(10, 240, 57, 31))
        self.etiquetaGateway.setMinimumSize(QtCore.QSize(57, 31))
        self.etiquetaGateway.setMaximumSize(QtCore.QSize(57, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("TeX Gyre Adventor"))
        font.setPointSize(9)
        self.etiquetaGateway.setFont(font)
        self.etiquetaGateway.setObjectName(_fromUtf8("etiquetaGateway"))
        self.etiquetaInterface = QtGui.QLabel(self.frameInferior)
        self.etiquetaInterface.setGeometry(QtCore.QRect(10, 120, 57, 31))
        self.etiquetaInterface.setMinimumSize(QtCore.QSize(57, 31))
        self.etiquetaInterface.setMaximumSize(QtCore.QSize(57, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("TeX Gyre Adventor"))
        font.setPointSize(9)
        self.etiquetaInterface.setFont(font)
        self.etiquetaInterface.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.etiquetaInterface.setFrameShape(QtGui.QFrame.NoFrame)
        self.etiquetaInterface.setObjectName(_fromUtf8("etiquetaInterface"))
        self.botonActualizar = QtGui.QPushButton(self.frameInferior)
        self.botonActualizar.setGeometry(QtCore.QRect(0, 320, 61, 51))
        self.botonActualizar.setMinimumSize(QtCore.QSize(61, 51))
        self.botonActualizar.setMaximumSize(QtCore.QSize(61, 51))
        self.botonActualizar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.botonActualizar.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("img/actualizar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botonActualizar.setIcon(icon3)
        self.botonActualizar.setIconSize(QtCore.QSize(48, 48))
        self.botonActualizar.setFlat(True)
        self.botonActualizar.setObjectName(_fromUtf8("botonActualizar"))
        self.frameSuperior = QtGui.QFrame(self.frameInferior)
        self.frameSuperior.setGeometry(QtCore.QRect(0, 0, 461, 91))
        self.frameSuperior.setMinimumSize(QtCore.QSize(461, 91))
        self.frameSuperior.setMaximumSize(QtCore.QSize(461, 91))
        self.frameSuperior.setStyleSheet(_fromUtf8("background-image: url(:/img/img/underc0de.png);"))
        self.frameSuperior.setFrameShape(QtGui.QFrame.NoFrame)
        self.frameSuperior.setFrameShadow(QtGui.QFrame.Plain)
        self.frameSuperior.setObjectName(_fromUtf8("frameSuperior"))
        self.lineaInferior = QtGui.QFrame(self.frameSuperior)
        self.lineaInferior.setGeometry(QtCore.QRect(10, 80, 441, 16))
        self.lineaInferior.setMinimumSize(QtCore.QSize(441, 16))
        self.lineaInferior.setMaximumSize(QtCore.QSize(441, 16))
        self.lineaInferior.setFrameShape(QtGui.QFrame.HLine)
        self.lineaInferior.setFrameShadow(QtGui.QFrame.Sunken)
        self.lineaInferior.setObjectName(_fromUtf8("lineaInferior"))
        self.lineaSuperior = QtGui.QFrame(self.frameSuperior)
        self.lineaSuperior.setGeometry(QtCore.QRect(10, 5, 441, 21))
        self.lineaSuperior.setMinimumSize(QtCore.QSize(441, 21))
        self.lineaSuperior.setMaximumSize(QtCore.QSize(441, 16777215))
        self.lineaSuperior.setFrameShape(QtGui.QFrame.HLine)
        self.lineaSuperior.setFrameShadow(QtGui.QFrame.Sunken)
        self.lineaSuperior.setObjectName(_fromUtf8("lineaSuperior"))
        self.checkMatarSesionesActivas = QtGui.QCheckBox(self.frameInferior)
        self.checkMatarSesionesActivas.setGeometry(QtCore.QRect(10, 290, 170, 21))
        self.checkMatarSesionesActivas.setMinimumSize(QtCore.QSize(170, 21))
        self.checkMatarSesionesActivas.setMaximumSize(QtCore.QSize(170, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("TeX Gyre Adventor"))
        font.setPointSize(9)
        self.checkMatarSesionesActivas.setFont(font)
        self.checkMatarSesionesActivas.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkMatarSesionesActivas.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.checkMatarSesionesActivas.setObjectName(_fromUtf8("checkMatarSesionesActivas"))

        self.retranslateUi(SSLStrip)
        QtCore.QMetaObject.connectSlotsByName(SSLStrip)

    def retranslateUi(self, SSLStrip):
        SSLStrip.setWindowTitle(_translate("SSLStrip", "SSLStrip", None))
        self.visor.setHtml(_translate("SSLStrip", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Monospace\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>", None))
        self.etiquetaRHost.setText(_translate("SSLStrip", "Remote host", None))
        self.etiquetaGateway.setText(_translate("SSLStrip", "<html><head/><body><p><span style=\" color:#ffffff;\">Gateway</span></p></body></html>", None))
        self.etiquetaInterface.setText(_translate("SSLStrip", "Interface", None))
        self.checkMatarSesionesActivas.setText(_translate("SSLStrip", "Matar sesiones activas", None))

import underc0de_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    SSLStrip = QtGui.QWidget()
    ui = Ui_SSLStrip()
    ui.setupUi(SSLStrip)
    SSLStrip.show()
    sys.exit(app.exec_())

