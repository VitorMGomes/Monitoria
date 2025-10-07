from fractions import Fraction

EPS = 1e-12

MSG_A_INVALIDO = "Valor inválido: a deve ser positivo e diferente de 1."
MSG_B_INVALIDO = "A equação não possui solução real para b <= 0."
MSG_INT_SOL    = "A equação a^x = b possui solução inteira: x = {x}."
MSG_NO_INT     = "A equação a^x = b não possui solução inteira; a solução está entre {lo} e {hi}."
# Observação: os extremos são inteiros consecutivos.

def parse_num(s: str) -> float:
    """
    Converte string para número:
    - aceita '3.5', '3,5' e frações 'p/q' (ex.: '1/8').
    """
    s = s.strip().replace(",", ".")
    if "/" in s:
        p, q = s.split("/", 1)
        return float(Fraction(p.strip()) / Fraction(q.strip()))
    return float(s)

def divisoes_sucessivas_base_maior_que_1(a: float, b: float):
    """
    Resolve por divisões sucessivas assumindo a > 1 e b > 0.
    Retorna:
      ("int", k)                 se encontrou 1 exatamente após k divisões
      ("intervalo", k-1, k)      se cruzou de >1 para <1 após k divisões
    Observação: k é o número de divisões realizadas.
    """
    if abs(b - 1.0) <= EPS:
        return ("int", 0)

    atual = b
    k = 0
    while atual > 1.0 + EPS:
        atual /= a
        k += 1
        if abs(atual - 1.0) <= EPS:
            return ("int", k)
        if k > 10**6:   # proteção teórica; não deve acontecer
            break
    # Se saiu do laço sem bater 1, cruzou para <1 na última divisão
    return ("intervalo", k-1, k)

def resolver_exponencial(a_in: str, b_in: str) -> str:
    """
    Segue exatamente os casos do enunciado para a^x = b.
    """
    # Parse de entrada (aceita frações e vírgula)
    try:
        a = parse_num(a_in)
        b = parse_num(b_in)
    except Exception:
        return "Entrada inválida: não foi possível interpretar a ou b."

    # Validações iniciais
    if a <= 0 or abs(a - 1.0) <= EPS:
        return MSG_A_INVALIDO
    if b <= 0:
        return MSG_B_INVALIDO

    # CASO 1: a > 1
    if a > 1.0:
        if b > 1.0 + EPS:
            tipo, *dados = divisoes_sucessivas_base_maior_que_1(a, b)
            if tipo == "int":
                k = dados[0]
                return MSG_INT_SOL.format(x=k)
            else:
                lo, hi = dados
                return MSG_NO_INT.format(lo=lo, hi=hi)

        elif abs(b - 1.0) <= EPS:
            return MSG_INT_SOL.format(x=0)

        else:  # 0 < b < 1  → resposta negativa; usa B = 1/b e inverte o sinal
            B = 1.0 / b
            tipo, *dados = divisoes_sucessivas_base_maior_que_1(a, B)
            if tipo == "int":
                k = dados[0]
                return MSG_INT_SOL.format(x=-k)
            else:
                lo, hi = dados
                # intervalo negativo correspondente: (-hi, -lo)
                return MSG_NO_INT.format(lo=-hi, hi=-lo)

    # CASO 2: 0 < a < 1
    else:
        # Use A = 1/a > 1 e resolva A^y = b; depois x = -y.
        A = 1.0 / a
        if b > 1.0 + EPS:
            tipo, *dados = divisoes_sucessivas_base_maior_que_1(A, b)
            if tipo == "int":
                k = dados[0]
                return MSG_INT_SOL.format(x=-k)  # troca o sinal
            else:
                lo, hi = dados   # y ∈ (lo, hi) positivos → x ∈ (-hi, -lo)
                return MSG_NO_INT.format(lo=-hi, hi=-lo)

        elif abs(b - 1.0) <= EPS:
            return MSG_INT_SOL.format(x=0)

        else:  # 0 < b < 1 → y negativo → x positivo
            B = 1.0 / b  # B > 1
            tipo, *dados = divisoes_sucessivas_base_maior_que_1(A, B)
            if tipo == "int":
                k = dados[0]
                return MSG_INT_SOL.format(x=+k)  # y = -k ⇒ x = k
            else:
                lo, hi = dados   # y ∈ (-hi, -(lo)) → x ∈ (lo, hi)
                return MSG_NO_INT.format(lo=lo, hi=hi)

if __name__ == "__main__":
    print("Verificador de a^x = b (entre inteiros)")
    a_str = input("Digite a (ex.: 2, 0.5, 3/2): ")
    b_str = input("Digite b (ex.: 9, 1/8, 7): ")
    print(resolver_exponencial(a_str, b_str))
