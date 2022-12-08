import random

matriz = [[random.randint(1, 100) for j in range(5)] for i in range(5)]

def buscar_secuencia(fila_o_columna):
  for i in range(3, len(fila_o_columna)):
    if fila_o_columna[i-3] + 1 == fila_o_columna[i-2] == fila_o_columna[i-1] + 1 == fila_o_columna[i]:
      print("Secuencia encontrada en la posición [{}, {}] hasta la posición [{}, {}]".format(i-3, fila_o_columna[i-3], i, fila_o_columna[i]))

for i in range(5):
  fila = matriz[i]
  buscar_secuencia(fila)

for j in range(5):
  columna = [matriz[i][j] for i in range(5)]
  buscar_secuencia(columna)



