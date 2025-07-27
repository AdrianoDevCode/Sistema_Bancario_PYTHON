saque_máximo = 500
saque_diario = 3
saldo = 1550
numero_saque_diario = 0
transacoes = []




while True:
    print("""
    Bem-vindo ao Banco!
    Opções disponíveis:
    -------------------
    |   0 - saque     | 
    |   1 - depósito  |
    |   2 - extrato   |
    |   3 - sair      |
    -------------------        
    """)

    operação = input('Escolha uma opção: ')
    if operação not in ('0', '1', '2', '3'):
        print('Opção inválida. Tente novamente.')

        
    elif operação == '0':
        if numero_saque_diario >= saque_diario:
            print('Limite diário de saques atingido.')
            continue
        print('Saque selecionado. Concluindo operação...')
        while True:
            valor_saque = float(input('Digite o valor do saque: '))
            if valor_saque <= 0 or valor_saque > saque_máximo:
                print('O valor do saque deve ser maior que 0 e menor ou igual a 500.')
            elif valor_saque > saldo:
                print('Saldo insuficiente.')
                break
            else:
                  saldo -= valor_saque 
                  numero_saque_diario += 1
                  transacoes.append(f'Saque: -R${valor_saque:.2f}')
                  print(f'Você sacou R${valor_saque:.2f}. Saldo atual: R${saldo:.2f}.')
                  break
      
    elif operação == '1':    
        print('Depósito selecionado. Concluindo operação...')      
        while True:
            deposito = float(input('Digite o valor do depósito: '))
            if deposito < 0:
                print('O valor do depósito deve ser maior que 0.')
            elif deposito == 0:
                print('Operação de depósito cancelada.')
                break
            else:
                saldo += deposito
                transacoes.append(f"Depósito: +R${deposito:.2f}")
                print(f'Depósito realizado com sucesso! Seu saldo atual é de R${saldo:.2f}.')
                break

    elif operação == '2':
        print('Extrato selecionado. Concluindo operação...')
        print(f'Número de saques realizados hoje: {numero_saque_diario}')
        print(f'Número de saques restantes para hoje: {saque_diario - numero_saque_diario}')
        print(f'Saldo atual: R${saldo:.2f}')     
        

        if not transacoes:
            print("Nenhuma movimentação realizada.")
        else:
            for t in transacoes:
                print(t)    
                

    elif operação == '3':
        print('Encerrando o sistema. Obrigado por usar o banco!')
        break


            
            