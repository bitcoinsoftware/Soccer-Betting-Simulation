class Team:
    name=""

    def __init__(self,name,sezon,kraj,liga):
        self.name=name
        self.sezon = sezon
        self.kraj = kraj
        self.liga = liga
        self.htresults=[]
        self.ftresults=[]
        self.htequal=[]
        self.ftequal=[]
        self.host_or_not = []
        
    def introduce(self):
        return self.name
    def addftresult(self,ft):
        self.ftresults.append(ft)
    def addhtresult(self,ht):
        self.htresults.append(ht)
        
    def allinfo(self):
        print(self.name)
		#print len(self.htresults)
        print(self.htresults)
        print(self.ftresults)
