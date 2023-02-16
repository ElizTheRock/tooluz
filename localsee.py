import os

# Obtener información IP con comando IFCONFIG
network_info = os.popen("ifconfig").read()

# dividir resultados en lineas
network_info = network_info.split("\n")

# Crear una lista con los equipos conectados
connected_machines_list = []

# Bucle para recorrer resultados obtenidos 
for info in network_info:
  # Generar una sublista con cada "ip" detectada
  words_list = info.split(" ")
  # Recorrer sublista
  for word in words_list: 
    # Chequear si hay alguna palabra con una ip
    if len(word.split(".")) == 4:
      # agregar a lista de equipos conectados
      connected_machines_list.append(word)

# Mostrar lista equipos conectados
print("Equipos conectados a la red: ")
for machine in connected_machines_list:
    print(machine)
