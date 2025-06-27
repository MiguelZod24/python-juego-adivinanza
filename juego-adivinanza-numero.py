import random

def juego_adivinanza():
    # Generar un numero del 1 al 100
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    # Primeras lineas del juego donde se da la bienvenida
    print("¡Bienvenido al juego de adivinanza del número!")
    print("¡Debes adivinar el número entre el 1 y el 100!")
    print("¡Intenta adivinarlo!")

    while not adivinado:
        # Solicitar un numero del 1 al 100
        adivinanza = input("Introduzca un número del 1 al 100: ")

        # Verificar que la entrada sea un número
        if adivinanza.isdigit():
            adivinanza = int(adivinanza)  # Lo pasamos de texto a entero
            intentos += 1

            if adivinanza < numero_secreto:
                print(f"El número secreto es mayor a {adivinanza}")
            elif adivinanza > numero_secreto:
                print(f"El número secreto es menor a {adivinanza}")
            else:
                print(f"¡Felicitaciones has ganado! El número {adivinanza} es el secreto y lo has logrado en {intentos} intentos")
                adivinado = True
        else:
            print("Por favor introduzca un número válido del 1 al 100")

# Llamar a la función para iniciar el juego
juego_adivinanza()

    