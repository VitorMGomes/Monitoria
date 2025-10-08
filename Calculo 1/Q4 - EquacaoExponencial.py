EPS = 1e-12  # tolerância

a = float(input("a: "))
b = float(input("b: "))

if a <= 0 or abs(a - 1.0) <= EPS or b <= 0:
    print("Entrada inválida.")
elif abs(b - 1.0) <= EPS:
    print("x = 0")
else:
    # CASO 1: a > 1 e b > 1  → x = y, dividindo b por a até chegar em 1
    if a > 1.0 and b > 1.0:
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
            print(f"x = {k}")
        else:
            print(f"x entre {k-1} e {k}")

    # CASO 2: a > 1 e 0 < b < 1  → x = -y, resolvendo a^y = 1/b
    elif a > 1.0 and b < 1.0:
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
            print(f"x = {-k}")
        else:
            print(f"x entre {-k} e {-(k-1)}")

    # CASO 3: 0 < a < 1 e b > 1  → x = -y, resolvendo (1/a)^y = b
    elif a < 1.0 and b > 1.0:
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
            print(f"x = {-k}")
        else:
            print(f"x entre {-k} e {-(k-1)}")

    # CASO 4: 0 < a < 1 e 0 < b < 1  → x = y, resolvendo (1/a)^y = 1/b
    else:
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
            print(f"x = {k}")
        else:
            print(f"x entre {k-1} e {k}")
