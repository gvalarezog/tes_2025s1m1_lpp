
try:
    archivo = open('archivo.txt', 'a') #w write r read a append
    archivo.write("Hola desde un archivo\n")
    archivo.write("Agregar otra linea\n")
    archivo.write("Otra linea\n")
    archivo.close()
except FileNotFoundError as e:
    print("Error: Archivo no existe")
except PermissionError as e:
    print("Error: Permisos denegados")
except Exception as e:
    print("Error en abrir el archivo.")
finally:
    archivo.close()