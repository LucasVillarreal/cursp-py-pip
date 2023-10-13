import utils

if __name__ == '__main__':
  # Almacenamos la ruta del archivo con los datos
  data = utils.read_csv('./app/data.csv')
  
  # Preguntamos al usuario que ingrese un país
  response = int(input("¿Qué quieres?\n1- Seleccionar 1 país\n2- Graficar un porcentaje?\n"))
  if response == 1:
    country = input("Ingresa el país: ")
    result = utils.population_by_country(data, country.capitalize())
    
    if len(result) > 0:
  #   # Almacenamos en una variable lo que trae
      country = result[0]
  #   # Llamamos a la fun dentro de utils pasandole el pais resultante con sus datos
      keys, values = utils.get_population(country)
  #   # print(country)
  #   # Generamos el gráfico de barras
      graph = input("Lanzar gráfica de barras? Si o No\n")
      if graph.lower() == 'si':
        utils.generate_bar_chart(country['Country'], keys, values)
  #   else:
  #     graph = input("Lanzar gráfica de torta? Si o No\n")
  elif response == 2:
    countries = list(map(lambda item: item['Country'], data))
    percentage = list(map(lambda item: item['Area (km²)'], data))
    
    utils.generate_pie_chart('area', countries, percentage)

    
  
  # Llamamos a la fun dentro de utils pasando los datos y el pais
  # result = utils.population_by_country(data, country.capitalize())

  # # Comprobamos que result contenga datos
  # if len(result) > 0:
  #   # Almacenamos en una variable lo que trae
  #   country = result[0]
  #   # Llamamos a la fun dentro de utils pasandole el pais resultante con sus datos
  #   keys, values = utils.get_population(country)
  #   # print(country)
  #   # Generamos el gráfico de barras
  #   graph = input("Lanzar gráfica de barras? Si o No\n")
  #   if graph.lower() == 'si':
  #     utils.generate_bar_chart(keys, values)
  #   else:
  #     graph = input("Lanzar gráfica de torta? Si o No\n")
      
