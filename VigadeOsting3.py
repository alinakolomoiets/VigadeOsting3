from module1 import*
s=pos=neg=null=[]
def vahetus (a:int,b:int):
	"""Kui a<b on vahetatud
	:param int a:Arv, mis on suurem kui b
	:param int b:Arv väiksem kui a
	:rtype:int
	"""
	abi=a
	a=b
	b=abi
	return a,b

def generaator (n:int,loend:list,a:int,b:int):
	"""Lisab loendisse n a kuni b
	:param int n:väärtuste arv loendis
	:param list loend:nimekirja
	:param int a: minimaalne väärtus
	:param int b:maksimaalne väärtus
	:rtype:int 
	"""
	for i in range (n):
			loend.append(randint(a,b))

def jagamine(loend:list,p:int,n:int,nol:int):
	"""Positiivse, negatiivse ja nulli lisamine
	:param loend:nimekirja
	:param p: positiivne lisamine
	:param n: negativne lisamine 
	:param nol: nulli lisamine
	:rtype:int
	"""
	for el in loend:
		if el>0:
			p.append(el)
		elif el<0:
			n.append(el)
		else:
			nol.append(el)

def keskmine(loend:list,n:int):
	"""Määrake keskmine
	:param loend:nimekirja
	:param n:väärtuste arv loendis
	:rtype:int
	"""
	n=len(loend)
	if n==0:
		kesk=0
	else:
		sum=0
		for i in loend:
			sum+=i
		kesk=round(sum/n,2)
	return kesk

def lisamine(loend:list,el:int):
	"""Lisage algsele massiivile keskmised
	:param loend :nimekirja
	:param el:numbrid
	:rtype:int
	"""
	loend.append(el)
	loend.sort()
arvud_loendis()
