import modules.tools

derivees_usuelles: dict[str, str] = {"k": "0", "k * x": "k", "x^n": "nx^(n-1)", "x^(1/2)": "1 / (2x^(1/2))",
                                     "1 / x": "-1 / (x^2)", "sin(x)": "cos(x)", "cos(x)": "-sin(x)",
                                     "ln(x)": "1 / x", "e^x": "e^x"}

derivees_fonctions: dict[str, str] = {"k * u": "k * u'", "u + v": "u' + v'", "u * v": "u'v + uv'",
                                      "u / v": "(u'v - uv') / v^2", "1 / u": "-u' / u^2", "k / u": "-ku' / u^2",
                                      "u^n": "nu'u^(n-1)", "sin(u)": "u'cos(u)", "cos(u)": "-u'sin(u)",
                                      "ln(u)": "u' / u", "e^u": "u'e^u"}


def main() -> None:
    variable = input("Entrez le nom de la variable : ")
    function = input(f"Entrez la fonction à dériver : f({variable})=")


def function_slicer():
    sliced_function = []
