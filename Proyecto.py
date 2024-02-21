import tkinter as tk
from tkinter import filedialog
import csv

def realizar_modificaciones(string, y, seleccion_combinacion):
    chunks = len(string) // y
    modificaciones = []

    seleccion_combinacion = int(seleccion_combinacion)


    indice_combinacion = seleccion_combinacion - 1
    total_combinaciones = 2**chunks

    if 1 <= seleccion_combinacion <= total_combinaciones:
        combinationes = f'{seleccion_combinacion:0{chunks}b}'
        stringModificado = list(string)
        modificacion = f"Combinación {seleccion_combinacion}\n"
        for i, x in enumerate(combinationes):
            indice = i + 1
            if x == '1':
                chunk = string[(indice - 1) * y:indice * y]
                stringModificado.extend(chunk)
                modificacion += f" - Chunk {indice}: {' '.join(chunk)}\n"

        modificacion += f"Secuencia ADN modificada: {' '.join(stringModificado)}\n"
        modificaciones.append(modificacion)
    else:
        modificaciones.append("Combinación seleccionada fuera de rango.")

    return modificaciones

def iniciar_back():
    global archivo_seleccionado
    if not archivo_seleccionado:
        etiqueta_aviso.config(text="Por favor, selecciona un archivo antes de iniciar modificaciones.")
        return

    seleccion_combinacion = entrada_combinacion.get()

    try:
        with open(archivo_seleccionado, 'r') as file:
            lector_csv = csv.reader(file)
            datos = list(lector_csv)

            fila = 1
            columna = 3

            if 0 <= fila < len(datos) and 0 <= columna < len(datos[0]):
                contenido_celda = datos[fila][columna]
                resultado_text.delete("1.0", tk.END)
                resultado_text.insert(tk.END, f"Cadena original: {contenido_celda}\n")
                etiqueta_aviso.config(text="Archivo seleccionado. Puedes iniciar modificaciones.")
                boton_modificaciones.pack(pady=10)

                y = 10
                modificaciones = realizar_modificaciones(list(contenido_celda), y, seleccion_combinacion)

                resultado_text.insert(tk.END, "\n".join(modificaciones))

            else:
                resultado_text.delete("1.0", tk.END)
                resultado_text.insert(tk.END, "Fila o columna fuera de rango.")

    except Exception as e:
        resultado_text.delete("1.0", tk.END)
        resultado_text.insert(tk.END, f"Error al abrir el archivo:\n{str(e)}")

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

etiqueta_instruccion = tk.Label(ventana, text="Introduce el número de la combinación que deseas ver:")
etiqueta_instruccion.pack(pady=5)

entrada_combinacion = tk.Entry(ventana, width=5)
entrada_combinacion.pack(pady=5, padx=10)

boton_modificaciones = tk.Button(ventana, text="Iniciar modificaciones", command=iniciar_back)
boton_modificaciones.pack(pady=10)

resultado_text = tk.Text(ventana, width=180, height=40)
resultado_text.pack(pady=10)

archivo_seleccionado = None

ventana.mainloop()

