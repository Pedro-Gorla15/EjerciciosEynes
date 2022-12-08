import random

def generar_lista_diccionarios():
  lista = []
  for i in range(10):
    diccionario = {"id": i, "edad": random.randint(1, 100)}
    lista.append(diccionario)
  return lista


def ordenar_lista(lista):
  lista_ordenada = sorted(lista, key=lambda x: x["edad"], reverse=True)
  print("La persona más joven tiene id:", lista_ordenada[-1]["id"])
  print("La persona más vieja tiene id:", lista_ordenada[0]["id"])
  return lista_ordenada


lista = generar_lista_diccionarios()
print(lista)

lista_ordenada = ordenar_lista(lista)
print(lista_ordenada)






