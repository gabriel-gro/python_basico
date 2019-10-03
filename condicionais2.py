# Condicionais simples: sistema venda papelaria

if __name__ == "__main__":
    custo_caneta = 1.50
    custo_caderno = 8.50
    custo_borracha = 6.0
    custo_regua = 2.0
    custo_papelA4 = 31.0
    custo_lapis = 0.5
    custo_portaLapis = 18.0


    qtd_caneta = int(input())
    qtd_caderno = int(input())
    qtd_borracha = int(input())
    qtd_regua = int(input())
    qtd_papelA4 = int(input())
    qtd_lapis = int(input())
    qtd_portaLapis = int(input())
    
    tipoPagamento = input()

    totalCompra = qtd_caneta * custo_caneta 
    totalCompra += qtd_caderno * custo_caderno 
    totalCompra += qtd_borracha * custo_borracha 
    totalCompra += qtd_regua * custo_regua 
    totalCompra += qtd_papelA4 * custo_papelA4 
    totalCompra += qtd_lapis * custo_lapis
    totalCompra += qtd_portaLapis * custo_portaLapis

    totalPagar = totalCompra
    if tipoPagamento == 'd':
        totalPagar *= 0.85
    elif tipoPagamento == 'c':
        totalPagar *= 0.90
    
    print(totalPagar)