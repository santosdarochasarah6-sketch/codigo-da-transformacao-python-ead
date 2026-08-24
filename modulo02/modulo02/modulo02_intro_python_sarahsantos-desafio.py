from datetime import datetime

nome = input("Por favor, digite o seu nome: ")
print("💛💙💛💙 DESAFIO EXTRA: SAUDAÇÃO + HORA ATUAL 💛💙💛💙")

agora = datetime.now()
hora_formatada = agora.strftime("%H:%M")
nome = input("Digite o seu nome: ")

print(f"Olá, {nome}! Agora são {hora_formatada}. Tenha um excelente momento de estudos!")
hora_atual = datetime.now().strftime("%H:%M")

print(f"Oi, {nome}! Agora são exatamente {hora_atual}. Seja bem-vindo!")