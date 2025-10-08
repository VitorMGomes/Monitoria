# Equação de 1º grau: a x + b = c x + d
# Entrada passo a passo: A, B, C, D
# Agora A e C podem ser digitados como "5x", "-x", "x" (interpreta 1x e -1x).
# Saídas:
#  - Se A == C → "A equação não é uma equação polinomial do 1º grau."
#  - Caso contrário → "A raiz da equação polinomial do 1º grau é x = ..."

EPS = 1e-12

def resolver_1grau():
    print("Resolver Ax + B = Cx + D")
    a = float(input("A"))
    b = float(input("B"))
    c = float(input("C"))
    d = float(input("D"))

    if abs(a - c) <= 0:
        print("A equação não é uma equação polinomial do 1º grau.")
        return

    a = a - c 
    b = b - d 
    x = -b / a
    print(f"A raiz da equação polinomial do 1º grau é x = {x}")

if __name__ == "__main__":
    resolver_1grau()
