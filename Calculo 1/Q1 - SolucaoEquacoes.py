import math

EPS = 1e-9  # tolerância numérica para comparar com zero

def parse_real(s: str) -> float:
    """Aceita 3,14 ou 3.14 e converte para float."""
    return float(s.strip().replace(",", "."))

# --- defina aqui as equações (lado esquerdo - lado direito) ---
def f1(x: float) -> float:
    # Eq. 1: x^4 - 4x^3 - x^2 + 16x - 12 = 0
    return x**4 - 4*x**3 - x**2 + 16*x - 12

def f2(x: float) -> float:
    # Eq. 2: 2^x = 64  ->  2^x - 64 = 0
    return (2.0**x) - 64.0

def f3(x: float) -> float:
    # Eq. 3 (assumida): x^2 = 16  ->  x^2 - 16 = 0
    # Se a sua eq. 3 for, por exemplo, sqrt(x) = 16, use: return math.sqrt(x) - 16
    return x*x - 16.0
# --------------------------------------------------------------

def eh_solucao(func, x: float, eps: float = EPS) -> bool:
    return abs(func(x)) <= eps

def main():
    print("Caso queira testar uma função f3 diferente, mude-a no código")
    print("Escolha a equação para testar:")
    print("  1) x^4 - 4x^3 - x^2 + 16x - 12 = 0")
    print("  2) 2^x = 64")
    print("  3) x^2 = 16")
    op = input("Digite 1, 2 ou 3: ").strip()

    try:
        x = parse_real(input("Digite o valor de x: "))
    except Exception:
        print("Entrada inválida para x.")
        return

    if op == "1":
        ok = eh_solucao(f1, x)
        idx = "(1)"
    elif op == "2":
        ok = eh_solucao(f2, x)
        idx = "(2)"
    elif op == "3":
        ok = eh_solucao(f3, x)
        idx = "(3)"
    else:
        print("Opção inválida.")
        return

    if ok:
        print(f"x = {x} é solução da equação {idx}.")
    else:
        print(f"x = {x} não é solução da equação {idx}.")

if __name__ == "__main__":
    main()
