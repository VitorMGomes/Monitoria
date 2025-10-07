import re

MSG_FORMATO_ERR = "A equação digitada não está no formato solicitado."
MSG_NAO_1GRAU   = "A equação não é uma equação polinomial do 1º grau."
MSG_RAIZ        = "A raiz da equação polinomial do 1º grau é"

# Expressão regular para validar números reais no formato decimal:
# - ^ e $ garantem que toda a string seja verificada (do início ao fim).
# - [+-]? aceita opcionalmente um sinal positivo ou negativo.
# - \d+(\.\d+)? aceita um número inteiro com parte decimal opcional (ex.: 123, 123.45).
# - |\.d+ aceita números sem parte inteira, mas com ponto seguido de decimais (ex.: .5, .123).
# Exemplos válidos: "42", "-3.5", "+0.99", ".75"
# Exemplos inválidos: "3,5", "12..3", ".", "abc"
float_re = re.compile(r'^[+-]?(\d+(\.\d+)?|\.\d+)$')


def _parse_side(side: str):
    """
    Converte um lado textual da equação em (coef_x, constante).
    Aceita: números reais (., ,), 'x' (ou 'X'), sinais +/-, espaços.
    Retorna (coef_x, const) ou levanta ValueError para formato inválido.
    """
    s = side.strip().lower().replace("x", "x").replace(",", ".")
    if not s:
        raise ValueError("lado vazio")

    # Normaliza: transforma '-' em '+-' e divide em termos por '+'
    # Ex.: "2 - x + 3.5" -> "2 +- x + 3.5" -> ["2", "- x", "3.5"]
    s = s.replace("-", "+-")
    if s.startswith("+"):
        s = s[1:]
    terms = [t.strip() for t in s.split("+") if t.strip()]

    coef_x = 0.0
    const  = 0.0

    for t in terms:
        if "x" in t:
            # Termo com x; não deve haver nada depois de 'x'
            if t.count("x") != 1 or not t.endswith("x"):
                raise ValueError("termo com x malformado")
            raw_coef = t[:-1].strip()
            if raw_coef in ("", "+"):
                c = 1.0
            elif raw_coef == "-":
                c = -1.0
            else:
                if not float_re.match(raw_coef):
                    raise ValueError("coeficiente inválido")
                c = float(raw_coef)
            coef_x += c
        else:
            # Termo constante
            if not float_re.match(t):
                raise ValueError("constante inválida")
            const += float(t)

    return coef_x, const


def resolver_equacao(expr: str) -> str:
    """
    Resolve ax + b = cx + d quando possível.
    Retorna mensagens conforme o enunciado.
    """
    if expr.count("=") != 1:
        return MSG_FORMATO_ERR

    left, right = expr.split("=")
    try:
        a, b = _parse_side(left)
        c, d = _parse_side(right)
    except ValueError:
        return MSG_FORMATO_ERR

    # Verificação do 1º grau conforme a regra dada
    if a == c:
        return MSG_NAO_1GRAU

    x = (d - b) / (a - c)
    return f"{MSG_RAIZ} x = {x}"


if __name__ == "__main__":
    try:
        entrada = input("Digite a equação (ex.: 3 + 4x = 2 - x): ")
    except EOFError:
        entrada = ""
    print(resolver_equacao(entrada))
