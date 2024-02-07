import pandas as pd
data = pd.read_csv('/content/dataset.csv')
print(data)

string = list(data["string_a_modificar"][0])
posicion = list(data["posicion"])
referencia = list(data["referencia"])
alteracion = list(data["alteracion"])

print(string)
n = 0
y = 5
for x in range(5, 20):
  for i in posicion:
    if string.index(string[x]) == i:
      string[i] = referencia[posicion.index(i)]

n = n + 3
y = y + 3

print(string)
