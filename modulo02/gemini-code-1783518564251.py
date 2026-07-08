import datetime

# ====================================================
# 1. CABEÇALHO DO SISTEMA
# ====================================================
print("🍇" + "=" * 50 + "🍇")
print("             💜 AÇAÍTERIA SUPREMO 💜             ")
print("          O sabor da energia no seu dia!         ")
print("🍇" + "=" * 50 + "🍇\n")

# ====================================================
# 2. ATIVIDADE 3 & DESAFIO: INTERAÇÃO E DATA/HORA
# ====================================================
nome_cliente = input("Para começarmos o seu atendimento, qual é o seu nome? ")

agora = datetime.datetime.now()
hora_pedido = agora.strftime("%H:%M")

print("\n" + "-" * 52)
print(f"Olá, {nome_cliente}! Que bom ter você por aqui! 🎉")
print(f"Seu atendimento foi iniciado às: {hora_pedido}")
print("-" * 52 + "\n")

# ====================================================
# 3. CONTRÔLE DE FLUXO (MENU DE PRODUTOS)
# ====================================================
print("--- CARDÁPIO DE TAMANHOS ---")
print("[1] Açaí Pequeno (300ml) - R$ 15,00")
print("[2] Açaí Médio (500ml)   - R$ 22,00")
print("[3] Açaí Grande (700ml)  - R$ 30,00")
print("[0] Cancelar e Sair")
print("-" * 28)

opcao = input("Digite o número do tamanho desejado: ")

# Validação das opções digitadas pelo usuário
if opcao == "1":
    print("\n✅ Perfeito! Você escolheu o Açaí Pequeno (300ml).")
    print("Agora é só escolher os adicionais no balcão! 🍓🍌")
elif opcao == "2":
    print("\n✅ Ótima escolha! Você escolheu o Açaí Médio (500ml).")
    print("Agora é só escolher os adicionais no balcão! 🍓🍌")
elif opcao == "3":
    print("\n✅ Respeitou o tamanho da fome! Açaí Grande (700ml) saindo.")
    print("Agora é só escolher os adicionais no balcão! 🍓🍌")
elif opcao == "0":
    print("\nSaindo do sistema... Atendimento encerrado. Volte sempre! 👋")
else:
    print("\n🔥 Erro: Produto não encontrado! Por favor, digite uma opção válida.")

print("\n🚀 Obrigado por usar o sistema da Açaiteria Supremo!")