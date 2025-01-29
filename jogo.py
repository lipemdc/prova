print("superman e flash encontram o portal")
while True:
    caminho = input("escolha o caminho:\n1:rapido\n2:seguro").strip().lower()
    if caminho == "1":
        print("chegam rapido, mas enfrentam danos magicos.")
        print("entraram em um labirinto de espelhos magicos.")
        while True:
            espelho = input("escolha o espelho (1, 2, 3)").strip().lower()
            if espelho == "1": 
                print("armadilha, voltam ao inicio do labirinto")
            elif espelho == "2":
                print ("encontram a saída e seguem adiante")
                print ("encontram o feiticeiro, que está pronto para lutar")
                break
            elif espelho == "3":
                print ("encontra o feiticeiro, mas ele ataca")
                print ("perdem por estarem machucados")
                exit()
            else: 
                print ("ESCOLHA UM NUMERO DE 1 A 3")
        while True:
            quem_vai_lutar = input("escolha quem vai lutar:\n1:flash sozinho\n2:superman sozinho\n3:ambos").strip().lower()
            if quem_vai_lutar == "1": 
                print("o feiticeiro lança um feitiço que cega o flash")
                print("flash morre")
                exit()
            elif quem_vai_lutar == "2": 
                print("o feiticeiro usa uma pedra de criptonita que deixa o superman fraco")
                print("superman morre")
                exit()
            elif quem_vai_lutar == "3":
                print("o feiticeiro não consegue reagir e é exterminado pelos dois")
                print("o feiticeiro morre")
                exit()
            else:
                print("ESCOLHA UM NUMERO DE 1 A 3")
    elif caminho == "2":
        print("chegam ao castelo, mas perdem tempo")
        print("entraram em um labirinto de espelhos magicos")
        while True:
            espelho = input("escolha o espelho (1, 2, 3)").strip().lower()
            if espelho == "1": 
                print("(armadilha, perde por falta de tempo")
                exit()
            elif espelho == "2":
                print ("encontram a saída e seguem adiante")
                print ("encontram o feiticeiro, que está pronto para lutar")
                break
            elif espelho == "3":
                print ("encontra o feiticeiro, mas ele ataca")
                quem_vai_lutar = input("escolha quem vai lutar:\n1:flash\n2:superman)").strip().lower()
                if quem_vai_lutar == "1":
                    print ("Usa a velocidade para desviar dos feiços e vence.")
                    exit()
                elif quem_vai_lutar == "2":
                    print("resiste e vence com a força bruta")
                    exit()
            else:
                print ("ESCOLHA UM NUMERO DE 1 A 3")
        while True:
            quem_vai_lutar = input("escolha quem vai lutar:\n1:flash sozinho\n2:superman sozinho\n3:ambos").strip().lower()
            if quem_vai_lutar == "1": 
                print("o feiticeiro lança um feitiço que cega o flash")
                print("flash morre")
                exit()
            elif quem_vai_lutar == "2": 
                print("o feiticeiro usa uma pedra de criptonita que deixa o superman fraco")
                print("superman morre")
                exit()
            elif quem_vai_lutar == "3":
                print("o feiticeiro não consegue reagir e é exterminado pelos dois")
                print("o feiticeiro morre")
                exit()
            else:
                print("ESCOLHA UM NUMERO DE 1 A 3")
    else:
        print("ESCOLHA UM NUMERO DE 1 A 2")
        
        
    
            
            
        
