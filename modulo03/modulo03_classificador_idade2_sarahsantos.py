idade = int(input("Digite a sua idade: "))


if idade < 13:
    print("Você é uma Criança.")
elif idade < 18:
    print("Você é um Adolescente.")
elif idade < 60:
    print("Você é um Adulto.")
else:
    print("Você é um Idoso.")