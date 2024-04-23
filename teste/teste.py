def recomendar_plano(consumo):
    if consumo <= 10:
        return 'Plano Essencial Fibra - 50Mbps'
    elif consumo > 10 and consumo <= 20:
        return 'Plano Prata Fibra - 100Mbps'
    else:
        return 'Plano Premium Fibra - 300Mbps'
print(recomendar_plano(10))  # Saída: Plano Essencial Fibra - 50Mbps
print(recomendar_plano(19))  # Saída: Plano Prata Fibra - 100Mbps
print(recomendar_plano(21))  # Saída: Plano Premium Fibra - 300Mbps
