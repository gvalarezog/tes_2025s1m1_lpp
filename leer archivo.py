try:
    archivo = None
    archivo = open('archivo1.txt', 'r') #w write r read a append
    for linea in archivo.readlines():
        print(linea)
    archivo.close()

except FileNotFoundError as e:
    print("Error: Archivo no existe")
except PermissionError as e:
    print("Error: Permisos denegados")
except Exception as e:
    print("Error en abrir el archivo.")
finally:
    if archivo:
        archivo.close()