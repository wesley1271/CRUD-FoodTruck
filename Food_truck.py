# Food Truck Virtual - CRUD de Pedidos
try:
    file_name = 'pedidos.txt'
    arquivo = open(file_name, 'r', encoding='utf-8')
    linhas = arquivo.readlines()
    arquivo.close()
    if linhas:
        ultima_linha = linhas[-1].strip()  
        partes = ultima_linha.split(",") 
        ultimo_id = int(partes[0])       
    else:
        ultimo_id = 0

    id_pedido = ultimo_id + 1
    while True:
        print("="*40)
        print(f"""\nBEM VINDO AO NOSSO FOOD TRUCK VIRTUAL!      
            
    Escolha uma das opões para fazer seu pedido:
    1 - Adicionar pedido e nome;
    2 - Ver carrinho;
    3 - Editar pedidos;
    4 - Excluir pedido;
    5 - Sair; (Os pedidos serão excluidos!)
        """)
        print("="*40)
        opcoes = input("Digite a opção desejada (1-5):")
                
        
        
        if opcoes == "1":
            satisfeito = False
            print("="*40)
            print("\nCREATE - Adicionando seu pedido! ")
            
            nome = input("Digite seu nome para identificação: ")
            while not satisfeito:
                pedido = input("Digite seu pedido para adicionar no cardápio: ")
                pedido_continuar = input("Voce quer algo mais?").upper
                if pedido_continuar == "S":
                        print("")
                preco = float(input("Digite o preço R$: "))
                confirma = input("Confirmar pedido? (S/N): ").upper().strip()
                if confirma == "S":
                    arquivo = open(file_name, 'a', encoding='utf-8')
                    arquivo.write(f"{id_pedido},{nome},{pedido},{preco:.2f} R$\n")
                    arquivo.close()
                    print(f"Pedido {id_pedido} adicionado!")
                    id_pedido += 1
                    ultimo_id = id_pedido
                else:
                    print("Pedido Cancelado!❌ ")
                continuar = input("Deseja adicionar mais pedidos? Será adicionado com mesmo nome! (S/N): ").strip().upper()
                
                if continuar == "N":
                    satisfeito = True      
        
        elif opcoes == "2":
            print("="*40)
            print("READ - Lendo os pedidos!")
            arquivo = open(file_name, 'r', encoding='utf-8')
            total_linhas = arquivo.readlines()
            arquivo.close()
            if total_linhas:
                for  i,linha in enumerate(total_linhas,1):
                    conteudo = linha.strip().split(',')
                    print("="*40)
                    print(f"Pedido {conteudo[0]}\n Nome: {conteudo[1]}\n Pedido: {conteudo[2]}\n Preço: {conteudo[3]}\n")
                
            else:
                print("Nenhum pedido adicionado!")
            
            
        elif opcoes == "3":
            print("="*40)
            print("EDIT - Editando pedidos!")
            arquivo = open(file_name, 'r', encoding='utf-8')
            total_linhas = arquivo.readlines()
            arquivo.close()
            if total_linhas:
                for  i,linha in enumerate(total_linhas,1):
                    conteudo = linha.strip().split(',')
                    print("="*40)
                    print(f"Pedido {conteudo[0]}\n Nome: {conteudo[1]}\n Pedido: {conteudo[2]}\n Preço: {conteudo[3]}\n")
                
            else:
                print("Nenhum pedido existente!")
                
            try:
                id_busca = int(input("Digite o número do pedido para editar: "))
            except ValueError:
                print("Digite um número válido")
                continue
            arquivo = open(file_name, 'r', encoding='utf-8')
            total_linhas = arquivo.readlines()
            arquivo.close()
                    
            encontrado = False
           
           
            for i in range(len(total_linhas)):
                conteudo = total_linhas[i].strip().split(',')
                if id_busca == int(conteudo[0]):
                    encontrado = True
                    nome_novo = input("Digite o novo nome do cliente: ")
                    novo_pedido = input("Adicione o novo pedido: ")
                    novo_preco = float(input("Digite o novo preço do pedido: "))
                    total_linhas[i] = f"{id_busca},{nome_novo},{novo_pedido},{novo_preco:.2f} R$\n"
            if encontrado:
                arquivo = open(file_name,'w',encoding='utf-8')
                arquivo.writelines(total_linhas)
                arquivo.close()
                print("="*40)
                print(f"Dados do usuário com o número do pedido {id_busca} atualizados com sucesso!!")

            else:
                print(f"Usuário com o número do pedido {id_busca} não encontrado.")


            
        elif opcoes == "4":
            print("="*40)
            print("DELETE - Deletando pedidos!")
            arquivo = open(file_name, 'r', encoding='utf-8')
            total_linhas = arquivo.readlines()
            arquivo.close()
            if total_linhas:
                print("Pedidos atuais:")
                for linha in total_linhas:
                    conteudo = linha.strip().split(',')
                    print("="*40)
                    print(f"Pedido {conteudo[0]}\n Nome: {conteudo[1]}\n Pedido: {conteudo[2]}\n Preço: {conteudo[3]}\n")
                    
                excluir = input("Digite o número do pedido para excluir: ").strip()
                nova_lista = []
                encontrado = False
                    
                for linha in total_linhas:
                    conteudo = linha.strip().split(',')
                    if conteudo[0] == excluir:
                        encontrado = True
                        continue  
                    nova_lista.append(linha)
                    
                if encontrado:
                    arquivo = open(file_name, 'w', encoding='utf-8')
                    arquivo.writelines(nova_lista)
                    arquivo.close()
                    print(f"Pedido {excluir} excluído com sucesso!")
                else:
                        print("Pedido com esse número não encontrado!")
            else:
                print("Nenhum pedido para excluir!!")
                
        elif opcoes == '5':
            print("="*40)
            print("\nSaindo!")
            arquivo = open(file_name, 'w', encoding='utf-8')
            arquivo.write("") 
            arquivo.close()
            ultimo_id = 0
            id_pedido = 1
            break
        else: 
            print("="*40)
            print("\nDigite um número entre 1 e 5!")    
except FileNotFoundError:
    print("Falha ao encontrar o arquivo")
except ValueError:
    print("Valor incorreto")
except PermissionError:
    print("Erro: Sem permissão para acessar o arquivo.")
except KeyboardInterrupt:
    print("\nPrograma encerrado pelo usuário.")
