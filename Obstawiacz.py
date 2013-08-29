
from random import *
class Obstawiacz:
    def __init__(self,stawka0,przedz_k,REKORD_Z_TAB_WYNIKI,tabela_iloczynowa,typ,kiedy,border,absolutna_granica, flaga_startowa,  czy_odrzucam,  kiedy_zaczynam,kiedy_koncze , czy_wyliczone,  czy_na_remisy,  zabezpieczenie_zerwania_progresji):
        
        self.winarray=[]
        self.border=border
        self.payarray=[]
        self.s0=stawka0
        self.kht = przedz_k
        self.absolutna_granica = absolutna_granica
        self.kiedy_zaczynam = kiedy_zaczynam
        self.kiedy_koncze = kiedy_koncze
        self.czy_wyliczone = czy_wyliczone
        self.czy_na_remisy = czy_na_remisy
        self.zabezpieczenie_zerwania_progresji =zabezpieczenie_zerwania_progresji
        if flaga_startowa ==1:
            self.flaga= border
        else:
            self.flaga = 0
        self.czy_odrzucam =czy_odrzucam  # mowi o tym czy po przekroczeniu granicy absolutnej odrzucam zespo czy resetuje kase ktora na niego stawiam
        if kiedy:
            self.ht=REKORD_Z_TAB_WYNIKI[1]
        else:	
            self.ht=REKORD_Z_TAB_WYNIKI[2]
            
        self.name=REKORD_Z_TAB_WYNIKI[0]
        self.typ = typ
        self.tabela_iloczynowa = tabela_iloczynowa
        
    def losuj_kurs(self,przedzial):
        k_max = int(100*przedzial[1])
        k_min = int(100*przedzial[0])
        seed()
        a= randint(k_min,k_max)
        return float(a/100.0)
		
    def fib(self,n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)	
              
    def wynik(self):
        i=0
        lh=0
        lf=0
        tabela_serii =[]
        wygranah=0
        wygranaf=0
        #tablica ciagow fibonacciego
        fi =[] 
        p2 = []
        fi=[ 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,233, 377, 610, 987, 1597 ,2548, 4181, 6729, 10910, 17639, 28549, 46188,74737,120925,195662,316587,512249,828836,1341085,2169921,3511006,5680927,9191933,14872860,24064793,38937653,63002446,101940099,164942545 ]
        #p2=[1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,524288*2,524288*4,524288*8,524288*16,524288*32,524288*64,524288*128,524288*256,524288*512,524288*1024]
        
        flaga=self.flaga   # gdy flaga = 0 to na poczatku wszystkie zespoly maja zielone swiatlo
        fullflaga=0
        tabh=[]
        tabf=[]
        wolumen=[]
        ile_juz=0
        border=self.border
        
        if self.typ =="fib":
            tabela_mnoznikow = fi
        else:
            tabela_mnoznikow = self.tabela_iloczynowa
        if self.kiedy_koncze>=len(self.ht):
            self.kiedy_koncze=len(self.ht)-1
        
        i=0
        wygranah = 0
        poziom_progresji=0
        ilosc_wtop = 0
        for wh in self.ht[:self.kiedy_koncze]:   # przegladam wyniki w ciagu zdarzen 
            wysokosc_wolumenu = 0
            if lh <self.absolutna_granica:  # jezeli zespol nie mial wiecej niz absolutna_granica niepowodzen pod rzad
                wh=(int(wh)==1)                    #zamieniam z char na int
                if not self.czy_na_remisy: wh = not wh   # jezeli gram przeciwko remisom 
                
                if wh==0 and flaga<border:  #jezeli nie bylo remisu a flaga pozwalala stawiac
                    
                    if i>=self.kiedy_zaczynam: 
                        if i == self.kiedy_zaczynam and self.czy_wyliczone:
                            lh =0
                        wysokosc_wolumenu =self.s0*tabela_mnoznikow[lh]
                    else: 
                        wysokosc_wolumenu =0   
                    if ilosc_wtop < self.zabezpieczenie_zerwania_progresji:
                        wygranah=wygranah- wysokosc_wolumenu #to przegrywam kase
                        lh=lh+1  # to jest zmienna do absolutnej ilosci niepowodzen - jezeli przekroczy np. 5 w systemie 2/5 to odrzucam zespol
                        flaga=flaga+1   # po kazdym niepowodzeniu zwiekszam flage o 1 , ale zeruje ja gdy wygrywam kase
                        ilosc_wtop +=1
                    
                elif wh and flaga<border:  # jezeli byl remis i flaga mniejsza od elementarnej granicy - np. 2 w systemie 2/5
                    if i>=self.kiedy_zaczynam: 
                        if i == self.kiedy_zaczynam and self.czy_wyliczone: 
                            lh =0
                        wysokosc_wolumenu =self.s0*tabela_mnoznikow[lh]
                    else:
                        wysokosc_wolumenu =0
                    if ilosc_wtop < self.zabezpieczenie_zerwania_progresji:
                        wygranah=wygranah +wysokosc_wolumenu*(self.losuj_kurs(self.kht)-1)  # zwiekszam kase o wygrana
                        tabela_serii.append(lh)  # do tabeli serii wpisuje dlugosc zakonczonej serii niepowodzen
                        lh=0   # zeruje absolutna ilosc niepowodzen
                        flaga=0 # zeruje elementarna ilosc niepowodzen
                        ilosc_wtop=0
                    else:
                        ilosc_wtop=0
                        print("bylo wiecej niepowodzen pod rzad niz pozwalasz")
                    
                elif wh and flaga>border-1:  # jezeli zespol jest "na stopie" czyli np. w syst 1/5 nie bylo remisu to stopuje do pojawienia sie remisu i pojawil sie remis
                    flaga =0
                    wysokosc_wolumenu = 0
                elif not wh and flaga>border-1:
                    wysokosc_wolumenu=0
                tabh.append(wygranah)	  
                wolumen.append(wysokosc_wolumenu)
            else:
                if (not self.czy_odrzucam) :  # jezeli zespol przekroczyl absolutna granice ale ustawilismy opcje resetowania stawki
                    flaga = border
                    lh =0
                    wolumen.append(0)
                    tabh.append(wygranah)
                else:           # jezeli zespol przekroczyl absolutna granice, ale nie resetujemy stawki tylko odrzucamy
                    #wolumen.
                    wolumen.append(0)
                    tabh.append(wygranah)
            #poziom_progresji = lh
                
            i+=1
        seria_niepowodzen = 0
        skladowy_rozklad_niepowodzen = 64*[0]
        a=0
        b= len(self.ht)
        for wh in self.ht:
            a+=1
            if int(wh) ==0:
                seria_niepowodzen+=1
                if a ==b: #jesli to ostatnia kolejka
                    skladowy_rozklad_niepowodzen[seria_niepowodzen]+=1
            if int(wh) ==1:
                skladowy_rozklad_niepowodzen[seria_niepowodzen]+=1
                seria_niepowodzen=0
        #print(self.name," wygrana do polowy" ,int(wygranah), "wygrana koniec" , int(wygranaf))
        return [tabh, tabela_serii,  wolumen,  skladowy_rozklad_niepowodzen]
        



