from Wyluskiwacz_z_tabeli import *
from Wyluskiwacz_wynikow import *
from Funkcje_przygotowujace_dane import *
from PyQt4 import QtCore, QtGui
import sqlite3
from Obstawiacz import *
from PyQt4.Qwt5 import Qwt
from HistogramItem import *
from Generator_tabeli_iloczynowej import *

class GuiFunctions(Funkcje_przygotowujace_dane):
    portfel=[]
    def wyluskaj_zespoly_z_tabeli(self):
        print("wyluskaj")
        self.wyluskiwacz = Wyluskiwacz_z_tabeli(self.plainTextEdit.toPlainText())
        self.wstaw_zespoly_do_okienka(self.wyluskiwacz.zespoly)
        kraj = self.textEdit.toPlainText()
        self.stworz_zespoly(self.wyluskiwacz.zespoly, kraj)
        
    def generuj_ciagi_wynikowe(self):
        print("generuj ciagi")
        kraj = self.textEdit.toPlainText()
        liga = self.spinBox.value()
        sezon = self.spinBox_2.value()
        self.wyluskiwacz_wynikow = Wyluskiwacz_wynikow(self.plainTextEdit_2.toPlainText(),self.wyluskiwacz.zespoly,kraj,liga,sezon)
        self.wyluskiwacz_wynikow.note_results()
        ciagi= self.wyluskiwacz_wynikow.daj_stringa_z_remisami()
        self.plainTextEdit_4.insertPlainText(self.wyluskiwacz_wynikow.daj_stringa_z_remisami())
        self.plainTextEdit_4.insertPlainText("\n")
 
    def czysc_okna(self):
        print("czysc okna")
        self.plainTextEdit.clear()
        self.plainTextEdit_2.clear()
        self.plainTextEdit_3.clear()
        self.plainTextEdit_4.clear()
	
            
    def zapisz_ciagi_do_pliku(self):
        print("zapisz")
        conn = sqlite3.connect('PROGRESJA')
        c =conn.cursor()
        for dane in self.wyluskiwacz_wynikow.dane_do_tabeli:
            cmd= "insert into WYNIKI values("+str(dane)+")"
            #print cmd.type()
            c.execute(cmd)
        conn.commit()
        
    def wyswietl_ligi(self):
        item_quant = self.listWidget.count()
        for i in range(item_quant):
            self.listWidget.takeItem(0)
        portfel_item_quant = self.listWidget_3.count()
        for i in range(portfel_item_quant):
            self.listWidget_3.takeItem(0)
        conn = sqlite3.connect('PROGRESJA')
        c =conn.cursor()
        sezon_max = self.spinBox_3.value()
        sezon_min = self.spinBox_9.value()
        cmd = "select distinct Kraj , Liga from WYNIKI where Sezon<="+str(sezon_max)+" and Sezon>="+str(sezon_min)
        #print cmd
        c.execute(cmd)
        for dane in c:
            dane = str(dane[0])+","+str(dane[1])
            self.listWidget.insertItem(0,QtCore.QString(dane))
        
			
    def wyswietl_zespoly(self):
        print("wyswietl zespoly")
        item_quant = self.listWidget_2.count()
        for i in range(item_quant):
            self.listWidget_2.takeItem(0)
			
        self.portfel = []
        
        if self.listWidget.currentRow()!=-1:
            a=str(self.listWidget.currentItem().text()).split(",")
            kraj ,liga = a[0],a[1]
        
            conn = sqlite3.connect('PROGRESJA')
            c =conn.cursor()
            sezon_max = self.spinBox_3.value()
            sezon_min = self.spinBox_9.value()
            cmd = "select distinct Nazwa,Kraj,Liga,Sezon from WYNIKI where Sezon<="+str(sezon_max)+" and Sezon>="+str(sezon_min)+" and Liga="+liga+" and Kraj=\""+kraj+"\""
            c.execute(cmd)
            for druzyna in c:
                self.listWidget_2.insertItem(0,QtCore.QString(str(druzyna)))
                
    def wyswietl_wszystkie_zespoly(self):
        print("wyswietl wszystkie zespoly")
        
        item_quant = self.listWidget_2.count()
        for i in range(item_quant):
            self.listWidget_2.takeItem(0)
        self.portfel = []
        
        for i in range(self.listWidget.count()): 
            a=str(self.listWidget.item(i).text()).split(",")
            kraj ,liga = a[0],a[1]
        
            conn = sqlite3.connect('PROGRESJA')
            c =conn.cursor()
            sezon = self.spinBox_3.value()
            cmd = "select distinct Nazwa,Kraj,Liga,Sezon from WYNIKI where Sezon="+str(sezon)+" and Liga="+liga+" and Kraj=\""+kraj+"\""
            c.execute(cmd)
            for druzyna in c:
                self.listWidget_2.insertItem(0,QtCore.QString(str(druzyna)))
                

			
    def usun_z_portfela(self):
        print("usun z portfela")
        if self.listWidget_3.currentRow()!=-1:
            #print len(self.portfel),self.listWidget_3.currentRow(), self.portfel.pop(len(self.portfel)- (1 + self.listWidget_3.currentRow()))
            self.listWidget_3.takeItem(self.listWidget_3.currentRow())
			
    def usun_wszystkie_z_portfela(self):
        print("usun wszystkie z portfela")
        item_quant = self.listWidget_3.count()
        for i in range(item_quant):
            self.listWidget_3.takeItem(0)
			
        self.portfel = []
        
    def dodaj_zespol_do_portfela(self):
        print("dodaj zespol do portfela")
        try:
            if self.listWidget_2.currentRow()!=-1:
                zespol = self.listWidget_2.currentItem().text()
                self.portfel.append([str(zespol).split("'")[1],str(zespol).split("'")[3],int(str(zespol).split("'")[5]),str(zespol).split("'")[6]])
                self.listWidget_3.insertItem(0,zespol)
            
                self.przelicz_jeszcze_raz()
        except:
            print("Unexpected error:", sys.exc_info()[0])
        
    def dodaj_wszystkie_sezony_zaznaczonej_druzyny_do_portfela(self):
        print("dodaj wszyskie zespol  do portf")
        if self.listWidget_2.currentRow()!=-1:
            nazwa_zespolu= str(self.listWidget_2.currentItem().text()).split("'")[1]
            for i in range(self.listWidget_2.count()):
                zespol = self.listWidget_2.item(i).text()
                if str(zespol).split("'")[1]== nazwa_zespolu:
                    self.portfel.append([str(zespol).split("'")[1],str(zespol).split("'")[3],int(str(zespol).split("'")[5]),str(zespol).split("'")[6]])
                    self.listWidget_3.insertItem(0,zespol)
        self.przelicz_jeszcze_raz()
        
    def dodaj_wszystkie_zespoly_do_portfela(self):
        print("dodaj_wszystkie_sezony_zaznaczonej_druzyny")
        for i in range(self.listWidget_2.count()):
            zespol = self.listWidget_2.item(i).text()
            self.portfel.append([str(zespol).split("'")[1],str(zespol).split("'")[3],int(str(zespol).split("'")[5]),str(zespol).split("'")[6]])
            self.listWidget_3.insertItem(0,zespol)
        self.przelicz_jeszcze_raz()
        
    def przelicz_jeszcze_raz(self):
        print("przelicz jeszcze raz")
		
        conn = sqlite3.connect('PROGRESJA')
        c =conn.cursor()
        stawka0 = self.doubleSpinBox.value()
        przedz_k=[self.doubleSpinBox_3.value(),self.doubleSpinBox_4.value()]
        border = self.spinBox_4.value()
        generator = Generator_tabeli_iloczynowej()
        
        flaga_startowa = self.radioButton_8.isChecked()
        czy_odrzucam = self.radioButton_5.isChecked()
        if self.radioButton.isChecked():
            typ = "fib"
        else:
            typ="iloraz"
            
        if self.radioButton_3.isChecked():
            kiedy=1
        else:
            kiedy=0
            
        kiedy_zaczynam = self.spinBox_6.value()
        kiedy_koncze = self.spinBox_7.value()
        if self.radioButton_9.isChecked():
            czy_wyliczone = 1
        else:
            czy_wyliczone =0
        
        czy_na_remisy = 1        # czy gramy na remisy czy preciwko remisom
        if self.radioButton_12.isChecked():
            czy_na_remisy = 0          
        zabezpieczenie_zerwania_progresji =99
        if self.radioButton.isChecked():
           zabezpieczenie_zerwania_progresji = self.spinBox_8.value() 
         

        mnoznik = self.doubleSpinBox_2.value()        
        absolutna_granica = self.spinBox_5.value()
        
        parametry_finansowe="Mnoznik,granica\tMaxCF\tMinCF\tMaxWol\tSrWol\tMaxPotrzeba\tWydajnosc\n"
        
        tabela_mnoznikow =[]
        if self.checkBox.isChecked():
            mnoznik =self.doubleSpinBox_5.value()
            while mnoznik<= self.doubleSpinBox_6.value():
                mnoznik+=self.doubleSpinBox_7.value()
                tabela_mnoznikow.append(mnoznik)
        else:
            tabela_mnoznikow=[mnoznik]
        #print tabela_mnoznikow
        if self.checkBox_3.isChecked():
            tabela_granic_absolutnych = range(self.spinBox_18.value(),self.spinBox_19.value())
        else:
            tabela_granic_absolutnych = [absolutna_granica]
        for absolutna_granica in tabela_granic_absolutnych:
            for mnoznik in tabela_mnoznikow:
                tabela_iloczynowa = generator.daj_tabele(mnoznik,34)
        
                tablica_cash_flow_zespolow=[]
                tablica_serii_zespolow =[]
                tablica_wolumenow=[]
                tablica_skladowych_rozkladow_niepowodzen=[]
                rozklad_remisow = [0]*64
                for rekord in self.portfel:  # lece po kazdym elemencie w portfelu
                    # postac rekordu :  ['Vicenza','Wlochy',2, ', 2010)']
                    cmd = "select Nazwa, htlogic, ftlogic from WYNIKI where Sezon="+rekord[3].rstrip(")").strip(",")+" and Liga="+str(rekord[2])+" and Kraj=\""+rekord[1]+"\" and Nazwa= \""+ rekord[0] +"\""
                    c.execute(cmd)
                    for druzyna in c:
                            a= Obstawiacz(stawka0,przedz_k,druzyna,tabela_iloczynowa,typ,kiedy,border,absolutna_granica, flaga_startowa,  czy_odrzucam, kiedy_zaczynam,kiedy_koncze,  czy_wyliczone,  czy_na_remisy, zabezpieczenie_zerwania_progresji)
                            flow_i, tab_serii,  wolumen, skladowy_rozklad_niepowodzen = a.wynik()
                            tablica_cash_flow_zespolow.append(flow_i)
                            tablica_serii_zespolow.append(tab_serii)
                            tablica_wolumenow.append(wolumen)
                            tablica_skladowych_rozkladow_niepowodzen.append(skladowy_rozklad_niepowodzen)
                    
                            #liczenie rozkladu remisow
                            kolejka =0
                            for czy_remis_w_kolejce in druzyna[1]:
                                if czy_remis_w_kolejce=="1":
                                    rozklad_remisow[kolejka]+=1
                                kolejka+=1
                
             
                    #liczenie 	cash flow dla wszystkich wybranych zespolow
            
                    tablica_dlugosci_cf_zespolow=[]     #sprawdzam maksymalna dlugosc ciagu wynikow
                    for flow_zespolu in tablica_cash_flow_zespolow:
                        tablica_dlugosci_cf_zespolow.append(len(flow_zespolu))
                    maksymalna_dlugosc_cf = max(tablica_dlugosci_cf_zespolow)
            
                    # dopelniam krotsze ciagi do dlugosci najdluzszego
                    for flow_zespolu in tablica_cash_flow_zespolow:
                        dlugosc_flow_zespolu =len(flow_zespolu) 
                        if dlugosc_flow_zespolu>0:
                            ostatni_indeks = dlugosc_flow_zespolu-1
                            ostatni_flow = flow_zespolu[ostatni_indeks]
                        else:
                            ostatni_flow = 0
                        roznica_dlugosci =maksymalna_dlugosc_cf -dlugosc_flow_zespolu
                        if roznica_dlugosci>0:
                            for i in range(roznica_dlugosci):
                                flow_zespolu.append(ostatni_flow)

                    #tablica_cash_flow = [0]*(maksymalna_dlugosc_cf)
                    tablica_cash_flow=[]
                    for flow_zespolu in tablica_cash_flow_zespolow:  
                        i=0
                        for stan in flow_zespolu:
                            if len(tablica_cash_flow)>i:
                                tablica_cash_flow[i]+=stan
                            else:   # jezeli tablica cash flow jest krotsza niz ten zespol rozegral meczow
                                tablica_cash_flow.append(stan)
                            i+=1

                    tablica_calkowitych_wolumenow=[]
                    for wolumeny in tablica_wolumenow:
                        i=0
                        for wolumen in wolumeny:
                            if len(tablica_calkowitych_wolumenow)>i:
                                tablica_calkowitych_wolumenow[i]+=wolumen
                            else:
                                tablica_calkowitych_wolumenow.append(wolumen)
                            i+=1
                    #liczenie rozkladu serii dla wszystkich wybranych zespolow
                    rozklad_niepowodzen_systemowych=[0]*64
                    for tab_serii in tablica_serii_zespolow:
                        for seria in tab_serii:
                            rozklad_niepowodzen_systemowych[seria]+=1
        
            
                    #suma= sum(rozklad)
                    rozklad_bez_remisow = [0]*64
                    for skladowy_rozklad in tablica_skladowych_rozkladow_niepowodzen:
                        i=0
                        for ilosc_wystapien_danej_serii in skladowy_rozklad:
                            rozklad_bez_remisow[i]+=ilosc_wystapien_danej_serii
                            i+=1    
                
            
                    cf_laczone=[]
                    i=0
                    poczatkowe_cf = 0
                    for wolumen in tablica_calkowitych_wolumenow:
                        cf_laczone.append(tablica_cash_flow[i] - wolumen)
                        i+=1      
                    self.rysuj_wykres(tablica_cash_flow,tablica_calkowitych_wolumenow, cf_laczone)
                    min_cf_laczone= min(cf_laczone)
                    indeks_najmniejszej = cf_laczone.index(min_cf_laczone)
                    maks_cf =0
                    for val in tablica_cash_flow[indeks_najmniejszej:]:
                        if i ==0:
                            maks_cf = val
                        if val >maks_cf:
                            maks_cf = val
                        i+=1
                    znak=1
                    if min_cf_laczone<0:
                        znak=-1
                    elif abs(min_cf_laczone)<1:
                        min_cf_laczone=1
                

                parametry_finansowe+=str(mnoznik)+"/"+str(absolutna_granica)+"\t"+str(maks_cf)+"\t"+str(min_cf_laczone)+"\t"
                parametry_finansowe+=str(max(tablica_calkowitych_wolumenow))+"\t"+str(sum(tablica_calkowitych_wolumenow)/ len(tablica_calkowitych_wolumenow))
                parametry_finansowe+="\t"+str(min(cf_laczone))+"\t"+str((maks_cf )/min_cf_laczone*znak)+"\n"
                self.textEdit_2.setText(parametry_finansowe)
            
            
                wydruk = "ROZKLAD REMISOW OD KOLEJKI\n"
                for a in rozklad_remisow:
                    wydruk +=str(a) +"\t"
                self.textEdit_3.setText(wydruk)
        

    def rysuj_wykres(self,tablica_cash_flow, tablica_wolumenow, cf_laczone):
        try:
            _fromUtf8 = QtCore.QString.fromUtf8
        except AttributeError:
            _fromUtf8 = lambda s: s
        self.qwtPlot.hide()
        self.qwtPlot.destroy()

        


        self.qwtPlot = Qwt.QwtPlot(self.tab_3)
        self.qwtPlot.setGeometry(QtCore.QRect(0, 0, 891, 256))
        self.qwtPlot.setObjectName(_fromUtf8("qwtPlot"))
        self.qwtPlot.setAxisScale(Qwt.QwtPlot.xBottom, 0.0, len(tablica_cash_flow))
        self.qwtPlot.setAxisScale(Qwt.QwtPlot.yLeft, min(cf_laczone), max(max(tablica_cash_flow),  max(tablica_wolumenow)))
        
        grid = Qwt.QwtPlotGrid()
        grid.enableXMin(True)
        grid.enableYMin(True)
        grid.setMajPen(QtGui.QPen(QtGui.QColor(0,0,0), 1));
        grid.setMinPen(QtGui.QPen(QtGui.QColor(100,100,100), 1));
     
        grid.attach(self.qwtPlot)

        #histogram = HistogramItem()
        #histogram.setColor(QtGui.QColor(170,170,100))

        
        numValues = len(tablica_cash_flow)
        intervals = []
        values = Qwt.QwtArrayDouble(numValues)

        argumenty = range(len(values))
        argumenty2=[]
        for arg in argumenty:
            argumenty2.append(float(arg))
        #argumenty2 = Qwt.QwtArrayDouble()
        i=0
        #for args in argumenty:
        curve = Qwt.QwtPlotCurve("Curve "+str(i))
        curve.setPen(QtGui.QPen(QtGui.QBrush(QtGui.QColor(0, 255, 0)), 2))  # cash flow zielone
        curve.setData(argumenty2, tablica_cash_flow )
        curve.attach(self.qwtPlot)
        i=1
        curve2 = Qwt.QwtPlotCurve("Curve "+str(i))
        curve2.setPen(QtGui.QPen(QtGui.QBrush(QtGui.QColor(255, 0, 0)), 2))  # wolumen czerwony
        curve2.setData(argumenty2, tablica_wolumenow )
        curve2.attach(self.qwtPlot)
        i=3
        curve3 = Qwt.QwtPlotCurve("Curve "+str(i))
        curve3.setPen(QtGui.QPen(QtGui.QBrush(QtGui.QColor(0, 0, 255)), 2))  # suma niebieska
        curve3.setData(argumenty2, cf_laczone )
        curve3.attach(self.qwtPlot)

        self.qwtPlot.replot()
        self.qwtPlot.show()
        
        
        

