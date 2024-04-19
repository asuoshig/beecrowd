# A fórmula para calcular o volume é: (4/3) * pi * R^3. Considere (atribua) para pi o valor 3.14159.

# Dica: Use (4/3.0) ou (4.0/3) em sua fórmula, porque algumas linguagens (incluindo C++) assumem que o resultado da divisão entre dois inteiros é outro inteiro. :)

# Entrada
# A entrada contém um valor de ponto flutuante (dupla precisão).

# Saída
# A saída deve ser uma mensagem "VOLUME" como o exemplo a seguir com um espaço antes e depois do sinal de igual. O valor deve ser apresentado com 3 dígitos após o ponto decimal.


import math

raio = float(input())

volume = (4/3) * math.pi * pow(raio, 3)

print("VOLUME = %0.3f"%volume)
