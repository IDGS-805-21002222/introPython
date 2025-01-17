from io import open

fichero=open('fichero.txt', 'r')
texto1=fichero.readlines()
print(texto1)
print(type(texto1))
fichero.close()


