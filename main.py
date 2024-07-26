import numpy as np


def getAscciValue(char):
    #Aqui se convierten el mensaje en numeros del 1 al 27
    if char == ' ':
        return 27
    if 'A' <= char <= 'Z':
        return ord(char) - ord('A') + 1
    raise ValueError("El mensaje solo puede contener letras mayúsculas y espacios.")

def numberToChar(num):
    #Aqui convierte los numeros del 1 al 27 en letras
    if num == 27:
        return ' '

    return chr((num - 1)  + ord('A'))


def messageToMatrix(message, key_length):
    #Aqui se crea la matriz del mensaje
    numbers = [getAscciValue(char) for char in message]
    # Rellenar con 27 si no es múltiplo de key_length
    while len(numbers) % key_length != 0:
        numbers.append(27)
    matrix = np.array(numbers).reshape(-1, key_length)
    return matrix


def keyToMatrix(key):
    #Convertimos la llave ingresada en una matriz
    key_numbers = [int(num) for num in key.split()]
    size = int(len(key_numbers) ** 0.5)
    if size ** 2 != len(key_numbers):
        raise ValueError("La longitud de la llave debe formar una matriz cuadrada.")
    matrix = np.array(key_numbers).reshape(size, size)
    return matrix



def main():
    try:
        message = input("Ingresa el mensaje: ")
        if not message:
            raise ValueError("El mensaje no puede estar vacío.")
        key = input(
            "Ingresa la llave numeros separados por espacios, la suficiente cantidad de numeros para formar una matriz cuadrada")
        if not key:
            raise ValueError("La llave no puede estar vacía.")

        keyMatrix = keyToMatrix(key)
        if np.linalg.det(keyMatrix) == 0:
            raise ValueError("La matriz de la llave no es invertible.")
        keyLength = keyMatrix.shape[0]
        messageMatrix = messageToMatrix(message, keyLength)
        print("\n Matriz del mensaje:")
        print(messageMatrix)
        print("\n Matriz de la llave:")
        print(keyMatrix)
        resultMatrix = np.dot(messageMatrix, keyMatrix)
        print("\n Matriz resultante de la multiplicación del mensaje y la llave:")
        print(resultMatrix)
        inverseKeyMatrix = np.linalg.inv(keyMatrix)
        print("\n Matriz inversa de la llave:")
        print(inverseKeyMatrix)
        decodedMatrix = np.dot(resultMatrix, inverseKeyMatrix)
        decodedMatrix = np.round(decodedMatrix).astype(int)
        print("\n Matriz resultante de la multiplicación de la matriz resultante ebtre la llave ye el mesnsaje  con la inversa de la llave:")
        print(decodedMatrix)
        decodedMessage = ''.join(numberToChar(num) for num in decodedMatrix.flatten())
        print("\nMensaje decodificado:")
        print(decodedMessage)

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")


if __name__ == "__main__":
    main()