import tkinter as tk
from PIL import Image, ImageTk
import math

tablaChiCuadrada = [[0.000039350,0.000157,0.000982,0.00393,3.841,5.024,6.635,7.879],
                    [0.010,0.020,0.051,0.103,5.991,7.378,9.210,10.597],
                    [0.072,0.115,0.216,0.352,7.815,9.348,11.345,12.838],
                    [0.207,0.297,0.484,0.711,9.488,11.143,13.277,14.860],
                    [0.412,0.554,0.831,1.145,11.070,12.832,15.086,16.750],
                    [0.676,0.872,1.237,1.635,12.592,14.449,16.812,18.548],
                    [0.989,1.239,1.690,2.167,14.067,16.013,18.475,20.278],
                    [1.344,1.647,2.180,2.733,15.507,17.535,20.090,21.955],
                    [1.735,2.088,2.700,3.325,16.919,19.023,21.666,23.589],
                    [2.156,2.558,3.247,3.940,18.307,20.483,23.209,25.188],
                    [2.603,3.053,3.816,4.575,19.675,21.920,24.725,26.757],
                    [3.074,3.571,4.404,5.226,21.026,23.337,26.217,28.300],
                    [3.565,4.107,5.009,5.892,22.362,24.736,27.688,29.819],
                    [4.075,4.660,5.629,6.571,23.685,26.119,29.141,31.319],
                    [4.601,5.229,6.262,7.261,24.996,27.488,30.578,32.801],
                    [5.142,5.812,6.908,7.962,26.296,28.845,32.000,34.267],
                    [5.697,6.408,7.564,8.672,27.587,30.191,33.409,35.718],
                    [6.265,7.015,8.231,9.390,28.869,31.526,34.805,37.156],
                    [6.844,7.633,8.907,10.117,30.144,32.852,36.191,38.582],
                    [7.434,8.260,9.591,10.851,31.410,34.170,37.566,39.997],
                    [8.034,8.897,10.283,11.591,32.671,35.479,38.932,41.401],
                    [8.643,9.542,10.982,12.338,33.924,36.781,40.289,42.796],
                    [9.260,10.196,11.689,13.091,35.172,38.076,41.638,44.181],
                    [9.886,10.856,12.401,13.848,36.415,39.364,42.980,45.558],
                    [10.520,11.524,13.120,14.611,37.652,40.646,44.314,46.928],
                    [11.160,12.198,13.844,15.379,38.885,41.923,45.642,48.290],
                    [11.808,12.878,14.573,16.151,40.113,43.195,46.963,49.645],
                    [12.461,13.565,15.308,16.928,41.337,44.461,48.278,50.994],
                    [13.121,14.256,16.047,17.708,42.557,45.722,49.588,52.335],
                    [13.787,14.953,16.791,18.493,43.773,46.979,50.892,53.672]]

def ventanaChiCuadrada(Ri):
    def option_changed(*args):
        global nivelSign
        current = var.get()
        if current == "0.005":
            nivelSign = 0.005
        elif current == "0.01":
            nivelSign = 0.01
        elif current == "0.025":
            nivelSign = 0.025
        elif current == "0.05":
            nivelSign = 0.05
        elif current == "0.95":
            nivelSign = 0.95
        elif current == "0.975":
            nivelSign = 0.975
        elif current == "0.99":
            nivelSign = 0.99
        elif current == "0.995":
            nivelSign = 0.995

    def option_changed2(*args):
        global gradosLibertad
        current = var2.get()
        gradosLibertad = int(current)

    def Chi():
        print("nivelSign: ",float(var.get()))
        print("gradosLibertad: ",float(var2.get()))
        ChiCuadrada(Ri, float(var.get()), int(var2.get()))

    TFont = ("Verdana", 15)

    listAlfa = ["0.005","0.01","0.025", "0.05", "0.95","0.975", "0.99", "0.995"]
    listGrados = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                  "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
                  "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"]

    app = tk.Tk()

    canvas = tk.Canvas(app, height=200, width=400, bg='#31a5db')
    canvas.pack()

    mainFrame = tk.Frame(canvas, bg='#2fe7ea')
    mainFrame.place(relx=0.05, rely=0, relwidth=0.9, relheight=1)

    

    # Frame 1 / Inicio

    frame1 = tk.Frame(mainFrame, bg='#74d9ee')
    frame1.place(relx=0, rely=0, relwidth=1, relheight=0.9)

    label = tk.Label(canvas, text="Chi-Cuadrada", fg='Black', bg='#74d9ee', font=TFont)
    label.place(relx=0, rely=0, relwidth=1, relheight=0.1)

    # Contenido del frame 1 / Inicio

    labelMetodo = tk.Label(frame1, text="Nivel de confianza: ", bg='#74ee7e')
    labelMetodo.place(relx=0.075, rely=0.27, relwidth=0.3)

    var = tk.StringVar(frame1)
    var.set(listAlfa[0])
    var.trace("w", option_changed)
    methodsMenu = tk.OptionMenu(frame1, var, *listAlfa)
    methodsMenu.config(highlightbackground ='#74d9ee')
    methodsMenu.place(relx=0.39, rely=0.25, relwidth=0.2)

    labelMetodo2 = tk.Label(frame1, text="Grados de libertad: ", bg='#74ee7e')
    labelMetodo2.place(relx=0.075, rely=0.57, relwidth=0.3)

    var2 = tk.StringVar(frame1)
    var2.set(listGrados[0])
    var2.trace("w", option_changed2)
    gradosMenu = tk.OptionMenu(frame1, var2, *listGrados)
    gradosMenu.config(highlightbackground ='#74d9ee')
    gradosMenu.place(relx=0.39, rely=0.55, relwidth=0.2)

    buttonCal = tk.Button(frame1, text="Validar", command=Chi)
    buttonCal.place(relx=0.7, rely = 0.5)

    app.mainloop()


def ChiCuadrada(Ri, nivelSign, gradosLibertad):
    Intervalos = []
    FrecAbs = []
    Ri.sort()
    n = len(Ri)
    k = math.floor(1 + 3.322*math.log10(n))
    
    clase = round(1 / k, 2)
    strClase = str(clase)
    if len(strClase)>3:
        if int(strClase[3]) >= 5:
            clase += 0.1
        clase = round(clase, 1)
    suma = 0
    for i in range(len(Ri)):
        suma += Ri[i]
    
    inf = 0
    top = 0
    for i in range(k):
        top = round(top + clase, 1)
        Intervalos.append([inf, top])
        inf = top

    for i in range(len(Intervalos)):
        FrecAbs.append(0)

    for i in range(0, n):
        encontrado = False
        valPos = Ri[i]
        j=0
        cont = 0
        while(encontrado != True and cont < len(Intervalos)):
            interAct = Intervalos[j]
            if(valPos >= interAct[0] and valPos < interAct[1]):
                valAnt = FrecAbs[j]
                FrecAbs[j] = valAnt + 1
                encontrado = True
            cont += 1
            j += 1

    FrecRel = []
    for i in range(len(FrecAbs)):
        FrecRel.append(FrecAbs[i]/n)

    EiTeorica = []
    for i in range(len(FrecAbs)):
        EiTeorica.append(n/k)

    aJuntar = verAJuntar(FrecAbs)
    resultados = ()
    if aJuntar != []:
        resultados = juntar(aJuntar, Intervalos, FrecAbs, EiTeorica)

    newFrecAbs = resultados[1]
    newEiTeorica = resultados[2]

    XiUNIF = 0
    for i in range(len(newFrecAbs)):
        Oi = newFrecAbs[i]
        Ei = newEiTeorica[i]
        XiUNIF = XiUNIF + (math.pow((Oi-Ei),2)/Ei)

    xTabla = 0
    if(nivelSign == 0.005):
        xTabla = 0
    elif(nivelSign == 0.01):
        xTabla = 1
    elif(nivelSign == 0.025):
        xTabla = 2
    elif(nivelSign == 0.05):
        xTabla = 3
    if(nivelSign == 0.95):
        xTabla = 4
    elif(nivelSign == 0.975):
        xTabla = 5
    elif(nivelSign == 0.99):
        xTabla = 6
    elif(nivelSign == 0.995):
        xTabla = 7

    tablas = tablaChiCuadrada[gradosLibertad-1][xTabla]
    testT = ""
    testT2 = ""
    if XiUNIF < tablas:
        testT = "No se rechaza la hipotesis nula de uniformidad."
        testT2 = "X0^2 ("+str(XiUNIF)+") < Xv,alpha^2 ("+str(tablas)+")"
    else:
        testT = "Se rechaza la hipotesis nula de uniformidad."
        testT2 = "X0^2 ("+str(XiUNIF)+") > Xv,alpha^2 ("+str(tablas)+")"
    response(testT, testT2)
    
    

def response(testT, testT2):
    
    app = tk.Tk()

    canvas = tk.Canvas(app, height=100, width=500, bg='#31a5db')
    canvas.pack()

    mainFrame = tk.Frame(canvas, bg='#2fe7ea')
    mainFrame.place(relx=0.05, rely=0, relwidth=0.9, relheight=1)

    TFont = ("Verdana", 10)
    TFont2 = ("Verdana", 13)

    # Frame 1 / Inicio

    frame1 = tk.Frame(mainFrame, bg='#74d9ee')
    frame1.place(relx=0, rely=0, relwidth=1, relheight=0.9)

    label1 = tk.Label(mainFrame, text=testT, fg='Black', bg='#74d9ee', font=TFont)
    label1.place(relx=0, rely=0.2, relwidth=1, relheight=0.1)

    label2 = tk.Label(mainFrame, text=testT2, fg='Black', bg='#74d9ee', font=TFont2)
    label2.place(relx=0, rely=0.5, relwidth=1, relheight=0.2)



def juntar(aJuntar, Intervalos, FrecAbs, EiTeorica):
    newIntervalos = []
    newFrecAbs = []
    newEiTeorica = []
    cont = 0
    cont2 = 0
    #while cont2 < len(Intervalos):
    for i in range(len(Intervalos)):
        if i < len(aJuntar):
            aModificar = aJuntar[cont] # [3, 4]
        n1 = aModificar[0] # 3
        n2 = aModificar[1] # 4
        if n1 == cont2 and cont2 < len(Intervalos): # 3 == 2
            inter1 = Intervalos[n1]
            inter2 = Intervalos[n2]
            arr = [inter1[0], inter2[1]]
            newIntervalos.append(arr)
            # Sumar Frecuencias absolutas de ambas clases
            sumaFrec = FrecAbs[n1] + FrecAbs[n2]
            # Se agrega a la nueva lista la suma de frecuencias
            newFrecAbs.append(sumaFrec)
            # Sumar Ei teorica
            sumaEi = EiTeorica[n1] + EiTeorica[n2]
            # Se agrega a la nueva lista la suma de Ei
            newEiTeorica.append(sumaEi)
            cont+=1
            cont2+=2
        elif cont2 < len(Intervalos):
            newIntervalos.append(Intervalos[cont2])
            # Se agrega la frecuencia del número
            newFrecAbs.append(FrecAbs[cont2])
            # Se agrega su Ei Teorica
            newEiTeorica.append(EiTeorica[cont2])
            cont2 +=1

    return newIntervalos, newFrecAbs, newEiTeorica


        

        

def verAJuntar(FrecAbs):
    # Identificar qué clases contienen observables menores a 5
    aJuntar = []
    for i in range(len(FrecAbs)):
        merg = []
        if FrecAbs[i] < 5 and i+1< len(FrecAbs):
            merg.append(i)
            if FrecAbs[i+1] < 5:
                merg.append(i+1)
                i+=2
                aJuntar.append(merg)
            else:
                i+=1
            
        elif i+1< len(FrecAbs):
            if FrecAbs[i+1] < 5 and i < 1:
                merg.append(i)
                merg.append(i+1)
                i+=2
                aJuntar.append(merg)
    return aJuntar


