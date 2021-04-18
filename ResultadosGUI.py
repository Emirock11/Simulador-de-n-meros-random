import tkinter as tk
from PIL import Image, ImageTk


TFont = ("Verdana", 15)

def res1(R, Semillas, Generadores, Ri):
    metod = "Metodo de los Centros Cuadrados"
    cargarVentana(metod, R, Semillas, Generadores, False, Ri)

def res2(R, m, c, a, Semillas, Ri):
    metod = "Metodo Congruencial"
    Generadores = []
    for i in range(len(R)):
        pos = 1+int(i)
        strGen = "x"+str(pos)+"=("+str(a)+"*"+str(Semillas[i])+"+"+str(c)+")mod("+str(m)+")"
        Generadores.append(strGen)
    cargarVentana(metod, R, Semillas, Generadores, False, Ri)

def res3(R, periodoCompleto, a, c, m, Semillas, Ri):
    metod = "Metodo Congruencial Mixto"
    Generadores = []
    for i in range(len(R)):
        pos = 1+int(i)
        strGen = "x"+str(pos)+"=("+str(a)+"*"+str(Semillas[i])+"+"+str(c)+")mod("+str(m)+")"
        Generadores.append(strGen)
    cargarVentana(metod, R, Semillas, Generadores, periodoCompleto, Ri)

def res4(Xn, Yn, Wn):
    metod = "Metodo Congruencial lineal Combinado"
    cargarVentana(metod, Wn, Xn, Yn, False, [])
    # diferentes botones

def res5(R, a, m, Semillas, Ri):
    metod = "Generador Multiplicativo"
    Generadores = []
    for i in range(len(R)):
        pos = 1+int(i)
        strGen = "x"+str(pos)+"=("+str(a)+"*"+str(Semillas[i])+")mod("+str(m)+")"
        Generadores.append(strGen)
    cargarVentana(metod, R, Semillas, Generadores, False, Ri)

def cargarVentana(metodo, R, Semillas, Generadores, periodoCompleto, Ri):
    root = tk.Tk()
    root.grid_rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    frame_main = tk.Frame(root, bg='#31a5db')
    frame_main.grid(sticky='news')

    title= "Resultados del "+metodo

    label1 = tk.Label(frame_main, text=title, font = TFont, bg='#31a5db')
    label1.grid(row=0, column=0, pady=(5, 0), sticky='nw')

    
    if metodo == "Metodo Congruencial Mixto":
        txt = ""
        if periodoCompleto:
            txt = "Segun el teorema de HULL-DOBELL, si se tiene el periodo completo"
        else:
            txt = "Segun el teorema de HULL-DOBELL, si se tiene el periodo completo"
        label2 = tk.Label(frame_main, text=txt, bg='#31a5db')
        label2.grid(row=1, column=0, pady=(5, 0), sticky='nw')

    # Create a frame for the canvas with non-zero row&column weights
    frame_canvas = tk.Frame(frame_main)
    frame_canvas.grid(row=2, column=0, pady=(5, 0), sticky='nw')
    frame_canvas.grid_rowconfigure(0, weight=1)
    frame_canvas.grid_columnconfigure(0, weight=1)
    # Set grid_propagate to False to allow 5-by-5 buttons resizing later
    frame_canvas.grid_propagate(False)

    # Add a canvas in that frame
    canvas = tk.Canvas(frame_canvas, bg="yellow")
    canvas.grid(row=0, column=0, sticky="news")

    # Link a scrollbar to the canvas
    vsb = tk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
    vsb.grid(row=0, column=1, sticky='ns')
    canvas.configure(yscrollcommand=vsb.set)

    # Create a frame to contain the buttons
    frame_buttons = tk.Frame(canvas, bg="blue")
    canvas.create_window((0, 0), window=frame_buttons, anchor='nw')

    # Add 9-by-5 buttons to the frame
    

    if metodo != "Metodo Congruencial lineal Combinado":

        rows = len(R)
        columns = 5
        pos = []
        for i in range(rows):
            pos.append(i)
        mainList=[pos,Semillas,Generadores,R, Ri]
        buttons = [[tk.Button() for j in range(columns)] for i in range(rows+1)]

        buttons[0][0] = tk.Button(frame_buttons, text=("___Posicion___"))
        buttons[0][0].grid(row=0, column=0, sticky='news')

        buttons[0][1] = tk.Button(frame_buttons, text=("___Semilla___"))
        buttons[0][1].grid(row=0, column=1, sticky='news')

        buttons[0][2] = tk.Button(frame_buttons, text=("___Generador___"))
        buttons[0][2].grid(row=0, column=2, sticky='news')

        buttons[0][3] = tk.Button(frame_buttons, text=("_No. Aleatorio_"))
        buttons[0][3].grid(row=0, column=3, sticky='news')

        buttons[0][4] = tk.Button(frame_buttons, text=("___Random Ri___"))
        buttons[0][4].grid(row=0, column=4, sticky='news')

        for i in range(1, rows+1):
            for j in range(0, columns):
                buttons[i][j] = tk.Button(frame_buttons, text=(mainList[j][i-1]))
                buttons[i][j].grid(row=i, column=j, sticky='news')

        # Update buttons frames idle tasks to let tkinter calculate buttons sizes
        frame_buttons.update_idletasks()

        # Resize the canvas frame to show exactly 5-by-5 buttons and the scrollbar
        first5columns_width = sum([buttons[0][j].winfo_width() for j in range(0, columns)])
        first5rows_height = sum([buttons[i][0].winfo_height() for i in range(0, 10)])
        frame_canvas.config(width=first5columns_width + vsb.winfo_width(),
                            height=first5rows_height)

        # Set the canvas scrolling region
        canvas.config(scrollregion=canvas.bbox("all"))

    else:
        rows = len(R)
        columns = 4
        pos = []
        for i in range(rows):
            pos.append(i)
        mainList=[pos,Semillas,Generadores,R]
        buttons = [[tk.Button() for j in range(columns)] for i in range(rows+1)]
        buttons[0][0] = tk.Button(frame_buttons, text=("_______n________"))
        buttons[0][0].grid(row=0, column=0, sticky='news')

        buttons[0][1] = tk.Button(frame_buttons, text=("_______Xn_______"))
        buttons[0][1].grid(row=0, column=1, sticky='news')

        buttons[0][2] = tk.Button(frame_buttons, text=("_______Yn_______"))
        buttons[0][2].grid(row=0, column=2, sticky='news')

        buttons[0][3] = tk.Button(frame_buttons, text=("_______Wn_______"))
        buttons[0][3].grid(row=0, column=3, sticky='news')

        for i in range(1, rows+1):
            for j in range(0, columns):
                buttons[i][j] = tk.Button(frame_buttons, text=(mainList[j][i-1]))
                buttons[i][j].grid(row=i, column=j, sticky='news')

        # Update buttons frames idle tasks to let tkinter calculate buttons sizes
        frame_buttons.update_idletasks()

        # Resize the canvas frame to show exactly 5-by-5 buttons and the scrollbar
        first5columns_width = sum([buttons[0][j].winfo_width() for j in range(0, columns)])
        first5rows_height = sum([buttons[i][0].winfo_height() for i in range(0, 10)])
        frame_canvas.config(width=first5columns_width + vsb.winfo_width(),
                            height=first5rows_height)

        # Set the canvas scrolling region
        canvas.config(scrollregion=canvas.bbox("all"))

    # Launch the GUI
    root.mainloop()




