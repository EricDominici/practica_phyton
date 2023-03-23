def mover_vector(vector):
    # Imprime el vector original
    print("Vector original:", vector)
    
    # Guarda el último elemento del vector
    ultimo = vector[-1]
    
    # Mueve cada elemento del vector a la posición siguiente
    for i in range(len(vector)-1, 0, -1):
        vector[i] = vector[i-1]
    
    # Coloca el último elemento en la primera posición
    vector[0] = ultimo
    
    # Imprime el vector final
    print("Vector final:", vector)

# Ejemplo de uso                
vector = [1, 2, 3, 4, 5]
mover_vector(vector)

    
        