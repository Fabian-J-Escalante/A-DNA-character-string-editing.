import tkinter as tk
from tkinter import filedialog
import csv

def iniciar_back():
    #poner aqui el back supongo, no se unirlos aun
    pass

def abrir_archivo():
    global archivo_seleccionado
    archivo_seleccionado = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv")])
    if archivo_seleccionado:
        print("Archivo seleccionado:", archivo_seleccionado)
        mostrar_contenido(archivo_seleccionado)

def mostrar_contenido(archivo):
    try:
        fila = 1  
        columna = 3  

        with open(archivo, 'r') as file:
            lector_csv = csv.reader(file)
            datos = list(lector_csv)

            if 0 <= fila < len(datos) and 0 <= columna < len(datos[0]):
                contenido_celda = datos[fila][columna]
                resultado_text.delete("1.0", tk.END)
                resultado_text.insert(tk.END, f"Cadena original: {contenido_celda}")
                etiqueta_aviso.config(text="Archivo seleccionado. Puedes iniciar modificaciones.")
                boton_modificaciones.pack(pady=10)
            else:
                resultado_text.delete("1.0", tk.END)
                resultado_text.insert(tk.END, "Fila o columna fuera de rango.")

    except Exception as e:
        resultado_text.delete("1.0", tk.END)
        resultado_text.insert(tk.END, f"Error al abrir el archivo:\n{str(e)}")

ventana = tk.Tk()
ventana.title("MODIFICACION DE CADENA POR CHUNKS")

etiqueta_autor = tk.Label(ventana, text="Actividad 4 - Emmanuel Martin Marin y Fabian Joheshua Escalante Fernandez")
etiqueta_autor.pack(pady=5)

boton_abrir = tk.Button(ventana, text="Abrir Archivo CSV", command=abrir_archivo)
boton_abrir.pack(pady=10)

etiqueta_aviso = tk.Label(ventana, text="Selecciona un archivo antes de iniciar modificaciones.")
etiqueta_aviso.pack(pady=5)

boton_modificaciones = tk.Button(ventana, text="Iniciar modificaciones", command=iniciar_back)

resultado_text = tk.Text(ventana, width=180, height=40)
resultado_text.pack(pady=10)

archivo_seleccionado = None 

ventana.mainloop()
