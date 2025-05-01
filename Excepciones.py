
try:
    numerador = int(input("Introduce un numerador: "))
    denominador = int(input("Introduce un denominador: "))
    resultado = numerador / denominador
    print(resultado)

except ZeroDivisionError as e:
    print("Error: División para cero.")
except ValueError as e:
    print("Error: El número ingresado no corresponde a un entero.")
except Exception as e:
    print(f'Error: Se produjo un error genérico: {e}')
else:
    print('No produjo error mi codigo')
finally:
    print('Codigo que siempre se ejecuta')

print(f'El programa sigue corriendo')

