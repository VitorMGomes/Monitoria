# Equação de 1º grau: a x + b = c x + d
# Entrada passo a passo: A, B, C, D
# Agora A e C podem ser digitados como "5x", "-x", "x" (interpreta 1x e -1x).
# Saídas:
#  - Se A == C → "A equação não é uma equação polinomial do 1º grau."
#  - Caso contrário → "A raiz da equação polinomial do 1º grau é x = ..."

EPS = 1e-12

def ler_real(rotulo: str, allow_x: bool = False) -> float:
    """
    Lê um número real (aceita vírgula/ponto). Se allow_x=True, aceita também:
      "x"  ->  1.0
      "+x" ->  1.0
      "-x" -> -1.0
      "5x" ->  5.0   (também aceita "5.2x" / "5,2x")
    """
    while True:
        s_raw = input(f"Digite {rotulo}: ")
        s = s_raw.strip().lower().replace(" ", "").replace(",", ".")
        try:
            if allow_x and s.endswith("x"):
                coef = s[:-1]  # tudo antes do 'x'
                if coef in ("", "+"):
                    return 1.0
                if coef == "-":
                    return -1.0
                return float(coef)
            if "x" in s:
                # 'x' não é permitido quando allow_x=False
                raise ValueError
            return float(s)
        except ValueError:
            if allow_x:
                print("Entrada inválida. Use números (ex.: 3,5) ou anexe 'x' (ex.: 5x, -x, x).")
            else:
                print("Entrada inválida. Use apenas números (ex.: 3,5 ou 3.5).")

def fmt(x: float) -> str:
    """Formata número evitando -0.0 e com até 10 dígitos significativos."""
    if abs(x) < EPS:
        x = 0.0
    return f"{x:.10g}"

def resolver_1grau():
    print("Resolver a x + b = c x + d")
    a = ler_real("A (pode usar 5x, -x, x)", allow_x=True)
    b = ler_real("B")
    c = ler_real("C (pode usar 5x, -x, x)", allow_x=True)
    d = ler_real("D")

    if abs(a - c) <= EPS:
        print("A equação não é uma equação polinomial do 1º grau.")
        return

    a = a - c 
    b = b - d 
    x = -b / a
    print(f"A raiz da equação polinomial do 1º grau é x = {fmt(x)}")

if __name__ == "__main__":
    resolver_1grau()
