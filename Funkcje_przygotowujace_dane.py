from PyQt4 import QtCore, QtGui
from Zespol import *

class Funkcje_przygotowujace_dane: 
    def wstaw_zespoly_do_okienka(self,zespoly):
        self.plainTextEdit_3.clear()
        for zespol in zespoly:
            #zespol=zespol + "\n"
            self.plainTextEdit_3.insertPlainText(zespol+"\n")
    def stworz_zespoly(self, zespoly,kraj):
        for zespol in zespoly:
            #print "tworze" , zespol
            Zespol(zespol,(0,[]))
            
    
