# EP - Design de Software
# Equipe: Adney Costa e Ricardo Mourão
# Caso você não saiba a contagem das cartas nós preparamos um resuminho para facilitar a sua vida:
# Ás vale 1. As cartas entre 2 e 9, incluindo ambos, possuem seus respectivos valores. Do 10 em diante as cartas valem 0.
# Bibliotecas importadas
import random

# Definindo o baralho
# Copas = C
# Ouro = O
# Paus = P
# Espadas = E
b1= ['A de Copas','1 de Copas','2 de Copas','3 de Copas','4 de Copas','5 de Copas','6 de Copas','7 de Copas','8 de Copas','9 de Copas','10 de Copas','J de Copas','Q de Copas','K de Copas']
b2= ['A de Ouro','1 de Ouro','2 de Ouro','3 de Ouro','4 de Ouro','5 de Ouro','6 de Ouro','7 de Ouro','8 de Ouro','9 de Ouro','10 de Ouro','J de Ouro','Q de Ouro','K de Ouro']
b3= ['A de Paus','1 de Paus','2 de Paus','3 de Paus','4 de Paus','5 de Paus','6 de Paus','7 de Paus','8 de Paus','9 de Paus','10 de Paus','J de Paus','Q de Paus','K de Paus']
b4= ['A de Espadas','1 de Espadas','2 de Espadas','3 de Espadas','4 de Espadas','5 de Espadas','6 de Espadas','7 de Espadas','8 de Espadas','9 de Espadas','10 de Espadas','J de Espadas','Q de Espadas','K de Espadas']
baralho= b1 + b2 + b3 + b4
lista_valores_1= [b1[0], b2[0], b3[0], b4[0], b1[1], b2[1], b3[1], b4[1]]
lista_valores_2= [b1[2], b2[2], b3[2], b4[2]]
lista_valores_3= [b1[3], b2[3], b3[3], b4[3]]
lista_valores_4= [b1[4], b2[4], b3[4], b4[4]]
lista_valores_5= [b1[5], b2[5], b3[5], b4[5]]
lista_valores_6= [b1[6], b2[6], b3[6], b4[6]]
lista_valores_7= [b1[7], b2[7], b3[7], b4[7]]
lista_valores_8= [b1[8], b2[8], b3[8], b4[8]]
lista_valores_9= [b1[9], b2[9], b3[9], b4[9]]
lista_valores_0= [b1[10],b2[10],b3[10],b4[10],  b1[11],b2[11],b3[11],b4[11],  b1[12],b2[12],b3[12],b4[12],  b1[13],b2[13],b3[13],b4[13]]

# Condições iniciais
soma_jogador= 0
soma_banco= 0
print("Seja bem vindo ao jogo! Vamos começar?!")
dinheiro= 100
print("Você tem R$ {0}".format(dinheiro))
# Começando o jogo
while dinheiro != 0:
    tipo_de_aposta= input("Em quem você quer apostar, Jogador, Banco ou Empate?")
    valor_da_aposta= int(input("Quanto você quer apostar"))

    # Caso o jogador aposte 0
    if valor_da_aposta== 0:
        print("Não quer jogar?, tudo bem! Até mais!")

    # Caso o jogador aposte um valor maior daquele que ele tem
    while valor_da_aposta > dinheiro:
        valor_da_aposta= int(input("Você não tem essa quantia de dinheiro. Por favor escolha um valor condizente com seu dinheiro:"))

    # Se o jogador escolher apostar no jogador
    if tipo_de_aposta== 'jogador' or "Jogador" or "JOGADOR":
        cartas_jogador= random.sample(baralho,2)
        cartas_banco= random.sample(baralho,2)
        print("As cartas do Jogador são: {0}".format(cartas_jogador))
        print("As cartas do Banco são: {0}".format(cartas_banco))
        while True:
            # Transformando as strings do baralho em números
            i= 0
            while i < len(cartas_jogador):
                if cartas_jogador[i] in lista_valores_0:
                    cartas_jogador[i]= 0
                if cartas_jogador[i] in lista_valores_1:
                    cartas_jogador[i]= 1
                if cartas_jogador[i] in lista_valores_2:
                    cartas_jogador[i]= 2
                if cartas_jogador[i] in lista_valores_3:
                    cartas_jogador[i]= 3
                if cartas_jogador[i] in lista_valores_4:
                    cartas_jogador[i]= 4
                if cartas_jogador[i] in lista_valores_5:
                    cartas_jogador[i]= 5
                if cartas_jogador[i] in lista_valores_6:
                    cartas_jogador[i]= 6
                if cartas_jogador[i] in lista_valores_7:
                    cartas_jogador[i]= 7
                if cartas_jogador[i] in lista_valores_8:
                    cartas_jogador[i]= 8
                if cartas_jogador[i] in lista_valores_9:
                    cartas_jogador[i]= 9
                i+=1
            k= 0
            while k < len(cartas_banco):
                if cartas_banco[k] in lista_valores_0:
                    cartas_banco[k]= 0
                if cartas_banco[k] in lista_valores_1:
                    cartas_banco[k]= 1
                if cartas_banco[k] in lista_valores_2:
                    cartas_banco[k]= 2
                if cartas_banco[k] in lista_valores_3:
                    cartas_banco[k]= 3
                if cartas_banco[k] in lista_valores_4:
                    cartas_banco[k]= 4
                if cartas_banco[k] in lista_valores_5:
                    cartas_banco[k]= 5
                if cartas_banco[k] in lista_valores_6:
                    cartas_banco[k]= 6
                if cartas_banco[k] in lista_valores_7:
                    cartas_banco[k]= 7
                if cartas_banco[k] in lista_valores_8:
                    cartas_banco[k]= 8
                if cartas_banco[k] in lista_valores_9:
                    cartas_banco[k]= 9
                k+=1
            # Somando o valor das cartas
            soma_banco= cartas_banco[0] + cartas_banco[1]
            soma_jogador= cartas_jogador[0] + cartas_jogador[1]
            # Condicionais para a soma de cartas
            # Se a soma do jogador for maior que 10
            if soma_jogador >= 10:
                soma_jogador= soma_jogador - 10
            # Se a soma do banco for maior que 10
            if soma_banco >= 10:
                soma_banco= soma_banco - 10
            # Quando alguma das somas for igual a 8 ou 9########
            if soma_jogador==8 or soma_jogador==9:
                break
                #print("A soma das cartas do jogador é: {0}".format(soma_jogador))
                #print("A soma das cartas do banco é: {0}".format(soma_banco))
            if soma_banco==8 or soma_banco==9:
                break
                #print("A soma das cartas do jogador é: {0}".format(soma_jogador))
                #print("A soma das cartas do banco é: {0}".format(soma_banco))

            # Se a soma do jogador ou banco for menor ou  igual a 5
            if soma_jogador <= 5 or soma_banco <= 5:
                if soma_jogador <= 5:
                    carta_jogador_extra= random.sample(baralho,1)
                    cartas_jogador= cartas_jogador + carta_jogador_extra
                    print("A carta extra do jogador é: {0}".format(carta_jogador_extra))
                    if carta_jogador_extra[0] in lista_valores_0:
                        carta_jogador_extra[0]= 0
                    if carta_jogador_extra[0] in lista_valores_1:
                        carta_jogador_extra[0]= 1
                    if carta_jogador_extra[0] in lista_valores_2:
                        carta_jogador_extra[0]= 2
                    if carta_jogador_extra[0] in lista_valores_3:
                        carta_jogador_extra[0]= 3
                    if carta_jogador_extra[0] in lista_valores_4:
                        carta_jogador_extra[0]= 4
                    if carta_jogador_extra[0] in lista_valores_5:
                        carta_jogador_extra[0]= 5
                    if carta_jogador_extra[0] in lista_valores_6:
                        carta_jogador_extra[0]= 6
                    if carta_jogador_extra[0] in lista_valores_7:
                        carta_jogador_extra[0]= 7
                    if carta_jogador_extra[0] in lista_valores_8:
                        carta_jogador_extra[0]= 8
                    if carta_jogador_extra[0] in lista_valores_9:
                        carta_jogador_extra[0]= 9
                    # Agora nós somamos a carta extra
                    soma_jogador= soma_jogador + carta_jogador_extra[0]
                    # Se a soma do jogador for maior que 10
                    if soma_jogador >= 10:
                        soma_jogador= soma_jogador - 10

                if soma_banco <= 5:
                    carta_banco_extra= random.sample(baralho,1)
                    cartas_banco= cartas_banco + carta_banco_extra
                    print("A carta extra do banco é: {0}".format(carta_banco_extra))
                    if carta_banco_extra[0] in lista_valores_0:
                        carta_banco_extra[0]= 0
                    if carta_banco_extra[0] in lista_valores_1:
                        carta_banco_extra[0]= 1
                    if carta_banco_extra[0] in lista_valores_2:
                        carta_banco_extra[0]= 2
                    if carta_banco_extra[0] in lista_valores_3:
                        carta_banco_extra[0]= 3
                    if carta_banco_extra[0] in lista_valores_4:
                        carta_banco_extra[0]= 4
                    if carta_banco_extra[0] in lista_valores_5:
                        carta_banco_extra[0]= 5
                    if carta_banco_extra[0] in lista_valores_6:
                        carta_banco_extra[0]= 6
                    if carta_banco_extra[0] in lista_valores_7:
                        carta_banco_extra[0]= 7
                    if carta_banco_extra[0] in lista_valores_8:
                        carta_banco_extra[0]= 8
                    if carta_banco_extra[0] in lista_valores_9:
                        carta_banco_extra[0]= 9
                    # Agora nós somamos a carta extra
                    soma_banco= soma_banco + carta_banco_extra[0]
                    # Se a soma do banco for maior que 10
                    if soma_banco >= 10:
                        soma_banco= soma_banco - 10
                break
            break
        print("A soma das cartas do jogador é: {0}".format(soma_jogador))
        print("A soma das cartas do banco é: {0}".format(soma_banco))
        if soma_jogador > soma_banco:
            print("Parabéns! A soma do jogador foi maior. Com isso, você ganhou {0} reais, e agora tem {1} reais".format(valor_da_aposta, dinheiro + valor_da_aposta))
            dinheiro= dinheiro + valor_da_aposta
        if soma_jogador <= soma_banco:
            print("Infelizmente você perdeu! Agora você tem {0} reais".format(dinheiro - valor_da_aposta))
            dinheiro= dinheiro - valor_da_aposta
    

# Se o jogador escolher apostar no Banco
if tipo_de_aposta== 'banco' or "Banco" or "BANCO":
    cartas_jogador= random.sample(baralho,2)
    cartas_banco= random.sample(baralho,2)
    print("As cartas do Jogador são: {0}".format(cartas_jogador))
    print("As cartas do Banco são: {0}".format(cartas_banco))
    # Transformando as strings do baralho em números
    if cartas_jogador[0] in lista_valores_0:
        cartas_jogador[0]= 0
    if cartas_jogador[0] in lista_valores_1:
        cartas_jogador[0]= 1
    if cartas_jogador[0] in lista_valores_2:
        cartas_jogador[0]= 2
    if cartas_jogador[0] in lista_valores_3:
        cartas_jogador[0]= 3
    if cartas_jogador[0] in lista_valores_4:
        cartas_jogador[0]= 4
    if cartas_jogador[0] in lista_valores_5:
        cartas_jogador[0]= 5
    if cartas_jogador[0] in lista_valores_6:
        cartas_jogador[0]= 6
    if cartas_jogador[0] in lista_valores_7:
        cartas_jogador[0]= 7
    if cartas_jogador[0] in lista_valores_8:
        cartas_jogador[0]= 8
    if cartas_jogador[0] in lista_valores_9:
        cartas_jogador[0]= 9

    if cartas_jogador[1] in lista_valores_0:
        cartas_jogador[1]= 0
    if cartas_jogador[1] in lista_valores_1:
        cartas_jogador[1]= 1
    if cartas_jogador[1] in lista_valores_2:
        cartas_jogador[1]= 2
    if cartas_jogador[1] in lista_valores_3:
        cartas_jogador[1]= 3
    if cartas_jogador[1] in lista_valores_4:
        cartas_jogador[1]= 4
    if cartas_jogador[1] in lista_valores_5:
        cartas_jogador[1]= 5
    if cartas_jogador[1] in lista_valores_6:
        cartas_jogador[1]= 6
    if cartas_jogador[1] in lista_valores_7:
        cartas_jogador[1]= 7
    if cartas_jogador[1] in lista_valores_8:
        cartas_jogador[1]= 8
    if cartas_jogador[1] in lista_valores_9:
        cartas_jogador[1]= 9

    if cartas_banco[0] in lista_valores_0:
        cartas_banco[0]= 0
    if cartas_banco[0] in lista_valores_1:
        cartas_banco[0]= 1
    if cartas_banco[0] in lista_valores_2:
        cartas_banco[0]= 2
    if cartas_banco[0] in lista_valores_3:
        cartas_banco[0]= 3
    if cartas_banco[0] in lista_valores_4:
        cartas_banco[0]= 4
    if cartas_banco[0] in lista_valores_5:
        cartas_banco[0]= 5
    if cartas_banco[0] in lista_valores_6:
        cartas_banco[0]= 6
    if cartas_banco[0] in lista_valores_7:
        cartas_banco[0]= 7
    if cartas_banco[0] in lista_valores_8:
        cartas_banco[0]= 8
    if cartas_banco[0] in lista_valores_9:
        cartas_banco[0]= 9

    if cartas_banco[1] in lista_valores_0:
        cartas_banco[1]= 0
    if cartas_banco[1] in lista_valores_1:
        cartas_banco[1]= 1
    if cartas_banco[1] in lista_valores_2:
        cartas_banco[1]= 2
    if cartas_banco[1] in lista_valores_3:
        cartas_banco[1]= 3
    if cartas_banco[1] in lista_valores_4:
        cartas_banco[1]= 4
    if cartas_banco[1] in lista_valores_5:
        cartas_banco[1]= 5
    if cartas_banco[1] in lista_valores_6:
        cartas_banco[1]= 6
    if cartas_banco[1] in lista_valores_7:
        cartas_banco[1]= 7
    if cartas_banco[1] in lista_valores_8:
        cartas_banco[1]= 8
    if cartas_banco[1] in lista_valores_9:
        cartas_banco[1]= 9

    # Somando o valor das cartas
    soma_banco= cartas_banco[0] + cartas_banco[1]
    soma_jogador= cartas_jogador[0] + cartas_jogador[1]

    # Condicionais para a soma de cartas
    # Se a soma do jogador for maior que 10
    if soma_jogador >= 10:
        soma_jogador= soma_jogador - 10
    # Se a soma do banco for maior que 10
    if soma_banco >= 10:
        soma_banco= soma_banco - 10
    # Se a soma do jogador for menor ou  igual a 5
    if soma_jogador <= 5:
        carta_jogador_extra= random.sample(baralho,1)
        cartas_jogador= cartas_jogador + carta_jogador_extra
        print("A carta extra do jogador é: {0}".format(carta_jogador_extra))
        if carta_jogador_extra[0] in lista_valores_0:
            carta_jogador_extra[0]= 0
        if carta_jogador_extra[0] in lista_valores_1:
            carta_jogador_extra[0]= 1
        if carta_jogador_extra[0] in lista_valores_2:
            carta_jogador_extra[0]= 2
        if carta_jogador_extra[0] in lista_valores_3:
            carta_jogador_extra[0]= 3
        if carta_jogador_extra[0] in lista_valores_4:
            carta_jogador_extra[0]= 4
        if carta_jogador_extra[0] in lista_valores_5:
            carta_jogador_extra[0]= 5
        if carta_jogador_extra[0] in lista_valores_6:
            carta_jogador_extra[0]= 6
        if carta_jogador_extra[0] in lista_valores_7:
            carta_jogador_extra[0]= 7
        if carta_jogador_extra[0] in lista_valores_8:
            carta_jogador_extra[0]= 8
        if carta_jogador_extra[0] in lista_valores_9:
            carta_jogador_extra[0]= 9
        # Agora nós somamos a carta extra
        soma_jogador= soma_jogador + carta_jogador_extra[0]

    # Se a soma do banco for menor ou  igual a 5
    if soma_banco <= 5:
        carta_banco_extra= random.sample(baralho,1)
        cartas_banco= cartas_banco + carta_banco_extra
        print("A carta extra do banco é: {0}".format(carta_banco_extra))
        if carta_banco_extra[0] in lista_valores_0:
            carta_banco_extra[0]= 0
        if carta_banco_extra[0] in lista_valores_1:
            carta_banco_extra[0]= 1
        if carta_banco_extra[0] in lista_valores_2:
            carta_banco_extra[0]= 2
        if carta_banco_extra[0] in lista_valores_3:
            carta_banco_extra[0]= 3
        if carta_banco_extra[0] in lista_valores_4:
            carta_banco_extra[0]= 4
        if carta_banco_extra[0] in lista_valores_5:
            carta_banco_extra[0]= 5
        if carta_banco_extra[0] in lista_valores_6:
            carta_banco_extra[0]= 6
        if carta_banco_extra[0] in lista_valores_7:
            carta_banco_extra[0]= 7
        if carta_banco_extra[0] in lista_valores_8:
            carta_banco_extra[0]= 8
        if carta_banco_extra[0] in lista_valores_9:
            carta_banco_extra[0]= 9
        # Agora nós somamos a carta extra
        soma_banco= soma_banco + carta_banco_extra[0]

        # Recolocando as condições de soma das cartas
        # Se a soma do jogador for maior que 10
        if soma_jogador >= 10:
            soma_jogador= soma_jogador - 10
        # Se a soma do banco for maior que 10
        if soma_banco >= 10:
            soma_banco= soma_banco - 10
    print("A soma das cartas do jogador é: {0}".format(soma_jogador))
    print("A soma das cartas do banco é: {0}".format(soma_banco))
 
# Se o jogador escolher apostar no Banco
elif tipo_de_aposta== 'empate' or "Empate" or "EMPATE":
    cartas_jogador= random.sample(baralho,2)
    cartas_banco= random.sample(baralho,2)
    print("As cartas do Jogador são: {0}".format(cartas_jogador))
    print("As cartas do Banco são: {0}".format(cartas_banco))
    # Transformando as strings do baralho em números
    if cartas_jogador[0] in lista_valores_0:
        cartas_jogador[0]= 0
    if cartas_jogador[0] in lista_valores_1:
        cartas_jogador[0]= 1
    if cartas_jogador[0] in lista_valores_2:
        cartas_jogador[0]= 2
    if cartas_jogador[0] in lista_valores_3:
        cartas_jogador[0]= 3
    if cartas_jogador[0] in lista_valores_4:
        cartas_jogador[0]= 4
    if cartas_jogador[0] in lista_valores_5:
        cartas_jogador[0]= 5
    if cartas_jogador[0] in lista_valores_6:
        cartas_jogador[0]= 6
    if cartas_jogador[0] in lista_valores_7:
        cartas_jogador[0]= 7
    if cartas_jogador[0] in lista_valores_8:
        cartas_jogador[0]= 8
    if cartas_jogador[0] in lista_valores_9:
        cartas_jogador[0]= 9

    if cartas_jogador[1] in lista_valores_0:
        cartas_jogador[1]= 0
    if cartas_jogador[1] in lista_valores_1:
        cartas_jogador[1]= 1
    if cartas_jogador[1] in lista_valores_2:
        cartas_jogador[1]= 2
    if cartas_jogador[1] in lista_valores_3:
        cartas_jogador[1]= 3
    if cartas_jogador[1] in lista_valores_4:
        cartas_jogador[1]= 4
    if cartas_jogador[1] in lista_valores_5:
        cartas_jogador[1]= 5
    if cartas_jogador[1] in lista_valores_6:
        cartas_jogador[1]= 6
    if cartas_jogador[1] in lista_valores_7:
        cartas_jogador[1]= 7
    if cartas_jogador[1] in lista_valores_8:
        cartas_jogador[1]= 8
    if cartas_jogador[1] in lista_valores_9:
        cartas_jogador[1]= 9

    if cartas_banco[0] in lista_valores_0:
        cartas_banco[0]= 0
    if cartas_banco[0] in lista_valores_1:
        cartas_banco[0]= 1
    if cartas_banco[0] in lista_valores_2:
        cartas_banco[0]= 2
    if cartas_banco[0] in lista_valores_3:
        cartas_banco[0]= 3
    if cartas_banco[0] in lista_valores_4:
        cartas_banco[0]= 4
    if cartas_banco[0] in lista_valores_5:
        cartas_banco[0]= 5
    if cartas_banco[0] in lista_valores_6:
        cartas_banco[0]= 6
    if cartas_banco[0] in lista_valores_7:
        cartas_banco[0]= 7
    if cartas_banco[0] in lista_valores_8:
        cartas_banco[0]= 8
    if cartas_banco[0] in lista_valores_9:
        cartas_banco[0]= 9

    if cartas_banco[1] in lista_valores_0:
        cartas_banco[1]= 0
    if cartas_banco[1] in lista_valores_1:
        cartas_banco[1]= 1
    if cartas_banco[1] in lista_valores_2:
        cartas_banco[1]= 2
    if cartas_banco[1] in lista_valores_3:
        cartas_banco[1]= 3
    if cartas_banco[1] in lista_valores_4:
        cartas_banco[1]= 4
    if cartas_banco[1] in lista_valores_5:
        cartas_banco[1]= 5
    if cartas_banco[1] in lista_valores_6:
        cartas_banco[1]= 6
    if cartas_banco[1] in lista_valores_7:
        cartas_banco[1]= 7
    if cartas_banco[1] in lista_valores_8:
        cartas_banco[1]= 8
    if cartas_banco[1] in lista_valores_9:
        cartas_banco[1]= 9

    # Somando o valor das cartas
    soma_banco= cartas_banco[0] + cartas_banco[1]
    soma_jogador= cartas_jogador[0] + cartas_jogador[1]

    # Condicionais para a soma de cartas
    # Se a soma do jogador for maior que 10
    if soma_jogador >= 10:
        soma_jogador= soma_jogador - 10
    # Se a soma do banco for maior que 10
    if soma_banco >= 10:
        soma_banco= soma_banco - 10
    # Se a soma do jogador for menor ou  igual a 5
    if soma_jogador <= 5:
        carta_jogador_extra= random.sample(baralho,1)
        cartas_jogador= cartas_jogador + carta_jogador_extra
        print("A carta extra do jogador é: {0}".format(carta_jogador_extra))
        if carta_jogador_extra[0] in lista_valores_0:
            carta_jogador_extra[0]= 0
        if carta_jogador_extra[0] in lista_valores_1:
            carta_jogador_extra[0]= 1
        if carta_jogador_extra[0] in lista_valores_2:
            carta_jogador_extra[0]= 2
        if carta_jogador_extra[0] in lista_valores_3:
            carta_jogador_extra[0]= 3
        if carta_jogador_extra[0] in lista_valores_4:
            carta_jogador_extra[0]= 4
        if carta_jogador_extra[0] in lista_valores_5:
            carta_jogador_extra[0]= 5
        if carta_jogador_extra[0] in lista_valores_6:
            carta_jogador_extra[0]= 6
        if carta_jogador_extra[0] in lista_valores_7:
            carta_jogador_extra[0]= 7
        if carta_jogador_extra[0] in lista_valores_8:
            carta_jogador_extra[0]= 8
        if carta_jogador_extra[0] in lista_valores_9:
            carta_jogador_extra[0]= 9
        # Agora nós somamos a carta extra
        soma_jogador= soma_jogador + carta_jogador_extra[0]

    # Se a soma do banco for menor ou  igual a 5
    if soma_banco <= 5:
        carta_banco_extra= random.sample(baralho,1)
        cartas_banco= cartas_banco + carta_banco_extra
        print("A carta extra do banco é: {0}".format(carta_banco_extra))
        if carta_banco_extra[0] in lista_valores_0:
            carta_banco_extra[0]= 0
        if carta_banco_extra[0] in lista_valores_1:
            carta_banco_extra[0]= 1
        if carta_banco_extra[0] in lista_valores_2:
            carta_banco_extra[0]= 2
        if carta_banco_extra[0] in lista_valores_3:
            carta_banco_extra[0]= 3
        if carta_banco_extra[0] in lista_valores_4:
            carta_banco_extra[0]= 4
        if carta_banco_extra[0] in lista_valores_5:
            carta_banco_extra[0]= 5
        if carta_banco_extra[0] in lista_valores_6:
            carta_banco_extra[0]= 6
        if carta_banco_extra[0] in lista_valores_7:
            carta_banco_extra[0]= 7
        if carta_banco_extra[0] in lista_valores_8:
            carta_banco_extra[0]= 8
        if carta_banco_extra[0] in lista_valores_9:
            carta_banco_extra[0]= 9
        # Agora nós somamos a carta extra
        soma_banco= soma_banco + carta_banco_extra[0]

        # Recolocando as condições de soma das cartas
        # Se a soma do jogador for maior que 10
        if soma_jogador >= 10:
            soma_jogador= soma_jogador - 10
        # Se a soma do banco for maior que 10
        if soma_banco >= 10:
            soma_banco= soma_banco - 10
    print("A soma das cartas do jogador é: {0}".format(soma_jogador))
    print("A soma das cartas do banco é: {0}".format(soma_banco))
 