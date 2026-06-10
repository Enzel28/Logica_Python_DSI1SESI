for pacote in range(0, 9 + 1, 1):
    print("Quanto pesa o pacote?")
    pacote = float(input())
    if pacote == 2:
        print("Pacote classificado como Leve")
        custo = 10.0
        print("Custo Fixo: R$10,00 ")
    else:
        if pacote >= 2 and pacote < 10:
            print("Pacote Classificado como Padrão ")
            custo = 20.0
            print("Custo fixo: R$20,00 ")
        else:
            if pacote >= 10 and pacote < 100:
                print("Pacote classificado como Pesado ")
                custo = 30.0
            else:
                print("Peso Indevido ")
    print("Pacote está com destino internacional? ")
    internacional = input()
    if internacional == "sim":
        print("Será aplicado um acréscimo de 20% sobre o valor do pacote ")
        custo = custo + custo * 0.2
    else:
        print("Não séra aplicado nenhum acréscimo sobre o valor final. ")
print("========== RESULTADO FINAL ========== > Total de pacotes: 10 .Carga total acumulada: 45.5 kg .Faturamento bruto do lote: R$ 240.00 .Ticket médio por pacote: R$ 24.00 ====================================")
