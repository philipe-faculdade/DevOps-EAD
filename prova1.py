# Campo da tabela
# Nome | Slaário | Anos | Av posiitva?
funcionarios = [['Ana', 3500.00, 5, True],
                ['Bia', 2450.00, 3, False],
                ['Clô', 6700.50, 10, False],
                ['Duda', 1212.00, 1, True],
                ['Elen', 5000.00, 2, True]]

investimento = 0

for funcionario in funcionarios:
    aumento = 0.10 * funcionario[2]
    funcionario[2] += aumento
    investimento += aumento
    if funcionario[3]:
        funcionario.append(0.50 * funcionario[2] * funcionario[1])
    investimento += funcionario[5]

print(f'Investimento: R$ {investimento:.2f}')
