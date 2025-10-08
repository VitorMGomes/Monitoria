import math

EPS = 1e-12  # tolerância para testar "zero"

def f(x: float) -> float:
    # f(x) = 2^x + x^2 - 4
    return math.pow(2.0, x) + x*x - 4.0

def sinal_str(y: float) -> str:
    if abs(y) <= EPS:
        return "= 0"
    return "< 0" if y < 0 else "> 0"

def main():
    # Entrada: precisão em casas decimais (inteiro >= 1)
    try:
        n = int(input("Deseja estimar a raiz da equação com precisão de quantas casas decimais? "))
    except ValueError:
        print("A entrada deve ser um número inteiro, maior ou igual a 1. Se não atender a esse critério, não funciona.")
        return

    if n < 1:
        print("A entrada deve ser um número inteiro, maior ou igual a 1. Se não atender a esse critério, não funciona.")
        return

    # No código, definir dois números reais: a = 0 e b = 3
    a = 0.0
    b = 3.0

    # Calcula f(a) e f(b)
    fa = f(a)
    fb = f(b)

    # Testar o mesmo que no código anterior
    print(f"f({a}) {sinal_str(fa)}")
    print(f"f({b}) {sinal_str(fb)}")

    # Se ocorrer um dos três primeiros casos, acabou.
    if abs(fa) <= EPS and abs(fb) <= EPS:
        print("a é uma raiz da equação.")
        print("b é uma raiz da equação.")
        return
    if abs(fa) <= EPS:
        print("a é uma raiz da equação.")
        return
    if abs(fb) <= EPS:
        print("b é uma raiz da equação.")
        return
    if fa * fb > 0:
        print("Não tem raiz no intervalo [0, 3] (f(a)·f(b) > 0).")
        return

    # Se f(a)·f(b) < 0, vai procurar a raiz (bisseção)
    prev_mid = None
    alvo = 10.0 ** (-n)

    while True:
        c = (a + b) / 2.0
        fc = f(c)
        print(f"Ponto médio {c}")
        print(f"f({c}) {sinal_str(fc)}")

        # Se f(c) = 0, retornar que c é a raiz da equação
        if abs(fc) <= EPS:
            print(f"{c} é a raiz da equação.")
            return

        # Precisamos identificar em qual intervalo estará a raiz
        if fa * fc < 0:
            print(f"Raiz entre {a} e {c}")
            b = c
            fb = fc
        else:
            print(f"Raiz entre {c} e {b}")
            a = c
            fa = fc

        # Critério de parada: diferença entre pontos médios consecutivos
        if prev_mid is not None:
            if abs(c - prev_mid) < alvo:
                print(f"Aproximação da raiz (precisão {n} casas decimais): {c:.{n}f}")
                return
        prev_mid = c

if __name__ == "__main__":
    main()
