from Team import *

class Wyluskiwacz_wynikow:

    
    def __init__(self,tresc_stronki_z_wynikami,druzyny,kraj,liga,sezon):
        years=[]
        self.teams=[]
        self.team_names=[]
        results=[]
        half=""
        whole=""
        file=0
        workarea=False
        print("tworze wyluskiwacz wynikow")
        
        self.team_names=druzyny
        
        w_tabeli=False
        url = "results_tmp"
        plik_tmp = open(url,"w")
        plik_tmp.write(tresc_stronki_z_wynikami)
        self.znacznik_poczatka_wynikow = "FT"
        self.zespoly =[]
        plik_tmp.close()
    
        self.file=open(url)
        i=0
        print(self.team_names)

        for name in self.team_names:
            t = Team(name,sezon,kraj,liga)
            self.teams.append(t)
			    
    def note_results(self):
		#inaczej bedzie
		# ide i szukam druzyn, jak znajde 2 to zgarniam wyniki
		# wyniki zgarniete to znowu szukam druzyn
        self.dupa=[]
        i=0
        g=0
        h=0
        czy_bylo=0
        for line in self.file:   #ide po linni
            line =line.rstrip()
            index_znaleziony= False
            i+=1
            
            j=0
            for team in self.team_names:  #sprawdzam czy w linii znajduje sie nazwa druzyny
                if line == team:
                    index= j
                    h+=1
                    break
                j+=1
                
            if h==1:
                t1 = self.teams[index]
                if czy_bylo==0:
				    t1.host_or_not.append(1)
				    czy_bylo+=1
            elif h==2:
                t2 = self.teams[index]
                t2.host_or_not.append(-1)
                czy_bylo =0
            if h==2:
                g = 0
                for line in self.file:
                    line=line.rstrip()
                    i=i+1
                    g=g+1
                    if g==2:
                        if len(line)<2:
                            ht=0
                            ht2=0
                        else:
                            tmp=line.split(":")
                            if int(int(tmp[0])==int(tmp[1])):
                                ht=1
                                ht2=1						    #jezeli liczba goli jest rowna to jest to remis to 1
                            elif int(int(tmp[0]) > int(tmp[1])):
						        ht=3
						        ht2=0
                            elif int(int(tmp[0])< int(tmp[1])):
                                ht=0
                                ht2=3
                        t1.htequal.append(ht)					
                        t2.htequal.append(ht2)
                        t1.htresults.append(line)
                        t2.htresults.append(line)
                    if g==4:
                        if len(line)<2:
                            ft=0
                            ft2=0
                        else:
                            tmp=line.split(":")
                            if int(int(tmp[0])==int(tmp[1])):
                                ft=1
                                ft2=1						    #jezeli liczba goli jest rowna to jest to remis to 1
                            elif int(int(tmp[0]) > int(tmp[1])):
						        ft=3
						        ft2=0
                            elif int(int(tmp[0])< int(tmp[1])):
                                ft=0
                                ft2=3
                        t1.ftequal.append(ft)
                        t2.ftequal.append(ft2)
                        t1.ftresults.append(line)
                        t2.ftresults.append(line)
                        g=0
                        h=0
                        break
                        
                    
            if line=="HT (Half Time) - wynik do przerwy":
                break
                
        for t1 in self.teams:
            t1.htequal.reverse()
            t1.htresults.reverse()
            t1.ftequal.reverse()
            t1.ftresults.reverse()
            t1.host_or_not.reverse()
            print t1.ftresults
            print t1.host_or_not
       					
    def daj_ciagi(self):
        wydruk =""
        for team in self.teams:
            wydruk=wydruk+ team.name +" Sezon " +str(team.sezon) + " Kraj " + team.kraj + " Liga " + str(team.liga) +"\n" + " ht " + str(team.htresults) +"\n" + "ft " +str(team.ftresults)	+"\n"	
            wydruk = wydruk + "Ciag ht " + str(team.htequal) +"\n"+ " Ciag ft " + str(team.ftequal) +"\n"
        return wydruk

    def daj_stringa_z_remisami(self):
        wydruk =""	
        self.dane_do_tabeli=[]		       
        for team in self.teams:
            htequal_string=""
            ftequal_string=""
            for equal in team.htequal:
                htequal_string +=str(equal)
				
            for equal in team.ftequal:
                ftequal_string +=str(equal)
								
            skladnik= "'"+str(team.name)+"',"+str(team.sezon) + ",'" + team.kraj + "'," + str(team.liga) +",'"  + htequal_string +"','" + ftequal_string+"'"
            wydruk += str(skladnik)
            self.dane_do_tabeli.append(skladnik)
        print(wydruk)
        return wydruk      
