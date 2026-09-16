def calcular_media():
    notas = []

    print("--- Sistema de Cálculo de Média ---")
    print("Digite as notas do aluno (ou digite -1 para encerrar):\n")

    while True:
        try:
            entrada = float(input(f"Digite a {len(notas) + 1}ª nota: "))

            if entrada == -1:
                break

            if 0 <= entrada <= 10:
                notas.append(entrada)
            else:
                print("Nota inválida! Digite um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Digite apenas números.")

    if not notas:
        print("\nNenhuma nota foi informada.")
        return

    media = sum(notas) / len(notas)

    print("\n" + "=" * 30)
    print(f"Total de notas inseridas: {len(notas)}")
    print(f"Média final: {media:.2f}")

    if media >= 7.0:
        print("Situação: Aprovado!")
    elif media >= 5.0:
        print("Situação: Recuperação.")
    else:
        print("Situação: Reprovado.")
    print("=" * 30)


# Executa a função
calcular_media()