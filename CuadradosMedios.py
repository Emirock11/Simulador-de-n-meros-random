from ResultadosGUI import res1

def cuadradosMedios(n1,n):
	tam1 = len(str(n1))
	R = []
	Semillas = []
	Generadores = []
	Ri = []

	for i in range(n):
		Semillas.append(n1)
		numero2 = n1**2
		Generadores.append(numero2)
		snumero2 = str(numero2)
		tam2 = len(snumero2)
		primerc = int((tam2 - tam1) / 2)
		snumero3 = snumero2[primerc:primerc+tam1]
		R.append(int(snumero3))
		Ri.append(int(snumero3)/10000)
		n1 = int(snumero3)
	
	res1(R, Semillas, Generadores, Ri)

