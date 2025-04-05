"""Semana_01_E1.ipynb

Automatically generated by Colab.

Original file is located at

## Ejercicio 1:
### Saludo Personalizado con Error de Concatenación (2 errores)
### Objetivo:
Imprimir un saludo personalizado.
### Código con errores:
"""

nombre = "Usuario"
    print("Hola, " + nombre . "¡Bienvenido!")

"""## Pistas:
- La concatenación de cadenas en Python utiliza un operador específico.
- Presta atención a la sintaxis al unir la variable "nombre" con el resto de la - cadena.
- Recuerda que los strings deben ir entre comillas.

##################################################################################################

---

## Ejercicio 02:
### Impresión con Separador Incorrecto (2 errores)
### Objetivo:
Imprimir una lista de elementos separados por comas.
### Código con errores:
"""

elementos = ["manzana", "banana", "cereza"]
    print(elementos[0] elementos[1] elementos[2] sep="-")

"""## Pistas:
- El argumento "sep" debe ser utilizado correctamente dentro de la función print.
- Revisa la sintaxis de como se separan los elementos al ser impresos.
- Revisa que el uso de los "," sea el correcto entre los elementos de la lista.

##################################################################################################

## Ejercicio 3:
### Formato de f-string con Error de Sintaxis (2 errores)

### Objetivo:
Imprimir una oración usando f-strings.
### Código con errores:
"""

nombre = "Python"
    version = 3.9
    print(f"El lenguaje {nombre} tiene la version {version}")

"""### Pistas:
- Los f-strings tienen una sintaxis específica para insertar variables.
- Recuerda colocar un punto al final de la oración.
- Los "f strings" requiere de un formato especifico cuando se hace llamado de las variables.

##################################################################################################

## Ejercicio 4: Tabla con Error de Tabulación (1 error)

### Objetivo:
Imprimir una tabla con tabulaciones para alinear las columnas.
### Código con errores:
"""

print("Nombre Edad Ciudad")
    print("---- ---- ------")
    print("Ana 25 Madrid")
    print("Carlos 30 Barcelona")
    print("Sofía 22 Sevilla")

"""### Pistas:
- La alineación de columnas requiere un carácter de escape específico para tabulaciones.
- Existe un caracter especial para realizar las tabulaciones.
- Verifica que la separacion de los datos en la tabla sea constante.

##################################################################################################

## Ejercicio 5: Formato con Alineación Incorrecta (1 error)

### Objetivo:
Imprimir datos con alineación y ancho específico usando .format().
### Código con errores:
"""

print("{:10} {:10} {:10}".format("Nombre", "Edad", "Ciudad"))
    print("{:10} {:10} {:10}".format("Ana", "25", "Madrid"))
    print("{:10} {:10} {:10}".format("Carlos", "30", "Barcelona"))
    print("{:10} {:10} {:10}".format("Sofia", "22", "Sevilla"))

"""### Pistas:
- La alineación a la derecha en el metodo format utiliza un caracter especial.
- Verifica que la información se encuentre alineada a la derecha.
revisa el formateo de los datos en la tabla.
"""