# 05. Equações Logarítmicas
# Determinar todos os números (na base 10) que podem ser escritos com k dígitos na base b.

b = int(input("Base numérica b (natural >= 2): "))
k = int(input("Número de dígitos k (natural >= 1): "))

# validações simples
if b < 2:
    print("A base não atende (precisa ser natural e >= 2).")
elif k < 1:
    print("O número de dígitos não atende (precisa ser natural e >= 1).")
else:
    # extremos do intervalo: b^(k-1) <= n <= b^k - 1
    low  = b**(k - 1)
    high = b**k - 1
    print(f"Todos os n naturais em [{low}, {high}] podem ser escritos com {k} dígitos na base {b}.")

    mostrar = input("Quer a lista? (0 pra não, 1 pra sim): ")
    if mostrar == "1":
        for n in range(low, high + 1):
            print(n)
