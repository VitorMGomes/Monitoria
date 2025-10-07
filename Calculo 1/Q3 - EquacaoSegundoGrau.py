import re
import math

MSG_FORMATO_ERR = "A equação digitada não está no formato solicitado."
MSG_NAO_2GRAU   = "A equação não é uma equação polinomial do 2º grau."
MSG_SEM_RAIZ    = "A equação polinomial do 2º grau não possui raiz real."
MSG_UMA_RAIZ    = "A raiz da equação polinomial do 2º grau é"
MSG_DUAS_RAIZES = "As raízes da equação polinomial do 2º grau são"

# Expressão regular para validar números reais no formato decimal:
# - ^ e $ garantem que toda a string seja verificada (do início ao fim).
# - [+-]? aceita opcionalmente um sinal positivo ou negativo.
# - \d+(\.\d+)? aceita um número inteiro com parte decimal opcional (ex.: 123, 123.45).
# - |\.d+ aceita números sem parte inteira, mas com ponto seguido de decimais (ex.: .5, .123).
# Exemplos válidos: "42", "-3.5", "+0.99", ".75"
# Exemplos inválidos: "3,5", "12..3", ".", "abc"
float_re = re.compile(r'^[+-]?(\d+(\.\d+)?|\.\d+)$')

def _parse_side_quadratic(side: str):
    """
    Converte um lado textual da equação em (A, B, C),
    onde A é o coeficiente de x^2, B de x e C a constante.
    Aceita: 'x^2' ou 'x²', sinal +/-, coeficiente implícito, reais com ponto ou vírgula.
    """
    s = side.strip().lower().replace(",", ".")
    # normalizar x² para x^2
    s = s.replace("x²", "x^2")

    if not s:
        raise ValueError("lado vazio")

    # quebrar por sinais
    s = s.replace("-", "+-")
    if s.startswith("+"):
        s = s[1:]
    terms = [t.strip() for t in s.split("+") if t.strip()]

    A = B = C = 0.0

    for t in terms:
        # Termos com x^2
        if "x^2" in t:
            if t.count("x") != 1 or not t.endswith("x^2"):
                raise ValueError("termo quadrático malformado")
            raw = t[:-3].strip()  # antes de 'x^2'
            if raw in ("", "+"):
                coef = 1.0
            elif raw == "-":
                coef = -1.0
            else:
                if not float_re.match(raw):
                    raise ValueError("coeficiente quadrático inválido")
                coef = float(raw)
            A += coef
        # Termos lineares (x)
        elif "x" in t:
            if t.count("x") != 1 or not t.endswith("x"):
                raise ValueError("termo linear malformado")
            raw = t[:-1].strip()
            if raw in ("", "+"):
                coef = 1.0
            elif raw == "-":
                coef = -1.0
            else:
                if not float_re.match(raw):
                    raise ValueError("coeficiente linear inválido")
                coef = float(raw)
            B += coef
        # Termo constante
        else:
            if not float_re.match(t):
                raise ValueError("constante inválida")
            C += float(t)

    return A, B, C

def resolver_equacao_2grau(expr: str) -> str:
    """
    Resolve Ax^2 + Bx + C = Dx^2 + Ex + F quando possível,
    seguindo as instruções do enunciado.
    """
    if expr.count("=") != 1:
        return MSG_FORMATO_ERR

    left, right = expr.split("=")
    try:
        A, B, C = _parse_side_quadratic(left)
        D, E, F = _parse_side_quadratic(right)
    except ValueError:
        return MSG_FORMATO_ERR

    # a = A - D, b = B - E, c = C - F
    a = A - D
    b = B - E
    c = C - F

    # Se a == 0, não é do 2º grau
    if a == 0:
        return MSG_NAO_2GRAU

    delta = b*b - 4*a*c

    if delta < 0:
        return MSG_SEM_RAIZ

    # delta >= 0 → calcular raízes
    sqrt_delta = math.sqrt(delta)
    x1 = (-b + sqrt_delta) / (2*a)
    x2 = (-b - sqrt_delta) / (2*a)

    if delta == 0:
        # Uma raiz real (x1 == x2)
        return f"{MSG_UMA_RAIZ} x = {x1}"
    else:
        return f"{MSG_DUAS_RAIZES} x1 = {x1} e x2 = {x2}"

if __name__ == "__main__":
    try:
        entrada = input("Digite a equação (ex.: 3 + 4x^2 - x = 2 - x^2 + 5x): ")
    except EOFError:
        entrada = ""
    print(resolver_equacao_2grau(entrada))
