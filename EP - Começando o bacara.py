# EP - Design de Software
# Equipe: Adney Costa e Ricardo Mourão

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


# Começando o jogo
soma_jogador= 0
soma_banco= 0
print("Seja bem vindo ao jogo! Vamos começar?!")
dinheiro= 100
print("Você tem R$ {0}".format(dinheiro))
tipo_de_aposta= input("Em quem você quer apostar, Jogador, Banco ou Empate?")
valor_da_aposta= int(input("Quanto você quer apostar"))

# Caso o jogador aposte 0
if valor_da_aposta== 0:
    print("Não quer jogar?, tudo bem! Até mais!")

# Caso o jogador aposte um valor maior daquele que ele tem
while valor_da_aposta > dinheiro:
    valor_da_aposta= int(input("Você não tem essa quantia de dinheiro. Por favor escolha um valor condizente com seu dinheiro:"))
