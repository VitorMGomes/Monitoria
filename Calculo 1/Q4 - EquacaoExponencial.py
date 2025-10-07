from fractions import Fraction

EPS = 1e-12  # tolerância para floats

def parse_num(s: str) -> float:
    """Aceita '3.5', '3,5' e frações 'p/q' (ex.: '1/8')."""
    s = s.strip().replace(",", ".")
    if "/" in s:
        p, q = s.split("/", 1)
        return float(Fraction(p.strip()) / Fraction(q.strip()))
    return float(s)

def ler_num(rotulo: str) -> float:
    while True:
        try:
            return parse_num(input(f"{rotulo}: "))
        except Exception:
            print("Entrada inválida.")

def solve_divisoes(A: float, T: float):
    """
    Resolve A^y = T por divisões sucessivas assumindo A > 1 e T > 1.
    Retorna:
      ("int", k)           se T chega exatamente a 1 após k divisões
      ("intervalo", lo, hi)  onde lo,hi são inteiros consecutivos com y ∈ (lo,hi)
    """
    if abs(T - 1.0) <= EPS:
        return ("int", 0)

    k = 0
    cur = T
    while cur > 1.0 + EPS:
        cur /= A
        k += 1
        if abs(cur - 1.0) <= EPS:
            return ("int", k)
        if k > 10**7:  # proteção teórica
            break
    return ("intervalo", k-1, k)

def fmt_int(n):
    return str(int(n))

def main():
    print("Resolver a^x = b (entradas a, b)")
    a = ler_num("a (ex.: 2, 0.5, 3/2)")
    b = ler_num("b (ex.: 9, 1/8, 7)")

    # validações básicas
    if a <= 0 or abs(a - 1.0) <= EPS:
        print("a deve ser positivo e diferente de 1.")
        return
    if b <= 0:
        print("b deve ser positivo (b > 0).")
        return

    if abs(b - 1.0) <= EPS:
        print("x = 0")
        return

    # Mapeamos todos os casos para resolver A^y = T com A>1 e T>1
    # e depois recuperamos x a partir de y.
    if a > 1.0:
        if b > 1.0:
            A, T, s = a, b, +1   # x = +y
        else:  # 0 < b < 1
            A, T, s = a, 1.0/b, -1  # x = -y
    else:  # 0 < a < 1
        if b > 1.0:
            A, T, s = 1.0/a, b, -1  # x = -y
        else:  # 0 < b < 1
            A, T, s = 1.0/a, 1.0/b, +1  # x = +y

    tipo, *dados = solve_divisoes(A, T)

    if tipo == "int":
        k = dados[0]
        x = s * k
        print(f"x = {fmt_int(x)}")
    else:
        lo, hi = dados  # y ∈ (lo, hi)
        # converter intervalo de y para x = s*y
        x1 = s * lo
        x2 = s * hi
        esquerda, direita = (min(x1, x2), max(x1, x2))
        print(f"x entre {fmt_int(esquerda)} e {fmt_int(direita)}")

if __name__ == "__main__":
    main()
