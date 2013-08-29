class Generator_tabeli_iloczynowej:
	
    def __init__(self):
		print "generator tabeli"
    def potega(self,x,n):
		print "potega"
		#if n==0:
		#	return 1
		#elif n%2==1:
		#	return x*self.potega(x,n-1)
		#else:
		#	a = self.potega(x,n/2)
		#return a*a
		return x**n
		
    def daj_tabele(self,x,n):
        self.tabela=[]
        for i in range(n):
            self.tabela.append(self.potega(x,i))
        print self.tabela
        return self.tabela
			
