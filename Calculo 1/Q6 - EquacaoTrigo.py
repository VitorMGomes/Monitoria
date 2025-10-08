import math
EPS = 1e-12

x = float(input("Digite x: "))

if x < -1 - EPS or x > 1 + EPS:
    print(f"A equação cos(θ) = {x} não possui solução no intervalo [0, 2π].")
elif abs(x - 1.0) <= EPS:
    print("A única solução de cos(θ) = 1 no intervalo [0, 2π] é θ = 0.")
elif abs(x + 1.0) <= EPS:
    print(f"A única solução de cos(θ) = -1 no intervalo [0, 2π] é θ = {math.pi}.")
else:
    x = min(1.0, max(-1.0, x))         # garante [-1,1]
    t1 = math.acos(x)                   # ∈ [0, π]
    t2 = 2*math.pi - t1
    print(f"A equação cos(θ) = {x} possui duas soluções no intervalo [0, 2π]:")
    print(f"θ = {t1} ou θ = {t2}")
