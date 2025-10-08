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
