# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Lucca Nazari da Silva e Souza, luccanss@al.insper.edu.br
# - aluno B: Luca Cazzolato Machado, lucacm@al.insper.edu.br



from pprint import pprint
import json
from random import randint
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


def carregar_cenarios():
    with open("Dicionario_Cenarios_EP1.json",'r') as cenario:
        conteudo_cenario = cenario.read()
    cenarios = json.loads(conteudo_cenario)

    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual


def carregar_inventário():
    with open('Dicionario_Inventario_EP1.json','r') as items:
        conteudo_inventario = items.read()
    inventario = json.loads(conteudo_inventario)
    return inventario


def carregar_combate_e_monstros():
    monstros = [ 
        {"veterano": {
            "nome": "Veterano",
            "fala": "Hahahaha, eu cursei anoooos de INSPER, acha mesmo que pode me derrotar?????",
            "status": {
                "hit points": 10,
                "pontos de ataque": 4,
                "pontos de defesa": 2
                }
            }
        },
        {"bibliotecaria": {
            "nome": "Bibliotecaria",
            "fala": "Ora se não é um forasteiro perdido procurando alguns livros.",
            "status": {
                "hit points": 15,
                "pontos de ataque": 5,
                "pontos de defesa": 4
                }
            }
        },
        {"fumante": {
            "nome": "Fumante",
            "fala": "Cof... Cof... Se você veio pedir um trago, pode ir se preparando pra levar um pé na bunda",
            "status": {
                "hit points": 5,
                "pontos de ataque": 10,
                "pontos de defesa": 1
                }
            }
        },
        {"professor 1": {
            "nome": "Daniel Guzzo",
            "fala": "Você veio ao FAB LAB, pois bem QUERO UM PROTÓTIPO!",
            "status": {
                "hit points": 50,
                "pontos de ataque": 20,
                "pontos de defesa": 10
                }
            }
        },
        {"professor 2": {
            "nome": "Paulina",
            "fala": "Iterar e Graficar...",
            "status": {
                "hit points": 65,
                "pontos de ataque": 15,
                "pontos de defesa": 20
                }
            }
        }
    ]
    combate = {
        "luta 0": {
                "titulo": "Parece que uma luta lhe espera!",
                "nome": monstros[0]["veterano"]["nome"],
                "fala": monstros[0]["veterano"]["fala"],
                "status_monstro": monstros[0]["veterano"]["status"],
                "opcoes": "lutar ou fugir? "
        },
        "luta 1": {
                "titulo": "Parece que uma luta lhe espera!",
                "nome": monstros[1]["bibliotecaria"]["nome"],
                "fala": monstros[1]["bibliotecaria"]["fala"],
                "status_monstro": monstros[1]["bibliotecaria"]["status"],
                "opcoes": "lutar ou fugir? "
            
        },
        "luta 2": {
                "titulo": "Parece que uma luta lhe espera!",
                "nome": monstros[2]["fumante"]["nome"],
                "fala": monstros[2]["fumante"]["fala"],
                "status_monstro": monstros[2]["fumante"]["status"],
                "opcoes": "lutar ou fugir? "
            
        },
        "luta 3": {
                "titulo": "Parece que uma luta lhe espera!",
                "nome": monstros[3]["professor 1"]["nome"],
                "fala": monstros[3]["professor 1"]["fala"],
                "status_monstro": monstros[3]["professor 1"]["status"],
                "opcoes": "lutar ou fugir? "
            
        },
        "luta 4": {
                "titulo": "Parece que uma luta lhe espera!",
                "nome": monstros[4]["professor 2"]["nome"],
                "fala": monstros[4]["professor 2"]["fala"],
                "status_monstro": monstros[4]["professor 2"]["status"],
                "opcoes": "lutar ou fugir? " 
            
            
        }
    }
    return combate, monstros
'''
'''
'''
combate = carregar_combate()
for a in combate:
    for b,c in combate[a].items():
        print("{0}: {1}".format(b,c))        
'''
'''
'''

def main():
    jogador = input("Diga seu nome aventureiro: ")
    atributos_jogador = {
        "hit points": 100,
        "pontos de ataque": 12,
        "pontos de defesa": 7
    }
    inventário_itens = []
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
    combate, monstros = carregar_combate_e_monstros()
    

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

            if escolha in opcoes and escolha == "biblioteca":
                    print(combate["luta 0"]["titulo"])
                    print()
                    print(combate["luta 0"]["nome"])
                    print()
                    print(combate["luta 0"]["fala"])
                    print(combate["luta 0"]["nome"],":", combate["luta 0"]["status_monstro"])
                    print(jogador, ":", atributos_jogador)
                    choice = input("o que deseja fazer: 'lutar' ou 'fugir'? ")
                    if choice == "lutar":
                        print(jogador, "atacou e causou {0} de dano!".format(atributos_jogador["pontos de ataque"]))
                        monstros[0]["veterano"]["status"]["hit points"] += monstros[0]["veterano"]["status"]["pontos de defesa"]
                        print("A vida de Veterano é: {0}".format(monstros[0]["veterano"]["status"]["hit points"]))


                    

                
'''
                cenario_anterior= nome_cenario_atual
                nome_cenario_atual = escolha

                
                
                if contador_biblioteca==0 and escolha== "biblioteca":
                    contador_biblioteca= 1
                    print("Voce achou a bibliotecaria maligna")
                    print()
                    pergunta= input("Deseja lutar? sim ou nao? ")
                    if pergunta== "nao":
                        nome_cenario_atual=cenario_anterior
                        print("voce voltou para o cenario anterior")
                        
                    elif pergunta== "sim":                        
                        while bibliotecaria>0:
                            ataque_random= randint(0,2)
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
                    nome_cenario_atual = escolha
                            '''
                            
                   

'''      
           else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    morte = "Você morreu!\n"
    for l in morte:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.2)
'''


# Programa principal.
if __name__ == "__main__":
    main()
