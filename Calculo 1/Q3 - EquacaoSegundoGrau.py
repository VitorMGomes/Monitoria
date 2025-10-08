import math

EPS = 1e-12  # tolerância numérica

def fmt(x: float) -> str:
    """Formata evitando -0.0 e com até 10 dígitos significativos."""
    if abs(x) < EPS:
        x = 0.0
    return f"{x:.10g}"

def main():
    print("Resolver Ax^2 + Bx + C = Dx^2 + Ex + F (entradas A, B, C, D, E, F -> sempre numeros inteiros ou float com '.' como separacao)")
    # A, B, C, D, E, F
    A = float(input("Digite o valor de A: "))
    B = float(input("Digite o valor de B: "))
    C = float(input("Digite o valor de C: "))
    D = float(input("Digite o valor de D: "))
    E = float(input("Digite o valor de E: ")) 
    F = float(input("Digite o valor de F: "))

    # reduzir para ax^2 + bx + c = 0
    a = A - D
    b = B - E
    c = C - F

    # checagem de grau
    if abs(a) == 0:
        print("Não é equação do 2º grau (a = 0)")
        return

    delta = b*b - 4*a*c

    if delta < 0:
        print("Sem raízes reais")
        return
    else:    
        sqrt_delta = math.sqrt(max(delta, 0.0))
        x1 = (-b + sqrt_delta) / (2*a)
        x2 = (-b - sqrt_delta) / (2*a)

    if abs(delta) <= 0:
        print(f"x = {fmt(x1)}")
    else:
        print(f"x1 = {fmt(x1)}, x2 = {fmt(x2)}")

if __name__ == "__main__":
    main()
