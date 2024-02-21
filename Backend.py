import pandas as pd

data = pd.read_csv('/content/dataset.csv')
print(data)

string = list(data["string_a_modificar"][0])
posicion = list(data["posicion"])
referencia = list(data["referencia"])
alteracion = list(data["alteracion"])

y = 10
chunks = len(string) // y


for acumuladorChunks in range(1, chunks + 2): 
    for b in range(1, 2**acumuladorChunks): 
        stringModificado = list(string)  
        combinationes = f'{b:0{acumuladorChunks}b}' 
        
        print(f"Combinación {b}")
        for i, x in enumerate(combinationes):  
            indice = i + 1  
            if x == '1': 
                stringModificado.extend(string[(indice - 1) * y:indice * y])
                print(f" - Chunk {indice}")
                
        print(f"Secuencia ADN modificada: {' '.join(stringModificado)}\n")
