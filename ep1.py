# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Lucca Nazari da Silva e Souza, lucca.n17@al.insper.edu.br
# - aluno B: Luca Cazzolato Machado, lucacm@al.insper.edu.br



from pprint import pprint
import json
import random as randint
import time
import sys


#x= bool(randint(0,1))
#pocao_de_vida=100 de vida 
#if pocao_de_vida= "algum lugar do jogo"
    #vida_jogador=100
#print('opa, voce encontrou uma pocao de vida, sua vida voltou aos 100.')
#ataque fraco, medio forte, pega o ataque da arma e usa *0.8 ou *1 ou *1.2
#espada=10
#ataque=randint(0,2)
    #if ataque=0:
        #ataque_final=espada*0.8
    #elif ataque=1:
        #ataque_final=espada
    #elif ataque=2:
        #ataque_final=espada*1.2

        
def inventario():
    itens = []


def carregar_cenarios():
    with open("Dicionario_Cenarios_EP1.json",'r') as cenario:
        conteudo_cenario = cenario.read()
    cenarios = json.loads(conteudo_cenario)

    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual

def carregar_monstros():
    with open("Arquivo_Monstros_EP!", "r") as monstros:
        conteudo_monstros = monstros.read()
    return conteudo_monstros


def carregar_items():
    with open('Dicionario_Inventario_EP1.json','r') as items:
        conteudo_inventario = items.read()
    inventario = json.loads(conteudo_inventario)
    return inventario


def carregar_combate():
    with open('Dicionario_Combate_EP1.json','r') as combate:
        conteudo_combate = combate.read()
    combate = json.loads(conteudo_combate)
    return combate

'''
combate = carregar_combate()
for a in combate:
    for b,c in combate[a].items():
        print("{0}: {1}".format(b,c))        
'''



def main():
    jogador = input("Diga seu nome aventureiro: ")
    print()
    print("Ola {0}, voce tem 100 de vida e uma adaga em seu inventario".format(jogador))
    print()
    pronto= input("voce esta pronto?: ")
    print("Vamos comecar")
    print("------------------")
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    while not game_over:
        
        
        bibliotecaria=45
        i=0
        ataque_jogador=20
        contador_biblioteca=0
        cenario_atual = cenarios[nome_cenario_atual]

        titulo= cenario_atual['titulo']
        print(titulo)
        print("-"*len(titulo))
        print()
        print(cenario_atual["descricao"])
        print()
        
        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:
            print("Escolha sua opção:")
            print()
            for k,v in cenario_atual["opcoes"].items():
                print("{0}: {1}".format(k,v))
            escolha = input("O que você quer fazer? ")
            print()

            if escolha in opcoes:
                cenario_anterior= nome_cenario_atual
                nome_cenario_atual = escolha
#e pq n tava definido antes, acho q algm apago sem quere, mas agr ta indo
                
                
                if contador_biblioteca==0 and escolha== "biblioteca":
                    contador_biblioteca+=1
                    print("Voce achou a bibliotecaria maligna")
                    print()
                    pergunta= input("Deseja lutar? sim ou nao? ")
                    if pergunta== "nao":
                        nome_cenario_atual=cenario_anterior
                        print("voce voltou para o cenario anterior")
                        
                    elif pergunta== "sim":                        
                        while bibliotecaria>0:
                            ataque_random= random.randint(0,2)
                            ataque_jogador=20
                            if ataque_random==0:
                                print("Ataque fracoo")
                                print()
                                ataque_jogador= ataque_jogador*0.8
                                
                            elif ataque_random==1:
                                print("Ataque medio")
                                print()
                                ataque_jogador= ataque_jogador*1
                                
                            elif ataque_random==2:
                                print("Ataque fortee")
                                print()
                                ataque_jogador= ataque_jogador*1.2
                                
                            print("seu ataque foi de {0}: ".format(ataque_jogador))
                            print()
                            bibliotecaria= bibliotecaria - ataque_jogador
                            if bibliotecaria < 0:
                                bibliotecaria=0
                            
                            print("a vida da bibliotecaria ficou {0}: ".format(bibliotecaria))
                            print()
                            
                            if bibliotecaria==0:
                                print("Parabens, voce derrotou a bibliotecaria")
                                print()
                                print("agora voce pode seguir seu caminho")
                                print()
                            
                            
                   

                    
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    morte = "Você morreu!\n"
    for l in morte:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.2)



# Programa principal.
if __name__ == "__main__":
    main()
