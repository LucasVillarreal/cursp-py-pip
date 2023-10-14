import csv
import matplotlib.pyplot as plt

# Recibimos el archivo de los datos y el pais que seleccionó el usuario
def population_by_country(data, country):
  # Guardamos el resultado 
  # de comparar los paises dentro del archivo
  # en la columna de "Country" con el que seleccionó el usuario
  result = list(filter(lambda item: item['Country'] == country, data))
  # Lo retornamos
  return result

# Recibimos el pais seleccionado
def get_population(country_dic):
  # Creamos la estructura donde vamos a mostrar 
  # los datos de la columna específica que tiene el archivo
  # Creamos una especie de "template" a mostrar
  population_dic = {
    '2022': int(country_dic['2022 Population']),
    '2020': int(country_dic['2020 Population']),
    '2015': int(country_dic['2015 Population']),
    '2010': int(country_dic['2010 Population']),
    '2000': int(country_dic['2000 Population'])
  }
  # Retornamos las llaves (años)
  # y los valores "datos de la columna seleccionada"
  return population_dic.keys(), population_dic.values()

# Recibimos los etiqetas y valores 
# para generar la gráfica
# (vienen del resultado de get_population)
def generate_bar_chart(name, labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f'./app/imgs/{name}.png')
  plt.show()

def generate_pie_chart(name, label, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=label)
  ax.axis('equal')
  plt.savefig(f'./imgs/{name}.png')
  plt.show()

# Fun donde leemos el archivo
def read_csv(path):
  # Método para abrir y cerrar el archivo de forma auto
  # Pasamos la ruta del archivo con la funcion y 
  # con que variable la manejamos
  with open(path, 'r') as csvfile:
    # le pasamos al reader con que se diferencian los datos
    reader = csv.reader(csvfile, delimiter=',')
    # salteamos linea a linea 
    header = next(reader)
    data = []
    # transformamos el resultado para generar un diccionario 
    # para poder manipularla luego
    for fila in reader:
      iterable = zip(header, fila)
      country_dicc = {key: value for key, value in iterable}
      # Almacenamos cada fila de datos dentro de la lista
      data.append(country_dicc)
      # Devolvemos la lista de diccionarios
    return data