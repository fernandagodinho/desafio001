import re
from unittest import result



def validate_numero_telefone_telefone(phone_number):
    pattern = r'\(\d{2}\) 9\d{4}-\d{4})'
    def is_dir (patch):
        if re.match(pattern, phone_number):
            return 'Número de telefone válido.'
        else:
            return 'Número de telefone inválido.'
        phone_number = input()
    result= validate_numero_telefone_telefone(phone_number)

print(result)