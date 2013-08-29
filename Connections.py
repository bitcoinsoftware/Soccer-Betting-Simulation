from GuiFunctions import *
from PyQt4 import QtCore, QtGui

class Connections(GuiFunctions):
    def connect(self):
        print("connect")
        QtCore.QObject.connect(self.pushButton,QtCore.SIGNAL('clicked()'),self.wyluskaj_zespoly_z_tabeli)
        QtCore.QObject.connect(self.pushButton_2,QtCore.SIGNAL('clicked()'),self.generuj_ciagi_wynikowe)
        QtCore.QObject.connect(self.spinBox_3,QtCore.SIGNAL('valueChanged(int)'),self.wyswietl_ligi)
        QtCore.QObject.connect(self.spinBox_9,QtCore.SIGNAL('valueChanged(int)'),self.wyswietl_ligi)
        QtCore.QObject.connect(self.pushButton_3,QtCore.SIGNAL('clicked()'),self.zapisz_ciagi_do_pliku)
        QtCore.QObject.connect(self.pushButton_9,QtCore.SIGNAL('clicked()'),self.czysc_okna)       
        
        QtCore.QObject.connect(self.listWidget,QtCore.SIGNAL('itemSelectionChanged()'),self.wyswietl_zespoly)
        QtCore.QObject.connect(self.pushButton_4,QtCore.SIGNAL('clicked()'),self.dodaj_zespol_do_portfela)
        QtCore.QObject.connect(self.pushButton_5,QtCore.SIGNAL('clicked()'),self.usun_z_portfela)
        QtCore.QObject.connect(self.pushButton_7,QtCore.SIGNAL('clicked()'),self.usun_wszystkie_z_portfela)
        QtCore.QObject.connect(self.pushButton_6,QtCore.SIGNAL('clicked()'),self.dodaj_wszystkie_zespoly_do_portfela)
        QtCore.QObject.connect(self.pushButton_8,QtCore.SIGNAL('clicked()'),self.przelicz_jeszcze_raz)
        QtCore.QObject.connect(self.pushButton_10,QtCore.SIGNAL('clicked()'),self.wyswietl_wszystkie_zespoly)
        QtCore.QObject.connect(self.pushButton_11,QtCore.SIGNAL('clicked()'),self.dodaj_wszystkie_sezony_zaznaczonej_druzyny_do_portfela)

           
        
        self.wyswietl_ligi()
