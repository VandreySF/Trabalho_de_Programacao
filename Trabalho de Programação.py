# Criamos a variável "continuar_usando" com "SIM" para iniciar o while loop.
continuar_usando = "SIM"

# Aqui o while verifica se a variável "continuar_usando" é "SIM" para fazer o loop.
while continuar_usando == "SIM":

# Mostramos as opções de operação com PRINT o 1 como Adição, o 2 como subtração, o 3 como multiplicação e logo depois o 4 como divisão.
    print("Escolha uma operação:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

# Com o INPUT Perguntamos qual das opções o usuário deseja e guardamos essa informação em "operacao".
    operacao = input("Digite sua opção : ")

# Aqui pedimos para o usuário inserir os valores 1 e 2 e armazenamos eles na variável "valor1" e "valor2".
# O float é usado para transformar o número inserido em decimal para se caso o usuário queira fazer uma conta quebrada.
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))

# O IF e os ELIF verifica se a variável "operacao" é 1, 2, 3 ou 4 para fazer o cálculo, armazenamos os resultados na variável "resultado".
# Logo depois usamos o PRINT para mostrar o resultado do cálculo.
    if operacao == "1":
        resultado = valor1 + valor2
        print("Resultado: ", resultado)
    elif operacao == "2":
        resultado = valor1 - valor2
        print("Resultado: ", resultado)
    elif operacao == "3":
        resultado = valor1 * valor2
        print("Resultado: ", resultado)
    elif operacao == "4":
        resultado = valor1 / valor2
        print("Resultado: ", resultado)

# O ELSE serve para se caso a variável "operacao" não for 1, 2, 3 ou 4 e mostra "Opção inválida" com PRINT.
    else:
        print("Opção inválida!")

# Perguntamos ao usuário se ele quer continuar usando a calculadora com SIM ou NÃO modificamos a variável "continuar_usando" com INPUT.
    continuar_usando = input("Deseja continuar usando a calculadora? (SIM/NÃO): ")