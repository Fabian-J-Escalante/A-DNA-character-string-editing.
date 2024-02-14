
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

def abrir_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv")])
    if archivo:
        print("Archivo seleccionado:", archivo)

ttk.Label(frm, text="Actividad 4").grid(column=0, row=0)
ttk.Button(frm, text="Buscar Archivo", command=abrir_archivo).grid(column=1, row=0)

root.mainloop()