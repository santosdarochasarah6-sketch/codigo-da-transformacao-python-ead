'''
Isso é um bloco de comentários.
>>projeto açaíteria:

>PO:(como dono do negócio: Quero um sistema de vendas para minha açaíteria, 
para que eu possa disponibilizar meus produtos virtualmente.)

>QA:(como cliente: (quero um sistema para que eu possa comprar os produtos com mais qualidade
e praticidade.)

>Tech:(como programador: (quero um sistema de vendas para minha açaíteria,
para que eu possa desenvolver um software eficiente e funcional paro negocio.)

>DEV:(como programador:(quero um sistema de vendas para minha açaíteria,
para que eu possa implementar funcionalidades necessárias para
atender as necessiddades do negócio w dos clientes.)

>UX:(como designer de experiencia do usuario:(quero um sistema de vendas para minha açaíteria,
para que eu possa criar uma interface instituitiva e agradavél para usuario,
garantindo uma experiencia de compras satisfatoria.)

>IA:(como analista de dados:(quero um sistema de vendas para a minha açaíteria,
par)a que eu possa coletar e analisar os dados de acesso do usuário,
identificando os erros e aprimorando  o sis)
'''
while True:
    print('bem-vindo ao projeto de desenvolvimento de um sistema de vendas para açaiteria')
    print('1 -cadastrar produto')
    print('2 -listar produtos')
    print('3 -selecionar produto')
    print('4 -cadastrar pagamento')
    print('5 -comfirmar compra')
    print('0 - sair')
    print('\n-------------------------------------------------------------------------\n')

    opcao = input('digite a opção desejada:')

    if opcao == '1':
        print('opção 1-cadastrando produto...\n') 
        p1_nome = input('digite o nome do produto: ')
        p1_descricao = input('descrição dp produto desejado:')
        p1_validade = input('validade do produto:')
        p1_estoque = int(input('digite o numero de produtos:'))

    elif opcao == '2':
        print('opção 2-listando produto...\n')
        p2_nome = input('digite o nome do produto: ')
        p2_descricao = input('descrição dp produto desejado:')
        p2_validade = input('validade do produto:')
        p2_estoque = int(input('digite o numero de produtos:'))

    elif opcao == '3':
        print('opção 3-selecionando pagamento...\n')
        p3_nome = input('digite o nome do produto: ')
        p3_descricao = input('descrição dp produto desejado:')
        p3_validade = input('validade do produto:')
        p3_estoque = int(input('digite o numero de produtos:'))
        p3_preco = float(input('digite preço desejado do produto:'))
        
    elif opcao == '4':
        print('opção 4-cadastrar pagamento...\n')
        cadastrar_pagamento = input('cadastrar forma de pagamento:')
    elif opcao == '5':
        print('opção 5-comfirmando compra...\n')
        confirmar_compra = input('confirmar compra:')
    elif opcao == '0':
        print('opção 0-saindo...')
    else:
        print('opção inválida.')


'''
Um Bloco de Comentarios. 
Para explicar o que o código faz, ou para deixar anotações para o programador.
>>projeto açaiteria:

>PO (Como dono do negocio: Quero um sistema de vendas para minha açaiteria, 
para que eu possa controlar as vendas e os produtos.)

>QA (Como cliente: Quero um sistema de vendas para minha açaiteria,
para que eu possa comprar meus produtos favoritos de forma rápida e fácil.)

>Tech (Como programador: Quero um sistema de vendas para minha açaiteria,
para que eu possa desenvolver um software eficiente e funcional para o negócio.)

>Dev (Como programador: Quero um sistema de vendas para minha açaiteria,
para que eu possa implementar as funcionalidades necessárias para 
atender as necessidades do negócio e dos clientes.)

>UX (Como designer de experiência do usuário: Quero um sistema de 
vendas para minha açaiteria,para que eu possa criar uma 
interface intuitiva e agradável para os usuários, 
garantindo uma experiência de compra satisfatória.)

>IA (Como analista de dados: Quero um sistema de vendas para minha 
açaiteria, para que eu possa coletar e analisar os dados de vendas, 
ajudando a identificar padrões de consumo e otimizar as 
estratégias de marketing e estoque.)


Ciclo de vida do projeto:
1. Planejamento: Definir os requisitos do sistema, identificar as necessidades do negócio e dos clientes, 
e criar um plano de desenvolvimento.
2. Análise: Analisar os requisitos e criar um modelo de dados e um design de sistema.
3. Desenvolvimento: Escrever o código para implementar as funcionalidades do sistema.
4. Testes: Testar o sistema para garantir que ele funcione corretamente e atenda aos requisitos.
5. Implantação: Implantar o sistema em um ambiente de produção e garantir que ele esteja funcionando 
corretamente.
6. Manutenção: Realizar manutenção contínua para corrigir bugs, adicionar novas funcionalidades e garantir 
que o sistema continue atendendo às necessidades do negócio e dos clientes.

>>Criar um aplicativo, sistema em CLI - Command Line Interface, ou seja, um sistema que funcione no terminal, sem interface gráfica.
>>Complementar e implementar o app / sistema em GUI - Graphical User Interface, ou seja, um sistema com interface gráfica, 
para que os usuários possam interagir de forma mais intuitiva e agradável.

'''
# Inicializando as variáveis para o Produto 1 (vazio)
p1_nome = "açaí comum"
p1_estoque = 100
p1_preco = 8.90
p1_validade = "10/12/2026"
p1_descricao = "Açaí comum, ideal para quem gosta de um sabor clássico."

# Inicializando as variáveis para o Produto 2 (vazio)
p2_nome = "açaí premium"
p2_estoque = 90
p2_preco = 19.99
p2_validade = "10/10/2026"
p2_descricao = "Açaí premium, uma experiência marcante e única com melhor qualidade."

# Inicializando as variáveis para o Produto 3 (vazio)
p3_nome = "açaí personalizavél"
p3_estoque = 130
p3_preco = 15.90
p3_validade = "10/12/2026"
p3_descricao = "Açaí personalizavél, personalize do seu jeito."

p4_nome = "açaí light"
p4_estoque = 95
p4_preco = 23.90
p4_validade = "05/12/2026"
p4_descricao = "Açaí light, sem açúcar e derivados glutinosos."


p5_nome = "barca de açaí"
p5_estoque = 123
p5_preco = 30.90
p5_validade = "08/12/2026"
p5_descricao = "barca de açaí, com varios tipos de frutas e acompanhamentos recheados."


# Isso é um comentário de linha única.

while True: 
    print('-' * 48 + '\n')
    print('Bem-vindo ao Sistema de vendas - açaiteria!\n')
    print('1 - Cadastrar produto')
    print('2 - Listar produtos')
    print('3 - Realizar venda')
    print('0 - Sair')
    print('\n--------------------------------------\n')

    opcao = input('Digite a opção desejada: ')

    if opcao == '1':
        print('Cadastrando produtos...\n')
    # faça a lógica para cadastrar o produto aqui, 
    ## e somente a inseção dos dados usando input e os tipos de dados.
        if p1_nome == "":
            p1_nome = input('Digite o nome do produto:açaí comum ')
            p1_estoque = int(input('Digite a quantidade em estoque:100'))
            p1_preco = float(input('Digite o preço do produto:8.90 '))
            p1_validade = input('Digite a validade do produto:10/12/2026')    
            p1_descricao = input('Digite a descrição do produto:Açaí comum, ideal para quem gosta de um sabor clássico.')
            print(f'\n🎉 Produto "{p1_nome}" cadastrado na vaga 1!')           
        elif p2_nome == "":
                p2_nome = input('Digite o nome do produto:açaí premium')
                p2_estoque = int(input('Digite a quantidade em estoque:90'))
                p2_preco = float(input('Digite o preço do produto:19.99'))
                p2_validade = input('Digite a validade do produto:10/10/2026')    
                p2_descricao = input('Digite a descrição do produto:Açaí premium, uma experiência marcante e única com melhor qualidade')
                print(f'\n🎉 Produto "{p2_nome}" cadastrado na vaga 2!')      
        elif p3_nome == "":
            p3_nome = input('Digite o nome do produto:açaí personalizavél')
            p3_estoque = int(input('Digite a quantidade em estoque:130'))
            p3_preco = float(input('Digite o preço do produto:15.90'))
            p3_validade = input('Digite a validade do produto:10/12/2026')    
            p3_descricao = input('Digite a descrição do produto:Açaí personalizavél, personalize do seu jeito.')
            print(f'\n🎉 Produto "{p3_nome}" cadastrado na vaga 3!')

        elif p4_nome == "":
            p4_nome = input('Digite o nome do produto:açaí light')
            p4_estoque = int(input('Digite a quantidade em estoque:95'))
            p4_preco = float(input('Digite o preço do produto:23.90'))
            p4_validade = input('Digite a validade do produto:05/12/2026')    
            p4_descricao = input('Digite a descrição do produto:Açaí light, sem açúcar e derivados glutinosos.')
            print(f'\n🎉 Produto "{p4_nome}" cadastrado na vaga 4!')

        elif p5_nome == "":
            p5_nome = input('Digite o nome do produto:barca de açaí')
            p5_estoque = int(input('Digite a quantidade em estoque:123'))
            p5_preco = float(input('Digite o preço do produto:30.90'))
            p5_validade = input('Digite a validade do produto:08/12/2026')    
            p5_descricao = input('Digite a descrição do produto:barca de açaí, com varios tipos de frutas' \
            'e acompanhamentos recheados.')
            print(f'\n🎉 Produto "{p5_nome}" cadastrado na vaga 5!')
            
            
        else:
            print('❌ Sistema cheio! Limite de 3 produtos atingido.')

    elif opcao == '2':
        print('Listando produtos...')

        if p1_nome == "açaí comum" and p2_nome == "açaí premium" and p3_nome == "açaí personalizavél":

            print('Nenhum produto cadastrado no sistema ainda.')

        else:
            # Mostra o Produto 1 se ele existir
            if p1_nome != "açaí comum":
                print(f"Nome:açaí comum {p1_nome} | Preço:8.90 R$ {p1_preco:.2f} | Estoque:100 {p1_estoque} unid.")

                print(f"Validade:10/12/2026 {p1_validade} | Descrição:açaí comum, ideal para quem gosta de um sabor classico {p1_descricao}")

                print('🔥' * 30)
                
            # Mostra o Produto 2 se ele existir
            if p2_nome != "açaí premium":

                print(f"Nome:açaí premium {p2_nome} | Preço:19.99 R$ {p2_preco:.2f} | Estoque:90 {p2_estoque} unid.")

                print(f"Validade:10/10/2026 {p2_validade} | Descrição:açaí premium, uma experiência marcante e única com melhor qualidade {p2_descricao}")

                print('🔥' * 30)
                
            # Mostra o Produto 3 se ele existir
            if p3_nome != "":

                print(f"Nome: {p3_nome} | Preço: R$ {p3_preco:.2f} | Estoque: {p3_estoque} unid.")

                print(f"Validade: {p3_validade} | Descrição: {p3_descricao}")

                print('🔥' * 30)

            if p4_nome != "":

                print(f"Nome: {p4_nome} | Preço: R$ {p4_preco:.2f} | Estoque: {p4_estoque} unid.")

                print(f"Validade: {p4validade} | Descrição: {p4_descricao}")

                print('🔥' * 30)

            if p5_nome != "":

                print(f"Nome: {p5_nome} | Preço: R$ {p5_preco:.2f} | Estoque: {p5_estoque} unid.")

                print(f"Validade: {p5_validade} | Descrição: {p5_descricao}")

                print('🔥' * 30)


    elif opcao == '3':
        print('Realizando venda...')

        if p1_nome == "" and p2_nome == "" and p3_nome == "":
            print(f'Não há produtos cadastrados para realizar vendas.')
        else:
            nome_venda = input('Digite o nome do produto que deseja vender: ')
            
            # Testamos o nome digitado contra o Produto 1
            if nome_venda.lower() == p1_nome.lower() and p1_nome != "":
                qtd_venda = int(input(f"Quantas unidades de '{p1_nome}' deseja vender? "))
                if qtd_venda <= p1_estoque:
                    p1_estoque -= qtd_venda
                    total = qtd_venda * p1_preco
                    print(f'\n✅ Venda realizada! Total: R$ {total:.2f}')
                    print(f'Estoque atual de {p1_nome}: {p1_estoque} unidades.')
                else:
                    print(f'❌ Estoque insuficiente! Temos apenas {p1_estoque}.')
            
            # Testamos contra o Produto 2
            elif nome_venda.lower() == p2_nome.lower() and p2_nome != "":
                qtd_venda = int(input(f"Quantas unidades de '{p2_nome}' deseja vender? "))
                if qtd_venda <= p2_estoque:
                    p2_estoque -= qtd_venda
                    total = qtd_venda * p2_preco
                    print(f'\n✅ Venda realizada! Total: R$ {total:.2f}')
                    print(f'Estoque atual de {p2_nome}: {p2_estoque} unidades.')
                else:
                    print(f'❌ Estoque insuficiente! Temos apenas {p2_estoque}.')
                    
            # Testamos contra o Produto 3
            elif nome_venda.lower() == p3_nome.lower() and p3_nome != "":
                qtd_venda = int(input(f"Quantas unidades de '{p3_nome}' deseja vender? "))
                if qtd_venda <= p3_estoque:
                    p3_estoque -= qtd_venda
                    total = qtd_venda * p3_preco
                    print(f'\n✅ Venda realizada! Total: R$ {total:.2f}')
                    print(f'Estoque atual de {p3_nome}: {p3_estoque} unidades.')
                else:
                    print(f'❌ Estoque insuficiente! Temos apenas {p3_estoque}.')
            
            else:
                print('🔥 Erro: Produto não encontrado!')

    elif opcao == '0':
        print('Saindo...')
        break
    else:
        print('Opção inválida!')
