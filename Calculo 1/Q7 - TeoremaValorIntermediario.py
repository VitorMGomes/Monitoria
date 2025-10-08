import math

EPS = 1e-9  # tolerância para comparar com zero

def f(x: float) -> float:
    # f(x) = x * ln(x^2 + 1) - x^2 + 4
    return x * math.log(x*x + 1.0) - x*x + 4.0

def eh_zero(y: float) -> bool:
    return abs(y) <= EPS

def fmt(v: float) -> str:
    # Formata de modo compacto e evita -0
    if abs(v) < EPS:
        v = 0.0
    return f"{v:.10g}"

a = float(input("Digite a: "))
b = float(input("Digite b: "))

fa = f(a)
fb = f(b)

low = min(a, b)
high = max(a, b)

# Segue exatamente as regras do enunciado:
if eh_zero(fa) and eh_zero(fb):
    print("a é uma raiz da função.")
    print("b é uma raiz da função.")
elif eh_zero(fa):
    print("a é uma raiz da função.")
elif eh_zero(fb):
    print("b é uma raiz da função.")
else:
    produto = fa * fb
    if produto < 0:
        print(f"existe uma raiz de f entre {fmt(low)} e {fmt(high)}.")
    else:  # produto > 0
        print(f"não é possível afirmar se existe ou não raiz de f entre {fmt(low)} e {fmt(high)}.")
