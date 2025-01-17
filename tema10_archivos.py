from io import open

texto="Una linea con texto\notra linea de texto"

fichero = open('fichero.txt', 'w')
fichero.write(texto)


cadena = "\nEsto es otra cadena"
fichero.write(cadena)
fichero.close()