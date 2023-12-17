extrato = []

def sacar(saldo, qtde):
    valor = float(input('Informe o valor do saque: '))
    if valor > 500:
        print('Valor maximo por operacao é R$ 500.00')
    elif valor < 0:
        print('Valor inválido')
    elif qtde > 0:
        extrato.append(f'Saque de R$ {valor}')
        saldo -= valor
        qtde -= 1
    else:
        print('Limite de saques esgotados \n')
    return saldo


def depositar(saldo):
    valor = float(input('Informe o valor do depósito: '))
    if valor <= 0 :
        print('Valor inválido!')
        return saldo
    else:
        extrato.append(f'Depósito de R$ {valor}')
        return saldo + valor 


def menu():
    qtde_saques = 3
    saldo = 0
    print('Bem vindo ao Banco xpto!')
    while True:
        print('O que deseja fazer? \n')
        opcao = input(f'OPÇÕES: \n "d" = Depositar \n "s" = Sacar \n "e" = Extrato \n "q" = Sair \n => ').lower()
        
        if opcao == 'd':
            saldo = depositar(saldo)
        elif opcao == 's':
                saldo = sacar(saldo, qtde_saques)                
        elif opcao == 'e':
            for i in extrato:
                print(i)
            print(f'R$ {saldo}', end='\n')
        elif opcao == 'q':
            break
        else:
            print('Opção inválida \n')

menu()
