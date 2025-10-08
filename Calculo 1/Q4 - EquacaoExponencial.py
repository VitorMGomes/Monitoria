EPS = 1e-12  # tolerância numérica


def resolver_a_maior_b_maior(a: float, b: float) -> str:
    """Caso 1: a > 1 e b > 1"""
    cur = b
    k = 0
    achou = False
    while cur > 1.0 + EPS:
        cur = cur / a
        k = k + 1
        if abs(cur - 1.0) <= EPS:
            achou = True
            break
    if achou:
        return f"x = {k}"
    else:
        return f"x entre {k-1} e {k}"


def resolver_a_maior_b_menor(a: float, b: float) -> str:
    """Caso 2: a > 1 e 0 < b < 1"""
    cur = 1.0 / b
    k = 0
    achou = False
    while cur > 1.0 + EPS:
        cur = cur / a
        k = k + 1
        if abs(cur - 1.0) <= EPS:
            achou = True
            break
    if achou:
        return f"x = {-k}"
    else:
        return f"x entre {-k} e {-(k-1)}"


def resolver_a_menor_b_maior(a: float, b: float) -> str:
    """Caso 3: 0 < a < 1 e b > 1"""
    base = 1.0 / a
    cur = b
    k = 0
    achou = False
    while cur > 1.0 + EPS:
        cur = cur / base
        k = k + 1
        if abs(cur - 1.0) <= EPS:
            achou = True
            break
    if achou:
        return f"x = {-k}"
    else:
        return f"x entre {-k} e {-(k-1)}"


def resolver_a_menor_b_menor(a: float, b: float) -> str:
    """Caso 4: 0 < a < 1 e 0 < b < 1"""
    base = 1.0 / a
    cur = 1.0 / b
    k = 0
    achou = False
    while cur > 1.0 + EPS:
        cur = cur / base
        k = k + 1
        if abs(cur - 1.0) <= EPS:
            achou = True
            break
    if achou:
        return f"x = {k}"
    else:
        return f"x entre {k-1} e {k}"


def main():
    print("Equação exponencial para A^x = B, sendo A e B > 0")
    a = float(input("Digite a: "))
    b = float(input("Digite b: "))

    if a <= 0 or b <= 0:
        print("Entrada inválida.")
    elif abs(b - 1.0) <= 0:
        print("x = 0")
    elif a > 1.0 and b > 1.0:
        print(resolver_a_maior_b_maior(a, b))
    elif a > 1.0 and b < 1.0:
        print(resolver_a_maior_b_menor(a, b))
    elif a < 1.0 and b > 1.0:
        print(resolver_a_menor_b_maior(a, b))
    else:  # a < 1 e b < 1
        print(resolver_a_menor_b_menor(a, b))


if __name__ == "__main__":
    main()
