import re

def validar_numero_telefone(numero):
    # Expressão regular para validar o formato de telefone brasileiro
    padrao = re.compile(r"^\(\d{2}\) \d{5}-\d{4}$")
    return padrao.match(numero) is not None

# Exemplo de uso
numero_teste = "(48) 91234-5678"
if validar_numero_telefone(numero_teste):
    print(f"O número {numero_teste} está no formato correto.")
else:
    print(f"O número {numero_teste} está no formato incorreto.")
