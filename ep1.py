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


#Váriaveis:
atributos_jogador = {
        "hit points": 100,
        "pontos de ataque": 12
    }

vida_player=100

inventario_jogador = ["carteirinha do insper"]
#adaga = 10 atk points
#escudo = 10 atk points
#poção de vida = restore 100 hit points



#Funções:
    
def carregar_cenarios():
    with open("Dicionario_Cenarios_EP1.json",'r') as cenario:
        conteudo_cenario = cenario.read()
    cenarios = json.loads(conteudo_cenario)
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual

def carregar_monstros():
    monstros = [ 
        {
            "nome": "Bibliotecaria",
            "fala": "Ora ora se não é um forasteiro perdido procurando alguns livros.",
            "premio": "adaga",
            "status": {
                "hit points": 15,
                "pontos de ataque": 10
                }
            },
        {
            "nome": "Veterano",
            "fala": "Hahahaha, eu cursei anoooos de INSPER, acha mesmo que pode me derrotar?????",
            "premio": "chave ss",
            "status": {
                "hit points": 25,
                "pontos de ataque": 14
                }
            },
        {
            "nome": "Fumante",
            "fala": "Cof... Cof... Se você veio pedir um trago, pode ir se preparando pra levar um pé na bunda",
            "premio": "poção de vida",
            "status": {
                "hit points": 5,
                "pontos de ataque": 15
                }
            },
        {
            "nome": "Daniel Guzzo",
            "fala": "Você veio ao FAB LAB, pois bem QUERO UM PROTÓTIPO!",
            "premio": "tapete deslizante",
            "status": {
                "hit points": 50,
                "pontos de ataque": 24
                }
            },
        {
            "nome": "Paulina",
            "fala": "Iterar e Graficar...",
            "premio": "mapa",
            "status": {
                "hit points": 65,
                "pontos de ataque": 24
                }
            },            
            {
            "nome": "Barbara",
            "fala": "Bar Bar Bar ba ra Ann, The beach Boys",
            "premio": "espada python",
            "status": {
                    "hit points": 85,
                    "pontos de ataque": 30
                                      
                    }
            },
        {
            "nome": "Tosh",
            "fala": "mestre dos magos",
            "premio": "ganho um A+ no EP",
            "status": {
                    "hit points": 120,
                    "pontos de ataque": 33                                   
                    }
            }
        ]
    return monstros

def carregar_combate():
    monstros = carregar_monstros()
    combate = {
        "luta 0": {
                "titulo": "Parece que uma luta lhe espera! E alguém lhe impede de prosseguir:",
                "nome": monstros[0]["nome"],
                "fala": monstros[0]["fala"],
                "status_monstro": monstros[0]["status"],
                "opcoes": "lutar ou fugir? "
        },
        "luta 1": {
                "titulo": "Parece que uma luta lhe espera! E alguém lhe impede de prosseguir:",
                "nome": monstros[1]["nome"],
                "fala": monstros[1]["fala"],
                "status_monstro": monstros[1]["status"],
                "opcoes": "lutar ou fugir? "            
        },
        "luta 2": {
                "titulo": "Parece que uma luta lhe espera! E alguém lhe impede de prosseguir:",
                "nome": monstros[2]["nome"],
                "fala": monstros[2]["fala"],
                "status_monstro": monstros[2]["status"],
                "opcoes": "lutar ou fugir? "
        },
        "luta 3": {
                "titulo": "Parece que uma luta lhe espera! E alguém lhe impede de prosseguir:",
                "nome": monstros[3]["nome"],
                "fala": monstros[3]["fala"],
                "status_monstro": monstros[3]["status"],
                "opcoes": "lutar ou fugir? "
        },
        "luta 4": {
                "titulo": "Parece que uma luta lhe espera! E alguém lhe impede de prosseguir:",
                "nome": monstros[4]["nome"],
                "fala": monstros[4]["fala"],
                "status_monstro": monstros[4]["status"],
                "opcoes": "lutar ou fugir? " 
        },
            "luta 5": {
                "titulo": "Bar bar bar ra Ann",
                "nome": monstros[5]["nome"],
                "fala": monstros[5]["fala"],
                "status_monstro": monstros[5]["status"],
                "opcoes": "lutar ou fugir? " 
                
        },
        "luta 6": {
                "titulo": "Voce encontrou o mestre dos magos, lute pela sua nota no Ep",
                "nome": monstros[6]["nome"],
                "fala": monstros[6]["fala"],
                "status_monstro": monstros[6]["status"],
                "opcoes": "lutar ou fugir? " 
        }           

            

        }

    

    return combate

def carregar_inventario(inventario):
    return inventario


def carregar_ataque(inventario):  
    ataque_jogador = 12 
    inventario_jogador = inventario
 
    if "adaga" in inventario_jogador: 
        ataque_jogador = 22
        
        if "espada master blaster" in inventario_jogador:
            ataque_jogador=40
        
            if "espada python" in inventario_jogador:
                ataque_jogador=60
    
 
    return ataque_jogador


def luta(i):
    monstros= carregar_monstros()

    vida_monstros = monstros[i]["status"]["hit points"]
    vida_jogador = vida_player
    ataque_jogador = carregar_ataque(inventario_jogador)
    ataque_monstro = monstros[i]["status"]["pontos de ataque"]

    contador_da_vez= randint(1,2)
    
    while vida_monstros >0 and vida_jogador>0:
        if contador_da_vez%2 == 0: #vez do jogador
            print("Sua vez de atacar")
            print()
            print("Você causou {0} de dano".format(ataque_jogador))
            vida_monstros-= ataque_jogador
            if vida_monstros < 0:
                vida_monstros = 0
                print("O monstro morreu")
            print ("A vida do monstro ficou: {0}".format(vida_monstros))
            print()

        elif contador_da_vez%2 !=0:
            print("É a vez do monstro de atacar")
            print()
            print("O monstro causou {0} de dano".format(ataque_monstro))
            vida_jogador -= ataque_monstro
            if vida_jogador < 0:
                vida_jogador = 0
                print("Voce morreu")
                game_over = True
            print("Após o ataque do monstro, sua vida ficou: {0}".format(vida_jogador))
            print()
        contador_da_vez+=1
    return "Fim da luta"




 
    

 



 



 

 



def main():
    jogador = input("Diga seu nome aventureiro: ")
    print()
    print("Olá {0}, sua vida é: 100 e você começa com sua carteirinha do Insper em seu inventário".format(jogador))
    print()
    print("por voce estar com a carteirinha Insper no seu inventario, sua vida sempre regernera ao final de cada luta")
    pronto= input("voce esta pronto?: ")
    print()
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
    combate = carregar_combate()
    monstros = carregar_monstros()
    
    
    contador_biblioteca=0
    contador_aquarios=0
    contador_fumodromo=0
    contador_fablab=0
    contador_objeto=0
    contador_barbara=0
    contador_tosh=0
    
    
    
    
    game_over = False

    while not game_over:
        if atributos_jogador["hit points"]==0:
            break
        
        
        cenario_atual = cenarios[nome_cenario_atual]
        cenario_anterior= nome_cenario_atual
        titulo= cenario_atual['titulo']
        print()
        print(titulo)
        print("-"*len(titulo))
        print()
        print(cenario_atual["descricao"])
        print()
        print("Seu inventário:", carregar_inventario(inventario_jogador))

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

            cenario_anterior= nome_cenario_atual
            nome_cenario_atual=escolha
            
            if escolha not in opcoes:
                print("Sua indecisão foi sua ruína!")
                game_over = True

            if contador_biblioteca==0 or contador_aquarios==0 or contador_fablab==0 or contador_fumodromo==0 or contador_objeto==0 or contador_barbara==0 or contador_tosh==0:
                if escolha == "bau":
                    inventario_jogador.append("espada master blaster")
                    
                    
                elif escolha == "sala secreta":
                    inventario_jogador.append("livro python")
                    
               
                if escolha == "biblioteca" and contador_biblioteca==0:
                    print(combate["luta 0"]["titulo"])
                    print()
                    print(combate["luta 0"]["nome"])
                    print()
                    print(combate["luta 0"]["fala"])
                    print(combate["luta 0"]["nome"], ":", combate["luta 0"]["status_monstro"])
                    print(jogador, ":", "hit points: {0}, pontos de ataque: {1}".format(vida_player,carregar_ataque(inventario_jogador)))
                    choice = input("O que deseja fazer: 'lutar' ou 'fugir'? ")
                    if choice == "lutar":
                        print(luta(0))
                        print()
                        print("Parece que esse monstro deixou um prêmio para você:", monstros[0]["premio"])
                        print("Este item adiciona 10 pontos de ataque ao seu avatar")
                        inventario_jogador.append(monstros[0]["premio"])
                        
                        contador_biblioteca+=1  
                    elif choice == "fugir":
                        nome_cenario_atual = cenario_anterior
                        print()
                        print("Você voltou para o cenário anterior")
                        print()
                    else:
                        print("Sua indecisão foi sua ruína!")
                        game_over = True
                elif escolha== "aquarios" and contador_aquarios==0:
                    print(combate["luta 1"]["titulo"])
                    print()
                    print(combate["luta 1"]["nome"])
                    print()
                    print(combate["luta 1"]["fala"])
                    print(combate["luta 1"]["nome"], ":", combate["luta 1"]["status_monstro"])
                    print(jogador, ":", "hit points: {0}, pontos de ataque: {1}".format(vida_player,carregar_ataque(inventario_jogador)))

                    choice = input("o que deseja fazer: 'lutar' ou 'fugir'? ")

                    if choice == "lutar":
                        print(luta(1))
                        print()
                        print("Parece que esse monstro deixou um prêmio para você:", monstros[1]["premio"])
                        print("Este item lhe permite acesso à sala secreta")   
                        inventario_jogador.append(monstros[1]["premio"])
                        contador_aquarios+=1  

                    elif choice == "fugir":
                        nome_cenario_atual = cenario_anterior
                        print()
                        print("Você voltou para o cenário anterior")
                        print()

                    else:
                        print("Sua indecisão foi sua ruína!")
                        game_over = True

                elif escolha == "fumodromo" and contador_fumodromo==0:
                    print(combate["luta 2"]["titulo"])
                    print()
                    print(combate["luta 2"]["nome"])
                    print()
                    print(combate["luta 2"]["fala"])
                    print(combate["luta 2"]["nome"], ":", combate["luta 2"]["status_monstro"])
                    print(jogador, ":", "hit points: {0}, pontos de ataque: {1}".format(vida_player,carregar_ataque(inventario_jogador)))
                    choice = input("o que deseja fazer: 'lutar' ou 'fugir'? ")
                    if choice == "lutar":
                        print(luta(2))                       
                        contador_fumodromo+=1  

                    elif choice == "fugir":
                        nome_cenario_atual = cenario_anterior
                        print()
                        print("Você voltou para o cenário anterior")
                        print()

                    else:
                        print("Sua indecisão foi sua ruína!")
                        game_over = True
                        
                elif escolha == "fablab" and contador_fablab==0:
                    print(combate["luta 3"]["titulo"])
                    print()
                    print(combate["luta 3"]["nome"])
                    print()
                    print(combate["luta 3"]["fala"])
                    print(combate["luta 3"]["nome"], ":", combate["luta 3"]["status_monstro"])
                    print(jogador, ":", "hit points: {0}, pontos de ataque: {1}".format(vida_player,carregar_ataque(inventario_jogador)))
                    choice = input("o que deseja fazer: 'lutar' ou 'fugir'? ")

                    if choice == "lutar":
                        print(luta(3))                       
                        contador_fablab+=1  

                    elif choice == "fugir":
                        nome_cenario_atual = cenario_anterior
                        print()
                        print("Você voltou para o cenário anterior")
                        print()
                    else:
                        print("Sua indecisão foi sua ruína!")
                        game_over = True
                        
                elif escolha == "objeto" and contador_objeto==0:
                    print(combate["luta 4"]["titulo"])
                    print()
                    print(combate["luta 4"]["nome"])
                    print()
                    print(combate["luta 4"]["fala"])
                    print(combate["luta 4"]["nome"], ":", combate["luta 4"]["status_monstro"])
                    print(jogador, ":", "hit points: {0}, pontos de ataque: {1}".format(vida_player,carregar_ataque(inventario_jogador)))
                    choice = input("o que deseja fazer: 'lutar' ou 'fugir'? ")
                    if choice == "lutar":
                        print(luta(4))                       
                        contador_objeto+=1  
                    elif choice == "fugir":
                        nome_cenario_atual = cenario_anterior
                        print()
                        print("Você voltou para o cenário anterior")
                        print()
                    else:
                        print("Sua indecisão foi sua ruína!")
                        game_over = True
                        
                elif escolha == "portal" and contador_barbara==0:
                    print(combate["luta 5"]["titulo"])
                    print()
                    print(combate["luta 5"]["nome"])
                    print()
                    print(combate["luta 5"]["fala"])
                    print(combate["luta 5"]["nome"], ":", combate["luta 5"]["status_monstro"])
                    print(jogador, ":", "hit points: {0}, pontos de ataque: {1}".format(vida_player,carregar_ataque(inventario_jogador)))
                    choice = input("o que deseja fazer: 'lutar' ou 'fugir'? ")
                    if choice == "lutar":
                        print(luta(5))
                        print()
                        print("Parece que esse monstro deixou um prêmio para você:", monstros[4]["premio"])
                        print("Este item permite você ter acesso para usar o toboga multidimensional para todos lugares")
                        
                        inventario_jogador.append(monstros[5]["premio"])                     
                        contador_barbara+=1  
                    elif choice == "fugir":
                        nome_cenario_atual = cenario_anterior
                        print()
                        print("Você voltou para o cenário anterior")
                        print()
                    else:
                        print("Sua indecisão foi sua ruína!")
                        game_over = True
                        
                        
                elif escolha == "toshandrew" and contador_tosh==0:
                    print(combate["luta 6"]["titulo"])
                    print()
                    print(combate["luta 6"]["nome"])
                    print()
                    print(combate["luta 6"]["fala"])
                    print(combate["luta 6"]["nome"], ":", combate["luta 6"]["status_monstro"])
                    print(jogador, ":", "hit points: {0}, pontos de ataque: {1}".format(vida_player,carregar_ataque(inventario_jogador)))
                    choice = input("o que deseja fazer: 'lutar' ou 'fugir'? ")
                    if choice == "lutar":
                        print(luta(6))
                        print()
                        print("Voce ganhou um premio por derrotar andrew:", monstros[6]["premio"])
                        print()
                        print("Voce venceu o Tosh e ganhou um A no EP")
                        print()
                        inventario_jogador.append(monstros[6]["premio"])
                        print("Seu inventario e:", inventario_jogador)
                        print()
                        print("parabens!")
                        print()
                        print("obrigado por jogar")
                        time.sleep(2)
                        print("No entanto, era tudo uma mentira, voce nunca ganhou a luta contra o tosh")
                        print()
                        print("Ninguem nunca ganha do Tosh")
                        game_over=True
                                               

                            
                    elif choice == "fugir":
                        nome_cenario_atual = cenario_anterior
                        print()
                        print("Você voltou para o cenário anterior")
                        print()
                    else:
                        print("Sua indecisão foi sua ruína!")
                        game_over = True
                    

                

            else:
                if escolha in opcoes:
                    nome_cenario_atual=escolha
                    
                    
                
                         
                
                    



    morte = "Voce morreu!\n Voce nao conseguiu adiar o EP"
    for l in morte:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.2)



                



# Programa principal.

if __name__ == "__main__":
    main()