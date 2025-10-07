import math

EPS = 1e-12  # tolerância numérica

def fmt(x: float) -> str:
    """Formata evitando -0.0 e com até 10 dígitos significativos."""
    if abs(x) < EPS:
        x = 0.0
    return f"{x:.10g}"

def _parse_coef(s: str, allow_x2: bool = False, allow_x: bool = False) -> float:
    """
    Converte a entrada em número:
      - sempre aceita números com ponto ou vírgula (ex.: 3.5, 3,5)
      - se allow_x2=True: aceita 'x^2', '+x^2', '-x^2', '5x^2', '5,2x^2' (e 'x²')
      - se allow_x=True : aceita 'x', '+x', '-x', '5x', '5,2x'
    """
    s = s.strip().lower().replace(" ", "").replace(",", ".").replace("x²", "x^2")

    # prioridade: tentar x^2 primeiro
    if allow_x2 and s.endswith("x^2"):
        coef = s[:-3]
        if coef in ("", "+"):
            return 1.0
        if coef == "-":
            return -1.0
        return float(coef)

    # depois termo linear 'x'
    if allow_x and s.endswith("x"):
        coef = s[:-1]
        if coef in ("", "+"):
            return 1.0
        if coef == "-":
            return -1.0
        return float(coef)

    # se ainda contiver 'x' aqui, é inválido para esse campo
    if "x" in s:
        raise ValueError("símbolo 'x' não permitido aqui")

    return float(s)

def ler_coef(rotulo: str, *, allow_x2: bool = False, allow_x: bool = False) -> float:
    while True:
        try:
            return _parse_coef(input(f"{rotulo}: "), allow_x2=allow_x2, allow_x=allow_x)
        except Exception:
            print("Entrada inválida.")

def main():
    print("Resolver Ax^2 + Bx + C = Dx^2 + Ex + F (entradas A, B, C, D, E, F)")
    # A, B, C, D, E, F
    A = ler_coef("A (ex.: x^2, -x^2, 5x^2 ou número)", allow_x2=True)
    B = ler_coef("B (ex.: x, -x, 5x ou número)", allow_x=True)
    C = ler_coef("C (número)")
    D = ler_coef("D (ex.: x^2, -x^2, 5x^2 ou número)", allow_x2=True)
    E = ler_coef("E (ex.: x, -x, 5x ou número)", allow_x=True)
    F = ler_coef("F (número)")

    # reduzir para ax^2 + bx + c = 0
    a = A - D
    b = B - E
    c = C - F

    # checagem de grau
    if abs(a) <= EPS:
        print("Não é equação do 2º grau (a = 0).")
        return

    delta = b*b - 4*a*c

    if delta < -EPS:
        print("Sem raízes reais.")
        return

    # delta >= 0
    sqrt_delta = math.sqrt(max(delta, 0.0))
    x1 = (-b + sqrt_delta) / (2*a)
    x2 = (-b - sqrt_delta) / (2*a)

    if abs(delta) <= EPS:
        print(f"x = {fmt(x1)}")
    else:
        print(f"x1 = {fmt(x1)}, x2 = {fmt(x2)}")

if __name__ == "__main__":
    main()
