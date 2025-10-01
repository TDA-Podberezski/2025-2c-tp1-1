import sys

def formar_escenario(cadena: str) -> str:
    # TODO: implementar algoritmo
    return cadena

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("uso: escenario.py <cadena>")
        sys.exit(1)

    entrada = sys.argv[1]
    resultado = formar_escenario(entrada)
    print(resultado)
