import csv


dados = [
    ["Nome", "Idade", "Departamento", "Salario"],
    ["Ana Silva", 28, "TI", 7500.00],
    ["Carlos Oliveira", 35, "Marketing", 6200.00],
    ["Mariana Santos", 22, "RH", 4800.00],
    ["Pedro Souza", 40, "Financeiro", 8900.00],
    ["Beatriz Lima", 31, "Vendas", 5500.00],
]


with open(
    "funcionarios.csv", mode="w", newline="", encoding="utf-8-sig"
) as arquivo:
    escritor = csv.writer(arquivo, delimiter=",")
    escritor.writerows(dados)

print("Arquivo CSV criado com sucesso!")