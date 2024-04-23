import re

def validar_telefone(telefone):
    padrao = r'\(\d{2}\) 9\d{4}-\d{4}'
    if re.fullmatch(padrao, telefone):
        return 'Número de telefone válido.'
    else:
        return 'Número de telefone inválido.'

print(validar_telefone('(88) 98888-8888'))  # Saída: Número de telefone válido.
print(validar_telefone('(11)91111-1111'))  # Saída: Número de telefone inválido.
print(validar_telefone('225555-555'))  # Saída: Número de telefone inválido.
print ('result')