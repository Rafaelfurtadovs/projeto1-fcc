

import numpy as np

def calculate(list_of_numbers):
    if len(list_of_numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    # Transforma a lista em um 3x3
    matrix = np.array(list_of_numbers).reshape(3, 3)

    # Calcula as estatisticas
    calculations = {
        'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean().tolist()],
        'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var().tolist()],
        'standard deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std().tolist()],
        'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max().tolist()],
        'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min().tolist()],
        'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum().tolist()]
    }

    return calculations

#define o resultado
resultado = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
print(resultado)