class Wyluskiwacz_z_tabeli:
    def __init__(self,tresc):
        print("wyluskiwacz z tabeli")
        w_tabeli=False
        plik_tmp = open("table_tmp","w")
        plik_tmp.write(tresc)
        znacznik_poczatka_tabeli = "Pkt"
        self.zespoly =[]
        plik_tmp.close()
        plik_tmp =open("table_tmp","r")
        i=0
        for line in plik_tmp:
            if line.find("Pkt\tASBR")!=-1 or line.find("Pkt\tOSBR")!=-1:
                print(line)
                w_tabeli=True
                i =0
            if (i-3)%21==0 and w_tabeli:
                self.zespoly.append(line.rstrip())
                
            if line.find("Ostatnia aktualizacja:")!=-1:
                w_tabeli=False
            i+=1
    
